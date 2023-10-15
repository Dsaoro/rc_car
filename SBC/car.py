import os
import sys
from time import sleep

import RPI.GPIO as gpio

class Car:
    
    BLINK_TIME = 0.2
    SAMPLE_TIME = 0.2

    def __init__(self,frMotorA,frMotorB,lrMotorA,lrMotorB,leftLed,rigthLed):
        
        gpio.setmode(gpio.BOARD)
        self.motor = motor(frMotorA,frMotorB)
        self.direccion = motor(lrMotorA,lrMotorB)
        self.leftLed = leftLed
        self.rigthLed = rigthLed 
        gpio.setcfg(self.leftLed, gpio.OUTPUT)
        gpio.setcfg(self.rigthLed, gpio.OUTPUT)

        
    def forward(self,speed,direction):
        if(direction<125):
            print("forward <")
            self.direccion.Backward()
            sleep(self.SAMPLE_TIME)
            self.direccion.stop()
        elif(direction>125):
            print("forward >")
            self.direccion.forward()
            sleep(self.SAMPLE_TIME)
            self.direccion.stop()
        if(speed >125):
            self.motor.forward()
            sleep(self.SAMPLE_TIME)
            self.motor.stop()
        print("forward")

    def reverse(self,speed, direction):
        if(direction<125):
            print("reverse <")
            self.direccion.Backward()
            sleep(self.SAMPLE_TIME)
            self.direccion.stop()
        elif(direction>125):
            print("reverse >")
            self.direccion.forward()
            sleep(self.SAMPLE_TIME)
            self.direccion.stop()
        if(speed >125):
            self.motor.backward()
            sleep(self.SAMPLE_TIME)
            self.motor.stop()
        print("reverse")

    def blinkL(self,bTime):
        print("<")
        gpio.output(self.leftLed,1)
        sleep(self.BLINK_TIME+bTime)
        gpio.output(self.leftLed,0)

    def blinkR(self,bTime):
        print(">")
        gpio.output(self.rigthLed,1)
        sleep(self.BLINK_TIME+bTime)
        gpio.output(self.rigthLed,0)

    def blinkStop(self,bTime):
        print("<   >")
        gpio.output(self.leftLed,1)
        gpio.output(self.rigthLed,1)
        sleep(self.BLINK_TIME+bTime)
        gpio.output(self.leftLed,0)
        gpio.output(self.rigthLed,0)
    
    def shutdown(self,bTime):
        print("the car is shuting down")
        gpio.cleanup();

class motor:
    
    SAMPLE_TIME=0.2

    def __init__(self, ina, inb):
        self.ina
        self.inb
        gpio.setup(ina, gpio.OUT)
        gpio.setup(inb, gpio.OUT)

    def forward(self):
        gpio.output(self.ina, 1)
        gpio.output(self.inb, 0)

    def Backward(self):
        gpio.output(self.ina, 0)
        gpio.output(self.inb, 1)

    def forwardSpeed(self,speed):
        gpio.output(self.ina, 1)
        gpio.output(self.inb, 0)

    def BackwardSpeed(self,speed):
        gpio.output(self.ina, 0)
        gpio.output(self.inb, 1)

    def stop(self):
        gpio.output(self.ina, 0)
        gpio.output(self.inb, 0)


    


