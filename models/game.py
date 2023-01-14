from models.player import Player
import time


class Game:

    def __init__(self, home_team_score=0, away_team_score=0):
        self.id = time.time_ns()
        self.home_team_score: int = home_team_score
        self.away_team_score: int = away_team_score
        self.home_team_players: list[Player]
        self.away_team_players: list[Player]

    def __str__(self):
        pass

    def as_dict(self):
        return {
            "home_team_score": self.home_team_score,
            "away_team_score": self.away_team_score,
            "home_team_players": self.home_team_players,
            "away_team_players": self.away_team_players
        }

    def fieldnames():
        return ["home_team_score", "away_team_score", "home_team_players", "away_team_players"]

    def id_field():
        return "id"

    def from_dict(game_dict: dict):
        game = Game()
        game.home_team_players = game_dict["home_team_players"]
        game.away_team_players = game_dict["away_team_players"]
        game.home_team_score = game_dict["home_team_score"]
        game.away_team_score = game_dict["away_team_score"]
        return game
