class GameStats():
    """track game statistics"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        #self.prep_high_score()

        #active when the game starts
        self.game_active = False

        #under no circumstances should the highest score be reset
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
    
    #def prep_high_score(self):
    #    """convert the highest score to a rendered image"""
    #    high_score = int(round(self.stats.high))
