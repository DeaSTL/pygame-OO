import particle
import pygameapp
import particleMechanics
import random
import mathaddons as ma
particle_array = []

class main(pygameapp.App,particleMechanics.mechanics):
	def drawText(self,string,x,y,color):
		myfont = self.pygame.font.SysFont("monospace", 14)
		label = myfont.render(string, 14, color)
		self.display.blit(label,(x,y))
	def onKeyPressed(self,key):
		if key == self.pygame.K_g:
			self.reCreateParticles()
		elif key == self.pygame.K_f:
			self.addParticle(particle.sandLarge((self.getWindowWidth()/2,self.getWindowHeight()-100),90))
	def onMouseClick(self,x,y,button):
		self.moveToPoint(x,y)
		print("1")
	def onStart(self):
		global particle_array
		self.initializeMechanics()
		particle_array = self.createParticles()
		self.drawParticles()
	def onExecute(self):
		global particle_array
		self.drawMouseRange()
		self.drawParticles()
		self.applyForce()
		self.checkCollision()
		self.drawText("FPS: "+str(self.clock.get_fps()),0,0,(255,255,255))
		self.drawText("FrameCount: "+str(self.frameCount),0,14,(255,255,255))
		self.drawText("Particles: "+str(len(particle_array)),0,28,(255,255,255))
		self.drawText("Debug: "+str(self.getDebugInfo()),0,14*3,(255,255,255))
main(500,500,20).start()

