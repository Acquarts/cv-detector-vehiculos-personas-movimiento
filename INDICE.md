# 📦 Contenido del Proyecto

## 📋 Archivos Principales

### 🎯 `video_detector.py`
**Aplicación principal con interfaz web Streamlit y análisis avanzado**
- Interfaz gráfica interactiva
- Sube videos mediante drag & drop
- **Tracking inteligente** de vehículos y personas
- **Visualización de trayectorias** en tiempo real
- **Análisis de velocidad** y tiempo de permanencia
- Estadísticas detalladas por objeto
- Panel analítico con métricas avanzadas
- Descarga del video procesado con anotaciones
- **USO:** `streamlit run video_detector.py`

### 🔧 `batch_processor.py`
**Script para procesamiento por lotes (sin interfaz)**
- Procesamiento desde línea de comandos
- Ideal para automatización
- Múltiples opciones configurables
- **USO:** `python batch_processor.py --input video.mp4 --output resultado.mp4`

---

## 🚀 Scripts de Inicio

### `start.sh` (macOS/Linux)
Script de inicio automático para sistemas Unix
- Crea el entorno virtual
- Instala dependencias
- Inicia la aplicación
- **USO:** `./start.sh`

### `start.bat` (Windows)
Script de inicio automático para Windows
- Configuración automática
- Instalación de dependencias
- Inicio de la aplicación
- **USO:** Doble clic en el archivo

---

## 📄 Documentación

### 📖 `README.md`
**Documentación completa del proyecto**
- Instrucciones de instalación detalladas
- Características de tracking y análisis de movimiento
- Casos de uso: tráfico, seguridad, movilidad urbana
- Lista completa de objetos detectables
- Configuración avanzada
- Solución de problemas
- Datos exportables y análisis estadístico

### ⚡ `GUIA_RAPIDA.md`
**Guía de inicio rápido**
- Inicio en 3 pasos
- Ejemplos prácticos para análisis de tráfico
- Casos de uso reales: vigilancia, monitoreo urbano
- Tips para análisis de movimiento
- Comparativa de modelos y rendimiento

---

## ⚙️ Configuración

### 📦 `requirements.txt`
**Dependencias del proyecto**
```
streamlit>=1.28.0      # Framework web
opencv-python>=4.8.0    # Procesamiento de video
numpy>=1.24.0           # Operaciones numéricas
ultralytics>=8.0.0      # YOLOv8
Pillow>=10.0.0          # Procesamiento de imágenes
```

### 🚫 `gitignore.txt`
Archivo `.gitignore` para control de versiones
- Excluye archivos temporales
- Ignora modelos descargados
- Omite videos de prueba

---

## 🎯 Cómo Empezar

### Opción 1: Inicio Automático (Recomendado)

**Windows:**
```
1. Doble clic en start.bat
2. Espera a que se instale todo
3. Se abrirá tu navegador automáticamente
```

**macOS/Linux:**
```bash
1. ./start.sh
2. Espera a que se instale todo
3. Se abrirá tu navegador automáticamente
```

### Opción 2: Instalación Manual

```bash
# 1. Crear entorno virtual
python -m venv venv

# 2. Activar entorno virtual
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar aplicación
streamlit run video_detector.py
```

### Opción 3: Procesamiento por Lotes

```bash
# Instalar dependencias (solo primera vez)
pip install -r requirements.txt

# Procesar video
python batch_processor.py --input mi_video.mp4 --output resultado.mp4
```

---

## 📊 Flujo de Trabajo Típico

```
1. Ejecutar aplicación
   ↓
2. Subir video
   ↓
3. Ajustar umbral de confianza (opcional)
   ↓
4. Hacer clic en "Detectar Objetos"
   ↓
5. Ver resultados y estadísticas
   ↓
6. Descargar video procesado
```

---

## 🎓 Niveles de Uso

### 🟢 Principiante
- Usa `start.sh` o `start.bat`
- Interfaz web visual
- No requiere conocimientos técnicos

### 🟡 Intermedio
- Usa `batch_processor.py` para automatización
- Ajusta parámetros según necesidades
- Procesa múltiples videos

### 🔴 Avanzado
- Modifica el código fuente
- Integra con otros sistemas
- Personaliza modelos y clases

---

## 📈 Características Implementadas

### ✅ Funcionalidades Actuales
1. **✅ Tracking de objetos**: Seguimiento con IDs únicos entre frames
2. **✅ Trayectorias visuales**: Visualización del recorrido completo
3. **✅ Análisis de velocidad**: Cálculo en tiempo real
4. **✅ Tiempo de permanencia**: Medición automática por objeto
5. **✅ Estadísticas avanzadas**: Panel completo con métricas
6. **✅ Exportación de datos**: Tabla interactiva con toda la información

### 🚀 Mejoras Futuras Sugeridas
1. **Zonas de interés**: Definir áreas específicas para detectar
2. **Alertas**: Notificaciones cuando se detectan objetos específicos
3. **Contadores automáticos**: Líneas de conteo para flujo vehicular
4. **API REST**: Exponer funcionalidad vía API
5. **Base de datos**: Almacenar histórico de detecciones
6. **Dashboard multi-video**: Panel de análisis de múltiples cámaras
7. **Análisis de velocidad real**: Calibración para velocidades en km/h

### 🎨 Personalización
- Entrenar el modelo con tus propias clases
- Ajustar colores de las trayectorias y anotaciones
- Agregar filtros específicos por tipo de objeto
- Exportar datos a formatos específicos (JSON, CSV, Excel)

---

## 🆘 ¿Necesitas Ayuda?

1. **Consulta primero:** `GUIA_RAPIDA.md` - Soluciones a problemas comunes
2. **Documentación completa:** `README.md` - Información detallada
3. **Ejemplos de código:** Dentro de los archivos `.py`

---

## ✅ Checklist de Verificación

Antes de empezar, asegúrate de tener:

- [ ] Python 3.8 o superior instalado
- [ ] pip actualizado
- [ ] Espacio en disco (al menos 500 MB)
- [ ] Video de prueba en formato compatible (MP4, AVI, MOV, MKV)
- [ ] Conexión a internet (para descargar modelos la primera vez)

---

## 🎬 ¡Listo para Empezar!

Todo está preparado. Solo necesitas:

1. Elegir tu método de inicio (automático o manual)
2. Subir un video de tráfico o monitoreo
3. Ver el tracking inteligente y análisis de movimiento
4. Analizar las trayectorias, velocidades y estadísticas

**¡Transforma tus videos en datos útiles! 🚗👥📊**
