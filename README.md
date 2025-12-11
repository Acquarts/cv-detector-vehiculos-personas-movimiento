# 🎥 Intelligent Vehicle and Person Movement Detector

An advanced web application built with Streamlit and YOLOv8 that detects, tracks, and analyzes the movement of vehicles and people in videos. Ideal for traffic analysis, security, urban monitoring, and behavioral studies.

## ✨ Key Features

### 🚗 Advanced Detection and Tracking
- **Vehicles**: Cars, motorcycles, buses, trucks, bicycles
- **People**: Pedestrians and people in motion
- **Tracking with unique IDs**: Individual tracking of each object throughout the video

### 📊 Movement Analysis
- 🛣️ **Visual trajectories**: Visualize the complete path of each object
- ⏱️ **Dwell time**: Measure how long each object is in scene
- 🚀 **Movement speed**: Calculate speed in pixels per second
- 📈 **Detailed statistics**: Complete analysis per individual object

### 📋 Analytics Dashboard
- Total distance traveled by each object
- Average speed and maximum speed
- Number of detected frames
- Average dwell time
- Interactive table with all exportable data

## 🚀 Live Demo

You can try the application online without installing anything:

**[🔗 Open App on Streamlit Cloud](https://cv-detector-vehiculos-personas-movimiento.streamlit.app/)**

## 📦 Local Installation

### Prerequisites

- Python 3.8 - 3.10 (3.10 recommended)
- pip

### Installation Steps

1. **Clone the repository**

```bash
git clone https://github.com/Acquarts/cv-object-and-person-detector.git
cd cv-object-and-person-detector
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

**Note for Windows:** If you encounter DLL errors with PyTorch, run the included repair script:
```bash
fix_dependencies.bat
```

Note: The first time you run the application, the YOLOv8 model will be automatically downloaded (~6MB).

## 🎮 Usage

1. **Run the application:**

```bash
streamlit run video_detector.py
```

2. **Open your browser:**
   - The application will automatically open at `http://localhost:8501`

3. **Upload a video:**
   - Click "Upload your video"
   - Select a file (MP4, AVI, MOV, MKV)
   - Ideal: Traffic videos, security cameras, urban monitoring

4. **Adjust settings (optional):**
   - Use the slider in the sidebar to adjust the confidence threshold
   - Higher values = fewer detections but more accurate
   - Lower values = more detections but may include false positives

5. **Analyze movement:**
   - Click "🚀 Detect Objects"
   - Wait while the video is processed with tracking
   - The system automatically tracks each vehicle and person

6. **Visualize results:**
   - **Processed video**: With bounding boxes, trajectories, speeds, and times
   - **Green lines**: Show the trajectory of each object
   - **Yellow text**: Current speed in px/s
   - **Cyan text**: Time spent in scene

7. **Analyze statistics:**
   - Detailed table with data for each tracked object
   - Aggregate metrics: total objects, average times, speeds
   - Distances traveled by each vehicle/person

8. **Download the result:**
   - Click "⬇️ Download Processed Video"
   - The video includes all annotations and trajectories

## 📋 Trackable Objects

The system is specially optimized for:

### 🚗 Vehicles (Priority Analysis)
- **Cars**: Sedans, SUVs, private vehicles
- **Motorcycles**: All types of motorcycles
- **Buses**: Public transportation
- **Trucks**: Cargo vehicles
- **Bicycles**: Cyclists and bicycles

### 👥 People (Priority Analysis)
- **Pedestrians**: Walking people
- **People in motion**: Running, moving
- **Groups of people**: Crowds and gatherings

### 🚦 Road Context Elements
- Traffic lights
- Stop signs
- Fire hydrants
- Benches and street furniture

### 🐕 Others (Additional Capability)
- Domestic animals (dogs, cats)
- Other vehicles (trains, planes, boats)
- 70+ additional object categories

**Note**: Although the system can detect 80+ categories, tracking and movement analysis are specially optimized for vehicles and people.

## 🛠️ Technologies Used

- **Streamlit**: Framework for interactive web interface
- **YOLOv8**: State-of-the-art object detection and tracking model
- **OpenCV**: Video processing and frame analysis
- **Ultralytics**: Advanced YOLO implementation with tracking
- **NumPy**: Speed, distance calculations and numerical operations
- **Pandas**: Data analysis and statistical presentation

## 🎯 Use Cases

### 🚦 Traffic Analysis
- Vehicle counting at intersections
- Vehicle flow measurement
- Traffic pattern identification
- Average speed analysis

### 🏙️ Urban Monitoring
- Pedestrian zone analysis
- Pedestrian behavior study
- Crowd detection
- Dwell time in specific areas

### 🔒 Security and Surveillance
- Tracking suspicious people and vehicles
- Access monitoring
- Unusual movement analysis
- Complete trajectory recording

### 📊 Mobility Studies
- Movement pattern analysis
- Road usage statistics
- Vehicle behavior studies
- Data-driven urban planning

## ⚙️ Advanced Configuration

### Change YOLO Model

By default, `yolov8n.pt` (nano) is used, which is fast but less accurate. You can switch to larger models on line 26 of the code:

```python
# Available options:
model = YOLO('yolov8n.pt')  # Nano (faster) ⚡
model = YOLO('yolov8s.pt')  # Small
model = YOLO('yolov8m.pt')  # Medium
model = YOLO('yolov8l.pt')  # Large
model = YOLO('yolov8x.pt')  # Extra Large (more accurate) 🎯
```

### Adjust Performance

- For long videos, consider reducing resolution
- Adjust processing FPS if you need more speed
- Use the nano model (yolov8n) for faster processing

## 🐛 Troubleshooting

### DLL Error on Windows (WinError 1114)
This is a common issue with PyTorch on Windows. Solution:
```bash
# Run the included repair script
fix_dependencies.bat
```

Or manually:
```bash
pip install torch==2.0.1 torchvision==0.15.2 --index-url https://download.pytorch.org/whl/cpu
pip install "numpy<2" opencv-python==4.10.0.84
```

### Error Loading Model
```bash
pip install --upgrade ultralytics
```

### OpenCV Issues
```bash
pip install opencv-python-headless==4.10.0.84
```

### Video Won't Play
- Make sure the video is in a compatible format (MP4, AVI, MOV, MKV)
- Try a different codec

### Processing is Very Slow
- Use the `yolov8n.pt` (nano) model
- Reduce input video resolution
- Process only part of the video

## 🌐 Deploy on Streamlit Cloud

To deploy your own version:

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select the repository and branch
5. The main file is `video_detector.py`
6. Automatic deployment!

The necessary files are already configured:
- `requirements.txt`: Python dependencies
- `packages.txt`: System dependencies (Linux)
- `.streamlit/config.toml`: App configuration

## 📝 Important Notes

- The first processing may take longer due to model download
- Processing time depends on:
  - Video duration
  - Video resolution
  - YOLO model used
  - Number of moving objects
  - Your hardware capacity
- High-resolution and long-duration videos require more time and resources
- Tracking works best with stable videos (without abrupt camera movements)
- For best results in traffic analysis, use videos with a fixed camera

## 📊 Exportable Data

The application generates the following data for each tracked object:
- **Unique ID**: Object identifier throughout the video
- **Class**: Object type (car, person, motorcycle, etc.)
- **Time in scene**: Seconds the object was visible
- **Distance traveled**: Total distance in pixels
- **Average speed**: Mean speed in pixels per second
- **Detected frames**: Number of frames where the object appeared

This data can be analyzed later for statistical studies or reports.

## 🤝 Contributions

Contributions are welcome! If you find any bugs or have suggestions for improvement, don't hesitate to report them.

## 📄 License

This project uses:
- YOLOv8: AGPL-3.0 License
- Streamlit: Apache 2.0 License

## 🙏 Acknowledgments

- [Ultralytics](https://github.com/ultralytics/ultralytics) for YOLOv8
- [Streamlit](https://streamlit.io/) for the framework
- The Open Source community

---

**Analyze vehicle and people movement with artificial intelligence! 🚗👥📊**
