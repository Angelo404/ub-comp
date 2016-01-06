
import bluetooth

class Bluetooth(object):

	def __init__(self):
		self.ownAddress = None
		self.socket = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
		self.port = 2

	def Scan(self):
		"""
		This will return a list of tuples with the mac address and the device lookup_names
		[(str(address),str(name)),(str(address),str(name))]
		"""
		return bluetooth.discover_devices(lookup_names = True)

if __name__ == "__main__":
	Bluetooth()
