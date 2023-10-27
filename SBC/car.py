import os
import sys
from time import sleep

import RPI.GPIO as gpio

# class Car:
    
#     BLINK_TIME = 0.2
#     SAMPLE_TIME = 0.2

#     def __init__(self,frMotorA,frMotorB,lrMotorA,lrMotorB,leftLed,rigthLed):
        
#         gpio.setmode(gpio.BOARD)
#         self.motor = motor(frMotorA,frMotorB)
#         self.direccion = motor(lrMotorA,lrMotorB)
#         self.leftLed = leftLed
#         self.rigthLed = rigthLed 
#         gpio.setcfg(self.leftLed, gpio.gpio.OUTPUT)
#         gpio.setcfg(self.rigthLed, gpio.gpio.OUTPUT)

        
#     def forward(self,speed,direction):
#         if(direction<125):
#             print("forward <")
#             self.direccion.Backward()
#             sleep(self.SAMPLE_TIME)
#             self.direccion.stop()
#         elif(direction>125):
#             print("forward >")
#             self.direccion.forward()
#             sleep(self.SAMPLE_TIME)
#             self.direccion.stop()
#         if(speed >125):
#             self.motor.forward()
#             sleep(self.SAMPLE_TIME)
#             self.motor.stop()
#         print("forward")

#     def reverse(self,speed, direction):
#         if(direction<125):
#             print("reverse <")
#             self.direccion.Backward()
#             sleep(self.SAMPLE_TIME)
#             self.direccion.stop()
#         elif(direction>125):
#             print("reverse >")
#             self.direccion.forward()
#             sleep(self.SAMPLE_TIME)
#             self.direccion.stop()
#         if(speed >125):
#             self.motor.backward()
#             sleep(self.SAMPLE_TIME)
#             self.motor.stop()
#         print("reverse")

#     def blinkL(self,bTime):
#         print("<")
#         gpio.gpio.output(self.leftLed,1)
#         sleep(self.BLINK_TIME+bTime)
#         gpio.gpio.output(self.leftLed,0)

#     def blinkR(self,bTime):
#         print(">")
#         gpio.gpio.output(self.rigthLed,1)
#         sleep(self.BLINK_TIME+bTime)
#         gpio.gpio.output(self.rigthLed,0)

#     def blinkStop(self,bTime):
#         print("<   >")
#         gpio.gpio.output(self.leftLed,1)
#         gpio.gpio.output(self.rigthLed,1)
#         sleep(self.BLINK_TIME+bTime)
#         gpio.gpio.output(self.leftLed,0)
#         gpio.gpio.output(self.rigthLed,0)
    
#     def shutdown(self,bTime):
#         print("the car is shuting down")
#         gpio.cleanup();

# class motor:
    
#     SAMPLE_TIME=0.2

#     def __init__(self, ina, inb):
#         self.ina
#         self.inb
#         gpio.setup(ina, gpio.gpio.OUT)
#         gpio.setup(inb, gpio.gpio.OUT)

#     def forward(self):
#         gpio.gpio.output(self.ina, 1)
#         gpio.gpio.output(self.inb, 0)

#     def Backward(self):
#         gpio.gpio.output(self.ina, 0)
#         gpio.gpio.output(self.inb, 1)

#     def forwardSpeed(self,speed):
#         gpio.gpio.output(self.ina, 1)
#         gpio.gpio.output(self.inb, 0)

#     def BackwardSpeed(self,speed):
#         gpio.gpio.output(self.ina, 0)
#         gpio.gpio.output(self.inb, 1)

#     def stop(self):
#         gpio.gpio.output(self.ina, 0)
#         gpio.gpio.output(self.inb, 0)

gpio.setmode(gpio, gpio.BOARD)

leftMotorC = 1
rightMotorC = 2
fowardMotorP = 3
backwardMotorP = 4

dutyCycle = 50

Stop = 0

gpio.setup(leftMotorC, gpio.OUT)
gpio.setup(rightMotorC, gpio.OUT)
gpio.setup(fowardMotorP, gpio.OUT)
gpio.setup(backwardMotorP, gpio.OUT)

pwmLeftMotorC = gpio.PWM(leftMotorC, 100)
pwmRightMotorC = gpio.PWM(rightMotorC, 100)
pwmFowardMotorP = gpio.PWM(fowardMotorP, 100)
pwmBackwardMotorP = gpio.PWM(backwardMotorP, 100)


def Left():
    pwmLeftMotorC.ChangeDutyCycle(50) #50% ciclo de trabajo giro izquierda
    pwmRightMotorC.ChangeDutyCycle(0)
    pwmFowardMotorP.ChangeDutyCycle(0)
    pwmBackwardMotorP.ChangeDutyCycle(0)

def Right():
    pwmLeftMotorC.ChangeDutyCycle(0) 
    pwmRightMotorC.ChangeDutyCycle(50) #50% giro derecha
    pwmFowardMotorP.ChangeDutyCycle(0)
    pwmBackwardMotorP.ChangeDutyCycle(0)

def Foward():
    pwmLeftMotorC.ChangeDutyCycle(0) 
    pwmRightMotorC.ChangeDutyCycle(0)
    pwmFowardMotorP.ChangeDutyCycle(50) #adelante
    pwmBackwardMotorP.ChangeDutyCycle(0)

def Backward():
    pwmLeftMotorC.ChangeDutyCycle(0) 
    pwmRightMotorC.ChangeDutyCycle(0)
    pwmFowardMotorP.ChangeDutyCycle(0)
    pwmBackwardMotorP.ChangeDutyCycle(50) #atrás





