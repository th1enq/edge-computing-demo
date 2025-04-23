# Edge Computing Object Detection

A distributed system for real-time human detection using edge devices and cloud server communication.

## Overview

This project demonstrates an edge computing architecture where:

1. **Edge Device**: Captures video from a camera, runs object detection locally using YOLOv5, and sends only the detection results to the cloud server
2. **Cloud Server**: Receives and processes detection data from edge devices

This approach reduces bandwidth usage by performing computation at the edge and only transmitting the results to the cloud.

## Components

### Edge Device (`edge_device.py`)

The edge device script:
- Captures video from the device's camera
- Runs YOLOv5 object detection to identify people
- Draws bounding boxes around detected people with confidence > 0.5
- Sends detection data to the cloud server
- Displays the video with detection boxes

### Cloud Server (`cloud_server.py`)

The cloud server:
- Runs a Flask web server
- Provides a `/receive` endpoint to accept POST requests
- Prints received detection data
- Returns confirmation of receipt

### Pre-trained Model

- `yolov5s.pt`: A pre-trained YOLOv5 model for object detection

## Setup and Installation

### Prerequisites

- Python 3.x
- Webcam (for edge device)
- Internet connection

### Environment Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv myenv
   source myenv/bin/activate   # On Linux/Mac
   ```

2. Install required packages:
   ```bash
   pip install torch torchvision opencv-python flask requests ultralytics
   ```

## Usage

1. Start the cloud server:
   ```bash
   python cloud_server.py
   ```

2. In a separate terminal, run the edge device script:
   ```bash
   python edge_device.py
   ```

3. The edge device will begin capturing video, detecting people, and sending data to the cloud server.

4. Press 'q' to exit the edge device application.

## How It Works

1. The edge device captures video frames in real-time
2. YOLOv5 processes each frame to detect people
3. When a person is detected with confidence > 0.5:
   - A green bounding box is drawn around the person
   - Detection data (label, confidence, bounding box coordinates) is sent to the cloud server
4. The cloud server receives the data and can perform additional processing or storage (currently just prints the data)

## Customization

- Adjust the confidence threshold in `edge_device.py` to change detection sensitivity
- Modify the detection classes to detect objects other than people
- Enhance the cloud server to store or further process received data