from dl.file_io import FileIO
from models.competition import Competition


class TeamStandingIO:

    def __init__(self, filepath: str):
        self.fieldnames = ["id", "team name", "competition name", "wins", "won legs"]
        self.id_field = self.fieldnames[0]
        self.fileio = FileIO(filepath, self.fieldnames, self.id_field)

    def get_standings(self, team_name: str):
        """Gets standings for team from file.

        Args:
            team_name (str): Name of team whose standings to get.

        Returns:
            dict: dict with the standings from the csv file for the team with that name.
        """
        all_standings = self.fileio.read_all_from_file()
        return [standing_data for standing_data in all_standings if standing_data["team name"] == team_name]

    def set_standings(self, team_name: str, standings: list[list[Competition, int, int]]):
        """Updates standings for team on file or adds them if it does not exist there.

        Args:
            team_name (team_name): The name of the team.
            standings (list[list[Competition, int, int]])
        """
        for standing in standings:
            competition_name = standing[0].name
            wins = standing[1]
            won_legs = standing[2]
            data = self._format_data(team_name, competition_name, wins, won_legs)
            if not self.fileio.update_file(data):
                self.fileio.write_file(data)

    def _format_data(self, team_name: str, competition_name: str, wins: int, won_legs) -> dict:
        """Formats the data into a dict.

        Args:
            team_name (str): name of team
            competition_name (str): name of competition
            wins (int): how many wins the team has in the competition
            won_legs (int): how many legs the team has won in the competition

        Returns:
            dict: A dictionary with the keys from the predetermined fieldnames
                  and the data passed to the dict.
        """
        return {
            self.fieldnames[0]: f"{team_name}+{competition_name}",
            self.fieldnames[1]: team_name,
            self.fieldnames[2]: competition_name,
            self.fieldnames[3]: wins,
            self.fieldnames[4]: won_legs
        }
