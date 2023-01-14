####################
# CSV file manager #
####################
from csv import DictReader, DictWriter, Sniffer, Dialect, QUOTE_ALL, unix_dialect
from os.path import exists, dirname
from tempfile import NamedTemporaryFile
import os
import shutil


class FileIO:

    def __init__(self, filepath: str, fieldnames: list[str], unique_id_column: str = "id"):
        if not exists(dirname(filepath)):
            os.makedirs(dirname(filepath))
        self.filepath = filepath
        self.id_column = unique_id_column
        self.fieldnames = fieldnames
        self.dialect = unix_dialect

    def read_file(self, id_value: str) -> dict:
        """"Get item from the csv file.

        Args:
            id_value (str): ID og item to get.

        Returns:
            dict: a dictionary of columns and values read from the csv file.
        """
        id_value = str(id_value)
        all_rows = self.read_all_from_file()
        for row in all_rows:
            if row[self.id_column] == id_value:
                return row
        if len(all_rows) > 1:
            raise IdDoesNotExistError()

    def read_all_from_file(self) -> list[dict]:
        """"Get all rows from the csv file.

        Returns:
            list[dict]: A list of dicts of columns and row from the csv file.
        """
        try:
            with open(self.filepath, "r", newline="", encoding="utf-8") as csv_file:
                reader = DictReader(csv_file, fieldnames=self.fieldnames, dialect=self.dialect)
                return list(reader)[1:]  # skip the header
        except FileNotFoundError:
            return []

    def write_file(self, data: dict) -> None:
        """Writes data to a row in a csv formatted file.

        Args:
            data (dict): A dictionary with the data to write to the file.
                         Keys in the dict must match values in self.fieldnames
        """
        write_header = True
        if exists(self.filepath) and os.path.getsize(self.filepath) > 0:
            write_header = False

        if self.id_column and self.id_in_file(data[self.id_column], self.filepath):
            raise IdAlreadyExistsError

        with open(self.filepath, "a+t", newline="", encoding="utf-8") as csv_file:
            writer = DictWriter(csv_file, fieldnames=self.fieldnames, dialect=self.dialect)
            if write_header:
                writer.writeheader()
            writer.writerow(data)
            csv_file.flush()

    def update_file(self, updated_data: dict) -> bool:
        """Updates data in a row whose ID column matches the id in the passed dict.
           Adds the data no row with the same ID exists already.

        Args:
            updated_data (dict): A dictionary with data to update or write.
                                 Keys in the dict must match values in self.fieldnames
        """
        updated = False
        tempfile = NamedTemporaryFile("w+t", newline="", delete=False, encoding="utf-8")
        if exists(self.filepath):
            mode = "r+"
        else:
            mode = "a+"
        with open(self.filepath, mode, newline="", encoding="utf-8") as csv_file, tempfile:
            reader = DictReader(csv_file, dialect=self.dialect)
            writer = DictWriter(tempfile, fieldnames=self.fieldnames, dialect=self.dialect)
            writer.writeheader()
            for row in reader:
                if row[self.id_column] == str(updated_data[self.id_column]):
                    row = updated_data
                    updated = True
                writer.writerow(row)
            csv_file.flush()
            tempfile.flush()
        shutil.move(tempfile.name, self.filepath)
        return updated

    def id_in_file(self, id: str, filepath: str) -> bool:
        """"Checks if a row with a particular ID exists in the csv file.

        Args:
            id (str): The ID to look for.
            filepath (str): The path of the csv file to search in.
        """
        id = str(id)
        if exists(filepath):
            with open(filepath, "r", newline="", encoding="utf-8") as file:
                reader = DictReader(file, dialect=self.dialect)
                found_id = False
                for row in reader:
                    if row[self.id_column] == id:
                        found_id = True
                file.seek(0)
                return found_id
        else:
            return False


class IdAlreadyExistsError(Exception):
    """Line with same ID already exists in file."""
    pass


class IdDoesNotExistError(Exception):
    """Line with the ID does not exist in the file."""
    pass
