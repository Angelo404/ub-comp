
import bluetooth
import json
from Bluetooth import Bluetooth
from RcvDataThread import RcvDataThread

class Server(Bluetooth):

	def __init__(self):
		super(self.__class__, self).__init__()

		#Address -> Name hash table
		self.listOfPeople = {}
		#Bind the socket
		self.socket.bind(("54:35:30:D4:11:AE",self.port))
		#Password for the trusting devices.
		self.password = "WeAreAllMadHere"

		while True:

			#Accept connections and recieve the very first package
			self.socket.listen(1)
			clientSocket,address = self.socket.accept()
			data = clientSocket.recv(1024)

			#debug line
			print (data)

			#Parse data into something readable
			data = json.loads(data)

			#Check if its a trusting device
			if data["IsHandshake"] == True and self.authentication(data):
				#add the device name and address to the hash table
				self.listOfPeople[str(bluetooth.lookup_name(address[0], 10))] = address[0]

				#Create and run thread to receive data
				rcvDataTh = RcvDataThread(clientSocket, address[0])
				rcvDataTh.start()
				break
			else:
				clientSocket.close()
				continue

		rcvDataTh.join()
		self.socket.close()

	def authentication(self, data):
		"""
		This will ensure that the device connected is trustworthy.
		"""
		if data["Password"] == self.password:
			return True
		return False

if __name__ == "__main__":
	Server()
