# Heart Rate Monitoring and Drowsiness Detection System

## Project Overview

The Drowsiness Detection System is a real-time application designed to monitor driver alertness using facial landmark analysis and Eye Aspect Ratio (EAR) calculations. It identifies early signs of fatigue by continuously tracking eye state through a webcam feed, providing timely alerts to prevent accidents caused by driver drowsiness. This project uses the dlib library for facial landmark detection and OpenCV for real-time video processing.

## Key Features

* **Real-Time Eye State Detection:** Continuously monitors eye openness using EAR.
* **Percentage Calculation:** Computes the proportion of open and closed eye frames.
* **Alert System:** Triggers a visual alert if eyes remain closed for a significant duration.
* **Integrated Web Dashboard:** Includes a Flask-based dashboard for real-time monitoring and control.
* **Scalable and Hardware-Free:** Requires only a webcam, eliminating the need for specialized hardware.
* **Flexible Testing:** Supports simulated heart rate data for experimental evaluation.
* **Real-Time Eye State Detection:** Continuously monitors eye openness using EAR.
* **Percentage Calculation:** Computes the proportion of open and closed eye frames.
* **Alert System:** Triggers a visual alert if eyes remain closed for a significant duration.
* **Scalable and Hardware-Free:** Requires only a webcam, eliminating the need for specialized hardware.
* **Flexible Testing:** Supports simulated heart rate data for experimental evaluation.

## Requirements

Ensure the following packages are installed:

```bash
pip install numpy opencv-python dlib imutils
```

Additionally, download the **shape predictor** file:

* **shape\_predictor\_68\_face\_landmarks.dat** (Available from the [dlib model repository](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2))

## File Structure

```
.
├── drowsy.py                      # Main detection script
├── app.py                         # Flask web server for dashboard
├── templates/                     # HTML templates for the web interface
│   ├── login.html                # Login page
│   ├── index.html                # Main dashboard
│   ├── pages/                    # Additional dashboard pages
│   └── ...
├── README.md                      # Project documentation
├── shape_predictor_68_face_landmarks.dat  # Facial landmark model
└── requirements.txt               # Required packages
```

```
.
├── drowsy.py                      # Main detection script
├── README.md                      # Project documentation
├── shape_predictor_68_face_landmarks.dat  # Facial landmark model
└── requirements.txt               # Required packages
```

## Running the System

To access the system, use the following login credentials:

* **Email:** [ljleo20@gmail.com](mailto:example@example.com)
* **Password:** 123456

To run the drowsiness detection system, execute the **drowsy.py** script:

```bash
python drowsy.py
```

This will start the real-time video feed with eye state detection and alert features.

To run the Flask web server for the dashboard:

```bash
python app.py
```

This will start the dashboard interface, allowing you to monitor the drowsiness detection system remotely.
To access the system, use the following login credentials:

* **Email:** \[[ljleo20@gmail.com](mailto:your-email@example.com)]
* **Password:** \[123456]

To run the drowsiness detection system, execute the **app.py** script:

```bash
python app.py
```

This will start the real-time video feed with eye state detection and alert features.

## Code Description (drowsy.py)

The main detection script includes the following components:

1. **Eye Aspect Ratio (EAR) Calculation**

   * Computes the EAR using six key facial landmarks for each eye.
   * EAR formula:

```
EAR = (||p2 - p6|| + ||p3 - p5||) / (2 * ||p1 - p4||)
```

2. **Real-Time Detection and Buffering**

   * Uses a sliding window buffer to calculate the percentage of open and closed frames.

3. **Alert System**

   * Triggers visual alerts when the closed percentage exceeds a predefined threshold.

## Performance and Evaluation

The system's performance is evaluated based on its ability to accurately identify and respond to early signs of driver fatigue. Key performance indicators include:

* **Detection Accuracy:** Correctly classifies frames as open or closed based on EAR.
* **Alert Responsiveness:** Quickly triggers alerts upon detecting prolonged eye closures.
* **System Stability:** Consistently identifies drowsiness across various lighting conditions and head positions.

## Future Work

* Integrate machine learning for adaptive thresholding.
* Add sound alerts for better driver notification.
* Implement logging for long-term performance analysis.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
