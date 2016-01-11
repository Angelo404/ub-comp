import os
import threading
import pygame


class Context:

    def __init__(self):
        self.state = {}
        self.stateLock = threading.Lock()

    def update(self, key, value):
        with self.stateLock:
            self.state[key] = value

        self.onContextChanged(key, value)
        self.printContext()

    def play_sound(self):
        os.system("aplay /home/pi/police_s.wav")

    def onContextChanged(self, key, value):
        if "Door" in key and value == "open":
            self.play_sound()

    def printContext(self):
        print "State: {}".format(self.state)