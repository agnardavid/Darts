###################################
# The interface to the data layer #
###################################

from dl.club_io import ClubIO
from dl.competition_io import CompetitionIO
from dl.link_table_io import LinkTableIO
from dl.match_io import MatchIO
from dl.player_io import PlayerIO
from dl.team_io import TeamIO
from dl.team_standing_io import TeamStandingIO
from models.club import Club
from models.competition import Competition
from models.match import Match
from models.player import Player
from models.team import Team
from os import makedirs
from os.path import exists
import dl.data_constants as dconst
from os.path import join


class DataLayerWrapper:

    def __init__(self, data_folder=dconst.DATA_FOLDER):
        self.data_folder = data_folder
        if not exists(self.data_folder):
            makedirs(self.data_folder)

        self.team_standing_io = TeamStandingIO(join(self.data_folder, dconst.TEAM_STANDINGS_FILENAME))
        self.competition_io = CompetitionIO(join(self.data_folder, dconst.COMPETITION_FILENAME))
        self.club_io = ClubIO(join(self.data_folder, dconst.CLUB_FILENAME))
        self.team_io = TeamIO(join(self.data_folder, dconst.TEAM_FILENAME))
        self.player_io = PlayerIO(join(self.data_folder, dconst.PLAYER_FILENAME))
        self.match_io = MatchIO(join(self.data_folder, dconst.MATCH_FILENAME))
        self.club_team_link_io = LinkTableIO(
            join(self.data_folder, dconst.CLUB_TEAM_LINK_FILENAME), ["club_id", "team_id"]
        )
        self.team_player_link_io = LinkTableIO(
            join(self.data_folder, dconst.TEAM_PLAYER_LINK_FILENAME), ["team_id", "player_id"]
        )
        self.competition_team_link_io = LinkTableIO(
            join(self.data_folder, dconst.COMPETITION_TEAM_LINK_FILENAME), ["competition_id", "team_id"]
        )
        self.competition_match_link_io = LinkTableIO(
            join(self.data_folder, dconst.COMPETITION_MATCH_LINK_FILENAME), ["competition_id", "match_id"]
        )
        self.match_competition_link_io = LinkTableIO(
            join(self.data_folder, dconst.MATCH_COMPETITION_LINK_FILENAME), ["match_id", "competition_id"]
        )

    def read_competition(self, competition_name: str) -> Competition:
        """Gets a competition by name.

        Args:
            competition_name (str): Name of competition to get.

        Returns:
            Competition: The competition with the specified name if it exists in the database.
        """
        comp_data = self.competition_io.read_competition(competition_name)
        comp = Competition.from_dict(comp_data)
        team_names = self.competition_team_link_io.get_all_with_id(comp.name)
        comp.teams = [self.read_team(name) for name in team_names]
        match_ids = self.competition_match_link_io.get_all_with_id(comp.name)
        comp.matches = [self.read_match(match_id) for match_id in match_ids]
        return comp

    def read_all_competitions(self) -> list[Competition]:
        """Get all competitions in the database.

        Returns:
            list[Competition]: A list of all competitions stored in the database.
        """
        comps = self.competition_io.read_all_competitions()
        return [self.read_competition(comp["name"]) for comp in comps]

    def read_club(self, club_name: str) -> Club:
        """Gets a club by name.

        Args:
            club_name (str): Name of club to get.

        Returns:
            Club: The club with the specified name if it exists in the database.
        """
        club_data = self.club_io.read_club(club_name)
        team_names = self.club_team_link_io.get_all_with_id(club_data["name"])
        club_data["teams"] = [self.read_team(team) for team in team_names]
        return Club.from_dict(club_data)

    def read_all_clubs(self) -> list[Club]:
        """Get all clubs in the database.

        Returns:
            list[Club]: A list of all clubs stored in the database.
        """
        clubs = self.club_io.read_all_clubs()
        return [self.read_club(club["name"]) for club in clubs]

    def read_team(self, team_name: str) -> Team:
        """Gets a team by name.

        Args:
            team_name (str): Name of team to get.

        Returns:
            Team: The team with the specified name if it exists in the database.
        """
        team = self.team_io.read_team(team_name)
        player_ids = self.team_player_link_io.get_all_with_id(team["name"])
        team["players"] = [self.read_player(pid) for pid in player_ids]
        standings = []
        for standing_data in self.team_standing_io.get_standings(team["name"]):
            competition = Competition.from_dict(self.competition_io.read_competition(standing_data["competition name"]))
            wins = int(standing_data["wins"])
            won_legs = int(standing_data["won legs"])
            standings.append([competition, wins, won_legs])
        team["team_standing"] = standings
        return Team.from_dict(team)

    def read_all_teams(self) -> list[Team]:
        """Get all teams in the database.

        Returns:
            list[Team]: A list of all teams stored in the database.
        """
        teams = self.team_io.read_all_teams()
        return [self.read_team(team["name"]) for team in teams]

    def read_player(self, player_social_id: str) -> Player:
        """Gets a player by social id.

        Args:
            player_social_id (str): Social ID of player  to get.

        Returns:
            Player: The player with the specified ID if they exist in the database.
        """
        player_data = self.player_io.read_player(player_social_id)
        return Player.from_dict(player_data)

    def read_all_players(self) -> list[Player]:
        """Get all players in the database.

        Returns:
            list[Player]: A list of all players stored in the database.
        """
        players_data = self.player_io.read_all_players()
        return [self.read_player(row["social_id"]) for row in players_data]

    def read_match(self, match_id: str) -> Match:
        """Gets a match by ID.

        Args:
            match_id (str): ID of match to get.

        Returns:
            Match: The match with the specified ID if it exists in the database.
        """
        match_dict = self.match_io.read_match(match_id)
        return Match.from_dict(match_dict)

    def read_all_matches(self) -> list[Match]:
        """Get all matches in the database.

        Returns:
            list[Match]: A list of all matches stored in the database.
        """
        return [self.read_match(data["match_id"]) for data in self.match_io.read_all_matches()]

    def write_competition(self, competition: Competition):
        """Adds a competition to the database.

        Args:
            competition (Competition): The competition object to add.

        """
        self.competition_io.write_competition(competition)
        for match in competition.matches:
            self.competition_match_link_io.add_link((competition.name, match.match_id))
        for team in competition.teams:
            self.competition_team_link_io.add_link((competition.name, team.name))

    def write_club(self, club: Club):
        """Adds a club to the database.

        Args:
            club (Club): The club object to add.

        """
        self.club_io.write_club(club)
        for team in club.teams:
            self.club_team_link_io.add_link((club.name, team.name))

    def write_team(self, team: Team):
        """Adds a team to the database.

        Args:
            team (Team): The team object to add.

        """
        self.team_io.write_team(team)
        for player in team.players:
            self.team_player_link_io.add_link((team.name, player.social_id))
        self.team_standing_io.set_standings(team.name, team.team_standing)

    def write_player(self, player: Player):
        """Adds a player to the database.

        Args:
            player (Player): The player object to add.

        """
        self.player_io.write_player(player)

    def write_match(self, match: Match):
        """Adds a match to the database.

        Args:
            match (Match): The match object to add.

        """
        self.match_io.write_match(match)

    def update_competition(self, competition: Competition):
        """Updates a competition in the database. Or adds it if it doesn't exist yet.

        Args:
            competition (Competition): The competition object to update.

        """
        self.competition_io.update_competition(competition)
        for match in competition.matches:
            self.competition_match_link_io.add_link((competition.name, str(match.match_id)))
        for team in competition.teams:
            self.competition_team_link_io.add_link((competition.name, team.name))

    def update_club(self, club: Club):
        """Updates a club in the database. Or adds it if it doesn't exist yet.

        Args:
            club (Club): The club object to update.

        """
        self.club_io.update_club(club)
        for team in club.teams:
            self.club_team_link_io.add_link((club.name, team.name))

    def update_team(self, team: Team):
        """Updates a team in the database. Or adds it if it doesn't exist yet.

        Args:
            team (Team): The team object to update.

        """
        self.team_io.update_team(team)
        for player in team.players:
            self.team_player_link_io.add_link((team.name, player.social_id))
        self.team_standing_io.set_standings(team.name, team.team_standing)

    def update_player(self, player: Player):
        """Updates a player in the database. Or adds it if it doesn't exist yet.

        Args:
            player (Player): The player object to update.

        """
        self.player_io.update_player(player)

    def update_match(self, match: Match):
        """Updates a match in the database. Or adds it if it doesn't exist yet.

        Args:
            match (Match): The match object to update.

        """
        self.match_io.update_match(match)
