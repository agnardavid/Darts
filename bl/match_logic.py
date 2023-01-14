from dl.dl_wrapper import DataLayerWrapper
from models.competition import Competition
from models.match import Match
import random

class MatchLogic:

    # MATCH LIST INDEXES
    HOME_TEAM = 0
    AWAY_TEAM = 1
    PLAYER_ONE = 0
    PLAYER_TWO = 1
    PLAYER_THREE = 2
    PLAYER_FOUR = 3
    DATE = 2
    COMPETITION = 3

    def __init__(self):
        self.match = Match()
        self.dl_wrapper = DataLayerWrapper()

    def add_match(self, match: list):
        """Add new match to competition"""
        new_match = Match(match[self.HOME_TEAM], match[self.AWAY_TEAM], match[self.DATE], match[self.COMPETITION])
        new_match.match_id = self._generate_match_id()
        new_match.games = self._generate_match_games(new_match.home_team, new_match.away_team)
        self._assign_competition_to_match(new_match, match[self.COMPETITION])

        self.dl_wrapper.write_match(new_match)

    def add_results(self, match_id: str, home_team_score: str, away_team_score: str):
        """Add game result to match, input won legs, updates match"""
        # Find match
        selected_match = self.dl_wrapper.read_match(match_id)
        home_team_score_int = int(home_team_score)
        away_team_score_int = int(away_team_score)

        # Update match score
        if home_team_score_int > away_team_score_int: # Home team won game
            selected_match.score_board[selected_match.HOME_TEAM] += 1
        elif home_team_score_int < away_team_score_int: # Away team won game
            selected_match.score_board[selected_match.AWAY_TEAM] += 1

        # Update legs won
        self._update_team_standings(selected_match.home_team, "",
                                    home_team_score_int,
                                    selected_match.competition)  # HOME TEAM
        self._update_team_standings(selected_match.away_team, "",
                                    away_team_score_int,
                                    selected_match.competition)  # AWAY TEAM

        # Save legs won
        selected_match.games_result.append([home_team_score, away_team_score])

        # Calculate who is winning and number of games played in match
        selected_match.calculate_winner()
        selected_match.games_played += 1

        # If match is finished update team standings in competition
        if selected_match.games_played == 7:
            self._update_team_standings(selected_match.home_team, selected_match.winning_team,
                                        0,
                                        selected_match.competition)  # Add home team stat
            self._update_team_standings(selected_match.away_team, selected_match.winning_team,
                                        0,
                                        selected_match.competition)  # Add away team stat

        # Save match information
        self.dl_wrapper.update_match(selected_match)

    def delay_match(self, match_id: str, new_date: str):
        """Set new date for match"""
        delayed_match = self.dl_wrapper.read_match(match_id)
        delayed_match.date = new_date
        self.dl_wrapper.update_match(delayed_match)

    def edit_match(self, match_id: str, games_list: list):
        """Edits results in match"""
        selected_match = self.dl_wrapper.read_match(match_id)
        selected_match.games_result = games_list
        self.dl_wrapper.update_match(selected_match)

    def reset_match_data(self, match_id: str):
        """Resets match scoreboard and games"""
        pass

    def _update_team_standings(self, team: str, winning_team: str, won_legs: int, competition):
        """Update team standing in the competition"""
        # Find team
        selected_team = self.dl_wrapper.read_team(team)

        # Add statistic
        for i in range(len(selected_team.team_standing)):
            if selected_team.team_standing[i][selected_team.COMPETITION].name == competition:
                if selected_team.name == winning_team:  # Add victory to team if that team won the match
                    selected_team.team_standing[i][selected_team.VICTORIES] += 1
                    selected_team.team_standing[i][selected_team.WON_LEGS] += won_legs
                else:  # If lost, only add the legs the team won
                    selected_team.team_standing[i][selected_team.WON_LEGS] += won_legs

        # Save information
        self.dl_wrapper.update_team(selected_team)

    def _generate_match_id(self) -> int:
        """Generate ID for match"""
        all_matches = self.dl_wrapper.read_all_matches()
        new_id = len(all_matches) + 10  # Match Id's will be multiplied by 10 to add inbetween
        return new_id

    def _get_match_competition(self, competition_name:str) -> Competition:
        """Get the matches' competition, returns competition object"""
        all_comps = self.dl_wrapper.read_all_competitions()
        match_competition = None
        for comp in all_comps:
            if comp.name == competition_name:
                match_competition = comp

        return match_competition
    
    def _generate_match_games(self, home_team:str, away_team:str) -> dict:
        """Generates round robin, assignes matches to days"""
        home = self.dl_wrapper.read_team(home_team)
        away = self.dl_wrapper.read_team(away_team)
        list_of_players_in_match = self._shuffle_players(home.players,away.players)
        game_dict = {}
        # Generating 501 game_nr
        for game_nr, count in enumerate(range(4),1):
            game_dict[f"501 {game_nr}"] = [list_of_players_in_match[self.HOME_TEAM][count].name, list_of_players_in_match[self.AWAY_TEAM][count].name]
        list_of_players_in_match = self._shuffle_players(list_of_players_in_match[self.HOME_TEAM],list_of_players_in_match[self.AWAY_TEAM])
        # Generating 301 and Cricket duos
        game_dict["301 HomeTeam"] = [list_of_players_in_match[self.HOME_TEAM][self.PLAYER_ONE].name, 
                                        list_of_players_in_match[self.HOME_TEAM][self.PLAYER_TWO].name]
        game_dict["301 AwayTeam"] = [list_of_players_in_match[self.AWAY_TEAM][self.PLAYER_ONE].name, 
                                        list_of_players_in_match[self.AWAY_TEAM][self.PLAYER_TWO].name]
        game_dict["Cricket HomeTeam"] = [list_of_players_in_match[self.HOME_TEAM][self.PLAYER_THREE].name, 
                                            list_of_players_in_match[self.HOME_TEAM][self.PLAYER_FOUR].name]
        game_dict["Cricket AwayTeam"] = [list_of_players_in_match[self.AWAY_TEAM][self.PLAYER_THREE].name, 
                                            list_of_players_in_match[self.AWAY_TEAM][self.PLAYER_FOUR].name]
        list_of_players_in_match = self._shuffle_players(home.players,away.players)
        # Generating 501 Quads
        game_dict["501 HomeTeam"] = [player.name for player in list_of_players_in_match[self.HOME_TEAM]]
        game_dict["501 AwayTeam"] = [player.name for player in list_of_players_in_match[self.AWAY_TEAM]]
        return game_dict

    def _shuffle_players(self, home_team:list, away_team:list) -> list[list]:
        """Shuffles the players in the teams, returns a shuffled list with home and away teams."""
        random.seed(1337)
        random.shuffle(home_team)
        random.shuffle(away_team)
        shuffled_player_list = [home_team, away_team]
        return shuffled_player_list

    def _assign_competition_to_match(self, match: Match, competition_name: str):
        """Assign competition to match"""
        selected_competition = self.dl_wrapper.read_competition(competition_name)
        selected_competition.matches.append(match)

        self.dl_wrapper.update_competition(selected_competition)

