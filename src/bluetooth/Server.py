
import bluetooth
import json
from Bluetooth import Bluetooth
from RcvDataThread import RcvDataThread
import time

class Server(Bluetooth):

	def __init__(self, mode):
		super(self.__class__, self).__init__()

		#Address -> Name hash table
		self.listOfPeople = {}
		#Loads the known users
		self.loadKnownPeople()
		#Bind the socket
		self.socket.bind(("54:35:30:D4:11:AE",self.port))
		#Password for the trusting devices.
		self.password = "WeAreAllMadHere"

		#Choose between just scanning or establishing connection.
		if mode == "scanning":
			self.scanningMode()
		elif mode == "connecting":
			self.connectionMode()

		self.socket.close()


	def scanningMode(self):
		"""
		Enter scanning mode.
		"""
		for i in range(1): #TO DO needs to be set to infinite
			#Scan for devices in the surrounding area.
			listOfDevicesPresent = bluetooth.discover_devices(lookup_names = True)
			print listOfDevicesPresent #DEBUG LINE
			self.isDeviceKnown(listOfDevicesPresent)
			time.sleep(2)

	def isDeviceKnown(self, listOfDevicesPresent):
		"""
		This will check if the devices in range are known devices.
		"""
		for person in listOfDevicesPresent:
			if person[0] in self.listOfPeople:
				print "FOUND" #TO DO

	def loadKnownPeople(self):
		"""
		This will load the json file that contains all the registered users. 
		"""
		with open('usersTable.json') as usersTable:    
			self.listOfPeople = json.load(usersTable)

	def connectionMode(self):
		while True:

			#Accept connections and recieve the very first package
			self.socket.listen(1)
			#Accept the connection
			clientSocket,address = self.socket.accept()
			
			data = clientSocket.recv(1024)

			#debug line
			print (data)

			#Parse data into something readable
			data = json.loads(data)

			#Create and run thread to receive data
			rcvDataTh = RcvDataThread(clientSocket, address[0])

			#Check if its a trusting device
			if data["IsHandshake"] == True and self.authentication(data):
				break
				
		rcvDataTh.start()
		rcvDataTh.join()

	def authentication(self, data):
		"""
		This will ensure that the device connected is trustworthy.
		"""
		if data["Password"] == self.password:
			return True
		return False

if __name__ == "__main__":

	Server("scanning") #Modes -> scanning/connecting

