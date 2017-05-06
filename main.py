import particle
import pygameapp
import particleMechanics
import random
import mathaddons as ma
particle_array = []

class main(pygameapp.App):
		
	def createParticles(self):
		for i in range(1,100):
			global particle_array
			rand_pos = (random.randrange(0,self.getWindowWidth()),
				random.randrange(0,self.getWindowHeight()))
			particle_array.append(particle.sand(rand_pos))
	def drawParticles(self):
		global particle_array
		for pos in particle_array:
			self.pygame.draw.rect(self.display,pos.color,(pos.getPosition()[0],pos.getPosition()[1],10,10),0)
	def applyForce(self):
		global particle_array
		for part in particle_array:
			part.setPositionX(part.getPositionX()+part.speed*part.getSlope()[0])
			part.setPositionY(part.getPositionY()+part.speed*part.getSlope()[1])
	def checkCollision(self):
		for part in particle_array:
			mouse_pos = self.pygame.mouse.get_pos()
			if part.getPositionX() > self.getWindowWidth():
				part.setSpeed(-part.getSpeed())
				part.setAngle(part.getAngle()+90)
			if part.getPositionX() < 0:
				part.setSpeed(-part.getSpeed())
				part.setAngle(part.getAngle()+90)
			if part.getPositionY() > self.getWindowHeight():
				part.setSpeed(-part.getSpeed())
				part.setAngle(part.getAngle()+90)
			if part.getPositionY() < 0:
				part.setSpeed(-part.getSpeed())
				part.setAngle(part.getAngle()+90)
			if ma.distance(part.getPositionX(),part.getPositionY(),mouse_pos[0],mouse_pos[1]) < 50:
				part.setPositionX(part.getPositionX()+100*part.getSlope()[0])
				part.setPositionY(part.getPositionY()+100*part.getSlope()[1])
	def drawMouseRange(self):
		self.pygame.draw.circle(self.display,(10,10,10),self.pygame.mouse.get_pos(),50,0)


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

