import random
import math
class sand(object):
	def __init__(self,position):
		self.partPosition = list(position)
		self.speed = random.randrange(1,15)
		self.angle = random.randrange(1,180)

		self.XSlope = math.cos(math.radians(self.angle)) 
		self.YSlope = math.sin(math.radians(self.angle))

		self.partX = self.partPosition[0]
		self.partY = self.partPosition[1]

		self.color = (random.randrange(1,255),
			random.randrange(1,255),
			random.randrange(1,255))
	def setPosition(self,position):
		self.partPosition = position
	def setPositionX(self,positionX):
		self.partPosition[0] = positionX
	def setPositionY(self,positionY):
		self.partPosition[1] = positionY
	def setSpeed(self,speed):
		self.speed = speed
	def setAngle(self,angle):
		self.angle = angle
		self.XSlope = math.cos(math.radians(self.angle)) 
		self.YSlope = math.sin(math.radians(self.angle))

	def getPosition(self):
		return self.partPosition
	def getPositionX(self):
		return self.partPosition[0]
	def getPositionY(self):
		return self.partPosition[1]
	def getSpeed(self):
		return self.speed
	def getAngle(self):
		return self.angle
	def getSlope(self):
		return (self.XSlope,self.YSlope)