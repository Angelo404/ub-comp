
import bluetooth
from Bluetooth import Bluetooth

class Client(Bluetooth):

	def __init__(self):
		super(self.__class__, self).__init__()

		self.bd_addr = "54:35:30:D4:11:AE"

		self.socket.connect((self.bd_addr, self.port))

		self.socket.send("hello!!")

		self.socket.close()

if __name__ == "__main__":
	Client()
