import os
import sys
from time import sleep

class Car:

    def __init__(self,frMotorA,frMotorB,lrMotorA,lrMotorB,leftLed,rigthLed):
        self.frMotorA = frMotorA
        self.frMotorB = frMotorB
        self.lrMotorA = lrMotorB
        self.lrMotorB = lrMotorB
        self.leftLed = leftLed
        self.rigthLed = rigthLed 
        
    def forward(speed,direction):
        if(direction<125):
            print("forward <")
        elif(direction>125):
            print("forward >")
        print("forward")

    def reverse(speed, direction):
        if(direction<125):
            print("reverse <")
        elif(direction>125):
            print("reverse >")
        print("reverse")

    def blinkL():
        print("<")
        sleep(0.2)
        print("_")

    def blinkR():
        print(">")
        sleep(0.2)
        print("_")




    


