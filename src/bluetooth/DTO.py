
import json

class DTO():
	
	def __init__(self, TerminateFlag, HeartBeatFlag, IsLightOn, IsHandshake, Data = "None"):

		self.TerminateFlag = TerminateFlag
		self.HeartBeatFlag = HeartBeatFlag
		self.IsLightOn = IsLightOn
		self.IsHandshake = IsHandshake
		self.Data = Data
		self.Pckg = []

	def createPckg(self):
		self.Pckg = {
			"TerminateFlag": self.TerminateFlag,
			"HeartBeatFlag": self.HeartBeatFlag,
			"IsLightOn": self.IsLightOn,
			"IsHandshake": self.IsHandshake,
			"Password": "WeAreAllMadHere",
			"Data": self.Data
		}
		return json.dumps(self.Pckg)

if __name__ == "__main__":
	dto = DTO(False, False, False, False, "asdf")
	dto.createPckg()