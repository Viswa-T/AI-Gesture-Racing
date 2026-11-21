# 🏎️ AI Gesture Racing

### Control Racing Games Using Hand Gestures | Computer Vision | Python | OpenCV | MediaPipe

AI Gesture Racing is a computer vision-based project that allows users to control racing games using real-time hand gestures through a webcam.

Instead of using a physical keyboard, the system tracks hand movements, detects steering gestures, and translates them into keyboard inputs to control a racing car.

## 🚀 Features

- 📷 Real-time webcam integration.
- ✋ Hand tracking using MediaPipe.
- 🎯 Detection of 21 hand landmarks.
- 🤲 Two-hand gesture recognition.
- 🏎️ Gesture-based left and right steering.
- ⌨️ Keyboard automation using PyAutoGUI.
- ⚡ Real-time gesture processing.
- 🎥 Live visual feedback with OpenCV.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Webcam capture and image processing |
| MediaPipe | Hand landmark detection |
| NumPy | Numerical operations |
| PyAutoGUI | Keyboard automation |

## 🧠 How It Works

The project follows a real-time computer vision pipeline:

Webcam → OpenCV → MediaPipe → Hand Detection → Hand Landmarks (21 Points) → Gesture Recognition → PyAutoGUI → Keyboard Input → Racing Game

### Working Process

1. The webcam captures live video frames.
2. OpenCV processes the captured frames.
3. MediaPipe detects hands and identifies 21 landmarks per hand.
4. The gesture recognition module analyzes hand positions.
5. Detected gestures are converted into steering directions.
6. PyAutoGUI sends corresponding keyboard inputs to the active racing game.

## 📂 Project Structure

AI-Gesture-Racing/

├── main.py  
├── hand_tracking.py  
├── gesture_control.py  
├── hand_landmarker.task  
├── requirements.txt  
├── README.md  
└── .gitignore

## ⚙️ Installation and Setup

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/AI-Gesture-Racing.git

### 2. Navigate to the project directory

cd AI-Gesture-Racing

### 3. Create a virtual environment

python -m venv venv

### 4. Activate the virtual environment

Windows:

venv\Scripts\activate

### 5. Install dependencies

pip install -r requirements.txt

### 6. Run the application

python main.py

## 📦 Dependencies

- opencv-python
- mediapipe
- numpy
- pyautogui

## 🎮 Controls

| Hand Gesture | Game Action |
|---|---|
| Steering gesture to the left | Steer Left |
| Steering gesture to the right | Steer Right |
| Neutral steering position | Release steering keys |
| Hands not detected | Release steering keys |

*The exact steering behaviour depends on the selected gesture-control implementation.*

## 🔮 Future Improvements

- [ ] More accurate two-hand steering-wheel rotation detection.
- [ ] Gesture-based acceleration.
- [ ] Gesture-based braking.
- [ ] Nitro activation using hand gestures.
- [ ] Gesture smoothing and noise reduction.
- [ ] GPU acceleration for faster hand tracking.
- [ ] Improved compatibility with different racing games.
- [ ] Performance optimization for higher FPS.

## 🎯 Project Objective

The main objective is to explore the integration of computer vision and human-computer interaction by creating a hands-free gaming control system.

This project demonstrates how real-time hand tracking and gesture recognition can be used to interact with existing applications without traditional input devices.

## 👨‍💻 Author

Viswa

GitHub: https://github.com/Viswa-T

⭐ If you find this project interesting, consider giving it a star!
