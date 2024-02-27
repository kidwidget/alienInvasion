import pygame

class Ship:
   """A class to mange the ship"""
   speedRight = 1
   speedLeft = 1
   speedUp = 1
   speedDown = 1
   def __init__(self, ai_game):
      """Initialize the ship and set its starting posistion."""
      self.screen = ai_game.screen
      self.screen_rect = ai_game.screen.get_rect()
      # Load the ship image and get its rect
      self.image = pygame.image.load('resources/images/ship.bmp')
      self.rect = self.image.get_rect()
      # Start each new ship at the bottem center of the screen
      self.rect.midbottom = self.screen_rect.midbottom
      # Movement flag; start with a ship that is not moving
      self.moving_right = False
      self.moving_left = False
      self.moving_up = False
      self.moving_down = False
   def update(self):
      """Update the ship's position based on the movement flag"""
      if self.moving_right == False:
         self.speedRight = 1
      if self.moving_left == False:
         self.speedLeft = 1
      if self.moving_up == False:
         self.speedUp = 1
      if self.moving_down == False:
         self.speedDown = 1
      if self.moving_right:
         self.rect.x += self.speedRight
         self.speedRight += .2
         if self.speedRight > 10:
            self.speedRight = 10
      if self.moving_left:
         self.rect.x -= self.speedLeft
         self.speedLeft += .2
         if self.speedLeft > 10:
            self.speedLeft = 10
      if self.moving_up:
         self.rect.y -= self.speedUp
         self.speedUp += .2
         if self.speedUp > 10:
            self.speedUp = 10
         if self.rect.y < 600:
            self.rect.y = 600
      if self.moving_down:
         self.rect.y += self.speedDown
         self.speedDown += .2
         if self.speedDown > 10:
            self.speedDown = 10
         if self.rect.y > 780:
            self.rect.y = 780

   def blitme(self):
      """Draw the ship at its current location"""
      self.screen.blit(self.image, self.rect)