class Player:
    def __init__(self, name, jersey_number, runs):
        self.name = name
        self.jersey_number = jersey_number
        self.runs = runs

    def get_category(self):
        if self.runs >= 1000:
            return "Excellent"
        elif self.runs >= 500:
            return "Good"
        else:
            return "Average"

    def display(self):
        print("Player Name:", self.name)
        print("Jersey Number:", self.jersey_number)
        print("Runs:", self.runs)
        print("Category:", self.get_category())
        print()


class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_players(self):
        for player in self.players:
            player.display()


team = Team()

p1 = Player("Virat", 18, 1200)
p2 = Player("Rohit", 45, 750)
p3 = Player("Rahul", 1, 300)

team.add_player(p1)
team.add_player(p2)
team.add_player(p3)

team.display_players()
