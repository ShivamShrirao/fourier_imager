import pygame
from pygame.locals import *
from pygame import gfxdraw
import numpy as np

SCR_HEIGHT	= 800
SCR_WIDTH	= 800
COLORS		= [(0, 0, 0),(192, 192, 192),(128, 128, 128),(255, 0, 0),(255, 255, 0),(128, 128, 0),(0, 255, 0),(167, 238, 45),(0, 128, 0),(0, 255, 255),(0, 128, 128),(0, 0, 255),(0, 0, 128),(255, 0, 255),(128, 0, 128)]
FPS			= 120		# I have 144 Hz monitor bish!
N 			= 10
SPEED 		= 0.005

class Roters:
	def __init__(self):
		self.screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
		self.center=(120,400)
		self.theta = 0
		self.speed = SPEED
		self.plotp = [[] for i in range(N)]

	def draw(self, center, n):
		nm=2*n-1
		rads = self.radius * 2/(nm*np.pi)
		gfxdraw.aacircle(self.screen,*center,int(rads),COLORS[(n-1)%len(COLORS)])
		x = int(center[0] + (-1)**n * rads * np.cos(nm*self.theta))
		y = int(center[1] + (-1)**n * rads * np.sin(nm*self.theta))
		self.theta=(self.theta+self.speed)%(2*np.pi)

		pygame.draw.aaline(self.screen,COLORS[(n-1)%len(COLORS)],center,(x,y))
		gfxdraw.aacircle(self.screen,x,y,0,COLORS[0])
		gfxdraw.filled_circle(self.screen,x,y,0,COLORS[0])

		if n<N:
			self.draw((x,y),n+1)
		else:
			dst=self.center[0]+150
			gfxdraw.aacircle(self.screen,dst,y,1,COLORS[0])
			gfxdraw.filled_circle(self.screen,dst,y,1,COLORS[0])

			self.plotp[n-1].insert(0,y)
			pygame.draw.aaline(self.screen,COLORS[0],(x,y),(dst,y))
			points=[(dst,y),(dst,y)]
			for i,pt in enumerate(self.plotp[n-1]):
				# gfxdraw.pixel(self.screen,dst+i,pt,(255,0,0))
				points.append((dst+i,pt))
			# pygame.draw.polygon(self.screen,(255,0,0),points,1)
			pygame.draw.aalines(self.screen,(255,0,0),False,points)
			if len(self.plotp[n-1])>600:
				self.plotp[n-1].pop()

	def run(self):
		clock = pygame.time.Clock()
		n_exit_game = True
		while n_exit_game:
			clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					n_exit_game=False
			self.screen.fill((255, 255, 255))
			self.radius=100
			self.draw(self.center,1)
			pygame.display.update()

if __name__ == "__main__":
	Roters().run()