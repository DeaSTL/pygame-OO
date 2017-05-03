import particle
import pygameapp
import random
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
			self.pygame.draw.rect(self.display,(100,100,100),(pos.getPosition()[0],pos.getPosition()[1],10,10),0)
	def applyForce(self):
		global particle_array
		for part in particle_array:
			part.setPositionX(part.getPositionX()+part.speed)
			part.setPositionY(part.getPositionY()+part.speed)
	def checkCollision(self):
		for part in particle_array:
			if part.getPositionX() > self.getWindowWidth():
				part.setSpeed(-part.getSpeed())
			if part.getPositionX() < 0:
				part.setSpeed(-part.getSpeed())
			if part.getPositionY() > self.getWindowHeight():
				part.setSpeed(-part.getSpeed())
			if part.getPositionY() < 0:
				part.setSpeed(-part.getSpeed())
	def onStart(self):
		self.createParticles()
		self.drawParticles()
	def onExecute(self):
		self.drawParticles()
		self.applyForce()
		self.checkCollision()
		
main(500,500,20).start()

