
import json
import threading

class RcvDataThread(threading.Thread):
	
	def __init__(self, clientSocket, threadID):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.clientSocket = clientSocket


	def run(self):
		print "running thread: " + self.threadID
		while True:
			data = self.clientSocket.recv(1024)
			data = json.loads(data)
			print data
			if data["TerminateFlag"] == True:
				print "WE ARE NOW EXITING"