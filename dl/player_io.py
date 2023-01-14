from dl.file_io import FileIO
from models.player import Player


class PlayerIO:

    def __init__(self, filepath: str):
        self.fileio = FileIO(filepath, Player.fieldnames(), Player.id_field())

    def read_player(self, player_id: str) -> dict:
        """Gets data for player from file.

        Args:
            player_id (str): Social ID of player whose data to get.

        Returns:
            dict: dict with the data from the csv file for the player with that ID.
        """
        return self.fileio.read_file(player_id)

    def read_all_players(self) -> list[dict]:
        """Gets data for all players from file.

        Returns:
            list[dict]: A list with the data from the csv file for all players in the file.
        """
        return self.fileio.read_all_from_file()

    def write_player(self, player: Player):
        """Writes data for player to file.

        Args:
            player (Player): The player object to write.
        """
        player_dict = player.as_dict()
        self.fileio.write_file(player_dict)

    def update_player(self, player: Player):
        """Updates data for player on file or adds if it does not exist there.

        Args:
            player (Player): The player object to update or write.
        """
        self.fileio.update_file(player.as_dict())
