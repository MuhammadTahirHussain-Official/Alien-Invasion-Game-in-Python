import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """a class to manage the bullets fired from the ships"""
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color
        
        # create the bullet rect at (0,0) and then set the correct position
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,
                                self.settings.bullet_height )     
        self.rect.midtop = ai_game.ship.rect.midtop # place the bullet at top of the ship
    
        # store the bullet position as a decimal value
        self.y = float(self.rect.y)
        
    def update(self):
        """move the bullets up and down on the screen"""
        # update the decimal positon of the bullet
        self.y -= self.settings.bullet_speed
        # update the rect position
        self.rect.y = self.y
        
    def draw_bullets(self):
        """draw the bullets on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
        