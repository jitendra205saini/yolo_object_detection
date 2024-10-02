# YOLOv8 Object Detection #

This project implements real-time object detection using the YOLOv8 model. The application captures video from a webcam, processes each frame to detect objects, and displays the results in a fullscreen window. YOLOv8 (You Only Look Once) is a state-of-the-art, real-time object detection system known for its speed and accuracy.

## Table of Contents
- Features
- Requirements
- Installation
- Usage
- How It Works
- Contributing

## Features
  
- Real-Time Detection: Detects objects in real-time from the webcam feed.
- Fullscreen Display: Provides a fullscreen window for better visibility of detections.
- Frame Rate Monitoring: Displays the frames per second (FPS) to monitor performance.
- User-Friendly Exit Options: Allows users to exit the application using the Enter key or the 'q' key.
- Object Annotation: Automatically annotates detected objects on the video feed for easy identification.

## Requirements
To run this project, you need the following:

- Python: Version 3.8 or higher.
- Libraries:
- OpenCV
- Ultralytics YOLOv8

## Installation
Follow these steps to set up the project on your local machine:

1. Clone the Repository:-<br>
Open your terminal or command prompt and run the following command:

     ```
     git clone https://github.com/yourusername/yolov8-object-detection.git
     cd yolov8-object-detection
    ```

2. Install Required Libraries:-<br>
Use pip to install the necessary Python libraries:

  ```
  pip install opencv-python ultralytics
  ```
3. Download YOLOv8 Model Weights:-<br>
Download the YOLOv8 model weights (yolov8s.pt) from the official Ultralytics YOLOv8 repository. Place the downloaded weights file in the project directory.

## Usage
To run the object detection application, follow these steps:

 1. Ensure your webcam is connected and accessible.

 2. Open a terminal or command prompt in the project directory.

 3. Execute the script with the following command:

   ```
   python your_script_name.py
   ```


 4. The application will open a fullscreen window displaying the video feed with detected objects highlighted.

 5. Press Enter or 'q' to exit the application.

## How It Works ##
- Model Initialization: The YOLOv8 model is loaded from the specified weights file.
- Webcam Capture: The application captures video frames from the webcam in real time.
- Object Detection: Each frame is processed by the YOLOv8 model to detect objects, which are then annotated on the frame.
- Display: The annotated frames are displayed in a fullscreen window for the user to see.
- Performance Monitoring: The application calculates and prints the FPS (frames per second) to the console, providing insight into the detection speed.

## Contributing

Contributions are welcome! If you would like to improve this project, please follow these guidelines:

 1. Fork the Repository: Click on the “Fork” button at the top right of this page.

 2. Create a Feature Branch: Use the command:
   ````
   git checkout -b feature/YourFeatureName
   ````
 3. Commit Your Changes: Make your changes and commit them with a meaningful message:
   ````
   git commit -m "Add some feature"
   ````
 4. Push to the Branch:

    ````
    git push origin feature/YourFeatureName
    ````
5. Create a Pull Request: Open a pull request and describe your changes.
