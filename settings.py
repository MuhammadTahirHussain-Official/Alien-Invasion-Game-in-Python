# Setting class

class Setting:
    """a class to store all the setting of the alien invasion"""

    def __init__(self):
        """initialize the game setting"""
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230,230,230)
        
        #ship speed settings
        self.ship_speed = 1.5 # here speed is 1.5 pixels speed in the decimal no to control the ship precisely
        self.ship_limit = 3
        
        # bullet setting
        self.bullet_speed = 1.5
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 20
        
        # alien speed
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10 # vertical drop speed of the alien fleet
        self.fleet_direction = 1 # fleet_direction of 1 represents right; -1 represents left
        
        # how quickly the game speed up
        self.speedup_scale = 1.1
        
        # how quickly the alien point values increases
        self.score_scale = 1.5
        
        # Scoring
        self.alien_points = 50
        
        # High score should never be reset
        self.high_score = 0
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """initialize the setting that changes throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1
        
    def increase_speed(self):
        """increase speed setting and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)
        
        
        