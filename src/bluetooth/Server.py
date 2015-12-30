
import bluetooth
from Bluetooth import Bluetooth
from AcceptingConnectionThread import AcceptingConnectionThread
from RcvDataThread import RcvDataThread

class Server(Bluetooth):

	def __init__(self):
		super(self.__class__, self).__init__()

		self.listOfPeople = {} # Address -> Name hash table
		self.tmpListOfPeople = []

		self.socket.bind(("54:35:30:D4:11:AE",self.port))

		#Create and run thread to accept connections
		self.accConTh = AcceptingConnectionThread(self.socket, self.tmpListOfPeople)
		self.accConTh.start()

		#Create and run thread to receive data
		#self.rcvDataTh = RcvDataThread(self.socket, self.tmpListOfPeople)
		#self.rcvDataTh.start()

		#print "Accepted connection from ",address
		#print str(bluetooth.lookup_name(address[0], 10))

		#data = self.clientSocket.recv(1024)
		#print "received [%s]" % data

		#self.TerminateConnection()
		
	def TerminateConnection(self):
		self.accConTh.join()
		self.clientSocket.close()
		self.socket.close()

if __name__ == "__main__":
	Server()
