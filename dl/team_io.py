from dl.file_io import FileIO
from models.team import Team


class TeamIO:

    def __init__(self, filepath: str):
        self.fileio = FileIO(filepath, Team.fieldnames(), Team.id_field())

    def read_team(self, team_name: str) -> dict:
        """Gets data for team from file.

        Args:
            team_name (str): Name of team whose data to get.

        Returns:
            dict: dict with the data from the csv file for the team with that name.
        """
        return self.fileio.read_file(team_name)

    def read_all_teams(self) -> list[dict]:
        """Gets data for all teams from file.

        Returns:
            list[dict]: A list with the data from the csv file for all teams in the file.
        """
        return self.fileio.read_all_from_file()

    def write_team(self, team: Team):
        """Writes data for team to file.

        Args:
            team (Team): The team object to write.
        """
        team_dict = team.as_dict()
        team_dict.pop("players")
        team_dict.pop("team_standing")
        self.fileio.write_file(team_dict)

    def update_team(self, team_to_update: Team):
        """Updates data for team on file or adds if it does not exist there.

        Args:
            team (Team): The team object to update or write.
        """
        data = team_to_update.as_dict()
        data.pop("players")
        data.pop("team_standing")
        self.fileio.update_file(data)
