
import threading
import json

class AcceptingConnectionThread(threading.Thread):
	
	def __init__(self, socket, tmpListOfPeople):
		threading.Thread.__init__(self)
		self._stop = threading.Event()
		self.socket = socket
		self.tmpListOfPeople = tmpListOfPeople
		self.password = "WeAreAllMadHere"

	def run(self):
		while True:
			self.socket.listen(1)
			clientSocket,address = self.socket.accept()
			self.tmpListOfPeople.append((clientSocket,address))
			data = clientSocket.recv(1024)
			print (data)
			data = json.loads(data)
			if data["IsHandshake"] == True:
				print "ITS A HANDSHAKE MOTHERFUCKER"
				tmp = json.loads(data)
				print tmp
			break
		clientSocket.close()
		self.socket.close()

	def terminateThread(self):
		exit()


