import sys
from time import sleep

import pygame

from settings import Setting
from ship import Ship
from bullet import Bullet
from alien import Aliens
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """overall class to manage game assests and behaviour"""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
         
        pygame.init()
        self.settings = Setting()          
        self.screen = pygame.display.set_mode(   
            (self.settings.screen_width,self.settings.screen_height)) 
        pygame.display.set_caption("ALIEN INVASION")  
        self.ship = Ship(self)  # ship
        self.ship.center_ship()
        self.bullets = pygame.sprite.Group()  # bullets
        self.aliens = pygame.sprite.Group()   # aliens
        self._create_fleet()
        self.play_button = Button(self, "PLAY") # make the play button
        self.bg_color = (230,230,230) # setting a background color # colors in the pygame are the RGB colors
        self.stats = GameStats(self) # create instance to store game stastics 
        self.sb = Scoreboard(self)     
              
    def run_game(self):
        """start with the main loop"""
        while True:  # give the infinite loop
            """watch for the keyboard and mouse event"""
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update()
                self._update_bullet()
                self._update_aliens()
            
            self._update_screen()
                                       
    def _check_events(self):
        """repond to keypress and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
    def _check_play_button(self, mouse_pos):
        """start a new game when player press the button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # reset the game elements speed
            self.settings.initialize_dynamic_settings()
            # reset the game status
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            # get rid of remaining bullets and aliens
            self.aliens.empty()
            self.bullets.empty()
            # create new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            
            # hide the mouse cursor
            pygame.mouse.set_visible(False)
            
    def _check_keydown_events(self, event):
        """Respond to keypresses."""            
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_event(self,event): 
        """Respond to key releases."""       
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
                     
    def _fire_bullet(self):
        """create new bullet and add it to the bullet group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullet(self):
        """update position of bullets and delete the old ones."""
        # update the bullet positions.
        self.bullets.update()
            
         # get rid of the bullets
        for bullet in self.bullets.copy():#we cnnot remove items from list or group in for loop so we use copy
            if bullet.rect.bottom <= 0: # mean if the bottom of the bullet touches the top of the screen
                self.bullets.remove(bullet)
            # print(len(self.bullets))
        self._check_bullet_alien_collosion()
        
    def _check_bullet_alien_collosion(self):
        """Respond to bullet-alien collosion"""
        # groupcollide() give dict in which collosion alien,bullets present as key and values respectively    
        collosion = pygame.sprite.groupcollide(
        # if the first value is false and other is true then the bullet remove all alien in its path
            self.bullets, self.aliens, True, True # here true use to delete the collided element
        )
        
        if collosion:
            for aliens in collosion.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            
        if not self.aliens: # an empty group evaluates to false so if statement become true
            # Destroy existing bullets and create new fleat
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            
            # increase level
            self.stats.level += 1
            self.sb.prep_level()
    
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien.
        alien = Aliens(self)
        alien_width, alien_height  = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width) # == 1120 pixels
        number_alien_x = available_space_x // (2 * alien_width) #  == total 9 aliens on the screen
        
        # determine the no of rows that are fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height ) # == 460 pixels
        number_rows = available_space_y // ( 2 * alien_height) # == 3.8 as // drop the float no so no row = 3
        
        # create full fleat of aliens
        for row_number in range(number_rows): # create rows of aleins till number_rows
            for alien_number in range(number_alien_x):  # Create the aliens in a single row
                self._create_aliens(alien_number, row_number)
                
    def _create_aliens(self, alien_number, row_number):
        """create alien and space it in a row"""
        alien = Aliens(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number # intitial position of the new alien on x-axis
        alien.rect.x = alien.x # coordinates set to the x axis
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number # position of alien on y-axis
        self.aliens.add(alien) #place the aliens on the screen
        
    def _check_fleet_edges(self):
        """respond appropriately if an alien reaches an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """drop the entire fleet and change the direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed # move alien fleet verticaly downward
        self.settings.fleet_direction *= -1 # change the fleet direction on x-axis
        
    def _update_aliens(self):
        """check if fleet is at the edge , then update the position of all the alien in fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        # look for the aliens hitting at the bottom of the screen
        self._check_aliens_bottom()
            
    def _ship_hit(self):
        """repond to the ship hit by the alien"""
        if self.stats.ship_left > 0:
        # decrement ship left, and update score board
            self.stats.ship_left -= 1
            self.sb.prep_ships()
            # get rid of remaining alien and bullets
            self.aliens.empty()
            self.bullets.empty()
            # create new fleet and centre the ship
            self._create_fleet()
            self.ship.center_ship()
            # pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
        
    def _check_aliens_bottom(self):
        """check if any alien have reached at the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat it the same way as the ship got hit
                self._ship_hit()
                break
                
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullets()   # make sure this matches your Bullet class
        self.aliens.draw(self.screen)
        
        # Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
            
        # Draw the score information
        self.sb.show_score()
         
        self.ship.blitme()
        pygame.display.flip()
         
            
if __name__ == '__main__':
    # Make the game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
          