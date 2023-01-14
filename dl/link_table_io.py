from dl.file_io import FileIO


class LinkTableIO:

    def __init__(self, filepath: str, columns: list[str]):
        if len(columns) != 2:
            raise ValueError("Thers should be only two columns.")
        self.fileio = FileIO(filepath, columns, None)
        self.columns = columns

    def get_all_with_id(self, id: str) -> list[dict]:
        """Get all values from link file with a particular ID.

        Args:
            id (str): the ID whose values to get.

        Returns:
            list[str]: list of all values from the link file with that ID
        """
        lines = self.fileio.read_all_from_file()
        return [row[self.columns[1]] for row in lines if row[self.columns[0]] == id]

    def add_link(self, link: tuple[str, str]):
        """Adds a link to the link file.

        Args:
            link (tuple[str, str]): A two tuple with an id and a value to add.

        """
        links = self.fileio.read_all_from_file()
        for existing_link in links:
            if existing_link[self.columns[1]] == link[1]:
                return
        self.fileio.write_file({self.columns[0]: link[0], self.columns[1]: link[1]})
