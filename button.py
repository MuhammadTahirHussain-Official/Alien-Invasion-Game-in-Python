import pygame.font

class Button:
    
    def __init__(self, ai_game, msg):
        """initialize the buttons attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0) 
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Build the button rect object and centre it
        self.rect = pygame.Rect(0, 0, self.width, self.height)   
        self.rect.center = self.screen_rect.center
        
        # the button messege need to be preped only once
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        """Turn messege into rendered image and center it into the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        # draw blank button and then draw messege
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)