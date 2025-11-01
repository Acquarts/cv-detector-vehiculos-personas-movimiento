# 🚀 Guía Rápida - Análisis de Vehículos y Personas

## Inicio Rápido (3 Pasos)

### 1️⃣ Ejecutar la aplicación

**En Windows:**
```
Doble clic en start.bat
```

**En macOS/Linux:**
```bash
./start.sh
```

O manualmente:
```bash
pip install -r requirements.txt
streamlit run video_detector.py
```

### 2️⃣ Subir tu video de tráfico/monitoreo

1. Abre tu navegador en `http://localhost:8501`
2. Haz clic en "📤 Sube tu video"
3. Selecciona tu archivo de video (ideal: cámaras de tráfico, vigilancia)

### 3️⃣ Analizar movimiento y descargar

1. Ajusta el umbral de confianza si lo deseas (sidebar)
2. Haz clic en "🚀 Detectar Objetos"
3. **Observa**: trayectorias, velocidades, tiempos de permanencia
4. **Revisa**: la tabla de estadísticas detalladas por objeto
5. Descarga el video procesado con todas las anotaciones

---

## 🎯 Ejemplos de Uso

### Interfaz Web (Streamlit)

La forma más fácil de usar la aplicación:

```bash
streamlit run video_detector.py
```

### Procesamiento por Lotes (CLI)

Para procesar videos sin interfaz gráfica:

```bash
# Ejemplo básico
python batch_processor.py --input mi_video.mp4 --output resultado.mp4

# Con configuración personalizada
python batch_processor.py \
  --input video_entrada.mp4 \
  --output video_salida.mp4 \
  --confidence 0.6 \
  --model yolov8m.pt
```

**Opciones disponibles:**

| Opción | Descripción | Default |
|--------|-------------|---------|
| `--input` / `-i` | Video de entrada (requerido) | - |
| `--output` / `-o` | Video de salida (requerido) | - |
| `--confidence` / `-c` | Umbral de confianza (0.0-1.0) | 0.5 |
| `--model` / `-m` | Modelo YOLO a usar | yolov8n.pt |

**Modelos disponibles:**
- `yolov8n.pt` - Nano (más rápido) ⚡
- `yolov8s.pt` - Small
- `yolov8m.pt` - Medium (balance)
- `yolov8l.pt` - Large
- `yolov8x.pt` - Extra Large (más preciso) 🎯

---

## ⚙️ Ajustar Configuraciones

### Umbral de Confianza

El umbral determina qué tan "seguro" debe estar el modelo:

- **0.3-0.4**: Más detecciones, pero puede incluir falsos positivos
- **0.5**: Balance recomendado (default)
- **0.7-0.9**: Menos detecciones, pero más precisas

### Elegir el Modelo

| Modelo | Velocidad | Precisión | Uso Recomendado |
|--------|-----------|-----------|-----------------|
| yolov8n | ⚡⚡⚡⚡⚡ | ⭐⭐⭐ | Videos largos, pruebas rápidas |
| yolov8s | ⚡⚡⚡⚡ | ⭐⭐⭐⭐ | Uso general |
| yolov8m | ⚡⚡⚡ | ⭐⭐⭐⭐ | Balance velocidad/precisión |
| yolov8l | ⚡⚡ | ⭐⭐⭐⭐⭐ | Alta precisión |
| yolov8x | ⚡ | ⭐⭐⭐⭐⭐ | Máxima precisión |

---

## 📝 Casos de Uso Prácticos

### 1. 🚦 Análisis de Tráfico Urbano
**Objetivo**: Contar vehículos, medir flujo, analizar patrones
```bash
streamlit run video_detector.py
# Sube un video de intersección o avenida
```
**Obtienes:**
- Conteo de cada tipo de vehículo (coches, motos, camiones, autobuses)
- Trayectorias de cada vehículo
- Tiempo de permanencia en intersección
- Velocidades promedio
- Tabla exportable con todos los datos

### 2. 🏙️ Monitoreo de Zonas Peatonales
**Objetivo**: Analizar flujo peatonal y aglomeraciones
```bash
streamlit run video_detector.py
# Sube video de zona peatonal, plaza o parque
```
**Obtienes:**
- Tracking individual de cada persona
- Patrones de movimiento y trayectorias
- Tiempo de permanencia en la zona
- Identificación de puntos de congestión
- Estadísticas de afluencia

### 3. 🔒 Seguridad y Vigilancia
**Objetivo**: Monitorear accesos y detectar movimientos
```bash
streamlit run video_detector.py
# Sube video de cámara de seguridad
```
**Obtienes:**
- Tracking de personas y vehículos
- Registro de trayectorias completas
- Tiempo de permanencia sospechoso
- Velocidades inusuales
- Datos para investigación posterior

### 4. 📊 Estudios de Movilidad
**Objetivo**: Análisis para planificación urbana
```bash
streamlit run video_detector.py
# Sube videos de diferentes ubicaciones/horarios
```
**Obtienes:**
- Patrones de desplazamiento
- Proporción vehículos/peatones/bicicletas
- Velocidades promedio por tipo
- Datos comparativos entre ubicaciones
- Base de datos para decisiones urbanas

---

## 🐛 Solución de Problemas Comunes

