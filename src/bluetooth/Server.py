
import bluetooth
from Bluetooth import Bluetooth

class Server(Bluetooth):

	def __init__(self):
		super(self.__class__, self).__init__()

		print self.Scan()

		self.port = 3
		self.socket.bind(("01:23:45:67:89:ab",self.port))
		self.socket.listen(1)
		
		self.clientSocket,address = self.socket.accept()

		print "Accepted connection from ",address

		data = self.clientSocket.recv(1024)
		print "received [%s]" % data

		self.TerminateConnection()
		
	def TerminateConnection(self):
		self.clientSocket.close()
		self.socket.close()

if __name__ == "__main__":
	Server()