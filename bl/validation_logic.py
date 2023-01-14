from dl.dl_wrapper import DataLayerWrapper
from datetime import date
import string

class ValidationLogic:
    
    def __init__(self) -> None:
        self.dl_wrapper = DataLayerWrapper()
    
    def validate_phone(self, phone_number:str) -> bool:
        """Validates a phone number.

        Args:
            phone_number (str): Phone number.

        Returns:
            bool: True if the phone number is valid, False if the phone number is invalid.
        """
        p_num = self.clean_numbers(phone_number)
        if len(p_num) == 7 or len(p_num) == 10:
            return True
        return False
    
    def clean_numbers(self, elem:str) -> str:
        """Cleans a string and return only numbers in string.

        Args:
            elem (str): A string.

        Returns:
            str: Returns only the numbers that were in the string in the same order.
        """
        number = ""
        for char in elem:
            if char.isdigit():
                number += char
        return number
    
    def validate_game_score(self, score:str) -> bool:
        """Validates that the input score is 0, 1 or 2.

        Args:
            score (str): Match score.

        Returns:
            bool: Returns True if the score is 0, 1 or 2, Returns False if score is something else.
        """
        if score.isdigit():
            if score in ["0", "1", "2"]:
                return True
        return False

    def validate_names(self, user_name:str) -> bool:
        """Checks if the name has digits or punctuations.

        Args:
            user_name (str): User name.

        Returns:
            bool: Returns True if the user name has no digits or punctuations, Returns False otherwise.
        """
        for char in user_name:
            if char in string.punctuation or char.isdigit():
                return False
        return True
    
    def validate_club(self, club_name:str) -> bool:
        """Validates that the club exists.

        Args:
            club_name (str): Club name.

        Returns:
            bool: True if the club exists, False if the club does not exist.
        """
        all_clubs = self.dl_wrapper.read_all_clubs()
        for club in all_clubs:
            if club.name == club_name:
                return True
        return False
    
    def validate_ssn(self, ssn:str) -> bool:
        """Validates if the social ID is real.

        Args:
            ssn (str): Social ID.

        Returns:
            bool: True if the social ID is valid for use, False if it is not valid for use.
        """
        ssn_num = self.clean_numbers(ssn)
        if len(ssn_num) == 10:
            return True
        return False
 
    def validate_ssn_of_team_captain(self, ssn:str) -> bool:
        """Validates if the ssn belongs to a Team Captain.

        Args:
            ssn (str): Social ID.

        Returns:
            bool: Returns True if the social ID belongs to a registerd Team Captain, returns False otherwise.
        """
        all_players = self.dl_wrapper.read_all_players()
        ssn_num = self.clean_numbers(ssn)
        for player in all_players:
                player_ssn = self.clean_numbers(player.social_id)
                if ssn_num == player_ssn and player.role == "Team Captain":
                    return True
        return False
    
    def validate_if_ssn_is_in_use(self, ssn:str) -> bool:
        """Validates if social id is already registerd.

        Args:
            ssn (str): Social ID.

        Returns:
            bool: True if the social id is not in use, False if it is in use.
        """
        all_players = self.dl_wrapper.read_all_players()
        ssn_num = self.clean_numbers(ssn)
        for player in all_players:
                player_ssn = self.clean_numbers(player.social_id)
                if ssn_num == player_ssn:
                    return False
        return True

    def validate_email(self, email:str) -> bool:
        """Validates the email address.

        Args:
            email (str): User email address.

        Returns:
            bool: True if the email is valid, False if the email is invalid.
        """
        if "@" in email:
            return True
        return False

    def validate_team(self, team_name:str) -> bool:
        """Validates that the team exists.

        Args:
            team_name (str): Name of the team.

        Returns:
            bool: True if the Team exists, False if the team does not exist.
        """
        all_teams = self.dl_wrapper.read_all_teams()
        for team in all_teams:
            if team.name == team_name:
                return True
        return False
    
    def validate_if_comp_name_is_unique(self, comp_name:str) -> bool:
        """Validates if the Competition name is unique.

        Args:
            comp_name (str): Name of the competition.

        Returns:
            bool: True if the name is unique, False if the name already exists.
        """
        all_comps = self.dl_wrapper.read_all_competitions()
        for comp in all_comps:
            if comp.name == comp_name:
                return False
        return True

    def validate_comp_rounds(self, rounds:str) -> bool:
        """Checks if comp rounds is >0.

        Args:
            rounds (str): Rounds of comp.

        Returns:
            bool: Returns True if rounds is higher then 0, Returns False otherwise.
        """
        if rounds.isdigit():
            if int(rounds) > 0:
                return True
        return False

    def validate_combined_game_score(self, home_team_score:str, away_team_score:str) -> bool:
        """Checks if the game score is valid.

        Args:
            home_team_score (str): Home team score.
            away_team_score (str): Away team score.

        Returns:
            bool: Returns True if score outcome is possible, Returns False otherwise.
        """
        if self._check_sum(home_team_score, away_team_score) and self._check_if_winner(home_team_score, away_team_score):
            return True
        return False
    
    def _check_sum(self, home_team:str, away_team:str) -> bool:
        """Checks if the sum of score is less than 3, returns True if it is less than 3"""
        if sum([int(home_team), int(away_team)]) > 3:
            return False
        return True
    
    def _check_if_winner(self, home_team:str, away_team:str) -> bool:
        """Checks if either home or away team is winner"""
        if home_team == "2" or away_team == "2":
            return True
        return False

    def validate_start_date(self, start_date:str) -> bool:
        """Validates if the starting date has passed or not and if the date is in calender.

        Args:
            start_date (str): Start date. DAY-MONTH-YEAR or DD-MM-YYYY.

        Returns:
            bool: _Returns True if the date is today or in the future, Returns False if the date has passed.
        """
        if self._check_if_date_is_real(start_date):
            clean_date = self._fix_date(start_date)
            starting_date = date.fromisoformat(clean_date)
            today = date.today()
            if starting_date >= today:
                return True
        return False
        
    def validate_dates(self, start_date:str,end_date:str) -> bool:
        """Validates if the start date is prior or the same as the end date. Also checks if the dates are in calender.

        Args:
            start_date (str): Start date. DAY-MONTH-YEAR or DD-MM-YYYY.
            end_date (str): End date. DAY-MONTH-YEAR or DD-MM-YYYY.

        Returns:
            bool: Returns True if the start date is prior or the same as the end date, returns False otherwise.
        """
        if self._check_if_date_is_real(start_date) and self._check_if_date_is_real(end_date):
            start_date = date.fromisoformat(self._fix_date(start_date))
            end_date = date.fromisoformat(self._fix_date(end_date))
            if end_date >= start_date:
                return True
        return False
    
    def validate_match_delay_date(self, start_date:str, end_date:str, new_date:str) -> bool:
        """Validates if delay date is within start and end dates.

        Args:
            start_date (str): Start date. DAY-MONTH-YEAR or DD-MM-YYYY.
            end_date (str): End date. DAY-MONTH-YEAR or DD-MM-YYYY.
            new_date (str): New/delay date. DAY-MONTH-YEAR or DD-MM-YYYY.

        Returns:
            bool: Returns True if the new/delay date is within start and end date, returns False otherwise.
        """
        if self._check_if_date_is_real(new_date):
            start_date = date.fromisoformat(self._fix_date(start_date))
            end_date = date.fromisoformat(self._fix_date(end_date))
            new_date = date.fromisoformat(self._fix_date(new_date))
            if start_date < new_date < end_date:
                return True
        return False
    
    def _check_if_date_is_real(self, my_date:str) -> bool:
        """Checks if the date is in calender.

        Args:
            my_date (str): Date. DAY-MONTH-YEAR or DD-MM-YYYY.

        Returns:
            bool: Returns True if the date is in calender.
        """
        my_date = self._fix_date(my_date)
        try:
            my_date = date.fromisoformat(my_date)
            return True
        except ValueError:
            return False

    def _fix_date(self, date:str) -> str:
        """Takes in a date and reformats it to a ISO format.

        Args:
            date (str): Date. DAY-MONTH-YEAR or DD-MM-YYYY.

        Returns:
            str: Returns date in ISO format. YYYY-MM-DD.
        """
        # Takes in a string with day-month-year.
        date_list = date.split("-")
        day = date_list[0]
        month = date_list[1]
        year = date_list[2]
        if len(day) == 1:
            day = "0" + day
        if len(month) == 1:
            month = "0" + month
        return f"{year}-{month}-{day}"
    
    def validate_year(self, year:str) -> bool:
        '''Validates the format for a year and checks if it can be casted to an int.
        
        Args:
            year (str): YYYY

        Returns:
            bool: Returns True if the given format is valid'''
        try:
            int_year = int(year)
            if len(year) == 4:
                return True
            else:
                return False
        except ValueError:
            return False

    def validate_month(self, month:str) -> bool:
        '''Validates the format for a month and checks if it can be casted to an int.
        
        Args:
            month (str): M or MM

        Returns:
            bool: Returns True if the given format is valid'''
        try:
            int_month = int(month)
            if int_month > 0 and int_month <= 12:
                return True
            else:
                return False
        except ValueError:
            return False

    def validate_day(self, day:str) -> bool:
        '''Validates the format for a day and checks if it can be casted to an int.
        
        Args:
            day (str): D or DD

        Returns:
            bool: Returns True if the given format is valid'''
        try:
            int_day = int(day)
            if int_day > 0 and int_day <= 31:
                return True
            else:
                return False
        except ValueError:
            return False