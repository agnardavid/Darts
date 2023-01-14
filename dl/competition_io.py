##########################################################
#         IO intermediate layer for Competition
##########################################################

from dl.file_io import FileIO
from models.competition import Competition


class CompetitionIO:

    def __init__(self, filepath):
        self.fileio = FileIO(filepath, Competition.fieldnames(), Competition.id_field())

    def read_competition(self, competition_name: str) -> dict:
        """Gets data for competition from file.

        Args:
            competition_name (str): Name of competition whose data to get.

        Returns:
            dict: dict with the data from the csv file for the competition with that name.
        """
        return self.fileio.read_file(competition_name)

    def read_all_competitions(self) -> list[dict]:
        """Gets data for all competitions from file.

        Returns:
            list[dict]: A list with the data from the csv file for all competitions in the file.
        """
        return self.fileio.read_all_from_file()

    def write_competition(self, competition: Competition):
        """Writes data for competition to file.

        Args:
            competition (Competition): The competition object to write.
        """
        comp_dict = competition.as_dict()
        comp_dict.pop("teams")
        comp_dict.pop("matches")
        self.fileio.write_file(comp_dict)

    def update_competition(self, competition: Competition):
        """Updates data for competition on file or adds if it does not exist there.

        Args:
            competition (Competition): The competition object to update or write.
        """
        comp_dict = competition.as_dict()
        comp_dict.pop("teams")
        comp_dict.pop("matches")
        self.fileio.update_file(comp_dict)
