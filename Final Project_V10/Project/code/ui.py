import pygame

class UI:
	def __init__(self,surface):

		# setup 
		self.display_surface = surface 

		# health 
		self.health_bar = pygame.image.load('../graphics/ui/BarHealth.png').convert_alpha()
		self.health_bar_topleft = (55,40)
		self.bar_max_width = 154
		self.bar_height = 5
	
	def show_health(self,current,full):
		self.display_surface.blit(self.health_bar,(20,10))
		current_health_ratio = current / full
		current_bar_width = self.bar_max_width * current_health_ratio
		health_bar_rect = pygame.Rect(self.health_bar_topleft,(current_bar_width,self.bar_height))
		pygame.draw.rect(self.display_surface,'#dc4949',health_bar_rect)
