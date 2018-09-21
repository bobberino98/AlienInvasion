class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 1.5
        self.fleet_drop_speed = 10
        # fleet direction: 1 is right, -1 is left
        self.fleet_direction = 1

        self.speedup_scale = 1.5
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def screen_width(self):
        return self.__screen_width

    def screen_height(self):
        return self.__screen_height

    def bg_color(self):
        return self.__bg_color

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self. alien_speed_factor = 1

        self.alien_points = 50

        self. fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)



