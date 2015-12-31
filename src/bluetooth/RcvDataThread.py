
import json
import threading

class RcvDataThread(threading.Thread):
	
	def __init__(self, clientSocket, threadID):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.clientSocket = clientSocket


	def run(self):
		print "running thread: " + self.threadID
		i = 1
		while True:
			print i
			data = self.clientSocket.recv(1024)
			data = json.loads(data)
			print data 
			if data["TerminateFlag"] == True:
				print "WE ARE NOW EXITING"

				self.clientSocket.close()
				return
<<<<<<< HEAD
=======
			i += 1
>>>>>>> 33fa3bd8e376913c2452c58c53ac0f007d0647de
