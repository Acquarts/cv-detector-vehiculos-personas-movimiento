# 🎥 Detector Inteligente de Vehículos y Personas en Movimiento

Una aplicación web avanzada construida con Streamlit y YOLOv8 que detecta, rastrea y analiza el movimiento de vehículos y personas en videos. Ideal para análisis de tráfico, seguridad, monitoreo urbano y estudios de comportamiento.

## ✨ Características Principales

### 🚗 Detección y Tracking Avanzado
- **Vehículos**: Coches, motos, autobuses, camiones, bicicletas
- **Personas**: Peatones y personas en movimiento
- **Tracking con IDs únicos**: Seguimiento individual de cada objeto a través del video

### 📊 Análisis de Movimiento
- 🛣️ **Trayectorias visuales**: Visualiza el recorrido completo de cada objeto
- ⏱️ **Tiempo de permanencia**: Mide cuánto tiempo cada objeto está en escena
- 🚀 **Velocidad de movimiento**: Calcula la velocidad en píxeles por segundo
- 📈 **Estadísticas detalladas**: Análisis completo por objeto individual

### 📋 Panel de Analítica
- Distancia total recorrida por cada objeto
- Velocidad promedio y velocidad máxima
- Número de frames detectados
- Tiempo promedio de permanencia
- Tabla interactiva con todos los datos exportables

## 🚀 Demo en Vivo

Puedes probar la aplicación en línea sin instalar nada:

