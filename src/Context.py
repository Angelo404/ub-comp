import os
import threading
import pygame


class Context:

    def __init__(self):
        self.state = {}
        self.stateLock = threading.Lock()
        self.update("Sensors:Door:BedRoom", "open")
        self.update("Sensors:Lights:Desk", "0")
        self.update("Sensors:Door:BedRoom", "Closed")

    def update(self, key, value):
        with self.stateLock:
            self.state[key] = value

        self.onContextChanged(key, value)
        self.printContext()

    def playSound(self):
        os.system("aplay /home/pi/police_s.wav")

    def onContextChanged(self, key, value):
        if "Door" in key and value == "Open":
            self.playSound()

    def printContext(self):
        print "State: {}".format(self.state)