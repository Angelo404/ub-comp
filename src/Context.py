import os
import threading


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

    def enable_light(self):
        os.system("sudo /home/pi/bin/elro 2 B on")
        self.update("Actuators:Lights:Desk", "on")

    def sunRised(self):
        # with no information assume it is dark
        if not self.state.has_key("Sensors:Sun:Rise"):
            return False
        if not self.state.has_key("Sensors:Sun:Set"):
            return False
        sunRise = datetime.strptime(self.state["Sensors:Sun:Rise"], "%Y-%m-%dT%H:%M:%S")
        sunSet = datetime.strftime(self.state["Sensors:Sun:Set"], "%Y-%m-%dT%H:%M:%S")
        now = datetime.now()
        return sunRise < now < sunSet

    def onDoorOpened(self):
        lightOn = self.state["Actuators:Lights:Desk"] == "on"
        sun_is_shining = self.sunRised()
        if not lightOn and not sun_is_shining and self.number_of_persons_in_room() > 0:
            self.enable_light()

    def number_of_persons_in_room(self):
        persons = 0
        for key in self.state.keys():
            if "Sensors:Devices:" in key:
                if self.state[key] == "present":
                    persons += 1
        return persons

    def onContextChanged(self, key, value):
        if "Door" in key and value == "open":
            self.onDoorOpened()

    def printContext(self):
        print "State: {}".format(self.state)