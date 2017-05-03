import random
import math
from pygame import Rect
class particle(object):
	def __init__(self,position):
		self.partPosition = list(position)
		self.speed = 1 #random.randrange(1,15)
		self.angle = 0
		self.size = 1

		self.rect = Rect(self.partPosition[0],self.partPosition[1],self.size,self.size)

		self.XSlope = math.cos(math.radians(self.angle)) 
		self.YSlope = math.sin(math.radians(self.angle))

		self.partX = self.partPosition[0]
		self.partY = self.partPosition[1]

		self.color = (255, 255, 255)

		self.name = "particle"
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
	def getSize(self):
		return self.size
	def getType(self):
		return self.name
	def getRect(self):
		return self.rect
	def collides(self,rect):
		return rect.collidepoint(self.partPosition[0],self.partPosition[1])

class sand(particle,object):
	def __init__(self,position):
		self.partPosition = list(position)
		self.speed = 5 #random.randrange(1,15)
		self.angle = random.randrange(1,360)
		self.size = 5

		self.rect = Rect(self.partPosition[0],self.partPosition[1],self.size,self.size)

		self.XSlope = math.cos(math.radians(self.angle)) 
		self.YSlope = math.sin(math.radians(self.angle))

		self.partX = self.partPosition[0]
		self.partY = self.partPosition[1]

		self.color = (193, 189, 129)

		self.name = "sand"
class sandLarge(particle,object):
	def __init__(self,position,direction):
		self.partPosition = list(position)
		self.speed = 5 #random.randrange(1,15)
		self.angle = direction
		self.size = 20

		self.rect = Rect(self.partPosition[0],self.partPosition[1],self.size,self.size)

		self.XSlope = math.cos(math.radians(self.angle)) 
		self.YSlope = math.sin(math.radians(self.angle))

		self.partX = self.partPosition[0]
		self.partY = self.partPosition[1]

		self.color = (193, 189, 129)

		self.name = "sand_large"
	