import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
   """A clas to represent a single alien in the fleet."""

   def __init__(self, ai_game):
      """Initialize th ealien and set it's starting position"""
      super().__init__()
      self.screen = ai_game.screen

      # load the alien image and set it's rect attribute.
      self.image = pygame.image.load('resources/images/alien.bmp')
      self.rect = self.image.get_rect()

      # Start each new alien near the top left of the screen.
      self.rect.x = self.rect.width
      self.rect.y = self.rect.height

      # Store the alien's exact horizontal position
      self.x = float(self.rect.x)
