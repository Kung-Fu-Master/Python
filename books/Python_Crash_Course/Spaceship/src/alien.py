import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class that represents a single alien"""
    def __init__(self, ai_settings, screen):
        """initialize the alien and set its starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load a alien image and set its rect property
        self.image = pygame.image.load("../images/alien.bmp")
        self.rect = self.image.get_rect()

        #each alien is initially near the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the exact location of the alien
        self.x = float(self.rect.x)

    def blitme(self):
        """draw aliens at specified location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """return true if the alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left < 0:
            return True
    
    def update(self):
        """move alien to the right"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x


