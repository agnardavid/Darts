from bl.club_logic import ClubLogic
from bl.competition_logic import CompetitionLogic
from bl.match_logic import MatchLogic
from bl.player_logic import PlayerLogic
from bl.show_logic import ShowLogic
from bl.team_logic import TeamLogic
from models.club import Club
from models.competition import Competition
from models.match import Match
from models.player import Player
from models.team import Team
from bl.validation_logic import ValidationLogic

class BusinessLogicWrapper:

    def __init__(self):
        self.competition_logic = CompetitionLogic()
        self.club_logic = ClubLogic()
        self.team_logic = TeamLogic()
        self.player_logic = PlayerLogic()
        self.match_logic = MatchLogic()
        self.show_logic = ShowLogic()
        self.validation_logic = ValidationLogic()
        self.is_test = False
# ----------------------------------------------------------------------------- Add methods

    def add_competition(self, competition_form: list):
        """Adds competition to database"""
        if self.is_test:
            return print(f"Competition {competition_form[0]} - added")  # DEL
        else:
            self.competition_logic.add_competition(competition_form)

    def add_team_to_competition(self, team_name, competition_name: str):
        """Adds team to selected competition"""
        if self.is_test:
            return print(f"{team_name} - Added")  # DEL
        else:
            self.competition_logic.add_team_to_competition(team_name, competition_name)

    def add_club(self, club_form: list):
        """Adds a new club to file."""
        if self.is_test:
            return print(f"Club {club_form[0]} - added")  # DEL
        else:
            self.club_logic.add_club(club_form)

    def add_team(self, team_form: list):
        """Adds a team to file"""
        if self.is_test:
            return print(f"Team {team_form[0]} - added")  # DEL
        else:
            self.team_logic.add_team(team_form)

    def add_player(self, player_form: list):
        """ Adds a new player to file"""
        if self.is_test:
            return print(f"Player {player_form[0]} - added")  # DEL
        else:
            self.player_logic.add_player(player_form)

    def add_result(self, match_id: str, home_team_score: str, away_team_score: str):
        """Adds new result to match"""
        if self.is_test:
            return print(f"Added result to game: {match_id}")  #DEL
        else:
            self.match_logic.add_results(match_id, home_team_score, away_team_score)

# ----------------------------------------------------------------------------- Get methods

    def get_competition_list(self) -> list[Competition]:
        """Gets all competitions in database as list"""
        if self.is_test:
            return [Competition("Comp 1", "Oliver", "8207476", "15-12-2022", "20-12-2022", 1),
                    Competition("Comp 2", "Daniel", "5812345", "02-12-2022", "24-12-2022", 1)]
        else:
            return self.competition_logic.get_competition_list()

    def get_competition_matches(self, competition_name) -> list[Match]:
        """Gets all matches registered in competition as list"""
        if self.is_test:
            return [Match("Pilu Kóngarnir", "Stormtroopers", "2022-11-28"),
                    Match("Stormtroopers", "Pilu Kóngarnir", "2022-11-29")]
        else:
            return self.competition_logic.get_competition_matches(competition_name)

    def get_competition_info(self, competition_name) -> Competition:
        """Gets info on competition (name, organizer, phone number, date, rounds)"""
        if self.is_test:
            return Competition("Comp 1", "Oliver", "8207476", "15-12-2022", "20-12-2022", 1)
        else:
            return self.competition_logic.get_competition_info(competition_name)

    def get_unplayed_matches(self, competition_name) -> list[Match]:
        """Gets all unplayed matches in competition returns as list of matches"""
        if self.is_test:
            return [Match("Pilu Kóngarnir", "Stormtroopers", "2022-11-28"),
                    Match("HK", "Valur", "2022-12-02")]
        else:
            return self.competition_logic.get_unplayed_matches(competition_name)

    def get_played_matches(self, competition_name) -> list[Match]:
        """Gets all played matches in competition returns as list of matches"""
        if self.is_test:
            return [Match("Stormtroopers", "Pilu Kóngarnir", "2022-11-29"),
                    Match("Pílu Kóngarnir", "Stormtroopers", "2022-11-30")]
        else:
            return self.competition_logic.get_played_matches(competition_name)

    def get_competition_standing(self, competition_name) -> list:
        """Gets standings in competition in order of won matches then number of won legs,
            otherwise in alphabetical order"""
        if self.is_test:
            return [Team("Pílulið 1"), Team("Pílulið 2"), Team("Pílulið 3")]
        else:
            return self.competition_logic.get_competition_standing(competition_name)

    def get_matches(self, competition_name) -> list[Match]:
        """Get all matches in competition, return as list"""
        if self.is_test:
            return [Match("Pilu Kóngarnir", "Stormtroopers", "2022-11-28"),
                    Match("Stormtroopers", "Pilu Kóngarnir", "2022-11-29")]
        else:
            return self.competition_logic.get_competition_matches(competition_name)

    def get_players(self, team_name) -> list[Player]:
        """Get list of all players in team"""
        if self.is_test:
            return [Player("Gylfi Þór Guðmundsson", "040377-2430", "gylfig@ru.is", "Menntavegi 1", "8625510", "Stormtroopers", "Team Captain", "5996200"),
                    Player("Oliver Ormar", "010801-2220", "gylfig@ru.is", "Menntavegi 1", "8625510", "Pilu Kóngarnir", "Player", "5996200")]
        else:
            return self.team_logic.get_players(team_name)

    def get_team_captain(self, team_name) -> Player:
        """Get name of team captain for team"""
        if self.is_test:
            return Player("Gylfi Þór Guðmundsson", "010177-6789", "gylfig@ru.is", "Menntavegi 1", "8625510", "Pilu Kóngarnir", "Teamcaptain", "5996200")
        else:
            return self.team_logic.get_team_captain(team_name)

    def get_competition_teams(self, competition_name) -> list[Team]:
        """Get list of teams in competition"""
        if self.is_test:
            return [Team("Stormtroopers", "Liverpool"),
                    Team("Pilu Kóngarnir", "Arsenal")]
        else:
            return self.competition_logic.get_competition_teams(competition_name)

    def get_all_teams(self) -> list[Team]:
        """Return a list of all teams registered in database"""
        if self.is_test:
            return [Team("Pílulið 1"), Team("Pílulið 2"), Team("Pílulið 3"), Team("Pílulið 4")]
        else:
            return self.team_logic.get_all_teams()

    def get_all_clubs(self) -> list[Club]:
        """Return list of all clubs in file"""
        if self.is_test:
            return [Club("Raketunar", "Menntavegi 1", "5996200"),
                    Club("Liverpool", "Street 14", "5812345"),
                    Club("Arsenal", "Dongle Street 4", "7771310"),]
        else:
            return self.club_logic.get_all_clubs()

    def get_captain_matches(self, competition_name, captain_ssn) -> list[Match]:
        """Gets list of matches that captain can edit"""
        if self.is_test:
            return [Match("Pilu Kóngarnir", "Stormtroopers", "2022-11-28"),
                    Match("Pilu Kóngarnir", "Liverpool", "2022-11-29"),
                    Match("Pilu Kóngarnir", "Arsenal", "2022-11-30")]
        else:
            return self.competition_logic.get_captain_matches(competition_name, captain_ssn)

