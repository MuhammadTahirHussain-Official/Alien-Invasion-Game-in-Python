import pygame
# from settings import Setting
from pygame.sprite import Sprite

class Ship(Sprite):
    """a class to manage the ship"""

    def __init__(self, ai_game):
        """initialize the ship and set its starting position"""
        super().__init__()
        
        self.screen = ai_game.screen # give access to the screen
        self.screen_rect = ai_game.screen.get_rect() # treat the screen as a first rectangle and then place 
    # the ship on it as a second rectangle
        
    # shipspeed settings
        self.settings = ai_game.settings
        
    # load the ship image and resize it
        self.image = pygame.image.load(r'E:\\Coding\\Python\\Projects\\ALIEN INVASION GAME\\images\\ship.bmp')
        self.image = pygame.transform.scale(self.image, (80, 80))  # resize ship
    # pygame is useful as it treat all the game elements as a rectangles(as a rects()) even if they so not 
    # shape like a rectangle
        self.rect = self.image.get_rect() # it places the ship correctly on the screen
    # get_rect return the rectangle which has usefull attributes like x,y coordinates image size and positon
        
    # place ship fully visible just above bottom edge
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= self.rect.height
        #15  #move up by 15 pixels          self.rect.height # move it up by its height
        
    # movement flags
        self.moving_right = False
        self.moving_left = False
        
        self.x = float(self.rect.x)
        
    def update(self):
        """update the ship movement based on the movement of the flag"""
        
 
         # Update the ship's x value, not the rect.
        """self.screen.right are the coordinaates of the right corner of the screen"""
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.x +=  self.settings.ship_speed
    # if we use elif instead of if in moving left then the left key will always take priority over right key
        if self.moving_left and self.rect.left > 0:
            self.x -=  self.settings.ship_speed
            
    # update the rect from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """centre the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        
