# Drowsiness Detection System

This project implements a drowsiness detection system using computer vision and machine learning techniques. The system captures video from a webcam, detects the driver's face, and analyzes the eye aspect ratio (EAR) to determine if the driver is drowsy. If drowsiness is detected, the system provides audio and visual alerts.

## Features

- Real-time face and eye detection using dlib and OpenCV.
- Calculates the Eye Aspect Ratio (EAR) to assess drowsiness.
- Provides audio alerts using text-to-speech.
- Sounds a buzzer when drowsiness is detected.
- Displays a "Drowsy" message on the video feed.

## Requirements

To run this project, you need to have the following Python packages installed:

- `opencv-python`
- `dlib`
- `scipy`
- `numpy`
- `pyttsx3`
- `winsound` (Windows only)

- `You need the "shape_predictor_68_face_landmarks.dat" to execute code`
