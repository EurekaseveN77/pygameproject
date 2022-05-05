import pygame, sys
from settings import * 
from level import Level

# Pygame setup

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((screen_width,screen_height))
		self.clock = pygame.time.Clock()
		self.level = Level(level_map,self.screen)
		
		
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						self.level.toggle_pause()
			self.screen.fill('black')
			self.level.run()
			pygame.display.update()
			self.clock.tick(60)

if __name__ == '__main__':
	game = Game()
	game.run()