**[🔗 Abrir App en Streamlit Cloud](https://cv-detector-vehiculos-personas-movimiento.streamlit.app/)**

## 📦 Instalación Local

### Prerrequisitos

- Python 3.8 - 3.10 (recomendado 3.10)
- pip

### Pasos de instalación

1. **Clona el repositorio**

```bash
git clone https://github.com/Acquarts/cv-object-and-person-detector.git
cd cv-object-and-person-detector
```

2. **Crea un entorno virtual (recomendado)**

```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```

3. **Instala las dependencias**

```bash
pip install -r requirements.txt
```

**Nota para Windows:** Si encuentras errores de DLL con PyTorch, ejecuta el script de reparación incluido:
```bash
fix_dependencies.bat
```

Nota: La primera vez que ejecutes la aplicación, se descargará automáticamente el modelo YOLOv8 (~6MB).

## 🎮 Uso

1. **Ejecuta la aplicación:**

```bash
streamlit run video_detector.py
```

2. **Abre tu navegador:**
   - La aplicación se abrirá automáticamente en `http://localhost:8501`

3. **Sube un video:**
   - Haz clic en "Sube tu video"
   - Selecciona un archivo (MP4, AVI, MOV, MKV)
   - Ideal: Videos de tráfico, cámaras de seguridad, monitoreo urbano

4. **Ajusta la configuración (opcional):**
   - Usa el slider en la barra lateral para ajustar el umbral de confianza
   - Valores más altos = menos detecciones pero más precisas
   - Valores más bajos = más detecciones pero pueden incluir falsos positivos

5. **Analiza el movimiento:**
   - Haz clic en "🚀 Detectar Objetos"
   - Espera mientras se procesa el video con tracking
   - El sistema rastrea automáticamente cada vehículo y persona

6. **Visualiza los resultados:**
   - **Video procesado**: Con bounding boxes, trayectorias, velocidades y tiempos
   - **Líneas verdes**: Muestran la trayectoria de cada objeto
   - **Texto amarillo**: Velocidad actual en px/s
   - **Texto cian**: Tiempo que lleva en escena

7. **Analiza las estadísticas:**
   - Tabla detallada con datos de cada objeto rastreado
   - Métricas agregadas: objetos totales, tiempos promedio, velocidades
   - Distancias recorridas por cada vehículo/persona

8. **Descarga el resultado:**
   - Haz clic en "⬇️ Descargar Video Procesado"
   - El video incluye todas las anotaciones y trayectorias

## 📋 Objetos Detectables con Tracking

El sistema está optimizado especialmente para:

### 🚗 Vehículos (Análisis Prioritario)
- **Coches**: Sedanes, SUVs, vehículos particulares
- **Motocicletas**: Motos de todo tipo
- **Autobuses**: Transporte público
- **Camiones**: Vehículos de carga
- **Bicicletas**: Ciclistas y bicicletas

### 👥 Personas (Análisis Prioritario)
- **Peatones**: Personas caminando
- **Personas en movimiento**: Corriendo, desplazándose
- **Grupos de personas**: Multitudes y aglomeraciones

### 🚦 Elementos de Contexto Vial
- Semáforos
- Señales de stop
- Hidrantes
- Bancos y mobiliario urbano

### 🐕 Otros (Capacidad Adicional)
- Animales domésticos (perros, gatos)
- Otros vehículos (trenes, aviones, barcos)
- 70+ categorías adicionales de objetos

**Nota**: Aunque el sistema puede detectar 80+ categorías, el tracking y análisis de movimiento están optimizados especialmente para vehículos y personas.

## 🛠️ Tecnologías Utilizadas

- **Streamlit**: Framework para la interfaz web interactiva
- **YOLOv8**: Modelo de detección y tracking de objetos de última generación
- **OpenCV**: Procesamiento de video y análisis de frames
- **Ultralytics**: Implementación avanzada de YOLO con tracking
- **NumPy**: Cálculos de velocidad, distancia y operaciones numéricas
- **Pandas**: Análisis y presentación de datos estadísticos

## 🎯 Casos de Uso

### 🚦 Análisis de Tráfico
- Conteo de vehículos en intersecciones
- Medición de flujo vehicular
- Identificación de patrones de tráfico
- Análisis de velocidades promedio

### 🏙️ Monitoreo Urbano
- Análisis de zonas peatonales
- Estudio de comportamiento de peatones
- Detección de aglomeraciones
- Tiempos de permanencia en áreas específicas

### 🔒 Seguridad y Vigilancia
- Tracking de personas y vehículos sospechosos
- Monitoreo de accesos
- Análisis de movimientos inusuales
- Registro de trayectorias completas

### 📊 Estudios de Movilidad
- Análisis de patrones de desplazamiento
- Estadísticas de uso de vías
- Estudios de comportamiento vehicular
- Planificación urbana basada en datos

## ⚙️ Configuración Avanzada

### Cambiar el modelo YOLO

Por defecto se usa `yolov8n.pt` (nano) que es rápido pero menos preciso. Puedes cambiar a modelos más grandes en la línea 26 del código:

```python
# Opciones disponibles:
model = YOLO('yolov8n.pt')  # Nano (más rápido) ⚡
model = YOLO('yolov8s.pt')  # Small
model = YOLO('yolov8m.pt')  # Medium
model = YOLO('yolov8l.pt')  # Large
model = YOLO('yolov8x.pt')  # Extra Large (más preciso) 🎯
```

### Ajustar el rendimiento

- Para videos largos, considera reducir la resolución
- Ajusta el FPS de procesamiento si necesitas más velocidad
- Usa el modelo nano (yolov8n) para procesamiento más rápido

## 🐛 Solución de Problemas

### Error de DLL en Windows (WinError 1114)
Este es un problema común con PyTorch en Windows. Solución:
```bash
# Ejecuta el script de reparación incluido
fix_dependencies.bat
```

O manualmente:
```bash
pip install torch==2.0.1 torchvision==0.15.2 --index-url https://download.pytorch.org/whl/cpu
pip install "numpy<2" opencv-python==4.10.0.84
```

### Error al cargar el modelo
```bash
pip install --upgrade ultralytics
```

### Problemas con OpenCV
```bash
pip install opencv-python-headless==4.10.0.84
```

### Video no se reproduce
- Asegúrate de que el video esté en un formato compatible (MP4, AVI, MOV, MKV)
- Prueba con un codec diferente

### El procesamiento es muy lento
- Usa el modelo `yolov8n.pt` (nano)
- Reduce la resolución del video de entrada
- Procesa solo una parte del video

## 🌐 Deploy en Streamlit Cloud

Para desplegar tu propia versión:

1. Haz fork de este repositorio
2. Ve a [share.streamlit.io](https://share.streamlit.io)
3. Conecta tu cuenta de GitHub
4. Selecciona el repositorio y la rama
5. El archivo principal es `video_detector.py`
6. ¡Deploy automático!

Los archivos necesarios ya están configurados:
- `requirements.txt`: Dependencias de Python
- `packages.txt`: Dependencias del sistema (Linux)
- `.streamlit/config.toml`: Configuración de la app

## 📝 Notas Importantes

- El primer procesamiento puede tardar más debido a la descarga del modelo
- El tiempo de procesamiento depende de:
  - Duración del video
  - Resolución del video
  - Modelo YOLO utilizado
  - Cantidad de objetos en movimiento
  - Capacidad de tu hardware
- Videos de alta resolución y larga duración requieren más tiempo y recursos
- El tracking funciona mejor con videos estables (sin movimientos bruscos de cámara)
- Para mejores resultados en análisis de tráfico, usa videos con cámara fija

## 📊 Datos Exportables

La aplicación genera los siguientes datos por cada objeto rastreado:
- **ID único**: Identificador del objeto a lo largo del video
- **Clase**: Tipo de objeto (coche, persona, moto, etc.)
- **Tiempo en escena**: Segundos que el objeto estuvo visible
- **Distancia recorrida**: Distancia total en píxeles
- **Velocidad promedio**: Velocidad media en píxeles por segundo
- **Frames detectados**: Número de frames donde apareció el objeto

Estos datos pueden ser analizados posteriormente para estudios estadísticos o reportes.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras algún bug o tienes sugerencias de mejora, no dudes en reportarlo.

## 📄 Licencia

Este proyecto utiliza:
- YOLOv8: Licencia AGPL-3.0
- Streamlit: Licencia Apache 2.0

## 🙏 Agradecimientos

- [Ultralytics](https://github.com/ultralytics/ultralytics) por YOLOv8
- [Streamlit](https://streamlit.io/) por el framework
- La comunidad de Open Source

---

**¡Analiza el movimiento de vehículos y personas con inteligencia artificial! 🚗👥📊**
