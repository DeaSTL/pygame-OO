import pygame

class App(object):
	def __init__(self,window_width,window_height,frame_rate):
		self.windowWidth = window_width
		self.windowHeight = window_height
		self.frameRate = frame_rate

		self.running = True

		self.pygame = pygame
		self.pygame.init()

		self.clock = self.pygame.Clock()

		self.display = pygame.display.set_mode(
			(self.windowWidth,self.windowHeight),
			self.pygame.RESIZABLE)

	def onExecute(self):
		pass
	def start(self):
		while self.running:
			self.onExecute()
			self.clock.tick(selfframeRate)
	def getWindowHeight(self): return self.windowHeight
	def getWindowWidth(self): return self.windowWidth
	def getFrameRate(self): return self.frameRate
	def getRunning(self): return self.running
	def getClock(self): return self.clock
	def getDisplay(self): return self.display

	def setWindowHeight(self,height):
		self.windowHeight = height
		self.display = 
			self.pygame.display.set_mode(
			(self.windowWidth,height),
			self.pygame.RESIZABLE)
	def setWindowWidth(self,width):
		self.windowWidth = width
		self.display = 
			self.pygame.display.set_mode(
			(width,self.windowHeight),
			self.pygame.RESIZABLE)
	def setFrameRate(self,frame_rate): self.frameRate = frame_rate
	def setDisplay(self,display): self.display = display 


