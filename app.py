from flask import Flask, render_template, request, jsonify
import subprocess
from imutils import face_utils

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/maps')
def maps():
    return render_template('pages/maps.html')

@app.route('/dashboard')
def dashboard():
    return render_template('pages/dashboard.html')

@app.route('/tables')
def tables():
    return render_template('pages/tables.html')

@app.route('/virtual-reality')  
def virtual_reality():
    return render_template('pages/virtual-reality.html')

@app.route('/rtl')
def rtl():
    return render_template('pages/rtl.html')

@app.route('/profile')
def profile():
    return render_template('pages/profile.html')

@app.route('/sign-in')
def sign_in():
    return render_template('pages/sign-in.html')

@app.route('/sign-up')
def sign_up():
    return render_template('pages/sign-up.html')

@app.route('/start_drowsiness_detection', methods=['POST'])
def start_drowsiness_detection():
    # Start the drowsiness detection script
    subprocess.Popen(["python", "E://University of Canberra/Semester 3/AIT/ASSIGNMENT III/fitbit-dashboard/drowsy.py"]) 
    return "Drowsiness detection started."

@app.route('/stop_drowsiness_detection', methods=['POST'])
def stop_drowsiness_detection():
    # Stop the drowsiness detection script (you may
    #  need to implement this)
    # For simplicity, you can kill the process, but in a real scenario, you may need a more controlled termination
    subprocess.Popen(["pkill", "-f", "E://University of Canberra/Semester 3/AIT/ASSIGNMENT III/fitbit-dashboard/drowsy.py"])
    return "Drowsiness detection stopped.", 200


if __name__ == '__main__':
    app.run(debug=True)