# ----------------------------------------------------------------------------- Special Methods

    def clean_numbers(self, elem:str) -> str:
        """Cleans a string and return only numbers in string.

        Args:
            elem (str): A string which may or may not contain numbers

        Returns:
            str: Returns only the numbers that were in the string in the same order.
        """
        return self.validation_logic.clean_numbers(elem)

    def delay_match(self, match_id, match_date):
        """Delays match to selected date"""
        if self.is_test:
            return print(f"{match_id} delayed to {match_date}")
        else:
            return self.match_logic.delay_match(match_id, match_date)

    def assign_captain(self, captain_id:str, team_name:str):
        """Assigns player as captain in team"""
        if self.is_test:
            return print(f"{captain_id} Added as Captain to {team_name}")
        else:
            self.player_logic.assign_captain(captain_id, team_name)

    def edit_match(self, match_id: str, games_list: list):
        """Changes the score in a match"""
        if self.is_test:
            return print(f"{match_id} - Edited")
        else:
            self.match_logic.edit_match(match_id, games_list)

    def generate_match_schedule(self, competition_name:str):
        """Generates all matches with all teams that have been added to competition.\n
        Uses Round Robin to generate matches.

        Args:
            competition_name (str): Name of competition.
        """
        self.competition_logic.generate_match_schedule(competition_name)

    def reset_match_data(self, match_id: str):
        """Reset match scorebard and games if user cancels adding score"""
        self.match_logic.reset_match_data(match_id)

