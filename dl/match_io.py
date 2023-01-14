from dl.file_io import FileIO
from models.match import Match


class MatchIO:

    def __init__(self, filepath: str):
        self.fileio = FileIO(filepath, Match.fieldnames(), Match.id_field())

    def read_match(self, match_id: int) -> dict:
        """Gets data for match from file.

        Args:
            match_id (str): ID of match whose data to get.

        Returns:
            dict: dict with the data from the csv file for the match with that ID.
        """
        return self.fileio.read_file(match_id)

    def read_all_matches(self) -> list[dict]:
        """Gets data for all matches from file.

        Returns:
            list[dict]: A list with the data from the csv file for all matches in the file.
        """
        return self.fileio.read_all_from_file()

    def write_match(self, match: Match):
        """Writes data for match to file.

        Args:
            match (Match): The match object to write.
        """
        match_dict = match.as_dict()
        self.fileio.write_file(match_dict)

    def update_match(self, match: Match):
        """Updates data for match on file or adds if it does not exist there.

        Args:
            match (Match): The match object to update or write.
        """
        self.fileio.update_file(match.as_dict())
