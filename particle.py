class sand(object):
	def __init__(self,position):
		self.partPosition = list(position)
		self.speed = 3

		self.partX = self.partPosition[0]
		self.partY = self.partPosition[1]
	def setPosition(self,position):
		self.partPosition = position
	def setPositionX(self,positionX):
		self.partPosition[0] = positionX
	def setPositionY(self,positionY):
		self.partPosition[1] = positionY
	def setSpeed(self,speed):
		self.speed = speed

	def getPosition(self):
		return self.partPosition
	def getPositionX(self):
		return self.partPosition[0]
	def getPositionY(self):
		return self.partPosition[1]
	def getSpeed(self):
		return self.speed