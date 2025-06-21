# Hand Gesture Volume Control 🖐️🔊

A real-time computer vision application that allows users to control system volume using hand gestures captured through a webcam. Built with MediaPipe, OpenCV, and platform-specific audio control libraries.

## Overview

The Hand Gesture Volume Control system uses advanced computer vision and machine learning to detect hand landmarks and translate finger movements into volume control commands. By measuring the distance between the thumb and index finger, users can intuitively adjust their system's audio volume without touching any physical controls.

## Key Features

### 🎯 Real-Time Hand Detection
- **MediaPipe Integration**: Utilizes Google's MediaPipe for accurate hand landmark detection
- **Multi-Hand Support**: Detects and processes multiple hands simultaneously
- **Robust Tracking**: Maintains consistent tracking across varying lighting conditions
- **Low Latency**: Real-time processing with minimal delay between gesture and response

### 🔊 Volume Control Capabilities
- **Gesture-Based Control**: Pinch gesture (thumb-index finger distance) controls volume
- **Cross-Platform Audio**: Support for Windows (PyCaw) and macOS (osascript) audio systems
- **Smooth Volume Mapping**: Linear interpolation between gesture distance and volume levels
- **Visual Feedback**: Real-time visual indicators showing finger positions and connections

### 📹 Computer Vision Features
- **Live Video Processing**: Real-time webcam feed processing
- **Visual Landmarks**: Clear visualization of hand landmarks and connections
- **Gesture Visualization**: Visual feedback showing the distance line between control fingers
- **Mirror Mode**: Horizontally flipped display for natural user interaction

### 🛠️ Technical Capabilities
- **Efficient Processing**: Optimized for real-time performance
- **Scalable Architecture**: Modular design allowing for easy feature additions
- **Error Handling**: Robust error handling for various edge cases
- **Cross-Platform Support**: Compatible with Windows and macOS systems

## Prerequisites

### System Requirements
- **Operating System**: Windows 10/11 or macOS 10.14+
- **Python**: 3.7 or higher (3.8+ recommended)
- **Webcam**: Built-in or external USB camera
- **RAM**: 4GB minimum (8GB recommended)
- **Processor**: Intel i5 or equivalent (for real-time processing)

### Hardware Requirements
- **Camera**: Minimum 720p resolution webcam
- **Lighting**: Adequate lighting for hand detection (avoid backlighting)
- **Audio System**: Windows: WASAPI-compatible audio device; macOS: Standard audio output

### Software Dependencies
```bash
# Core dependencies
opencv-python>=4.5.0
mediapipe>=0.8.9
numpy>=1.21.0

# Windows-specific audio control
pycaw>=20220416        # Windows only
comtypes>=1.1.10       # Windows only

# macOS-specific audio control
osascript>=2021.1.1    # macOS only
