
import bluetooth
from Bluetooth import Bluetooth
from DTO import DTO
import time

class Client(Bluetooth):
	"""
	ONLY USED IN CONNECTION MODE
	"""
	def __init__(self):
		super(self.__class__, self).__init__()

		#Declare server's address
		self.serverAddr = "54:35:30:D4:11:AE"
		#Bind the socket
		self.socket.connect((self.serverAddr, self.port))
		#Flag to keep running
		self.runningFlag = True

		#Send handshake package
		self.socket.send(DTO(False, False, False, True, "init packg").createPckg())

		while self.runningFlag:
		
			self.socket.send(DTO(False, False, False, False, "testing").createPckg())
			
			self.runningFlag = False


		self.socket.close()




if __name__ == "__main__":
	Client()