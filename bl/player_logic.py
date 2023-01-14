from models.team import Team
from dl.dl_wrapper import DataLayerWrapper
from models.player import Player


class PlayerLogic:
    
    # PLAYER LIST INDEX
    PLAYER_NAME = 0
    SOCIAL_ID = 1
    EMAIL = 2
    ADDRESS = 3
    GSM_NUMBER = 4
    TEAM_NAME = 5
    ROLE = 6
    HOME_PHONE_NUMBER = 7


    def __init__(self):
        self.player = Player()
        self.dl_wrapper = DataLayerWrapper()

    def add_player(self, player: list):
        """ Adds a new player to a team and to the database.

        Args:
            player (Player): Takes in an instance of Player().

        Returns:
            None:
        """
        new_player = Player(player[self.PLAYER_NAME], player[self.SOCIAL_ID], player[self.EMAIL], player[self.ADDRESS],
                            player[self.GSM_NUMBER], player[self.TEAM_NAME], player[self.ROLE],
                            player[self.HOME_PHONE_NUMBER])

        self._add_player_to_team(new_player, player[self.TEAM_NAME])
        self.dl_wrapper.write_player(new_player)

    def _get_player_team(self, team_name: str) -> Team:
        """Retrives the Team() instance from the database.

        Args:
            team_name (str): Name of the team.

        Returns:
            Team: Returns a Team() instance from the database.
        """
        all_teams = self.dl_wrapper.read_all_teams()
        player_team = None
        for team in all_teams:
            if team.name == team_name:
                player_team = team
        return player_team

    def assign_captain(self, captain_id:str, team_name:str):
        """Assigns a given player to a given team.

        Args:
            captain_id (str): Player social ID
            team_name (str): Team name
        """
        # Find
        player_team = self._get_player_team(team_name)
        all_players = self.dl_wrapper.read_all_players()
        # Update Team Captain
        captain = None
        for player in all_players:
            if player.social_id == captain_id:
                captain = player
        player_team.team_captain = captain.social_id
        captain.role = "Team Captain"
        # Save
        self.dl_wrapper.update_team(player_team)
        self.dl_wrapper.update_player(captain)

    def _add_player_to_team(self, player: Player, player_team: str):
        """Adds player to list of players in team object

        Args:
            player (Player): Instance of Player() to be added to team.
            player_team (Team): Instance of Team() that the player gets added to.
        """
        selected_player_team = self.dl_wrapper.read_team(player_team)
        selected_player_team.players.append(player)
        self.dl_wrapper.update_team(selected_player_team)
