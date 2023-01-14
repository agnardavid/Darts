
class Competition:

    def __init__(self, name="", organizer="", phone_number="", start_date="", end_date="", rounds=1, days=1):
        self.name: str = name
        self.organizer: str = organizer
        self.phone_number: str = phone_number
        self.start_date: str = start_date
        self.end_date: str = end_date
        self.teams: list = []
        self.rounds: int = rounds
        self.matches: list = []
        self.days: str = days

    def __str__(self):
        return f"""Competition:
    Name: {self.name},
    Teams: {self.teams},
    Phone number: {self.phone_number}
    Start date: {self.start_date}
    End date: {self.end_date}
    Teams: {self.teams}
    Rounds: {self.rounds}
    Matches: {self.matches}
    Days: {self.days}
"""

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        if not o:
            return False
        else:
            return (self.name == o.name
                    and self.organizer == o.organizer
                    and self.phone_number == o.phone_number
                    and self.start_date == o.start_date
                    and self.end_date == o.end_date
                    and self.teams == o.teams
                    and self.rounds == o.rounds
                    and self.matches == o.matches
                    and self.days == o.days
        )

    def as_dict(self):
        return {"name": self.name,
                "organizer": self.organizer,
                "phone_number": self.phone_number,
                "start_date": self.start_date,
                "end_date": self.end_date,
                "teams": self.teams,
                "rounds": self.rounds,
                "matches": self.matches,
                "days": self.days
                }

    def fieldnames():
        return ["name", "organizer", "phone_number", "start_date", "end_date",
                "rounds", "days"]

    def id_field():
        return "name"

    def from_dict(comp_dict: dict):
        comp = Competition()
        comp.name = comp_dict["name"]
        if "organizer" in comp_dict:
            comp.organizer = comp_dict["organizer"]
        if "phone_number" in comp_dict:
            comp.phone_number = comp_dict["phone_number"]
        if "start_date" in comp_dict:
            comp.start_date = comp_dict["start_date"]
        if "end_date" in comp_dict:
            comp.end_date = comp_dict["end_date"]
        if "teams" in comp_dict:
            comp.teams = comp_dict["teams"]
        if "rounds" in comp_dict:
            comp.rounds = int(comp_dict["rounds"])
        if "matches" in comp_dict:
            comp.matches = comp_dict["matches"]
        if "days" in comp_dict:
            comp.days = int(comp_dict["days"])
        return comp
