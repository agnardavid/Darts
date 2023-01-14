from dl.dl_wrapper import DataLayerWrapper
from models.club import Club


class ClubLogic:

    # CLUB LIST INDEXES
    CLUB_NAME = 0
    ADDRESS = 1
    PHONE_NUMBER = 2
    
    def __init__(self):
        self.club = Club()
        self.dl_wrapper = DataLayerWrapper()

    def add_club(self, club: list):
        """Adds a new club to the database.

        Args:
            club (Club): Takes in instance of Club().

        Returns:
            None:
        """
        new_club = Club(club[self.CLUB_NAME], club[self.ADDRESS], club[self.PHONE_NUMBER])

        self.dl_wrapper.write_club(new_club)

    def get_all_clubs(self) -> list[Club]:
        """Gets all clubs in file"""
        all_clubs = self.dl_wrapper.read_all_clubs()
        return all_clubs