# ----------------------------------------------------------------------------- Validate

    def validate_phone(self, phone_number:str) -> bool:
        """Validates a phone number.

        Args:
            phone_number (str): Phone number.

        Returns:
            bool: True if the phone number is valid, False if the phone number is invalid.
        """
        return self.validation_logic.validate_phone(phone_number)
    
    def validate_game_score(self, score:str) -> bool:
        """Validates that the input score is 0, 1 or 2.

        Args:
            score (str): Match score.

        Returns:
            bool: Returns True if the score is 0, 1 or 2, Returns False if score is something else.
        """
        return self.validation_logic.validate_game_score(score)

    def validate_names(self, user_name:str) -> bool:
        """Checks if the name has digits or punctuations.

        Args:
            user_name (str): User name.

        Returns:
            bool: Returns True if the user name has no digits or punctuations, Returns False otherwise.
        """
        return self.validation_logic.validate_names(user_name)

    def validate_club(self, club_name:str) -> bool:
        """Validates that the club exists.

        Args:
            club_name (str): Club name.

        Returns:
            bool: True if the club exists, False if the club does not exist.
        """
        return self.validation_logic.validate_club(club_name)

    def validate_ssn(self, ssn:str) -> bool:
        """Validates if the social ID is real.

        Args:
            ssn (str): Social ID.

        Returns:
            bool: True if the social ID is valid for use, False if it is not valid for use.
        """
        return self.validation_logic.validate_ssn(ssn)

    def validate_ssn_of_team_captain(self, ssn:str) -> bool:
        """Validates if the ssn belongs to a Team Captain.

        Args:
            ssn (str): Social ID.

        Returns:
            bool: Returns True if the social ID belongs to a registerd Team Captain, returns False otherwise.
        """
        return self.validation_logic.validate_ssn_of_team_captain(ssn)

    def validate_if_ssn_is_in_use(self, ssn:str) -> bool:
        """Validates if social id is already registerd.

        Args:
            ssn (str): Social ID.

        Returns:
            bool: True if the social id is not in use, False if it is in use.
        """
        return self.validation_logic.validate_if_ssn_is_in_use(ssn)

    def validate_email(self, email:str) -> bool:
        """Validates the email address.

        Args:
            email (str): User email address.

        Returns:
            bool: True if the email is valid, False if the email is invalid.
        """
        return self.validation_logic.validate_email(email)

    def validate_team(self, team_name:str) -> bool:
        """Validates that the team exists.

        Args:
            team_name (str): Name of the team.

        Returns:
            bool: True if the Team exists, False if the team does not exist.
        """
        return self.validation_logic.validate_team(team_name)

    def validate_if_comp_name_is_unique(self, comp_name:str) -> bool:
        """Validates if the Competition name is unique.

        Args:
            comp_name (str): Name of the competition.

        Returns:
            bool: True if the name is unique, False if the name already exists.
        """
        # return self.validation_logic.validate_if_comp_name_is_unique(comp_name)
        return True
    
    def validate_comp_rounds(self, rounds:str) -> bool:
        """Checks if comp rounds is >0.

        Args:
            rounds (str): Rounds of comp.

        Returns:
            bool: Returns True if rounds is higher then 0, Returns False otherwise.
        """
        return self.validation_logic.validate_comp_rounds(rounds)
    
    def validate_combined_game_score(self, home_team_score:str, away_team_score:str) -> bool:
        """Checks if the game score is valid.

        Args:
            home_team_score (str): Home team score.
            away_team_score (str): Away team score.

        Returns:
            bool: Returns True if score outcome is possible, Returns False otherwise.
        """
        return self.validation_logic.validate_combined_game_score(home_team_score, away_team_score)

    def validate_start_date(self, start_date:str) -> bool:
        """Validates if the starting date has passed or not and if the date is in calender.

        Args:
            start_date (str): Start date. DAY-MONTH-YEAR or DD-MM-YYYY.

        Returns:
            bool: _Returns True if the date is today or in the future, Returns False if the date has passed.
        """
        return self.validation_logic.validate_start_date(start_date)

    def validate_match_delay_date(self, start_date:str, end_date:str, new_date:str) -> bool:
        """Validates if delay date is within start and end dates.

        Args:
            start_date (str): Start date. DAY-MONTH-YEAR or DD-MM-YYYY.
            end_date (str): End date. DAY-MONTH-YEAR or DD-MM-YYYY.
            new_date (str): New/delay date. DAY-MONTH-YEAR or DD-MM-YYYY.

        Returns:
            bool: Returns True if the new/delay date is within start and end date, returns False otherwise.
        """
        return self.validation_logic.validate_match_delay_date(start_date, end_date, new_date)

    def validate_dates(self, start_date:str,end_date:str) -> bool:
        """Validates if the start date is prior or the same as the end date. Also checks if the dates are in calender.

        Args:
            start_date (str): Start date. DAY-MONTH-YEAR or DD-MM-YYYY.
            end_date (str): End date. DAY-MONTH-YEAR or DD-MM-YYYY.

        Returns:
            bool: Returns True if the start date is prior or the same as the end date, returns False otherwise.
        """
        return self.validation_logic.validate_dates(start_date, end_date)

    def validate_year(self, year:str) -> bool:
        '''Validates the format for a year and checks if it can be casted to an int.
        
        Args:
            year (str): YYYY

        Returns:
            bool: Returns True if the given format is valid'''
        return self.validation_logic.validate_year(year)

    def validate_month(self, month:str) -> bool:
        '''Validates the format for a month and checks if it can be casted to an int.
        
        Args:
            month (str): M or MM

        Returns:
            bool: Returns True if the given format is valid'''
        return self.validation_logic.validate_month(month)

    def validate_day(self, day:str) -> bool:
        '''Validates the format for a day and checks if it can be casted to an int.
        
        Args:
            day (str): D or DD

        Returns:
            bool: Returns True if the given format is valid'''
        return self.validation_logic.validate_day(day)

# ----------------------------------------------------------------------------- UI and Display

    def get_darts_display(self) -> list:
        '''gets a list of lines to display at the top and bottom of a menu'''
        return self.show_logic.get_darts_display()
    
    def ui_menu_option_width(self,option_list, width:str) -> tuple:
        '''gets list of menu options and width to calculate spaces to 
        center menu based on the longest line'''
        return self.show_logic.ui_menu_option_width(option_list, width)
    
    def ui_menu_option_center_colon(self,option:str) -> tuple:
        '''gets a menu option with colon, splits in two on colon and returns'''
        return self.show_logic.ui_menu_option_center_colon(option)