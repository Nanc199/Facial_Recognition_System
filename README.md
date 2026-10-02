# 👤  Facial Recognition System

A Python-based computer vision project built using OpenCV. This project demonstrates real-time face and eye detection along with image, video, camera, color, shape, blur, edge detection, and frame-processing operations.

---

## ✨ Features

- 👤 Face detection
- 👁️ Eye detection
- 🎥 Face detection in video
- 📷 Camera input and processing
- 🖼️ Image reading and processing
- 🎬 Video reading and processing
- 🌫️ Image and video blurring
- 📐 Edge detection
- 🔷 Shape detection and processing
- 🎨 Color processing
- ✏️ Writing text on image frames
- 📝 Writing text on videos
- ⚡ Real-time computer vision processing

---

## 🛠️ Tech Stack

- **Python**
- **OpenCV**
- **NumPy**
- **Computer Vision**
- **Git & GitHub**

---

## 📂 Project Structure

```text
Facial_Recognition_System/
│
├── Opencv/
│   │
│   ├── face_detection.py
│   ├── detect_eyes_in_vd.py
│   ├── detect_eyes.py
│   ├── detect_face_in_vd.py
│   ├── face_detector.py
│   │
│   ├── blur_img.py
│   ├── blur_video.py
│   ├── detect_edges.py
│   ├── learn_shapes.py
│   ├── read_cameras.py
│   ├── read_img.py
│   ├── read_video.py
│   ├── work_with_colors.py
│   ├── write_on_frames.py
│   └── write_on_video.py
│
├── .gitignore
└── README.md
```

---

## 🧩 Project Modules

### 👤 Face Detection

The project includes different Python scripts for detecting human faces using OpenCV.

- `face_detection.py`
- `face_detector.py`
- `detect_face_in_vd.py`

These scripts demonstrate face detection from images, camera input, and video.

---

### 👁️ Eye Detection

Eye detection is implemented using OpenCV-based computer vision techniques.

Files:

- `detect_eyes.py`
- `detect_eyes_in_vd.py`

The system can detect eyes from image or video input.

---

### 📷 Camera Processing

The `read_cameras.py` module is used to access and process live camera input.

It can be used as a base for real-time computer vision applications.

---

### 🖼️ Image Processing

The project contains image-processing operations using OpenCV.

File:

- `read_img.py`

It demonstrates how images can be loaded and processed using Python and OpenCV.

---

### 🎥 Video Processing

The project supports reading and processing video files.

File:

- `read_video.py`

---

### 🌫️ Image & Video Blurring

Blurring operations are demonstrated using:

- `blur_img.py`
- `blur_video.py`

These modules can be used for image and video privacy processing.

---

### 📐 Edge Detection

The `detect_edges.py` module demonstrates edge detection using OpenCV.

Edge detection can be useful for identifying boundaries and structures within images.

---

### 🔷 Shape Detection

The `learn_shapes.py` module demonstrates basic shape-related computer vision operations.

---

### 🎨 Color Processing

The `work_with_colors.py` module demonstrates working with colors and image color information using OpenCV.

---

### ✏️ Writing on Frames

The project also demonstrates how to add text or information directly onto image frames.

File:

- `write_on_frames.py`

---

### 📝 Writing on Video

The `write_on_video.py` module demonstrates adding text or information to video frames while processing video.

---


## 📸 Screenshots

<img width="478" height="379" alt="Screenshot 2026-08-25 230904" src="https://github.com/user-attachments/assets/7e7a6801-7c7f-4171-a7d7-5fb3ac8ad99c" />


<img width="470" height="348" alt="Screenshot 2026-08-25 231010" src="https://github.com/user-attachments/assets/c1938b94-5ba0-4028-aae2-bbd827b9f40f" />


## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Nanc199/Facial_Recognition_System.git
```

### 2. Navigate to the Project Directory

```bash
cd Facial_Recognition_System
```

### 3. Navigate to the OpenCV Project

```bash
cd Opencv
```

### 4. Create a Virtual Environment

```bash
python -m venv venv
```

### 5. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 6. Install Required Libraries

```bash
pip install opencv-python numpy
```

---

## ▶️ Running the Project

After activating the virtual environment, run the required Python file.

For example:

```bash
python face_detection.py
```

For eye detection:

```bash
python detect_eyes.py
```

For camera processing:

```bash
python read_cameras.py
```

For video processing:

```bash
python read_video.py
```

For image blurring:

```bash
python blur_img.py
```

For video blurring:

```bash
python blur_video.py
```

---

## 💡 How It Works

The project uses OpenCV to process different types of visual input.

### Basic Workflow

```text
Camera / Image / Video
          ↓
     OpenCV Processing
          ↓
   Detection / Processing
          ↓
   Result Displayed
```

For face detection:

```text
Camera / Video
      ↓
Read Frame
      ↓
Detect Face
      ↓
Identify Face Region
      ↓
Display Detection
```

---

## 📸 Applications

This project provides a foundation for building:

- 🔐 Face-based security systems
- 👥 Identity verification systems
- 📊 Attendance systems
- 🏢 Access control systems
- 🎥 Video surveillance applications
- 🖼️ Image processing applications
- 🤖 Computer vision applications
- 📷 Real-time camera applications

---

## 🔐 Security

- Keep API keys and sensitive credentials private.
- Do not upload `.env` files containing secret keys.
- Use `.gitignore` for sensitive configuration files.
- Do not upload private or personal facial data to public repositories.
- Store biometric data securely when developing real-world applications.

---

## 🔮 Future Improvements

- 🎯 Improve face recognition accuracy
- 👥 Support multiple face recognition
- 💾 Add database integration
- 📊 Add attendance management
- 🔐 Add secure authentication
- 🖥️ Build a graphical user interface
- 🌐 Create a web-based interface
- 📱 Add mobile support
- ☁️ Add cloud integration
- ⚡ Improve real-time processing performance

---

## 📌 Future Scope

The current OpenCV modules can be extended into a complete facial recognition and identity management system by integrating a database, face recognition models, secure biometric storage, authentication, attendance tracking, and a web-based dashboard.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push the changes to your branch.
6. Create a Pull Request.

---

## 👩‍💻 Author

**Nancy**

GitHub: [Nanc199](https://github.com/Nanc199)

---
## 📄 License

This project is created for learning and development purposes.
