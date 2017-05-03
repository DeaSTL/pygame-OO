import pygame
import sys

class App(object):
	def __init__(self,window_width,window_height,frame_rate):
		self.windowWidth = window_width
		self.windowHeight = window_height
		self.frameRate = frame_rate

		self.running = True

		self.pygame = pygame
		self.pygame.init()

		self.clock = self.pygame.time.Clock()

		self.pygame.display.init()
		self.display = self.pygame.display.set_mode(
			(self.windowWidth,self.windowHeight),
			self.pygame.RESIZABLE)


	def onExecute(self):
		pass
	def onStart(self):
		pass
	def onMousePressed(self,x,y,button):
		pass
	def onKeyPressed(self,key):
		pass
	def start(self):
		self.onStart()
		while self.running:
			self.ticks = self.pygame.time.get_ticks()
			self.display.fill((0,0,0))
			self.onExecute()
			self.clock.tick(self.frameRate)

			self.pygame.display.update()
			
			for event in self.pygame.event.get():
				if event.type == self.pygame.QUIT:
					sys.exit(0)
				if event.type == self.pygame.VIDEORESIZE:
					self.display = self.pygame.display.set_mode(
					(event.w,event.h),
					self.pygame.RESIZABLE)
					self.windowWidth = event.w
					self.windowHeight = event.h
				if event.type == self.pygame.MOUSEBUTTONDOWN:
					print(event.button)
					self.onMousePressed(event.pos[0],event.pos[1],event.button)
				if event.type == self.pygame.KEYDOWN:
					self.onKeyPressed(event.key)

	def getWindowHeight(self): return self.windowHeight
	def getWindowWidth(self): return self.windowWidth
	def getFrameRate(self): return self.frameRate
	def getRunning(self): return self.running
	def getClock(self): return self.clock
	def getDisplay(self): return self.display

	def setWindowHeight(self,height):
		self.windowHeight = height
		self.display = self.pygame.display.set_mode(
			(self.windowWidth,height),
			self.pygame.RESIZABLE)
	def setWindowWidth(self,width):
		self.windowWidth = width
		self.display = self.pygame.display.set_mode(
			(width,self.windowHeight),
			self.pygame.RESIZABLE)
	def setFrameRate(self,frame_rate): self.frameRate = frame_rate
	def setDisplay(self,display): self.display = display 


