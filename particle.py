class sand(object):
	def __init__(self,position):
		self.partPosition = position
		self.partX = partPosition[0]
		self.partY = partPosition[1]
	def setPosition(self,position):
		self.partPosition = position
	def setX(self,positionX):
		self.partPosition[0] = positionX
	def setY(self,positionY):
		self.partPosition[1] = positionY

	def getPosition(self):
		return self.partPosition
	def getPositionX(self):
		return self.partPosition[0]
	def getPositionX(self):
		return self.partPosition[1]