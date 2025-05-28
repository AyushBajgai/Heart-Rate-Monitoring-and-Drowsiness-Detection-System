# drowsiness_detection.py
from scipy.spatial import distance
from imutils import face_utils
import dlib
import cv2

# Define landmarks for the left and right eyes
lStart, lEnd = 42, 48  # Example values, adjust based on your landmarks
rStart, rEnd = 36, 42  # Example values, adjust based on your landmarks

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    EAR = (A + B) / (2.0 * C)
    return EAR

def detect_drowsiness(frame):
    # Your drowsiness detection logic using the camera
    threshold_value = 0.25
    frames = 20
    detect = dlib.get_frontal_face_detector()
    predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    objects = detect(gray, 0)
    flag = 0

    for x in objects:
        shape = predict(gray, x)
        shape = face_utils.shape_to_np(shape)
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        EAR = (leftEAR + rightEAR) / 2.0

        if EAR < threshold_value:
            flag += 1
            print(flag)
            if flag >= frames:
                return True  # Drowsiness detected
        else:
            flag = 0

    return False  # No drowsiness detected