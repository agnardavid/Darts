

class Club:

    def __init__(self, name="", address="", phone_number="", teams=[]) -> None:
        self.name: str = name
        self.address: str = address
        self.phone_number: str = phone_number
        self.teams: list = teams

    def __str__(self) -> str:
        return f"Club name: {self.name}, Address: {self.address}, Phone number: {self.phone_number}, Teams: {self.teams}\n"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        if not o:
            return False
        else:
            return self.name == o.name and self.address == o.address and self.phone_number == o.phone_number and self.teams == o.teams

    def as_dict(self):
        return {"name": self.name,
                "address": self.address,
                "phone_number": self.phone_number,
                # "teams": self.teams
                }

    def fieldnames():
        return ["name", "address", "phone_number"]

    def id_field():
        return "name"

    def from_dict(club_data: dict):
        club = Club()
        if "name" in club_data:
            club.name = club_data["name"]
        if "address" in club_data:
            club.address = club_data["address"]
        if "phone_number" in club_data:
            club.phone_number = club_data["phone_number"]
        if "teams" in club_data:
            club.teams = club_data["teams"]
        return club
