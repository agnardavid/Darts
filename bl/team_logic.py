from dl.dl_wrapper import DataLayerWrapper
from models.club import Club
from models.player import Player
from models.team import Team


class TeamLogic:

    # TEAM LIST INDEXES
    TEAM_NAME = 0
    CLUB_NAME = 1
    
    def __init__(self):
        self.team = Team()
        self.dl_wrapper = DataLayerWrapper()

    def add_team(self, team: list):
        """Adds a team to the database

        Args:
            list: list of team information

        Returns:
            None:
        """
        new_team = Team(team[self.TEAM_NAME], team[self.CLUB_NAME])

        self._add_team_to_club(new_team, team[self.CLUB_NAME])
        self.dl_wrapper.write_team(new_team)

    def get_players(self, team_name:str) -> list:
        """Retrieve a list of all registerd players in the mentioned team.

        Args:
            team_name (str): The name of the team you wish to look at players in.

        Returns:
            list: A list of all players registerd to a team.
        """
        team = self.dl_wrapper.read_team(team_name)
        return team.players

    def get_team_captain(self, team_name:str) -> Player:
        """Retrieve the player information for the team captain of the mentioned team.

        Args:
            team_name (str): The name of the team you wish to look at the captain in.

        Returns:
            Player: A instance of Player() with all the information on the player.
        """
        team = self.dl_wrapper.read_team(team_name)
        captain_id = team.team_captain
        return self.dl_wrapper.read_player(captain_id)

    def get_all_teams(self) -> list[Team]:
        """Returns list of teams in file"""
        return self.dl_wrapper.read_all_teams()

    def _get_team_club(self, club_name: str) -> Club:
        """Gets the club that the team is signed into"""
        all_clubs = self.dl_wrapper.read_all_clubs()
        team_club = None
        for club in all_clubs:
            if club.name == club_name:
                team_club = club
        return team_club

    def _add_team_to_club(self, team: Team, club_name: str):
        """Adds a team to a club"""
        all_clubs = self.dl_wrapper.read_all_clubs()
        for club in all_clubs:
            if club.name == club_name:
                club.teams.append(team)
        club = self.dl_wrapper.read_club(club_name)
        self.dl_wrapper.update_club(club)
