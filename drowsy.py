import cv2
import dlib
from imutils import face_utils
from scipy.spatial import distance
from collections import deque

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    EAR = (A + B) / (2.0 * C)
    return EAR

def detect():
    threshold_value = 0.25
    frame_buffer_size = 100
    alert_threshold = 60
    alert_frames = 20
    eye_states = deque(maxlen=frame_buffer_size)
    alert_counter = 0

    # Initialize the face detector and shape predictor
    detect_face = dlib.get_frontal_face_detector()
    predict_shape = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            print("Failed to grab a frame")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detect_face(gray)

        for face in faces:
            shape = predict_shape(gray, face)
            shape = face_utils.shape_to_np(shape)
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            EAR = (leftEAR + rightEAR) / 2.0

            # Store the current eye state (open or closed)
            if EAR < threshold_value:
                eye_states.append(0)  # Closed
            else:
                eye_states.append(1)  # Open

            # Calculate percentages from the buffer
            open_percentage = (eye_states.count(1) / len(eye_states)) * 100
            closed_percentage = (eye_states.count(0) / len(eye_states)) * 100

            # Trigger alert if closed percentage is too high
            if closed_percentage > alert_threshold:
                alert_counter += 1
                if alert_counter >= alert_frames:
                    cv2.putText(frame, "*ALERT! DROWSINESS DETECTED*", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            else:
                alert_counter = 0

            # Draw contours
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

            # Display percentages on the frame
            cv2.putText(frame, f"Eyes Open: {open_percentage:.2f}%", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            cv2.putText(frame, f"Eyes Closed: {closed_percentage:.2f}%", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q") or cv2.getWindowProperty("Frame", cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()

detect()
