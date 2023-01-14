import ast


class Match:

    HOME_TEAM = 0
    AWAY_TEAM = 1

    def __init__(self, home_team="", away_team="", date="", competition=""):
        self.home_team: str = home_team
        self.away_team: str = away_team
        self.date: str = date
        self.winning_team = "Draw"
        self.score_board: list[int] = [0, 0]
        self.won_legs: list[int] = [0, 0]
        self.match_id: int = 0
        self.competition: str = competition
        self.games_played: int = 0
        self.games: dict = {}
        self.games_result: list = []

    def calculate_winner(self):
        if self.score_board[self.HOME_TEAM] > self.score_board[self.AWAY_TEAM]:
            self.winning_team = self.home_team
        elif self.score_board[self.HOME_TEAM] < self.score_board[self.AWAY_TEAM]:
            self.winning_team = self.away_team
        else:
            self.winning_team = "Draw"

    def __str__(self):
        return f"""Match:
    Home team: {self.home_team}
    Away team: {self.away_team}
    Date: {self.date}
    Winning team: {self.winning_team}
    Score board: {self.score_board}
    Won legs: {self.won_legs}
    Match id: {self.match_id}
    Competition: {self.competition}
    Games played: {self.games_played}
    Games: {self.games}
    Games results: {self.games_result}
"""

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        if not o:
            return False
        else:
            return (self.home_team == o.home_team
                    and self.away_team == o.away_team
                    and self.date == o.date
                    and self.winning_team == o.winning_team
                    and self.score_board == o.score_board
                    and self.won_legs == o.won_legs
                    and self.match_id == o.match_id
                    and self.competition == o.competition
                    and self.games_played == o.games_played
                    and self.games == o.games
                    and self.games_result == o.games_result)

    def as_dict(self):
        return {
            "home_team": self.home_team,
            "away_team": self.away_team,
            "date": self.date,
            "winning_team": self.winning_team,
            "score_board": self.score_board,
            "won_legs": self.won_legs,
            "match_id": self.match_id,
            "competition": self.competition,
            "game_played": self.games_played,
            "games": self.games,
            "games_result": self.games_result
        }

    def fieldnames():
        return ["home_team", "away_team", "date", "winning_team", "score_board",
                "won_legs", "match_id", "game_played", "games", "games_result", "competition"]

    def id_field():
        return "match_id"

    def from_dict(match_dict: dict):
        match = Match()
        match.match_id = int(match_dict["match_id"])
        match.home_team = match_dict["home_team"]
        match.away_team = match_dict["away_team"]
        match.date = match_dict["date"]
        match.winning_team = match_dict["winning_team"]
        match.score_board = ast.literal_eval(match_dict["score_board"])
        match.won_legs = ast.literal_eval(match_dict["won_legs"])
        match.competition = match_dict["competition"]
        match.games_played = int(match_dict["game_played"])
        match.games = ast.literal_eval(match_dict["games"])
        match.games_result = ast.literal_eval(match_dict["games_result"])
        return match
