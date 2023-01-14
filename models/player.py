

MONTHS = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "Agust",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}


class Player:

    def __init__(self, name="", social_id="", email="", address="", gsm_number="", team="", role="Player", home_phone_number=""):
        self.name: str = name
        self.social_id: str = social_id
        self.email: str = email
        self.address: str = address
        self.home_phone_number: str = home_phone_number
        self.gsm_number: str = gsm_number
        self.team: str = team
        self.role: str = role
        self.date_of_birth: str = self._get_date_of_birth(self.social_id)

    def __str__(self) -> str:
        return f"""Player:
    Name: {self.name}
    Social id: {self.social_id}
    Email: {self.email}
    Address: {self.address}
    Home phone: {self.home_phone_number}
    GSM: {self.gsm_number}
    Team name: {self.team}
    Role: {self.role}
    DOB: {self.date_of_birth}
"""

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        if not o:
            return False
        else:
            return (self.name == o.name
                    and self.social_id == o.social_id
                    and self.email == o.email
                    and self.address == o.address
                    and self.home_phone_number == o.home_phone_number
                    and self.gsm_number == o.gsm_number
                    and self.team == o.team
                    and self.role == o.role
                    and self.date_of_birth == o.date_of_birth)

    def _get_date_of_birth(self, social_id: str):
        # Check if the social id is missing the first 0
        if len(social_id) == 9:
            social_id = "0" + social_id
        date = social_id[:2]
        # Slicing the 0 of if the person is born in the first 9 days of the month
        if date[0:1] == "0":
            dd = date[1:]
        else:
            dd = date
        mm = social_id[2:4]
        # Iterate over the MONTHS dict to find the correct written month
        for num, name in MONTHS.items():
            if num == mm:
                return f"{dd}. {name}"
        return f"{dd} some other month!"

    def fieldnames():
        return ["name", "social_id", "email", "address", "home_phone_number", "gsm_number", "role", "date_of_birth", "team"]

    def id_field():
        return "social_id"

    def as_dict(self):
        return {"name": self.name,
                "social_id": self.social_id,
                "email": self.email,
                "address": self.address,
                "home_phone_number": self.home_phone_number,
                "gsm_number": self.gsm_number,
                "team": self.team,
                "role": self.role,
                "date_of_birth": self.date_of_birth}

    def from_dict(player_data: dict):
        player = Player()
        player.name = player_data["name"]
        player.social_id = player_data["social_id"]
        player.email = player_data["email"]
        player.address = player_data["address"]
        player.home_phone_number = player_data["home_phone_number"]
        player.gsm_number = player_data["gsm_number"]
        player.team = player_data["team"]
        player.role = player_data["role"]
        player.date_of_birth = player_data["date_of_birth"]
        return player
