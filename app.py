from flask import Flask, render_template, Response
import cv2
import numpy as np

app = Flask(__name__)

first_camera = cv2.VideoCapture('assets/v1.mp4')
second_camera = cv2.VideoCapture('assets/v2.mp4')
third_camera = cv2.VideoCapture('assets/v3.mp4')


def generate_frames(camera):
    while True:
        success, frame = camera.read()

        if not success:
            # If the video reaches the end, reset to the beginning
            camera.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
        )
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_first')
def video_first():
    return Response(generate_frames(first_camera), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_second')
def video_second():
    return Response(generate_frames(second_camera), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_third')
def video_third():
    return Response(generate_frames(third_camera), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
