import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """a class that manages bullets fired by spacecraft"""
    def __init__(self, ai_settings, screen, ship):
        #inheriting class Sprite
        super(Bullet, self).__init__()
        self.screen = screen

        #set the rectangle of bullet at (0,0) and set the correct position
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store bullets positions in decimals
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #move the bullet up
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

