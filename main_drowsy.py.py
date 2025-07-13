import cv2
import dlib
from scipy.spatial import distance
import numpy as np
import pyttsx3  # speech
import winsound  # buzzer
import threading  # for threading
import time  # for sleep

engine = pyttsx3.init()

# Calculate eye aspect ratio (EAR)
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Define constants for eye aspect ratio (EAR) thresholds
EAR_THRESHOLD = 0.3
CONSECUTIVE_FRAMES_THRESHOLD = 30
AWAKE_FRAMES_THRESHOLD = 15  # Number of frames to confirm the driver is awake

# Initialize the dlib face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Start capturing video
video_capture = cv2.VideoCapture(0)

global buzzer_running
# Initialize frame counters and drowsy status flag
frame_counter = 0
awake_counter = 0
drowsy = False
buzzer_thread = None
buzzer_running = False

def alert():
    """Function to handle the alert when drowsiness is detected."""
    engine.say('You are looking drowsy.')
    engine.runAndWait()

def buzzer():
    """Function to sound the buzzer continuously."""
    while buzzer_running:
        winsound.Beep(1000, 500)  # Beep at 1000 Hz for 500 ms
        time.sleep(0.5)  # Pause for a short duration before the next beep

while True:
    # Read frame from video stream
    ret, frame = video_capture.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = detector(gray)

    for face in faces:
        # Determine facial landmarks for the face
        shape = predictor(gray, face)
        shape = [(shape.part(i).x, shape.part(i).y) for i in range(68)]

        # Extract left and right eye coordinates
        left_eye = shape[36:42]
        right_eye = shape[42:48]

        # Calculate eye aspect ratio (EAR) for both eyes
        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)

        # Average the eye aspect ratios
        ear = (left_ear + right_ear) / 2.0

        # Check if eye aspect ratio is below the threshold
        if ear < EAR_THRESHOLD:
            frame_counter += 1

            # If eyes are closed for consecutive frames, indicate drowsiness
            if frame_counter >= CONSECUTIVE_FRAMES_THRESHOLD and not drowsy:
                cv2.putText(frame, "Drowsy", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                drowsy = True
                # Start the alert in a separate thread
                threading.Thread(target=alert).start()
                # Start the buzzer thread
                
                buzzer_running = True
                if buzzer_thread is None or not buzzer_thread.is_alive():
                    buzzer_thread = threading.Thread(target=buzzer)
                    buzzer_thread.start()

        else:
            frame_counter = 0
            awake_counter += 1

            # If the driver is awake for a certain number of frames, remove the drowsy message
            if awake_counter >= AWAKE_FRAMES_THRESHOLD and drowsy:
                drowsy = False
                awake_counter = 0  # Reset awake counter
                # Stop the buzzer
                buzzer_running = False

        # Draw eye regions on the frame
        cv2.polylines(frame, [np.array(left_eye)], True, (0, 255, 0), 1)
        cv2.polylines(frame, [np.array(right_eye)], True, (0, 255, 0), 1)

        # Display the "Drowsy" message if the driver is drowsy
        if drowsy:
            cv2.putText(frame, "Drowsy", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow("Drowsiness Detection", frame)

    # Quit program if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
video_capture.release()
cv2.destroyAllWindows()
