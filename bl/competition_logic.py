from bl.match_logic import MatchLogic
from models.competition import Competition
from dl.dl_wrapper import DataLayerWrapper
from datetime import date

from models.team import Team


class CompetitionLogic:

    # COMPETITION LIST INDEXES
    COMPETITION_NAME = 0
    ORGANIZER_NAME = 1
    PHONE_NUMBER = 2
    START_DATE = 3
    END_DATE = 4
    ROUNDS = 5

    def __init__(self):
        self.competition = Competition()
        self.dl_wrapper = DataLayerWrapper()
        self.match_logic = MatchLogic()

    def add_competition(self, comp_elems: list):
        """Adds competition to database"""
        new_competition = Competition(comp_elems[self.COMPETITION_NAME], comp_elems[self.ORGANIZER_NAME],
                                      comp_elems[self.PHONE_NUMBER], comp_elems[self.START_DATE],
                                      comp_elems[self.END_DATE], comp_elems[self.ROUNDS])

        self.dl_wrapper.write_competition(new_competition)

    def add_team_to_competition(self, team_name: str, competition_name: str):
        """Adds team to competition"""
        # Find
        selected_comp = self.dl_wrapper.read_competition(competition_name)
        selected_team = self.dl_wrapper.read_team(team_name)

        # Update information
        selected_comp.teams.append(selected_team)
        selected_team.team_standing.append([selected_comp, 0, 0])

        # Save
        self.dl_wrapper.update_team(selected_team)
        self.dl_wrapper.update_competition(selected_comp)

    def get_competition_list(self) -> list[Competition]:
        """Gets all competitions in database as list"""
        return self.dl_wrapper.read_all_competitions()

    def get_competition_matches(self, competition_name: str) -> list:
        """Gets all matches registered in competition as list"""
        # Find competition
        all_matches = self.dl_wrapper.read_all_matches()

        # Get matches in competition
        competition_matches = []
        for match in all_matches:
            if match.competition == competition_name:
                competition_matches.append(match)
        # Send list of matches
        return competition_matches

    def get_competition_info(self, competition: str) -> Competition:
        """Returns single competition object"""
        return self.dl_wrapper.read_competition(competition)

    def get_unplayed_matches(self, competition: str) -> list:
        """Gets all unplayed matches in competition returns as list of matches"""
        # Get matches in competition
        competition_matches = self.get_competition_matches(competition)

        # Find unplayed matches
        unplayed_matches = []
        for match in competition_matches:
            if match.score_board[0] == 0 and match.score_board[1] == 0:
                unplayed_matches.append(match)

        # Send unplayed matches
        return unplayed_matches

    def get_played_matches(self, competition: str) -> list:
        """Gets all played matches in competition returns as list of matches"""
        # Get matches in competition
        competition_matches = self.get_competition_matches(competition)

        # Get matches that have updated scoreboard
        played_matches = []
        for match in competition_matches:
            if match.score_board[0] == 0 and match.score_board[1] == 0:
                continue
            else:
                played_matches.append(match)

        # Send played matches
        return played_matches

    def get_competition_standing(self, competition_name: str) -> list[(int, int, str)]:
        """Gets team standings in competition as sorted list of tuples: (victories, won legs, team name)"""

        # Find competition and teams in competition
        competition = self.dl_wrapper.read_competition(competition_name)
        all_teams = self.dl_wrapper.read_all_teams()

        # Get team standings list
        teams = []

        for team in all_teams:
            for i in range(len(team.team_standing)):
                if team.team_standing[i][team.COMPETITION].name == competition_name:
                    teams.append({"team": team.name,
                                  "wins": team.team_standing[i][team.VICTORIES],
                                  "won legs": team.team_standing[i][team.WON_LEGS]})

        teams = sorted(teams, key=lambda k: (-k["wins"], -k["won legs"], k["team"]))

        # Send sorted list by won matches
        return teams

    def get_matches(self, competition_name: str) -> list:
        """Get all matches in competition, return as list"""
        # Find competition and matches
        selected_competition = self.dl_wrapper.read_competition(competition_name)
        all_matches = self.dl_wrapper.read_all_matches()

        # Get matches in selected competition
        competition_matches = []
        for match in all_matches:
            if match.competition == selected_competition.name:
                competition_matches.append(match)

        # Send list of matches
        return competition_matches

    def get_competition_teams(self, competition_name: str) -> list:
        """Get all teams in competition, return as list"""
        # Get competitions
        all_competitions = self.dl_wrapper.read_all_competitions()

        # Find selected competition
        selected_competition = None
        for competition in all_competitions:
            if competition.name == competition_name:
                selected_competition = competition

        # Send list of teams in competition
        return selected_competition.teams

    def get_captain_matches(self, competition_name: str, captain_ssn: str) -> list:
        """Returns list of matches that captain can get add results to"""
        # Find competition and captain player and unplayed matches in competition
        selected_competition = self.dl_wrapper.read_competition(competition_name)
        team_captain = self.dl_wrapper.read_player(captain_ssn)
        unplayed_matches = self.get_unplayed_matches(competition_name)
        all_teams = self.dl_wrapper.read_all_teams()

        # Get captains team and home unplayed matches
        captains_team = None
        teams_home_matches = []

        for team in all_teams:
            if team.team_captain == team_captain.social_id:
                captains_team = team
        for match in unplayed_matches:
            if match.home_team == captains_team.name:
                teams_home_matches.append(match)

        # Send
        return teams_home_matches

    def generate_match_schedule(self, competition_name:str):
        """Generates all matches with all teams that have been added to competition.\n
        Uses Round Robin to generate matches.

        Args:
            competition_name (str): Name of competition.
        """
        selected_competition = self.dl_wrapper.read_competition(competition_name)
        rounds_played = selected_competition.rounds
        # ROUND ROBIN

        # Conditions
        competition_days = selected_competition.days
        day, month, year = selected_competition.start_date.split("-")
        start_date = date(int(year), int(month), int(day))

        # Input list
        teams = selected_competition.teams

        # Odd num of teams
        if len(teams) % 2:
            teams.append(Team("Bye", "Temp Club"))
        n = len(teams)

        # Rounds condition
        num_games = (n / 2 * (n - 1)) * 2
        one_round = False
        if rounds_played == 1:  # ONE ROUND CONDITION
            num_games = n/2*(n-1)
            one_round = True
        games_per_day = round(num_games / float(competition_days))

        # Match lists
        matchs = []  # Home matches
        return_matchs = []  # Away matches
        fixtures = []  # All matches

        match_date = start_date
        games_count = 0

        # Algorithm
        for fixture in range(1, n):
            for i in range(int((round(n / 2)))):

                # Home
                if games_count == games_per_day:
                    match_date = match_date.replace(day=match_date.day + 1)
                    games_count = 0
                matchs.append((teams[i], teams[n - 1 - i], match_date.isoformat()))
                games_count += 1

                # Away (if rounds is more than 1)
                if not one_round:
                    if games_count == games_per_day:
                        match_date = match_date.replace(day=match_date.day + 1)
                        games_count = 0
                    return_matchs.append((teams[n - 1 - i], teams[i], match_date.isoformat()))
                    games_count += 1

            teams.insert(1, teams.pop())
            fixtures.insert(round(len(fixtures) / 2), matchs)
            fixtures.append(return_matchs)
            matchs = []
            return_matchs = []

        for fixture in fixtures:
            for match in fixture:
                if match[0].name != "Bye" and match[1].name != "Bye":
                    self.match_logic.add_match([match[0].name, match[1].name, match[2], competition_name])
