# 😴 Real-time Drowsiness Detection System

This project implements an intelligent, real-time **Drowsiness Detection System** designed to enhance safety by monitoring a user's eye movements. Utilizing computer vision and machine learning techniques, the system actively detects signs of drowsiness and provides immediate audio and visual alerts to prevent accidents caused by fatigue.

Perfect for drivers, long-hour workers, or anyone who needs to stay alert, this system offers a practical application of machine learning in daily life.

-----

## ✨ Features

  * **Real-time Monitoring**: Continuously processes live video feed from a webcam.
  * **Facial Landmark Detection**: Accurately identifies key facial features, particularly around the eyes, using `dlib`.
  * **Eye Aspect Ratio (EAR) Analysis**: Calculates the EAR to quantify eye openness, serving as a robust indicator of drowsiness.
  * **Intelligent Alert System**:
      * **Audio Warnings**: Provides spoken alerts (e.g., "Drowsy\!") via text-to-speech.
      * **Buzzer Sound**: Triggers an audible buzzer sound for immediate attention.
      * **Visual Cues**: Displays a "Drowsy" message directly on the video feed.
  * **Configurable Thresholds**: Easily adjust sensitivity for eye closure duration.

-----

## 🚀 Getting Started

Follow these steps to set up and run the Drowsiness Detection System on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

  * **Python 3.x**
  * **`shape_predictor_68_face_landmarks.dat`**: This file is crucial for `dlib` to detect facial landmarks. You can download it from [this link](https://www.google.com/search?q=http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) (you'll need to uncompress it). Place this file in the same directory as `main_drowsy.py`.

### Installation

1.  **Clone the Repository (if applicable)**:
    If this project is part of a larger repository, navigate to its directory.

    ```bash
    git clone https://github.com/YourUsername/YourRepoName.git # Replace with your repo URL
    cd YourRepoName/DrowsinessDetectionSystem # Adjust path as necessary
    ```

2.  **Create a Virtual Environment (Recommended)**:
    It's good practice to use a virtual environment to manage project dependencies.

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install Dependencies**:
    All required Python packages are listed in `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

      * **Note for Windows users**: `winsound` is a built-in module for Windows and doesn't need to be installed via `pip`.
      * **Note for Linux/macOS users**: For audio alerts, `pyttsx3` might require additional setup for speech engines (e.g., `espeak`, `nsspeechsynthesizer`). Refer to `pyttsx3` documentation for details.

### Running the System

1.  **Ensure `shape_predictor_68_face_landmarks.dat` is in the correct directory.**
2.  **Execute the main script**:
    ```bash
    python main_drowsy.py
    ```
    Your webcam feed should open, and the system will start monitoring for drowsiness.

-----

## 🛠 Technologies Used

  * **Python**: Core programming language.
  * **OpenCV**: For real-time video capture and image processing.
  * **dlib**: For robust face detection and facial landmark prediction.
  * **NumPy**: For numerical operations, especially with array manipulations.
  * **SciPy**: Specifically for `scipy.spatial.distance.euclidean` to calculate distances for EAR.
  * **pyttsx3**: For text-to-speech audio alerts.
  * **winsound**: For playing buzzer sounds (Windows-specific).
  * **threading**: To manage concurrent audio alerts without freezing the video feed.

-----

## 🤝 Contributing

We welcome contributions to improve this project\! If you have ideas for new features, bug fixes, or performance enhancements, please feel free to:

  * Open an issue
  * Submit a pull request

-----

## 🙏 Acknowledgments

  * Inspired by various computer vision and machine learning tutorials on drowsiness detection.
  * Thanks to the `dlib` and `OpenCV` communities for their robust libraries.

-----
