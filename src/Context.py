import threading


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

    def onContextChanged(self, key, value):
        # Do actions based on the changed context
        pass

    def printContext(self):
        print "State: {}".format(self.state)