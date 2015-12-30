
import bluetooth
from Bluetooth import Bluetooth
from DTO import DTO

class Client(Bluetooth):

	def __init__(self):
		super(self.__class__, self).__init__()

		self.serverAddr = "54:35:30:D4:11:AE"

		self.socket.connect((self.serverAddr, self.port))

		handShakeDTO = DTO(False, False, False, True, "testing")

		self.socket.send(handShakeDTO.createPckg())

		self.socket.close()

if __name__ == "__main__":
	Client()