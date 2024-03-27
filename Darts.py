#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random

class Darts():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicSensor(Port.S4)
        #self.ir = InfraredSensor(Port.S4)

        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)

        self.ido= StopWatch()


    def csipog(self):
        self.ev3.speaker.beep()

    def darts1(self):
        self.ev3.screen.clear()
        self.ev3.screen.draw_circle(90, 60, 50, fill=True, color=Color.BLACK)
        db=0
        for lovesdb in range(0,10,1):
            rLoves=2
            x= random.randint(0+rLoves,177-rLoves)
            y= random.randint(0+rLoves,127-rLoves)
            if (90-x)**2+(60-y)**2<=50**2:
                self.ev3.screen.draw_circle(x, y, rLoves, fill=True, color=Color.WHITE)
                self.ev3.speaker.beep()
                db += 1
            else:
                self.ev3.screen.draw_circle(x, y, rLoves, fill=True, color=Color.BLACK)
            wait(100)
        szoveg = "Találat:"+str(db)+"."
        self.ev3.screen.draw_text(60,110,szoveg,text_color=Color.BLACK,background_color=None)
        wait(6000)

    def darts2a(self): 
        #self.ev3.screen.draw_box(172,40,177,80,fill=True, color=Color.BLACK)
        y = random.randint(0,127)
        #self.ev3.screen.draw_circle(0, y, 2, fill=True, color=Color.BLACK)

        for i in range(184):
            self.ev3.screen.draw_box(172,40,177,80,fill=True, color=Color.BLACK)
            self.ev3.screen.draw_circle(i, y, 4, fill=True, color=Color.BLACK)
            wait(30)
            self.ev3.screen.clear()
        wait(1000)

    def darts2b(self): 
        #self.ev3.screen.draw_box(172,40,177,80,fill=True, color=Color.BLACK)
        y = random.randint(0,127)
        #self.ev3.screen.draw_circle(0, y, 2, fill=True, color=Color.BLACK)

        for i in range(184):
            self.ev3.screen.draw_box(172,40,177,80,fill=True, color=Color.BLACK)
            self.ev3.screen.draw_circle(i, y, 4, fill=True, color=Color.BLACK)
            wait(30)
            self.ev3.screen.draw_circle(i, y, 4, fill=True, color=Color.WHITE)
        wait(5000)