### El video no se procesa
- ✅ Verifica que el formato sea compatible (MP4, AVI, MOV, MKV)
- ✅ Asegúrate de tener suficiente espacio en disco
- ✅ Intenta con un video más corto para probar

### Procesamiento muy lento
- ✅ Usa el modelo `yolov8n.pt` (más rápido)
- ✅ Reduce la resolución del video de entrada
- ✅ Cierra otras aplicaciones para liberar recursos

### Pocas detecciones
- ✅ Reduce el umbral de confianza (ej: 0.3-0.4)
- ✅ Usa un modelo más grande (ej: yolov8m.pt)
- ✅ Verifica que los objetos sean de las categorías soportadas

### Muchos falsos positivos
- ✅ Aumenta el umbral de confianza (ej: 0.7-0.8)
- ✅ Usa un modelo más preciso (yolov8l.pt o yolov8x.pt)

---

## 💡 Tips y Trucos para Análisis de Movimiento

### 1. Mejores Resultados en Análisis de Tráfico
**Para cámaras de tráfico:**
- Usa videos con cámara fija (sin movimiento)
- Resolución mínima recomendada: 720p
- Iluminación adecuada mejora la detección
- Ángulo cenital o semi-cenital funciona mejor

### 2. Interpretar las Trayectorias
**Líneas verdes en el video:**
- Más gruesas = movimiento reciente
- Más finas = movimiento pasado
- Trayectorias rectas = movimiento constante
- Trayectorias zigzag = objeto deteniéndose/acelerando

### 3. Entender las Velocidades
**El sistema muestra píxeles/segundo:**
- Alta velocidad (>100 px/s) = vehículos rápidos
- Media velocidad (30-100 px/s) = vehículos normales o personas corriendo
- Baja velocidad (<30 px/s) = peatones o vehículos lentos
- Para convertir a km/h necesitas calibración con referencias conocidas

### 4. Análisis de Tiempos de Permanencia
**Usa esta métrica para:**
- Detectar congestión (tiempos largos en intersección)
- Identificar estacionamiento no autorizado
- Analizar tiempo de cruce peatonal
- Estudiar comportamiento en zonas específicas

### 5. Filtrar Solo Vehículos o Personas
**En la tabla de resultados:**
- Busca en la columna "Clase"
- Filtra manualmente por: car, motorcycle, bus, truck, person
- Suma las distancias/velocidades por tipo
- Compara comportamiento entre categorías

### 6. Exportar Datos para Análisis
**Usa la tabla interactiva:**
- Copia los datos directamente
- Pega en Excel o Google Sheets
- Crea gráficos personalizados
- Genera reportes profesionales

### 7. Mejora el Tracking
**Para mejor seguimiento:**
- Umbral de confianza: 0.5-0.6 (balance)
- Videos más largos = más datos estadísticos
- Evita cambios bruscos de iluminación
- Mantén distancia de cámara constante

---

## 📊 Rendimiento Esperado

### En una PC con CPU moderna:

| Resolución | FPS Procesamiento | Modelo |
|------------|-------------------|--------|
| 720p | ~15-20 FPS | yolov8n |
| 1080p | ~8-12 FPS | yolov8n |
| 720p | ~5-8 FPS | yolov8m |
| 1080p | ~3-5 FPS | yolov8m |

### Con GPU (NVIDIA con CUDA):

| Resolución | FPS Procesamiento | Modelo |
|------------|-------------------|--------|
| 720p | ~60-80 FPS | yolov8n |
| 1080p | ~30-40 FPS | yolov8n |
| 720p | ~25-35 FPS | yolov8m |
| 1080p | ~15-20 FPS | yolov8m |

---

## 📚 Recursos Adicionales

- [Documentación YOLOv8](https://docs.ultralytics.com/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [OpenCV Tutorials](https://docs.opencv.org/master/d9/df8/tutorial_root.html)

---

## 🆘 Soporte

Si encuentras algún problema:
1. Revisa la sección de Solución de Problemas
2. Verifica que todas las dependencias estén instaladas
3. Consulta el README.md para más detalles

---

## 📊 Visualización de Resultados

### En el Video Procesado Verás:
- **Bounding boxes**: Rectángulos alrededor de cada objeto
- **🟩 Líneas verdes**: Trayectoria completa del objeto
- **🟨 Texto amarillo** (arriba): Velocidad actual en px/s
- **🔵 Texto cian** (abajo): Tiempo en escena en segundos
- **ID numérico**: Identificador único de cada objeto

### En la Tabla de Estadísticas:
- **ID**: Identificador único del tracking
- **Clase**: Tipo de objeto (car, person, motorcycle, etc.)
- **Tiempo en escena**: Segundos totales visible
- **Distancia recorrida**: Píxeles totales de movimiento
- **Velocidad promedio**: Velocidad media durante su recorrido
- **Frames detectado**: Cuántos frames apareció

### Métricas de Resumen:
- **Objetos rastreados**: Total de objetos con tracking único
- **Tiempo promedio**: Media de permanencia en escena
- **Velocidad máxima**: El objeto más rápido detectado
- **Distancia total**: Suma de todas las distancias recorridas

**¡Analiza el movimiento con inteligencia artificial! 🚗👥📊**
