import pygame
from pygame.sprite import Sprite

class Aliens(Sprite):
    """a class to represent the single alien in the fleet."""
    
    def __init__(self, ai_game):
        """initialize the allien and set it starting position."""
        super().__init__()
        self.screen = ai_game.screen
        
        # load the alien and set it rect attributes
        self.image = pygame.image.load('E:\Coding\Python\Projects\ALIEN INVASION GAME\images\\alien2.bmp')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        
        # start new alien at the top of the screen
        self.rect.x = self.rect.width # initail position on the x-axis
        self.rect.y = self.rect.height # initial position on the y-axis
        
        # store the alien's exact horizental position
        self.x = float(self.rect.x)
        
        # alien movement
        self.settings = ai_game.settings
        
        
    def check_edges(self):
        """return true if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0: 
            return True
        
    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed *self.settings.fleet_direction)
        self.rect.x = self.x
        
    

