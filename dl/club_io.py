##########################################################
#             IO intermediate layer for Club
##########################################################

from dl.file_io import FileIO
from models.club import Club


class ClubIO:

    def __init__(self, filepath: str):
        self.fileio = FileIO(filepath, Club.fieldnames(), Club.id_field())

    def read_club(self, club_name: str) -> dict:
        """Gets data for club from file.

        Args:
            club_name (str): Name of club whose data to get.

        Returns:
            dict: dict with the data from the csv file for the club with that name.
        """
        return self.fileio.read_file(club_name)

    def read_all_clubs(self) -> list[dict]:
        """Gets data for all clubs from file.

        Returns:
            list[dict]: A list with the data from the csv file for all clubs in the file.
        """
        return self.fileio.read_all_from_file()

    def write_club(self, club: Club):
        """Writes data for club to file.

        Args:
            club (Club): The Club object to write.
        """
        club_dict = club.as_dict()
        self.fileio.write_file(club_dict)

    def update_club(self, club_to_update: Club):
        """Updates data for club on file or adds if it does not exist there.

        Args:
            club (Club): The Club object to update or write.
        """
        club_dict = club_to_update.as_dict()
        self.fileio.update_file(club_dict)
