
import threading
import json
import bluetooth

from RcvDataThread import RcvDataThread

class AcceptingConnectionThread(threading.Thread):
	
	def __init__(self, socket, listOfPeople):
		threading.Thread.__init__(self)
		self._stop = threading.Event()
		self.socket = socket
		self.listOfPeople = listOfPeople
		self.password = "WeAreAllMadHere"

	def run(self):
		while True:
			self.socket.listen(1)
			clientSocket,address = self.socket.accept()
			data = clientSocket.recv(1024)
			print (data)
			data = json.loads(data)
			if data["IsHandshake"] == True and self.authentication(data):
				self.listOfPeople[str(bluetooth.lookup_name(address[0], 10))] = address[0]

				#Create and run thread to receive data
				rcvDataTh = RcvDataThread(clientSocket, address[0])
				rcvDataTh.start()
				rcvDataTh.join()
			break
		
		clientSocket.close()
		self.socket.close()


	def authentication(self, data):
		if data["Password"] == self.password:
			return True
		return False


	def terminateThread(self):
		exit()


