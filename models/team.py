from models.club import Club
from models.player import Player


class Team:

    COMPETITION = 0
    VICTORIES = 1
    WON_LEGS = 2

    def __init__(self, name="", club_name=""):
        self.name = name
        self.players = []
        self.team_captain = ""
        self.club = club_name
        self.team_standing = []

    def __str__(self) -> str:
        return f"""Team:
    Name: {self.name}
    Players: {self.players}
    Club: {self.club}
    Team standing: {self.team_standing}
    Team captain: {self.team_captain}
"""

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        if not o:
            return False
        else:
            return (self.name == o.name
                    and self.players == o.players
                    and self.team_captain == o.team_captain
                    and self.club == o.club
                    and self.team_standing == o.team_standing)

    def fieldnames():
        return ["name", "team_captain", "club"]

    def id_field():
        return "name"

    def as_dict(self):
        return {
            "name": self.name,
            "players": self.players,
            "team_captain": self.team_captain,
            "club": self.club,
            "team_standing": self.team_standing
        }

    def from_dict(team_data: dict):
        team = Team()
        team.name = team_data["name"]
        team.players = team_data["players"]
        team.club = team_data["club"]
        team.team_standing = team_data["team_standing"]
        team.team_captain = team_data["team_captain"]
        return team
