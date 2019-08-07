class Settings():
    #"""
    def __init__(self):
        """init settings"""
        #screen set
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (200,200,200)

        #spaceship speed
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #bullet setting
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #aliens setting
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 80
        #"1" move to the right, "-1" move to the left
        self.fleet_direction = 1

        #at what speed to speed up the game
        self.speed_scale = 1.1
        #score points increase speed
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #initialize settings that change as the game progresses
        self.slip_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        #"1" move to the right, "-1" move to the left
        self.fleet_direction = 1

        #the points of score
        self.alien_points = 50

    def increase_speed(self):
        #increase speed setting
        self.ship_speed_factor *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

