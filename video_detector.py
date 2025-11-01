import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import tempfile
import os
from pathlib import Path
from collections import defaultdict, deque
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Detector de Objetos en Video",
    page_icon="🎥",
    layout="wide"
)

# Título y descripción
st.title("🎥 DETECTOR DE VEHÍCULOS Y PERSONAS EN MOVIMIENTO")
st.markdown("""
Esta aplicación utiliza inteligencia artificial para detectar y analizar automáticamente:
- 👥 **Personas y Vehículos** - Detección en tiempo real
- 🛣️ **Trayectorias** - Visualización del recorrido de cada objeto
- ⏱️ **Tiempo en Escena** - Cuánto tiempo permanece cada objeto
- 🚀 **Velocidad de Movimiento** - Análisis de velocidad en píxeles/segundo
- 📦 **80+ Categorías** - Animales, objetos cotidianos y más
""")

@st.cache_resource
def load_model():
    """Carga el modelo YOLO"""
    try:
        model = YOLO('yolov8n.pt')  # Modelo nano (más rápido)
        return model
    except Exception as e:
        st.error(f"Error cargando el modelo: {e}")
        return None

def process_video(video_path, model, confidence_threshold):
    """Procesa el video y detecta objetos con tracking, trayectorias y análisis"""
    cap = cv2.VideoCapture(video_path)

    # Obtener propiedades del video
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Crear archivo de salida
    output_path = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4').name
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Barra de progreso
    progress_bar = st.progress(0)
    status_text = st.empty()

    # Contador de objetos detectados
    detected_objects = {}

    # Tracking: almacenar trayectorias y datos de cada objeto
    track_history = defaultdict(lambda: deque(maxlen=30))  # Últimos 30 puntos de trayectoria
    track_data = {}  # Información de cada track: {track_id: {class, first_frame, last_frame, positions}}

    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Realizar detección con tracking
        results = model.track(frame, conf=confidence_threshold, verbose=False, persist=True)

        # Obtener frame anotado
        annotated_frame = results[0].plot()

        # Procesar cada detección con tracking
        if results[0].boxes.id is not None:
            boxes = results[0].boxes.xyxy.cpu().numpy()
            track_ids = results[0].boxes.id.cpu().numpy().astype(int)
            classes = results[0].boxes.cls.cpu().numpy().astype(int)

            for box, track_id, class_id in zip(boxes, track_ids, classes):
                class_name = model.names[class_id]
                detected_objects[class_name] = detected_objects.get(class_name, 0) + 1

                # Calcular centro del bounding box
                x_center = (box[0] + box[2]) / 2
                y_center = (box[1] + box[3]) / 2
                center = (int(x_center), int(y_center))

                # Actualizar historial de trayectoria
                track_history[track_id].append(center)

                # Actualizar datos del track
                if track_id not in track_data:
                    track_data[track_id] = {
                        'class': class_name,
                        'first_frame': frame_count,
                        'last_frame': frame_count,
                        'positions': [center],
                        'start_time': frame_count / fps
                    }
                else:
                    track_data[track_id]['last_frame'] = frame_count
                    track_data[track_id]['positions'].append(center)

                # Dibujar trayectoria
                points = list(track_history[track_id])
                if len(points) > 1:
                    for i in range(1, len(points)):
                        # Gradiente de color: más reciente = más opaco
                        thickness = int(2 * (i / len(points)) + 1)
                        cv2.line(annotated_frame, points[i-1], points[i], (0, 255, 0), thickness)

                # Calcular velocidad si hay suficientes datos
                if len(track_data[track_id]['positions']) >= 2:
                    # Velocidad basada en últimos 5 frames
                    recent_positions = track_data[track_id]['positions'][-5:]
                    if len(recent_positions) >= 2:
                        dist = np.sqrt(
                            (recent_positions[-1][0] - recent_positions[0][0])**2 +
                            (recent_positions[-1][1] - recent_positions[0][1])**2
                        )
                        time_elapsed = len(recent_positions) / fps
                        speed = dist / time_elapsed if time_elapsed > 0 else 0

                        # Mostrar velocidad en el frame
                        speed_text = f"{speed:.1f} px/s"
                        cv2.putText(annotated_frame, speed_text,
                                  (int(box[0]), int(box[1]) - 10),
                                  cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

                # Calcular tiempo en escena
                time_in_scene = (frame_count - track_data[track_id]['first_frame']) / fps
                time_text = f"{time_in_scene:.1f}s"
                cv2.putText(annotated_frame, time_text,
                          (int(box[0]), int(box[3]) + 20),
                          cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

        # Escribir frame procesado
        out.write(annotated_frame)

        # Actualizar progreso
        frame_count += 1
        progress = frame_count / total_frames
        progress_bar.progress(progress)
        status_text.text(f"Procesando frame {frame_count}/{total_frames}")

    cap.release()
    out.release()
    progress_bar.empty()
    status_text.empty()

    # Calcular estadísticas finales
    tracking_stats = []
    for track_id, data in track_data.items():
        total_distance = 0
        positions = data['positions']

        # Calcular distancia total recorrida
        for i in range(1, len(positions)):
            dist = np.sqrt(
                (positions[i][0] - positions[i-1][0])**2 +
                (positions[i][1] - positions[i-1][1])**2
            )
            total_distance += dist

        duration = (data['last_frame'] - data['first_frame']) / fps
        avg_speed = total_distance / duration if duration > 0 else 0

        tracking_stats.append({
            'ID': track_id,
            'Clase': data['class'],
            'Tiempo en escena (s)': round(duration, 2),
            'Distancia recorrida (px)': round(total_distance, 2),
            'Velocidad promedio (px/s)': round(avg_speed, 2),
            'Frames detectado': data['last_frame'] - data['first_frame'] + 1
        })

    return output_path, detected_objects, tracking_stats

# Sidebar con configuración
st.sidebar.header("⚙️ Configuración")
confidence = st.sidebar.slider(
    "Umbral de confianza",
    min_value=0.1,
    max_value=1.0,
    value=0.5,
    step=0.05,
    help="Nivel mínimo de confianza para detectar un objeto"
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
### ℹ️ Información
Este detector usa **YOLOv8**, uno de los modelos más avanzados
para detección y tracking de objetos en tiempo real.

**Características:**
- Detección de 80+ tipos de objetos
- Tracking con IDs únicos
- Trayectorias visualizadas en video
- Tiempo de permanencia en escena
- Velocidad de movimiento
- Análisis estadístico completo

**En el video verás:**
- 🟩 Líneas verdes = Trayectorias
- 🟨 Texto amarillo = Velocidad
- 🔵 Texto cian = Tiempo en escena
""")

# Cargar modelo
with st.spinner("🔄 Cargando modelo de IA..."):
    model = load_model()

if model is None:
    st.error("❌ No se pudo cargar el modelo. Por favor, verifica la instalación.")
    st.stop()

st.success("✅ Modelo cargado correctamente")

# Uploader de video
uploaded_file = st.file_uploader(
    "📤 Sube tu video",
    type=['mp4', 'avi', 'mov', 'mkv'],
    help="Formatos soportados: MP4, AVI, MOV, MKV"
)

if uploaded_file is not None:
    # Guardar video temporalmente
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    tfile.write(uploaded_file.read())
    video_path = tfile.name
    
    # Crear dos columnas
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📹 Video Original")
        st.video(video_path)
    
    # Botón para procesar
    if st.button("🚀 Detectar Objetos", type="primary", use_container_width=True):
        with st.spinner("🔍 Analizando video..."):
            try:
                output_path, detected_objects, tracking_stats = process_video(
                    video_path,
                    model,
                    confidence
                )

                with col2:
                    st.subheader("🎯 Video Procesado")
                    st.video(output_path)

                # Mostrar estadísticas
                st.markdown("---")
                st.subheader("📊 Objetos Detectados")

                if detected_objects:
                    # Ordenar por cantidad
                    sorted_objects = sorted(
                        detected_objects.items(),
                        key=lambda x: x[1],
                        reverse=True
                    )

                    # Mostrar en columnas
                    cols = st.columns(3)
                    for idx, (obj_name, count) in enumerate(sorted_objects):
                        col_idx = idx % 3
                        with cols[col_idx]:
                            st.metric(
                                label=obj_name.capitalize(),
                                value=count,
                                delta="detecciones"
                            )

                    # Mostrar estadísticas de tracking
                    if tracking_stats:
                        st.markdown("---")
                        st.subheader("🎯 Análisis de Trayectorias y Movimiento")

                        # Crear DataFrame
                        df_stats = pd.DataFrame(tracking_stats)
                        df_stats = df_stats.sort_values('Tiempo en escena (s)', ascending=False)

                        # Mostrar tabla interactiva
                        st.dataframe(
                            df_stats,
                            use_container_width=True,
                            hide_index=True,
                            column_config={
                                "ID": st.column_config.NumberColumn("ID", help="ID único del objeto rastreado"),
                                "Clase": st.column_config.TextColumn("Tipo de Objeto"),
                                "Tiempo en escena (s)": st.column_config.NumberColumn(
                                    "Tiempo en Escena",
                                    help="Segundos que el objeto estuvo visible",
                                    format="%.2f s"
                                ),
                                "Distancia recorrida (px)": st.column_config.NumberColumn(
                                    "Distancia Recorrida",
                                    help="Distancia total en píxeles",
                                    format="%.1f px"
                                ),
                                "Velocidad promedio (px/s)": st.column_config.NumberColumn(
                                    "Velocidad Promedio",
                                    help="Velocidad promedio en píxeles por segundo",
                                    format="%.1f px/s"
                                ),
                                "Frames detectado": st.column_config.NumberColumn(
                                    "Frames",
                                    help="Número de frames donde fue detectado"
                                )
                            }
                        )

                        # Métricas resumen
                        st.markdown("### 📈 Resumen General")
                        col_a, col_b, col_c, col_d = st.columns(4)

                        with col_a:
                            st.metric(
                                "Objetos rastreados",
                                len(tracking_stats)
                            )

                        with col_b:
                            avg_time = df_stats['Tiempo en escena (s)'].mean()
                            st.metric(
                                "Tiempo promedio",
                                f"{avg_time:.1f}s"
                            )

                        with col_c:
                            max_speed = df_stats['Velocidad promedio (px/s)'].max()
                            st.metric(
                                "Velocidad máxima",
                                f"{max_speed:.1f} px/s"
                            )

                        with col_d:
                            total_dist = df_stats['Distancia recorrida (px)'].sum()
                            st.metric(
                                "Distancia total",
                                f"{total_dist:.0f} px"
                            )

                    # Botón de descarga
                    st.markdown("---")
                    with open(output_path, 'rb') as f:
                        st.download_button(
                            label="⬇️ Descargar Video Procesado",
                            data=f,
                            file_name="video_detectado.mp4",
                            mime="video/mp4",
                            use_container_width=True
                        )
                else:
                    st.warning("⚠️ No se detectaron objetos. Intenta ajustar el umbral de confianza.")

                # Limpiar archivos temporales
                try:
                    os.unlink(output_path)
                except:
                    pass

            except Exception as e:
                st.error(f"❌ Error procesando el video: {str(e)}")
    
    # Limpiar archivo temporal
    try:
        os.unlink(video_path)
    except:
        pass

else:
    st.info("👆 Sube un video para comenzar la detección")
    
    # Ejemplo visual
    st.markdown("---")
    st.subheader("🎬 ¿Cómo funciona?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 1️⃣ Sube tu video")
        st.markdown("Selecciona cualquier video de tu dispositivo")
    
    with col2:
        st.markdown("### 2️⃣ Procesamiento IA")
        st.markdown("El modelo analiza cada frame detectando objetos")
    
    with col3:
        st.markdown("### 3️⃣ Resultados")
        st.markdown("Descarga el video con las detecciones marcadas")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Desarrollado con ❤️ usando Streamlit y YOLOv8</p>
    </div>
    """,
    unsafe_allow_html=True
)
