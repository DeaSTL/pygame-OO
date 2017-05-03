import particle
import pygameapp
import random
import mathaddons as ma
particle_array = []
class main(pygameapp.App):
		
	def createParticles(self):
		for i in range(1,1000):
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
	def onStart(self):
		self.createParticles()
		self.drawParticles()
	def onExecute(self):
		self.drawParticles()
		self.applyForce()
		self.checkCollision()
		
main(500,500,60).start()

