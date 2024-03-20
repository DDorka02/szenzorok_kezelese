#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Feladatok():

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

    def akku(self):
       print("Az akkumulátor töltési szintje: "+str(int(self.ev3.battery.voltage())/1000)+" V")
       akkuErtek = "Az akkumulátor töltési \n szintje: "+str(int(self.ev3.battery.voltage())/1000)+" V"
       self.ev3.screen.print(akkuErtek)
       wait(1000)

    def feladat1(self):
        while(self.cs.reflection()>39.5):
            self.robot.drive(100,0)
            print("Szín:"+str(self.cs.reflection()))
        self.robot.stop(Stop.BRAKE)

        #asztal lap: 53
        #fekete vonal:8
        #asztal széle:0
        #asztal széle fele:26

    def visszamenes(self):
        self.ido.reset()
        while(self.cs.reflection()>39.5):
            self.robot.drive(100,0)
        self.robot.stop(Stop.BRAKE)
        elteltIdo = self.ido.time()
        self.ido.pause()
        self.robot.drive(-100,0)
        wait(elteltIdo)
        self.robot.stop(Stop.BRAKE)


    def utbautkozes(self):
        while(self.us.distance()>100):
            self.robot.drive(self.us.distance(),0)
            print("Távolság:"+str(self.us.distance()))
        self.robot.stop(Stop.BRAKE)

    def csipog(self):
        self.ev3.speaker.beep()

    def vonalrajzolas2(self):
        self.robot.drive(100,0)
        self.ido.reset()
        hol = 0
        while (self.ido.time()<3000):
            if (self.cs.reflection()>40):
                self.ev3.screen.draw_line(hol,0,hol,127)
            hol += 1
            wait(3000/170)
        self.robot.stop(Stop.BRAKE)
        wait(10000)

    def vonalutanmegall(self):
        while(self.cs.reflection()>30):
            self.robot.drive(100,0)
        while(self.cs.reflection()<30):
            self.robot.drive(100,0)
        self.robot.stop(Stop.BRAKE)

        
