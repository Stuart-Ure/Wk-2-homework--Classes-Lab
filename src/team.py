class Team:

    def __init__ (self, input_team_name, input_players, input_coach):
        self.name = input_team_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0 
        self._game_win={
            'True':3,
            'False':0
        }

    def add_player (self, new_player):
            self.players.append(new_player)


    def has_player(self,input_name):
        for self.name in self.players:
            if self.name == input_name:
                return True
        else:
            return False
        

    def play_game(self,game_win):
        if game_win==True:
            self.points+=3
        else: self.points =0 
