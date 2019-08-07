
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""initial spaceship"""
	def __init__(self, ai_settings, screen):
		super(Ship, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		#load spaceship
		self.image = pygame.image.load("../images/ship.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#set spaceship at the bottom of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.center = float(self.rect.centerx)

		#move flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def blitme(self):
		"""Drawing a spaceship"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right + (self.rect.right - self.rect.left)/2:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0 - (self.rect.right - self.rect.left)/2:
			self.center -= self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top > 0:
			self.rect.bottom -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.bottom += self.ai_settings.ship_speed_factor

		self.rect.centerx = self.center

	def center_ship(self):
		self.center = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

