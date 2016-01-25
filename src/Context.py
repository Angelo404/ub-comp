import os
import threading
from datetime import datetime

# import SpotifyPlayer


class Context:

    def __init__(self):
        self.state = {}
        self.stateLock = threading.Lock()
        # self.spotify = SpotifyPlayer.SpotifyPlayer()
        self.update("Actuators:Lights:Desk", "off")

    def update(self, key, value):
        value = str(value)
        value = str.replace(value, "+", " ")
        with self.stateLock:
            self.state[key] = value

        self.onContextChanged(key, value)
        self.printContext()

    def play_sound(self):
        if self.spotify.isPlaying():
            self.spotify.stopPlaying()
        track_uri = 'spotify:track:0rCuRc07y6l1kPYj0JSRg5'

        self.spotify.play_track(track_uri)


    def enable_light(self):
        print "Turn on light!"
        os.system("sudo /home/pi/bin/elro 2 B on")
        self.update("Actuators:Lights:Desk", "on")

    def sunRised(self):
        print "Checking state of sun"
        # with no information assume it is dark
        if not self.state.has_key("Sensors:Sun:Rise"):
            return False
        if not self.state.has_key("Sensors:Sun:Set"):
            return False
        riseTime = str(self.state["Sensors:Sun:Rise"])
        setTime = str(self.state["Sensors:Sun:Set"])
        sunRise = datetime.strptime(riseTime, "%Y-%m-%d %H:%M:%S")
        sunSet = datetime.strptime(setTime, "%Y-%m-%d %H:%M:%S")
        now = datetime.now()
        return sunRise < now < sunSet

    def onDoorOpened(self):
        print "OnDoorOpened..."
        lightOn = self.state["Actuators:Lights:Desk"] == "on"
        print "LightOn: {}".format(lightOn)
        sun_is_shining = self.sunRised()
        print "Sun shining: {}".format(sun_is_shining)
        if not lightOn and not sun_is_shining and self.number_of_persons_in_room() > 0:
            self.enable_light()

    def getPresentDevices(self):
        persons = []
        for key in self.state.keys():
            if "Sensors:Devices:" in key:
                if self.state[key] == "present":
                    persons.append(self.state[key])
        return persons

    def number_of_persons_in_room(self):
        persons = 0
        print "Checking persons in room"
        for key in self.state.keys():
            if "Sensors:Devices:" in key:
                if self.state[key] == "present":
                    persons += 1
        print "Persons {}".format(persons)
        return persons

    def onContextChanged(self, key, value):
        if "Door" in key and value == "open":
            self.onDoorOpened()
        if "Alarms:" in key and value == "fire":
            self.play_sound()

    def printContext(self):
        print "State: {}".format(self.state)