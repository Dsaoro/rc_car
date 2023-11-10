from operator import le
import os
import sys
from time import sleep
from flask import Flask, render_template, Response, url_for, redirect,request,jsonify
import RPi.GPIO as gpio
# from camera import VideoCamera

try:

    # pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.

    gpio.setmode(gpio.BOARD)
    gpio.setwarnings(False)

    leftMotorC = 33
    rightMotorC = 35
    forwardMotorP = 29
    backwardMotorP = 31

    gpio.setup(leftMotorC, gpio.OUT)
    gpio.setup(rightMotorC, gpio.OUT)
    gpio.setup(forwardMotorP, gpio.OUT)
    gpio.setup(backwardMotorP, gpio.OUT)

    def Left():
        gpio.output(leftMotorC,gpio.HIGH)
        gpio.output(rightMotorC,gpio.LOW)


    def Right():
        gpio.output(leftMotorC,gpio.LOW)
        gpio.output(rightMotorC,gpio.HIGH)

    def Forward():
        gpio.output(forwardMotorP,gpio.HIGH)
        gpio.output(backwardMotorP,gpio.LOW)

    def Backward():
        gpio.output(forwardMotorP,gpio.LOW)
        gpio.output(backwardMotorP,gpio.HIGH)

    def Stop():
        gpio.output(forwardMotorP,gpio.LOW)
        gpio.output(backwardMotorP,gpio.LOW)
        gpio.output(leftMotorC,gpio.LOW)
        gpio.output(rightMotorC,gpio.LOW)

    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/left/', methods=['POST'])
    def leftMovement():
        Left()
        sleep(2)
        Stop()
        return render_template('index.html')

    @app.route('/right/', methods=['POST'])
    def rigthMovement():
        Right()
        sleep(2)
        Stop()
        return render_template('index.html')

    @app.route('/forward/', methods=['POST'])
    def forwardMovement():
        Forward()
        sleep(2)
        Stop()
        return render_template('index.html')

    @app.route('/backward/', methods=['POST'])
    def backwardMovement():
        Backward()
        sleep(2)
        Stop()
        return render_template('index.html')
    
    @app.route('/joystick', methods=['POST'])
    def recibir_datos_joystick():
        x_pos = int(request.form.get('xPos'))
        y_pos = int(request.form.get('yPos'))

        if(y_pos > 50):
            Backward()
        if(y_pos < -50):
            Forward()
        if(x_pos > 50):
            Right()
        if(x_pos < -50):
            Left()
        if(y_pos > -50 and y_pos < 50):
            gpio.output(forwardMotorP,gpio.LOW)
            gpio.output(backwardMotorP,gpio.LOW)
        if(x_pos > -50 and x_pos < 50):
            gpio.output(leftMotorC,gpio.LOW)
            gpio.output(rightMotorC,gpio.LOW)

        return jsonify({"mensaje": "Datos recibidos correctamente"})

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', threaded=True)

except EOFError:
    gpio.cleanup()
except KeyboardInterrupt:
    gpio.cleanup()
finally:
    gpio.cleanup()





