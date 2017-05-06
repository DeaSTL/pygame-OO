import random
import mathaddons as ma
import particle
import math
particle_array = []
largeSand = []


class mechanics(object):
	def initializeMechanics(self):
		self.debugInfo = {}
		self.debugInfo["added_particles"] = 0
		self.debugInfo["collisions"] = 0
	def getDebugInfo(self):
		return self.debugInfo
	def createParticles(self):
		for i in range(1,50):
			global particle_array
			rand_pos = (random.randrange(0,self.getWindowWidth()),
				random.randrange(0,self.getWindowHeight()))
			particle_array.append(particle.sand(rand_pos))
		return particle_array
	def reCreateParticles(self):
		global particle_array
		particle_array = []
		self.createParticles()

	def addParticle(self,particle):
		particle_array.append(particle)
		if particle.getType() == "sand_large":
			largeSand.append(particle)
		else:
			particle_array.append(particle)
		self.debugInfo["added_particles"] += 1

	def drawParticles(self):
		global particle_array
		for pos in particle_array:
			self.pygame.draw.rect(self.display,pos.color,(pos.getPosition()[0],pos.getPosition()[1],pos.getSize(),pos.getSize()),0)
	def applyForce(self):
		global particle_array
		for part in particle_array:
			part.setPositionX(part.getPositionX()+part.speed*part.getSlope()[0])
			part.setPositionY(part.getPositionY()+part.speed*part.getSlope()[1])
	def checkCollision(self):
		for part in particle_array:
			mouse_pos = self.pygame.mouse.get_pos()
			if part.getPositionX() > self.getWindowWidth():
				self.reflectParticle(part)
				self.debugInfo["collisions"]+=1
			if part.getPositionX() < 0:
				self.reflectParticle(part)
				self.debugInfo["collisions"]+=1
			if part.getPositionY() > self.getWindowHeight():
				self.reflectParticle(part)
				self.debugInfo["collisions"]+=1
			if part.getPositionY() < 0:
				self.reflectParticle(part)
				self.debugInfo["collisions"]+=1
			for lpart in largeSand:
				pass
					

	def pullToPoint(self,x,y):
		pass
	def repelFromPoint(self,part,x,y):
		part.setAngle(math.degrees(math.atan2(part.getPositionX()-x,part.getPositionY()-y))-90)
	def moveToPoint(self,x,y):
		for part in particle_array:
			part.setPosition((x,y))
	def reflectParticle(self,part):
		part.setSpeed(-part.getSpeed())
		part.setAngle(part.getAngle()+90)
	def drawMouseRange(self):
		if self.pygame.mouse.get_focused():
			self.pygame.draw.circle(self.display,(10,10,10),self.pygame.mouse.get_pos(),10,0)