
import bluetooth
from Bluetooth import Bluetooth

class Client(Bluetooth):

	def __init__(self):
		super(self.__class__, self).__init__()

		self.bd_addr = "01:23:45:67:89:ab"

		self.port = 3

		self.socket.connect((self.bd_addr, self.port))

		self.socket.send("hello!!")

		self.socket.close()

if __name__ == "__main__":
	Client()