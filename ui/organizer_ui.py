from ui.display_UI import DisplayUI,bcolors
from ui.user_ui import UserUI
from bl.bl_wrapper import BusinessLogicWrapper
from ui.constants import GlobalConst,OrganizerConst,UserUIConst

class OrganizerUI(UserUI):
    """ Class for organizer funtions """
    
    def __init__(self):
        self.user_ui = UserUI()
        self.ui_logic = DisplayUI()
        self.bl_wrapper = BusinessLogicWrapper()
        self.UI_MAX_LEN = GlobalConst.UI_MAX_LEN

# display

    def display_updated_competition_information(self, input_options:str="", competition_name="", organizer_name="", phone_number="",
                                        start_date="", end_date="", rounds=""):
        """ Prints information board for when filling out a new competition.

        Args:
            input_options (str, optional): Empty user input options. Defaults to "".
            competition_name (str, optional): The name of the competition. Defaults to "".
            organizer_name (str, optional):  The name of the organizer. Defaults to "".
            phone_number (str, optional): Organizer phone number. Defaults to "".
            start_date (str, optional): Start date. Defaults to "".
            end_date (str, optional): End date. Defaults to "".
            rounds (str, optional): Rounds played. Defaults to "".
        Returns: 
            None    
        """
        
        menu_options = [OrganizerConst.MENU_COMP_NAME.format(competition_name),
                        OrganizerConst.MENU_ORG_NAME.format(organizer_name),
                        OrganizerConst.MENU_PHONE.format(phone_number),
                        OrganizerConst.MENU_START_DATE.format(start_date),
                        OrganizerConst.MENU_END_DATE.format(end_date),
                        OrganizerConst.MENU_ROUNDS.format(rounds),
                        ]
        
        self.ui_logic.print_ui(menu_options,
                               input_options, 
                               OrganizerConst.HEADER_ADD_COMP,
                               GlobalConst.COLON)

    def display_create_start_date_menu(self, competition_name:str = "", year:str = "", month:str = "", day:str = "") -> None:
        """ Prints the information board when filling out start date

        Args:
            competition_name (str, optional): Name of the competition. Defaults to "".
            year (str, optional): Year of the competition. Defaults to "".
            month (str, optional): Month of the competition. Defaults to "".
            day (str, optional): Day of the competition. Defaults to "".

        Returns:
            None
        """

        menu_options = [OrganizerConst.MENU_YEAR.format(year),
                        OrganizerConst.MENU_MONTH.format(month),
                        OrganizerConst.MENU_DAY.format(day)]
        
        self.ui_logic.print_ui(menu_options,
                               GlobalConst.MENU_OPTIONS_BM,
                               OrganizerConst.HEADER_SET_START_DATE.format(competition_name),
                               GlobalConst.COLON)

    def display_create_end_date_menu(self, competition_name:str = "", year:str = "", month:str = "", day:str = "") -> None:
        """ Prints the information board when filling out end date

        Args:
            competition_name (str, optional): Name of the competition. Defaults to "".
            year (str, optional): Year of the competition. Defaults to "".
            month (str, optional): Month of the competition. Defaults to "".
            day (str, optional): Day of the competition. Defaults to "".
            
        Returns:
            None
        """

        menu_options = [OrganizerConst.MENU_YEAR.format(year),
                        OrganizerConst.MENU_MONTH.format(month),
                        OrganizerConst.MENU_DAY.format(day)]
        
        self.ui_logic.print_ui(menu_options,
                               GlobalConst.MENU_OPTIONS_BM,
                               OrganizerConst.HEADER_SET_END_DATE.format(competition_name),
                               GlobalConst.COLON)

    def display_change_date_menu(self, selected_competition, match, year:str = "", month:str = "", day:str = "") -> None:
        """ Display information board for when changing the date

        Args:
            selected_competition (_type_): The competition for changing dates
            match (_type_): a match in the competition
            year (str, optional): Year of the competition. Defaults to "".
            month (str, optional): Month of the competition. Defaults to "".
            day (str, optional): Day of the competition. Defaults to "".
        
        Returns:
            None
        """

        menu_options = [OrganizerConst.SELECTED_DATE_START_END.format(selected_competition.start_date, 
                                                                       selected_competition.end_date),
                         OrganizerConst.CURRENT_DATE.format(match.date),
                         OrganizerConst.MENU_YEAR.format(year), 
                         OrganizerConst.MENU_MONTH.format(month),
                         OrganizerConst.MENU_DAY.format(day)]
        
        self.ui_logic.print_ui(menu_options,
                               GlobalConst.MENU_OPTIONS_BM,
                               OrganizerConst.HEADER_CHANGE_DATE.format(match.home_team, match.away_team),
                               GlobalConst.COLON)

    def display_updated_team_information(self, team_name:str="", team_club:str="", team_players:list=["","","",""], input_options:str = GlobalConst.MENU_OPTIONS_BM) -> None:
        """ Prints information board after creating a team

        Args:
            team_name (str, optional): Name of the team. Defaults to "".
            team_club (str, optional): Name of the teams club. Defaults to "".
            team_players (list, optional): Name of the teams players. Defaults to ["","","",""].
            input_options (str, optional): Prints the input options. Defaults to GlobalConst.MENU_OPTIONS_BM.

        Returns:
            None
        """
        header = OrganizerConst.HEADER_ADD_NEW_TEAM

        menu_options = [OrganizerConst.MENU_TEAM_NAME.format(team_name),
                        OrganizerConst.MENU_TEAM_CLUB.format(team_club),
                        OrganizerConst.MENU_TEAM_CAPTAIN.format(team_players[0]),
                        OrganizerConst.MEANU_TEAM_PLAYER2.format(team_players[1]),
                        OrganizerConst.MEANU_TEAM_PLAYER3.format(team_players[2]),
                        OrganizerConst.MEANU_TEAM_PLAYER4.format(team_players[3])]

        self.ui_logic.print_ui(menu_options, input_options, header,
                               GlobalConst.COLON)

    def display_all_clubs(self, menu_options:list = [], team_name:str = "") -> None:
        """ Prints a list of all the clubs for when adding a team to a club

        Args:
            menu_options (list, optional): Prints the input options. Defaults to [].
            team_name (str, optional): Name of the team to be added Defaults to "".

        Returns:
            None
        """
        header = OrganizerConst.HEADER_SELECT_CLUB.format(team_name)

        input_options = GlobalConst.MENU_OPTIONS_BMNP

        self.ui_logic.print_ui(menu_options, input_options, header)
        
    def display_updated_player_information(self, role:str = "", player_name="", player_ssn="", player_email="",
                               player_address="", player_gsm="", player_home_phone="", input_options:str = GlobalConst.MENU_OPTIONS_BM):
        """ Prints the information board for when adding players to a team

        Args:
            role (str, optional): Team Captain or Team Player. Defaults to "".
            player_name (str, optional):Name of the player. Defaults to "".
            player_ssn (str, optional): Player SSN. Defaults to "".
            player_email (str, optional): Player emain. Defaults to "".
            player_address (str, optional): Player home address. Defaults to "".
            player_gsm (str, optional): Player gsm number. Defaults to "".
            player_home_phone (str, optional): Player home phone number Defaults to "".
            input_options (str, optional): Prints the input options. Defaults to GlobalConst.MENU_OPTIONS_BM.

        Returns:
            None
        """
        
        menu_options = [OrganizerConst.MENU_PLAYER_NAME.format(player_name),
                        OrganizerConst.MENU_PLAYER_SSN.format(player_ssn),
                        OrganizerConst.MENU_PLAYER_EMAIL.format(player_email),
                        OrganizerConst.MENU_PLAYER_HOME.format(player_address),
                        OrganizerConst.MENU_PLAYER_MOBILE.format(player_gsm),
                        OrganizerConst.MENU_PLAYER_PHONE.format(player_home_phone)]
        
        header = OrganizerConst.HEADER_ADD_ROLE.format(role)

        self.ui_logic.print_ui(menu_options, input_options, header,
                               GlobalConst.COLON)

    def display_updated_club_information(self, club_name="", club_address="", club_phone="", input_options:str = GlobalConst.MENU_OPTIONS_BM):
        """ Prints the information board for when addind a new club

        Args:
            club_name (str, optional): Name of the club. Defaults to "".
            club_address (str, optional): Address of the club. Defaults to "".
            club_phone (str, optional): Phone number for the club. Defaults to "".
            input_options (str, optional): Prints the input options. Defaults to GlobalConst.MENU_OPTIONS_BM.

        Returns:
            None
        """

        
        header = OrganizerConst.HEADER_ADD_NEW_CLUB
        
        menu_options = [OrganizerConst.MENU_CLUB_NAME.format(club_name),
                        OrganizerConst.MENU_HOME_ADDRESS.format(club_address),
                        OrganizerConst.MENU_PHONE.format(club_phone),]

        self.ui_logic.print_ui(menu_options, input_options, header,
                               GlobalConst.COLON)
        
# Virkni -------------------------------------------------------------------------------------------------

    def show_organizer_menu(self):
        """ Show organizer options, get existing competition or create new competition

        Returns: 
                self.show_competition_list(GlobalConst.ORGANIZER) or
                self.show_add_competition() or
                None.
        """
        
        # Display the menu
        self.ui_logic.print_ui(OrganizerConst.MENU_OPTIONS_SCL_CNP,
                               GlobalConst.MENU_OPTIONS_BMNP,
                               OrganizerConst.HEADER_ORGANIZER)        
        error = False
        
        while True:
            error = self.ui_logic.print_error_line(error)
            user_selection = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()

            if user_selection == GlobalConst.USER_SELECT_1: # Organizer menu -> List of competitions
                return self.show_competition_list(GlobalConst.ORGANIZER)
            elif user_selection == GlobalConst.USER_SELECT_2: # Organizer menu -> Create new competition
                return self.show_add_competition()
            elif user_selection == GlobalConst.USER_SELECT_B: # Main Menu <- Organizer menu
                break
            elif user_selection == GlobalConst.USER_SELECT_M: # Main Menu <- Organizer menu
                return
            else:
                self.ui_logic.print_ui(OrganizerConst.MENU_OPTIONS_SCL_CNP,
                               GlobalConst.MENU_OPTIONS_BMNP,
                               OrganizerConst.HEADER_ORGANIZER)  
                print(bcolors.FAIL + 
                      GlobalConst.INVALID_INPUT + 
                      bcolors.ENDC)
                error = True
                
    def show_competition_list(self, user: str):
        """ Show list of existing competitions

        Args:
            user (str): What user is signed in : Organizer
        """

        # Displays list of competitions in system

        competition_list = self.bl_wrapper.get_competition_list()
        current_opt = 1
        option_list = list()
        for competition in competition_list:
            option_list.append(OrganizerConst.MENU_SEL_COMP.format(current_opt,
                                                                   competition.name))
            current_opt += 1
        lower_boundary = 0
        upper_boundary = 10
        self.ui_logic.print_ui(self.get_list_boundary(option_list), 
                               GlobalConst.MENU_OPTIONS_BMNP, 
                               GlobalConst.HEADER_LIST_ALL_COMP)
        error = False
        # User Selection
        while True:
            error = self.ui_logic.print_error_line(error)
            user_input = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()

            for count, opt in enumerate(range(len(competition_list)), 1):  
                if user_input.isdigit():
                    if int(user_input) == count: # If user selects one of the listed competitions
                        selected_competition = self.bl_wrapper.get_competition_info(competition_list[opt].name)
                        if len(selected_competition.matches) != 0:
                            return self.show_competition_menu_organizer_overview(selected_competition.name) # List of competitions -> Competition menu overview (before generating match schedule)
                        else:
                            return self.show_competition_menu_organizer(selected_competition.name) # List of competitions -> Competition menu (after generating match schedule)
            if user_input == GlobalConst.USER_SELECT_M:  # Main Menu <- List of competitions
                return
            elif user_input == GlobalConst.USER_SELECT_B:  # Organizer menu <- List of competitions
                return self.show_organizer_menu()
            elif user_input == GlobalConst.USER_SELECT_N or user_input == GlobalConst.USER_SELECT_P: # Turns pages back and forth if there are more than one
                lower_boundary, upper_boundary, error = self._page_turn_display(user_input, 
                                                                        lower_boundary, 
                                                                        upper_boundary, 
                                                                        option_list, 
                                                                        GlobalConst.MENU_OPTIONS_BMNP, 
                                                                        GlobalConst.HEADER_LIST_ALL_COMP)
            else:
                error = True      
                self.ui_logic.print_ui(self.get_list_boundary(option_list,
                                                              lower_boundary,
                                                              upper_boundary),
                                       GlobalConst.MENU_OPTIONS_BMNP, 
                                       GlobalConst.HEADER_LIST_ALL_COMP)
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)   

    def organizer_view_switch(self, competition_name):
        """Switches menu if generate matches has been done."""
        selected_competition = self.bl_wrapper.get_competition_info(competition_name)
        if len(selected_competition.matches) != 0:
            # -> Competition menu overview (before generating match schedule)
            return self.show_competition_menu_organizer_overview(selected_competition.name)
        else:
            # -> Competition menu (after generating match schedule)
            return self.show_competition_menu_organizer(selected_competition.name)

    def show_competition_menu_organizer(self, competition_name):
        """ Show organizer competition menu options after generating match schedule

        Args:
            competition_name (str): Name of the competition.
        """

        selected_competition = self.bl_wrapper.get_competition_info(competition_name)
        # User selection
        error = False
        self.ui_logic.print_ui(OrganizerConst.MENU_OPTIONS_SHOW_COMP,
                                GlobalConst.MENU_OPTIONS_BMNP,
                                OrganizerConst.HEADER_COMPETITION.format(selected_competition.name))

        while True:
            # Print organizer options
            error = self.ui_logic.print_error_line(error)
            user_selection = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()

            if user_selection == GlobalConst.USER_SELECT_M: # Main Menu <- Competition menu
                return
            elif user_selection == GlobalConst.USER_SELECT_B: # List of competitions <- Competition menu
                return self.show_competition_list(OrganizerConst.HEADER_ORGANIZER)
            elif user_selection == GlobalConst.USER_SELECT_1: # Competition menu -> Add teams
                return self.show_add_team(selected_competition.name) 
            elif user_selection == GlobalConst.USER_SELECT_2: # Competition menu -> Competition menu / Competition menu overview
                user_confirm = input(bcolors.FAIL + OrganizerConst.PROMPT_CONFIRM + bcolors.ENDC).lower()
                if user_confirm == GlobalConst.USER_SELECT_Y: # Competition menu -> Competition menu
                    self.bl_wrapper.generate_match_schedule(competition_name)
                    return self.show_competition_menu_organizer_overview(competition_name)
                else:                                           # Competition menu -> Competition menu overview
                    return self.show_competition_menu_organizer(competition_name)
            elif user_selection == GlobalConst.USER_SELECT_3: # Competition menu -> Edit match results
                return self.show_edit_result_match_list(selected_competition.name)
            elif user_selection == GlobalConst.USER_SELECT_4: # Competition menu -> Delay match
                return self.show_delay_match_list(selected_competition.name)
            elif user_selection == GlobalConst.USER_SELECT_5: # Competition menu -> List of all teams
                user_input = self.show_teams(selected_competition.name, OrganizerConst.HEADER_ORGANIZER)
                if user_input == GlobalConst.USER_SELECT_M: # Main Menu <- List of all teams
                    return
                self.ui_logic.print_ui(OrganizerConst.MENU_OPTIONS_SHOW_COMP,
                                       GlobalConst.MENU_OPTIONS_BMNP,
                                       OrganizerConst.HEADER_COMPETITION.format(selected_competition.name))
            elif user_selection == GlobalConst.USER_SELECT_6: # Competition menu -> List of unfinished matches
                user_input = self.show_unfinished_matches(selected_competition.name, OrganizerConst.HEADER_ORGANIZER)
                if user_input == GlobalConst.USER_SELECT_M: # Main Menu <- List of unifinished matches
                    return
                self.ui_logic.print_ui(OrganizerConst.MENU_OPTIONS_SHOW_COMP,
                                       GlobalConst.MENU_OPTIONS_BMNP,
                                       OrganizerConst.HEADER_COMPETITION.format(selected_competition.name))
            elif user_selection == GlobalConst.USER_SELECT_7: # Competition menu -> List of finished matches
                user_input = self.show_finished_matches(selected_competition.name, OrganizerConst.HEADER_ORGANIZER)
                if user_input == GlobalConst.USER_SELECT_M: # Main menu <- List of finished matches 
                    return
                self.ui_logic.print_ui(OrganizerConst.MENU_OPTIONS_SHOW_COMP,
                                       GlobalConst.MENU_OPTIONS_BMNP,
                                       OrganizerConst.HEADER_COMPETITION.format(selected_competition.name))
            elif user_selection == GlobalConst.USER_SELECT_8: # Competition menu -> Competition score overview
                user_input = self.show_competition_standing(selected_competition.name, OrganizerConst.HEADER_ORGANIZER)
                if user_input == GlobalConst.USER_SELECT_M: # Main Menu <- Competition score overview
                    return
                self.ui_logic.print_ui(OrganizerConst.MENU_OPTIONS_SHOW_COMP,
                                       GlobalConst.MENU_OPTIONS_BMNP,
                                       OrganizerConst.HEADER_COMPETITION.format(selected_competition.name))
            else:
                error = True
                self.ui_logic.print_ui(OrganizerConst.MENU_OPTIONS_SHOW_COMP, 
                                       GlobalConst.MENU_OPTIONS_BMNP, 
                                       OrganizerConst.HEADER_COMPETITION.format(selected_competition.name))
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)

    def show_competition_menu_organizer_overview(self, competition_name):
        """ Show organizer competition menu options before generating match schedule

        Args:
            competition_name (str): Name of the competition.
        """

        selected_competition = self.bl_wrapper.get_competition_info(competition_name)
        # User selection
        error = False
        self.ui_logic.print_ui(OrganizerConst.MENU_OPTIONS_SHOW_COMP_2,
                               GlobalConst.MENU_OPTIONS_BMNP,
                               OrganizerConst.HEADER_COMPETITION.format(selected_competition.name))
        while True:
            # Print organizer options
            error = self.ui_logic.print_error_line(error)

            user_selection = input(bcolors.OKGREEN + GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()

            if user_selection == GlobalConst.USER_SELECT_M: # Main Menu <- Competition menu overview
                return
            elif user_selection == GlobalConst.USER_SELECT_B: # List of competitions <- Competition menu overview
                return self.show_competition_list(OrganizerConst.HEADER_ORGANIZER)
            elif user_selection == GlobalConst.USER_SELECT_1: # Competition menu overview -> Edit match results
                return self.show_edit_result_match_list(selected_competition.name)
            elif user_selection == GlobalConst.USER_SELECT_2: # Competition menu overview -> Delay match
                return self.show_delay_match_list(selected_competition.name)
            elif user_selection == GlobalConst.USER_SELECT_3: # Competition menu overview -> List of all teams
                user_input = self.show_teams(selected_competition.name, OrganizerConst.HEADER_ORGANIZER)
                if user_input == GlobalConst.USER_SELECT_M: # Main Menu <- List of all teams
                    return
                self.ui_logic.print_ui(OrganizerConst.MENU_OPTIONS_SHOW_COMP_2,
                                       GlobalConst.MENU_OPTIONS_BMNP,
                                       OrganizerConst.HEADER_COMPETITION.format(selected_competition.name))
            elif user_selection == GlobalConst.USER_SELECT_4: # Competition menu overview -> List of unfinished matches
                user_input = self.show_unfinished_matches(selected_competition.name, OrganizerConst.HEADER_ORGANIZER)
                self.ui_logic.print_ui(OrganizerConst.MENU_OPTIONS_SHOW_COMP_2,
                                       GlobalConst.MENU_OPTIONS_BMNP,
                                       OrganizerConst.HEADER_COMPETITION.format(selected_competition.name))
                if user_input == GlobalConst.USER_SELECT_M: # Main Menu <- List of unfinished matches
                    return
            elif user_selection == GlobalConst.USER_SELECT_5: # Competition menu overview -> List of finished matches
                user_input = self.show_finished_matches(selected_competition.name, OrganizerConst.HEADER_ORGANIZER)
                if user_input == GlobalConst.USER_SELECT_M: # Main Menu <- List of finished matches
                    return
                self.ui_logic.print_ui(OrganizerConst.MENU_OPTIONS_SHOW_COMP_2,
                                       GlobalConst.MENU_OPTIONS_BMNP,
                                       OrganizerConst.HEADER_COMPETITION.format(selected_competition.name))
            elif user_selection == GlobalConst.USER_SELECT_6: # Competition menu overview -> Competition score overview
                user_input = self.show_competition_standing(selected_competition.name, OrganizerConst.HEADER_ORGANIZER)
                if user_input == GlobalConst.USER_SELECT_M: # Main Menu <- Competition score overview
                    return
                self.ui_logic.print_ui(OrganizerConst.MENU_OPTIONS_SHOW_COMP_2,
                                       GlobalConst.MENU_OPTIONS_BMNP,
                                       OrganizerConst.HEADER_COMPETITION.format(selected_competition.name))
            else:
                error = True
                self.ui_logic.print_ui(OrganizerConst.MENU_OPTIONS_SHOW_COMP_2,
                                       GlobalConst.MENU_OPTIONS_BMNP,
                                       OrganizerConst.HEADER_COMPETITION.format(selected_competition.name))
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)
    
    def show_edit_result_match_list(self, competition_name):
        """ Get list of played matches to edit scores

        Args:
            competition_name (str): Name of the competition.
        """

        # Display played matches
        played_matches = self.bl_wrapper.get_played_matches(competition_name)

        current_opt = 1
        option_list = list()
        for match in played_matches:
            option_list.append(UserUIConst.MENU_OPTIONS_SEL_HOME_AWAY.format(current_opt,
                                                                             match.home_team,
                                                                             match.away_team))
            current_opt += 1

        lower_boundary = 0
        upper_boundary = 10
        self.ui_logic.print_ui(option_list,
                               GlobalConst.MENU_OPTIONS_BMNP,
                               UserUIConst.HEADER_COMP_FINISHED.format(competition_name))

        # User Selection
        error = False
        
        while True:
            error = self.ui_logic.print_error_line(error)
            user_input = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()

            for count, opt in enumerate(range(len(played_matches)), 1):
                if user_input.isdigit(): 
                    if int(user_input) == count: # If user selects one of the listed options
                        return self.show_edit_result(played_matches[opt], competition_name) # Edit match results list -> Edit match results
            if user_input == GlobalConst.USER_SELECT_M:  # Main Menu <- Edit match results list
                return
            elif user_input == GlobalConst.USER_SELECT_B:  # Competition menu <- Edit match results list
                return self.organizer_view_switch(competition_name)
            elif user_input == GlobalConst.USER_SELECT_N or user_input == GlobalConst.USER_SELECT_P: # Turns pages back and forth if there are more than one
                lower_boundary, upper_boundary, error = self._page_turn_display(user_input, 
                                                                        lower_boundary, 
                                                                        upper_boundary, 
                                                                        option_list, 
                                                                        GlobalConst.MENU_OPTIONS_BMNP, 
                                                                        UserUIConst.HEADER_COMP_FINISHED.format(competition_name))
            else:
                error = True
                self.ui_logic.print_ui(self.get_list_boundary(option_list, 
                                                              lower_boundary, 
                                                              upper_boundary), 
                                           GlobalConst.MENU_OPTIONS_BMNP, 
                                           UserUIConst.HEADER_COMP_FINISHED.format(competition_name))
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)

    def show_edit_result(self, match, competition_name):
        """ Edit scorecard on selected match

        Args:
            match (str): The match to be edited.
            competition_name (str): The name of the competition with the match.
        """
        match_games = match.games_result
        match_dict = match.games

        self.display_score_card(match, match_dict, match_games)
        error = False

        while True:
            error = self.ui_logic.print_error_line(error)
            game_select = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()

            if game_select == GlobalConst.USER_SELECT_M: # Main Menu <- Edit match results
                return
            elif game_select == GlobalConst.USER_SELECT_B: # Edit match results list <- Edit match results
                self.bl_wrapper.edit_match(match.match_id, match_games)
                return self.show_edit_result_match_list(competition_name)
            game_not_found = True

            for opt in range(len(match_games) + 1):
                if game_select.isdigit():
                    if int(game_select) == opt: # If user selects one of the listed options
                        match_games[opt-1] = ["x", "x"]
                        self.display_score_card(match, match_dict, match_games)
                        home_team_score = input(OrganizerConst.PROMPT_HOME_SCORE)
                        # VALIDATE
                        match_games[opt-1][0] = home_team_score
                        self.display_score_card(match, match_dict, match_games)
                        away_team_score = input(OrganizerConst.PROMPT_AWAY_SCORE)
                        # VALIDATE
                        match_games[opt-1][1] = away_team_score
                        self.display_score_card(match, match_dict, match_games)
                        game_not_found = False
            if game_not_found:
                error = True
                self.display_score_card(match, match_dict, match_games)
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)

    def show_delay_match_list(self, competition_name):
        """ Show list of unfinished matches if needed to delay them

        Args:
            competition_name (str): Name of the competition with the match to delay
        """
        
        # Display unplayed matches
        unfinished_matches = self.bl_wrapper.get_unplayed_matches(competition_name)

        current_opt = 1
        option_list = list()
        for match in unfinished_matches:
            option_list.append(UserUIConst.MENU_OPTIONS_SEL_HOME_AWAY_CURRENT_DATE.format(current_opt,
                                                                             match.home_team,
                                                                             match.away_team,
                                                                             match.date))
            current_opt += 1

        lower_boundary = 0
        upper_boundary = 10
        self.ui_logic.print_ui(option_list,
                               GlobalConst.MENU_OPTIONS_BMNP,
                               UserUIConst.HEADER_COMP_UNFINISHED.format(competition_name))

        # User Selection
        error = False
        while True:
            error = self.ui_logic.print_error_line(error)
            user_input = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()

            for count, opt in enumerate(range(len(unfinished_matches)), 1):  # SELECTION IN LIST
                if user_input.isdigit():
                    if int(user_input) == count: # If user selects one of the listed options
                        return self.show_delay_match(unfinished_matches[opt], competition_name) # Delay match list -> Delay match

            if user_input == GlobalConst.USER_SELECT_M:  # Main Menu <- Delay match list
                return
            elif user_input == GlobalConst.USER_SELECT_B:  # Competition menu <- Delay match list
                return self.organizer_view_switch(competition_name)
            elif user_input == GlobalConst.USER_SELECT_N or user_input == GlobalConst.USER_SELECT_P: # Turns pages back and forth if there are more than one
                lower_boundary, upper_boundary, error = self._page_turn_display(user_input, 
                                                                        lower_boundary, 
                                                                        upper_boundary, 
                                                                        option_list, 
                                                                        GlobalConst.MENU_OPTIONS_BMNP, 
                                                                        UserUIConst.HEADER_COMP_UNFINISHED.format(competition_name))
            else:
                error = True
                self.ui_logic.print_ui(self.get_list_boundary(option_list, 
                                                              lower_boundary, 
                                                              upper_boundary), 
                                        GlobalConst.MENU_OPTIONS_BMNP, 
                                        UserUIConst.HEADER_COMP_UNFINISHED.format(competition_name),
                                        GlobalConst.COLON) 
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)           

    def show_delay_match(self, match, competition_name):
        """ Delay match menu, new date is set on match.

        Args:
            match (str): The match to be edited.
            competition_name (str): Name of the competition.
        """
        selected_competition = self.bl_wrapper.get_competition_info(competition_name)

        self.display_change_date_menu(selected_competition, match)
        
        # New date input
        # Validation loop
        error = False
        
        while True:
                # New date year
            while True:
                error = self.ui_logic.print_error_line(error)
                year = input(bcolors.OKGREEN + OrganizerConst.PROMPT_YEAR + bcolors.ENDC).lower()
                if self.bl_wrapper.validate_year(year):
                    self.display_change_date_menu(selected_competition, match, year)
                    break
                elif year.isdigit() == False:
                    if year == GlobalConst.USER_SELECT_M: # Main Menu <- Delay match
                        return
                    elif year == GlobalConst.USER_SELECT_B: # Delay match list <- Delay match
                        return self.show_delay_match_list(competition_name)
                    else:
                        error = True
                        self.display_change_date_menu(selected_competition, match)
                        print(bcolors.FAIL + OrganizerConst.INVALID_YEAR + bcolors.ENDC) 
                else:
                    error = True
                    self.display_change_date_menu(selected_competition, match)
                    print(bcolors.FAIL + OrganizerConst.INVALID_YEAR + bcolors.ENDC)

                # New Date Month
            while True:
                error = self.ui_logic.print_error_line(error)
                month = input(bcolors.OKGREEN + OrganizerConst.PROMPT_MONTH + bcolors.ENDC).lower()
                if self.bl_wrapper.validate_month(month):
                    self.display_change_date_menu(selected_competition, match, year, month)
                    break
                elif month.isdigit() == False:
                    if month == GlobalConst.USER_SELECT_M: # Main Menu <- Delay match
                        return
                    elif month == GlobalConst.USER_SELECT_B: # Delay match list <- Delay match
                        return self.show_delay_match_list(competition_name)
                    else:
                        error = True
                        self.display_change_date_menu(selected_competition, match, year)
                        print(bcolors.FAIL + OrganizerConst.INVALID_MONTH + bcolors.ENDC) 
                else:
                    error = True
                    self.display_change_date_menu(selected_competition, match, year)
                    print(bcolors.FAIL + OrganizerConst.INVALID_MONTH + bcolors.ENDC)

                # New Date Day
            while True:
                error = self.ui_logic.print_error_line(error)
                day = input(bcolors.OKGREEN + OrganizerConst.PROMPT_DAY + bcolors.ENDC).lower()
                if self.bl_wrapper.validate_day(day):
                    self.ui_logic.print_ui([OrganizerConst.SELECTED_DATE_START_END.format(selected_competition.start_date, 
                                                                                          selected_competition.end_date),
                                            OrganizerConst.CURRENT_DATE.format(match.date),
                                            OrganizerConst.MENU_YEAR.format(year), 
                                            OrganizerConst.MENU_MONTH.format(month),
                                            OrganizerConst.MENU_DAY.format(day)
                                            ], 
                    GlobalConst.MENU_OPTIONS_BMNP,
                    OrganizerConst.HEADER_CHANGE_DATE.format(match.home_team, match.away_team),
                    GlobalConst.COLON)
                    break
                elif day.isdigit() == False:
                    if day == GlobalConst.USER_SELECT_M: # Main Menu <- Delay match
                        return
                    elif day == GlobalConst.USER_SELECT_B: # Delay match list <- Delay match
                        return self.show_delay_match_list(competition_name)
                    else:
                        error = True
                        self.display_change_date_menu(selected_competition, match, year, month)
                        print(bcolors.FAIL + OrganizerConst.INVALID_DAY + bcolors.ENDC)
                else:
                    error = True
                    self.display_change_date_menu(selected_competition, match, year, month)
                    print(bcolors.FAIL + OrganizerConst.INVALID_DAY + bcolors.ENDC)

            # verifying that the data inserted is correct
            while True:
                error = self.ui_logic.print_error_line(error)
                user_input = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()
                if user_input == GlobalConst.USER_SELECT_B: # Delay match list <- Delay match
                    return self.show_delay_match_list(competition_name)
                elif user_input == GlobalConst.USER_SELECT_M: # Main Menu <- Delay match
                    return
                elif user_input == GlobalConst.USER_SELECT_N: # Delay match list <- Delay match
                    new_date = f"{day}-{month}-{year}"
                    if self.bl_wrapper.validate_start_date(new_date):
                        # check if new match date is within competition dates
                        if self.bl_wrapper.validate_match_delay_date(selected_competition.start_date,
                                                                     selected_competition.end_date,
                                                                     new_date):
                            self.bl_wrapper.delay_match(match.match_id, new_date)
                            return self.show_delay_match_list(competition_name)
                        else:
                            error = True
                            self.display_change_date_menu(selected_competition, match)
                            print(bcolors.FAIL + OrganizerConst.DATE_OUT_OF_RANGE + bcolors.ENDC)
                            break
                    else:
                        error = True
                        self.display_change_date_menu(selected_competition, match)
                        print(bcolors.FAIL + OrganizerConst.INVALID_DATE + bcolors.ENDC)
                        break
                elif user_input == GlobalConst.USER_SELECT_P: # Delay match list <- Delay match
                    return self.show_delay_match_list(competition_name)
                else:
                    error = True
                    self.ui_logic.print_ui([OrganizerConst.SELECTED_DATE_START_END.format(selected_competition.start_date, 
                                                                                          selected_competition.end_date),
                                            OrganizerConst.CURRENT_DATE.format(match.date),
                                            OrganizerConst.MENU_YEAR.format(year), 
                                            OrganizerConst.MENU_MONTH.format(month),
                                            OrganizerConst.MENU_DAY.format(day)
                                            ], 
                    GlobalConst.MENU_OPTIONS_BMNP,
                    OrganizerConst.HEADER_CHANGE_DATE.format(match.home_team, match.away_team),
                    GlobalConst.COLON)                    
                    print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)
       
    def show_add_competition(self):
        """ Takes in information about a new competition, fills out information board and 
            asks user if it is right and should be saved. 
        """

        new_competition = []

        self.display_updated_competition_information(GlobalConst.MENU_OPTIONS_BM)

        # Competition Name
        error = False
        while True:
            error = self.ui_logic.print_error_line(error)
            competition_name = input(bcolors.OKGREEN+ OrganizerConst.PROMPT_COMP_NAME + bcolors.ENDC)

            if competition_name.lower() == GlobalConst.USER_SELECT_M: # Main Menu <- Create new competition
                return
            elif competition_name.lower() == GlobalConst.USER_SELECT_B: # Organizer menu <- Create new competition
                return self.show_organizer_menu()
            elif ":" in competition_name:
                self.display_updated_competition_information(GlobalConst.MENU_OPTIONS_BM)
                print(bcolors.FAIL + OrganizerConst.INVALID_COMP_NAME + bcolors.ENDC)
            elif self.bl_wrapper.validate_if_comp_name_is_unique(competition_name): # Create new competition -> Create new competition (update)
                self.display_updated_competition_information(GlobalConst.MENU_OPTIONS_BM, competition_name)
                new_competition.append(competition_name)
                break
            else:
                error = True
                self.display_updated_competition_information(GlobalConst.MENU_OPTIONS_BM)
                print(bcolors.FAIL + OrganizerConst.INVALID_COMP_NAME_ALREADY_EXISTS + bcolors.ENDC)
                

        # Competition Organizer
        
        while True:
            error = self.ui_logic.print_error_line(error)
            organizer_name = input(bcolors.OKGREEN + OrganizerConst.PROMPT_ORG_NAME + bcolors.ENDC)
            if organizer_name == GlobalConst.USER_SELECT_M: # Main Menu <- Create new competition
                return
            elif organizer_name == GlobalConst.USER_SELECT_B: # Organizer menu <- Create new competition
                return self.show_organizer_menu()
            elif ":" in competition_name:
                error = True
                self.display_updated_competition_information(GlobalConst.MENU_OPTIONS_BM,competition_name)
                print(bcolors.FAIL + OrganizerConst.INVALID_NAME + bcolors.ENDC)
            elif self.bl_wrapper.validate_names(organizer_name): # Create new competition -> Create new competition (update)
                self.display_updated_competition_information(GlobalConst.MENU_OPTIONS_BM, competition_name, organizer_name)
                new_competition.append(organizer_name)
                break

            else:
                error = True
                self.display_updated_competition_information(GlobalConst.MENU_OPTIONS_BM,competition_name)
                print(bcolors.FAIL + OrganizerConst.INVALID_NAME + bcolors.ENDC)
                

        # Competition Phone
        while True:
            error = self.ui_logic.print_error_line(error)
            phone = input(bcolors.OKGREEN+ OrganizerConst.PROMPT_COMP_PHONE + bcolors.ENDC).lower()
            if phone == GlobalConst.USER_SELECT_M: # Main Menu <- Create new competition
                return
            elif phone == GlobalConst.USER_SELECT_B: # Organizer menu <- Create new competition
                return self.show_organizer_menu()
            elif ":" in competition_name:
                self.display_updated_competition_information(GlobalConst.MENU_OPTIONS_BM, competition_name, organizer_name)
                print(bcolors.FAIL + OrganizerConst.INVALID_PHONE_NUMBER + bcolors.ENDC)
            elif self.bl_wrapper.validate_phone(phone): # Create new competition -> Create new competition (update)
                new_competition.append(phone)
                break
            
            else:
                error = True
                self.display_updated_competition_information(GlobalConst.MENU_OPTIONS_BM, competition_name, organizer_name)
                print(bcolors.FAIL + OrganizerConst.INVALID_PHONE_NUMBER + bcolors.ENDC)
                
        self.display_create_start_date_menu(competition_name)

        # Competition Dates Validation loop
        while True:
            # Start Date Validation loop
            while True:    
                # Start Date Year
                while True:
                    error = self.ui_logic.print_error_line(error)
                    year = input(bcolors.OKGREEN+ OrganizerConst.PROMPT_YEAR + bcolors.ENDC).lower()
                    if self.bl_wrapper.validate_year(year):
                        self.display_create_start_date_menu(competition_name, year)
                        break
                    elif year.isdigit() == False:
                        if year == GlobalConst.USER_SELECT_M: # Main Menu <- Create new competition
                            return
                        elif year == GlobalConst.USER_SELECT_B: # Organizer menu <- Create new competition
                            return self.show_organizer_menu()
                        else:
                            error = True
                            self.display_create_start_date_menu(competition_name)
                            print(bcolors.FAIL + OrganizerConst.INVALID_YEAR + bcolors.ENDC) 
                    else:
                        error = True
                        self.display_create_start_date_menu(competition_name)
                        print(bcolors.FAIL + OrganizerConst.INVALID_YEAR + bcolors.ENDC)

                # Start Date Month
                while True:
                    error = self.ui_logic.print_error_line(error)
                    month = input(bcolors.OKGREEN+ OrganizerConst.PROMPT_MONTH + bcolors.ENDC).lower()
                    if self.bl_wrapper.validate_month(month):
                        self.display_create_start_date_menu(competition_name, year, month)
                        break
                    elif month.isdigit() == False:
                        if month == GlobalConst.USER_SELECT_M: # Main Menu <- Create new competition
                            return
                        elif month == GlobalConst.USER_SELECT_B: # Organizer menu <- Create new competition
                            return self.show_organizer_menu()
                        else:
                            error = True
                            self.display_create_start_date_menu(competition_name, year)
                            print(bcolors.FAIL + OrganizerConst.INVALID_MONTH + bcolors.ENDC) 
                    else:
                        error = True
                        self.display_create_start_date_menu(competition_name, year)
                        print(bcolors.FAIL + OrganizerConst.INVALID_MONTH + bcolors.ENDC)

                # Start Date Day
                while True:
                    error = self.ui_logic.print_error_line(error)
                    day = input(bcolors.OKGREEN+ OrganizerConst.PROMPT_DAY + bcolors.ENDC).lower()
                    if self.bl_wrapper.validate_day(day):
                        self.ui_logic.print_ui([OrganizerConst.MENU_YEAR.format(year),
                                                OrganizerConst.MENU_MONTH.format(month),
                                                OrganizerConst.MENU_DAY.format(day)],
                        GlobalConst.MENU_OPTIONS_BMNP,
                        OrganizerConst.HEADER_SET_START_DATE.format(competition_name),
                        GlobalConst.COLON)
                        break
                    elif day.isdigit() == False:
                        if day == GlobalConst.USER_SELECT_M: # Main Menu <- Create new competition
                            return
                        elif day == GlobalConst.USER_SELECT_B: # Organizer menu <- Create new competition
                            return self.show_organizer_menu()
                        else:
                            error = True
                            self.display_create_start_date_menu(competition_name, year, month)
                            print(bcolors.FAIL + OrganizerConst.INVALID_DAY + bcolors.ENDC)
                    else:
                        error = True
                        self.display_create_start_date_menu(competition_name, year, month)
                        print(bcolors.FAIL + OrganizerConst.INVALID_DAY + bcolors.ENDC)   

                # Start Date Information Validation loop
                while True:
                    error = self.ui_logic.print_error_line(error)
                    user_input = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()
                    if user_input == GlobalConst.USER_SELECT_B: # Organizer menu <- Create new competition
                        return self.show_organizer_menu()
                    elif user_input == GlobalConst.USER_SELECT_M: # Main Menu <- Create new competition
                        return
                    elif user_input == GlobalConst.USER_SELECT_N: # NEXT
                        start_date = f"{day}-{month}-{year}"
                        if self.bl_wrapper.validate_start_date(start_date):
                            break
                        else:
                            error = True
                            self.display_create_start_date_menu(competition_name) 
                            print(bcolors.FAIL + OrganizerConst.INVALID_DATE + bcolors.ENDC)
                            break
                    elif user_input == GlobalConst.USER_SELECT_C: # Organizer menu <- Create new competition
                        return self.show_organizer_menu()
                    else:
                        error = True
                        self.ui_logic.print_ui([OrganizerConst.MENU_YEAR.format(year),
                                                OrganizerConst.MENU_MONTH.format(month),
                                                OrganizerConst.MENU_DAY.format(day)], 
                        GlobalConst.MENU_OPTIONS_BMNC,
                        OrganizerConst.HEADER_SET_START_DATE.format(competition_name),
                        GlobalConst.COLON)                        
                        print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)
                if self.bl_wrapper.validate_start_date(start_date):
                    break

            self.display_create_end_date_menu(competition_name)
            # End Date Validation loop
            while True:   
                # End Date Year
                while True:
                    error = self.ui_logic.print_error_line(error)
                    year = input(bcolors.OKGREEN+ OrganizerConst.PROMPT_YEAR + bcolors.ENDC).lower()
                    if self.bl_wrapper.validate_year(year):
                        self.display_create_end_date_menu(competition_name, year)
                        break
                    elif year.isdigit() == False:
                        if year == GlobalConst.USER_SELECT_M: # Main Menu <- Create new competition
                            return
                        elif year == GlobalConst.USER_SELECT_B: # Organizer menu <- Create new competition
                            return self.show_organizer_menu()
                        else:
                            error = True
                            self.display_create_end_date_menu(competition_name)
                            print(bcolors.FAIL + OrganizerConst.INVALID_YEAR + bcolors.ENDC) 
                    else:
                        error = True
                        self.display_create_end_date_menu(competition_name)
                        print(bcolors.FAIL + OrganizerConst.INVALID_YEAR + bcolors.ENDC)

                # End Date Month
                while True:
                    error = self.ui_logic.print_error_line(error)
                    month = input(bcolors.OKGREEN+ OrganizerConst.PROMPT_MONTH + bcolors.ENDC).lower()
                    if self.bl_wrapper.validate_month(month):
                        self.display_create_end_date_menu(competition_name, year, month)
                        break
                    elif month.isdigit() == False:
                        if month == GlobalConst.USER_SELECT_M: # Main Menu <- Create new competition
                            return
                        elif month == GlobalConst.USER_SELECT_B: # Organizer menu <- Create new competition
                            return self.show_organizer_menu()
                        else:
                            error = True
                            self.display_create_end_date_menu(competition_name, year)
                            print(bcolors.FAIL + OrganizerConst.INVALID_MONTH + bcolors.ENDC) 
                    else:
                        error = True
                        self.display_create_end_date_menu(competition_name, year)
                        print(bcolors.FAIL + OrganizerConst.INVALID_MONTH + bcolors.ENDC)

                # End Date Day
                while True:
                    error = self.ui_logic.print_error_line(error)
                    day = input(bcolors.OKGREEN+ OrganizerConst.PROMPT_DAY + bcolors.ENDC).lower()
                    if self.bl_wrapper.validate_day(day):
                        self.ui_logic.print_ui([OrganizerConst.MENU_YEAR.format(year),
                                                OrganizerConst.MENU_MONTH.format(month),
                                                OrganizerConst.MENU_DAY.format(day)], 
                        GlobalConst.MENU_OPTIONS_BMNP,
                        OrganizerConst.HEADER_SET_END_DATE.format(competition_name),
                        GlobalConst.COLON)                        
                        break
                    elif day.isdigit() == False:
                        if day == GlobalConst.USER_SELECT_M: # Main Menu <- Create new competition
                            return
                        elif day == GlobalConst.USER_SELECT_B: # Organizer menu <- Create new competition
                            return self.show_organizer_menu()
                        else:
                            error = True
                            self.display_create_end_date_menu(competition_name, year, month)
                            print(bcolors.FAIL + OrganizerConst.INVALID_DAY + bcolors.ENDC)
                    else:
                        error = True
                        self.display_create_end_date_menu(competition_name, year, month)
                        print(bcolors.FAIL + OrganizerConst.INVALID_DAY + bcolors.ENDC)

                # End Date Information Validation loop
                while True:
                    error = self.ui_logic.print_error_line(error)
                    user_input = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()
                    if user_input == GlobalConst.USER_SELECT_B: # Organizer menu <- Create new competition
                        return self.show_organizer_menu()
                    elif user_input == GlobalConst.USER_SELECT_M: # Main Menu <- Create new competition
                        return
                    elif user_input == GlobalConst.USER_SELECT_N: # NEXT
                        end_date = f"{day}-{month}-{year}"
                        if self.bl_wrapper.validate_start_date(start_date):
                            if self.bl_wrapper.validate_dates(start_date, end_date):
                                break
                            else:
                                error = True
                                self.display_create_end_date_menu(competition_name)
                                print(bcolors.FAIL + OrganizerConst.INVALID_START_DATE + bcolors.ENDC)
                                break
                        else:
                            error = True
                            self.display_create_end_date_menu(competition_name)
                            print(bcolors.FAIL + OrganizerConst.INVALID_DATE + bcolors.ENDC)
                            break
                    elif user_input == GlobalConst.USER_SELECT_C: # Organizer menu <- Create new competition
                        return self.show_organizer_menu()
                    else:
                        error = True
                        self.ui_logic.print_ui([OrganizerConst.MENU_YEAR.format(year),
                                                OrganizerConst.MENU_MONTH.format(month),
                                                OrganizerConst.MENU_DAY.format(day)], 
                        GlobalConst.MENU_OPTIONS_BMNC,
                        OrganizerConst.HEADER_SET_END_DATE.format(competition_name),
                        GlobalConst.COLON)
                        print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)   
                if self.bl_wrapper.validate_start_date(start_date):
                    if self.bl_wrapper.validate_dates(start_date, end_date):
                        break
            break

        self.display_updated_competition_information(GlobalConst.MENU_OPTIONS_BM, competition_name, organizer_name, phone, start_date, end_date)
        new_competition.append(end_date)
        new_competition.append(start_date)

        # Competition Rounds
        while True:
            error = self.ui_logic.print_error_line(error)
            rounds = input(bcolors.OKGREEN+ OrganizerConst.PROMPT_ROUNDS + bcolors.ENDC).lower()

            if self.bl_wrapper.validate_comp_rounds(rounds):
                self.display_updated_competition_information(GlobalConst.MENU_OPTIONS_BMSC, competition_name, organizer_name, phone, start_date,
                                             end_date, rounds)
                new_competition.append(rounds)
                break
            if rounds.isdigit() == False:
                if rounds == GlobalConst.USER_SELECT_M: # Main Menu <- Create new competition
                    return
                elif rounds == GlobalConst.USER_SELECT_B: # Organizer menu <- Create new competition
                    return self.show_organizer_menu()
                else:
                    error = True
                    self.display_updated_competition_information(GlobalConst.MENU_OPTIONS_BM, competition_name, organizer_name, phone, start_date,
                                                     end_date)
                    print(bcolors.FAIL + OrganizerConst.INVALID_ROUNDS + bcolors.ENDC)
            else:
                error = True
                self.display_updated_competition_information(GlobalConst.MENU_OPTIONS_BM, competition_name, organizer_name, phone, start_date,
                                                     end_date)
                print(bcolors.FAIL + OrganizerConst.INVALID_ROUNDS + bcolors.ENDC)

        # Save new competition to file
        while True:
            error = self.ui_logic.print_error_line(error)
            user_input = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()

            if user_input == GlobalConst.USER_SELECT_S: # Competition menu <- Create new competition
                self.bl_wrapper.add_competition(new_competition)
                return self.show_competition_menu_organizer(competition_name)
            elif user_input == GlobalConst.USER_SELECT_B: # Organizer menu <- Create new competition
                return self.show_organizer_menu()
            elif user_input == GlobalConst.USER_SELECT_M: # Main Menu <- Create new competition
                return
            elif user_input == GlobalConst.USER_SELECT_C: # Organizer menu <- Create new competition
                return self.show_organizer_menu()

            else:
                error = True
                self.display_updated_competition_information(GlobalConst.MENU_OPTIONS_BMSC, competition_name, organizer_name, phone, start_date,
                                             end_date, rounds)
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)

    def show_add_team(self, competition_name):
        """ Add new team to competition

        Args:
            competition_name (str): Name of the competition.
        """
        all_teams = self.bl_wrapper.get_all_teams()

        current_opt = 1
        option_list = list()
        for team in all_teams:
            option_list.append(OrganizerConst.MENU_SEL_COMP.format(current_opt, team.name))
            current_opt += 1
        option_list.append(OrganizerConst.SELECTIOM_ADD_NEW_TEAM.format(current_opt))
        lower_boundary = 0
        upper_boundary = 10
        
        error = False
        self.ui_logic.print_ui(self.get_list_boundary(option_list), 
                       GlobalConst.MENU_OPTIONS_BMNP, 
                       OrganizerConst.HEADER_COMP_ADD_TEAM.format(competition_name))

        while True:
            error = self.ui_logic.print_error_line(error)

            user_input = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()
            for count, opt in enumerate(range(len(all_teams)), 1):  
                if user_input.isdigit():
                    if int(user_input) == count: # If user selects one of the listed options
                        self.bl_wrapper.add_team_to_competition(all_teams[opt].name, competition_name)
                        return self.show_competition_menu_organizer(competition_name) # Competition menu <- Add teams
            
            if user_input == GlobalConst.USER_SELECT_M:  # Main Menu <- Add teams
                return
            elif user_input == GlobalConst.USER_SELECT_B:  # Competition menu <- Add teams
                return self.show_competition_menu_organizer(competition_name)
            elif user_input.isdigit():
                if int(user_input) == current_opt: # If user selects one of the listed options
                    user_choice = self.show_add_new_team(competition_name) # Add teams -> Add new team
                    if user_choice == GlobalConst.USER_SELECT_M:
                        return user_choice
                    elif user_choice == GlobalConst.USER_SELECT_B:
                        self.ui_logic.print_ui(self.get_list_boundary(option_list,
                                                                        lower_boundary,
                                                                        upper_boundary),
                                                GlobalConst.MENU_OPTIONS_BMNP, 
                                                OrganizerConst.HEADER_COMP_ADD_TEAM.format(competition_name))  
                    else:
                        continue
                else:
                    error = True
                
                    self.ui_logic.print_ui(self.get_list_boundary(option_list,
                                                                    lower_boundary,
                                                                    upper_boundary),
                                            GlobalConst.MENU_OPTIONS_BMNP, 
                                            OrganizerConst.HEADER_COMP_ADD_TEAM.format(competition_name))  
                    print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)   
            elif user_input == GlobalConst.USER_SELECT_N or user_input == GlobalConst.USER_SELECT_P: # Turns pages back and forth if there are more than one
                lower_boundary, upper_boundary, error = self._page_turn_display(user_input, 
                                                                        lower_boundary, 
                                                                        upper_boundary, 
                                                                        option_list, 
                                                                        GlobalConst.MENU_OPTIONS_BMNP, 
                                                                        OrganizerConst.HEADER_COMP_ADD_TEAM.format(competition_name))
            else:
                error = True
                
                self.ui_logic.print_ui(self.get_list_boundary(option_list,
                                                                lower_boundary,
                                                                upper_boundary),
                                        GlobalConst.MENU_OPTIONS_BMNP, 
                                        OrganizerConst.HEADER_COMP_ADD_TEAM.format(competition_name))  
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)       

    def show_add_new_team(self, competition_name):
        """ Menu to add new team to database.

        Args:
            competition_name (str): Name of the competition.
        """
        new_team = []

        # Display inputted information
        
        self.display_updated_team_information()
        error = False
        # Team name
        while True:
            error = self.ui_logic.print_error_line(error)
            team_name = input(bcolors.OKGREEN + OrganizerConst.PROMPT_TEAM_NAME + bcolors.ENDC)
            if team_name.lower() == GlobalConst.USER_SELECT_B: # Add team <- Add new team
                return self.show_add_team(competition_name)
            elif team_name.lower() == GlobalConst.USER_SELECT_M: # Main Menu <- Add new team
                return
            elif ":" in team_name:
                error = True
                self.display_updated_team_information()
                print(bcolors.FAIL + OrganizerConst.INVALID_TEAM_NAME + bcolors.ENDC)
            elif not self.bl_wrapper.validate_team(team_name):
                new_team.append(team_name)
                break
            else:
                error = True
                self.display_updated_team_information()
                print(bcolors.FAIL + OrganizerConst.INVALID_TEAM_NAME_ALREADY_EXISTS + bcolors.ENDC)

        # Select team club
        all_clubs = self.bl_wrapper.get_all_clubs()

        # Display clubs in file-
        current_opt = 1
        option_list = []
        
        for club in all_clubs:
            option_list.append(OrganizerConst.MENU_SEL_COMP.format(current_opt, club.name))
            current_opt += 1
        option_list.append(OrganizerConst.SELECTIOM_ADD_NEW_CLUB.format(current_opt))
        lower_boundary = 0
        upper_boundary = 10
        
        
        
        self.display_all_clubs(option_list, team_name)
        while True:
            
            # Club selection
            while True:
                is_option = False
                error = self.ui_logic.print_error_line(error)
                user_input = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()
                if user_input == GlobalConst.USER_SELECT_M:  # Main Menu <- Add new team
                    return user_input
                elif user_input == GlobalConst.USER_SELECT_B: # Add team <- Add new team
                    return user_input
                elif user_input.isdigit():
                    for opt in range(len(all_clubs)+1): # If user selects one of the listed options
                        if int(user_input) == opt:
                            team_club = all_clubs[opt-1].name
                            is_option = True
                            break
                    if is_option == False:
                        if int(user_input) == current_opt:  # Add new team -> Add new club
                            team_club = self.show_add_new_club(competition_name) 
                            if team_club == None or team_club == GlobalConst.USER_SELECT_M: # Main Menu <- Add new club
                                return GlobalConst.USER_SELECT_M
                            else:
                                break
                        else:
                            error = True
                            self.ui_logic.print_ui(self.get_list_boundary(option_list, 
                                                                          lower_boundary, 
                                                                          upper_boundary), 
                                                       GlobalConst.MENU_OPTIONS_BMNP, 
                                                       OrganizerConst.HEADER_SELECT_CLUB.format(team_name))
                            print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)
                    else:
                        break
                        
                elif user_input == GlobalConst.USER_SELECT_N or user_input == GlobalConst.USER_SELECT_P: # Turns pages back and forth if there are more than one
                    lower_boundary, upper_boundary, error = self._page_turn_display(user_input, 
                                                    lower_boundary,
                                                    upper_boundary,
                                                    option_list,
                                                    GlobalConst.MENU_OPTIONS_BMNP,
                                                    OrganizerConst.HEADER_SELECT_CLUB.format(team_name))
                else:
                    error = True
                    self.ui_logic.print_ui(self.get_list_boundary(option_list, 
                                                                  lower_boundary, 
                                                                  upper_boundary), 
                                               GlobalConst.MENU_OPTIONS_BMNP, 
                                               OrganizerConst.HEADER_SELECT_CLUB.format(team_name))
                    print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)

            
            captain = self.show_add_player(GlobalConst.TEAM_CAPTAIN, team_name, competition_name) # Add new team -> Add player
            if captain == GlobalConst.USER_SELECT_M: # Main Menu <- Add player
                return captain
            elif captain == GlobalConst.USER_SELECT_B: # Add team <- Add player
                return captain
            team_player1 = self.show_add_player(GlobalConst.PLAYER2, team_name, competition_name, captain) # Add new team -> Add player
            if team_player1 == GlobalConst.USER_SELECT_M: # Main Menu <- Add player
                return team_player1
            elif team_player1 == GlobalConst.USER_SELECT_B: # Add team <- Add player
                return captain
            team_player2 = self.show_add_player(GlobalConst.PLAYER3, team_name, competition_name, captain, team_player1) # Add new team -> Add player
            if team_player2 == GlobalConst.USER_SELECT_M: # Main Menu <- Add player
                return team_player2
            elif team_player2 == GlobalConst.USER_SELECT_B: # Add team <- Add player
                return captain
            team_player3 = self.show_add_player(GlobalConst.PLAYER4, team_name, competition_name, captain, team_player1, team_player2) # Add new team -> Add player
            if team_player3 == GlobalConst.USER_SELECT_M: # Main Menu <- Add player
                return team_player3
            elif team_player3 == GlobalConst.USER_SELECT_B: # Add team <- Add player
                return captain
            team_players = [captain[0], team_player1[0], team_player2[0], team_player3[0]]
            self.display_updated_team_information(team_name, team_club, team_players, GlobalConst.MENU_OPTIONS_BMSC)
            # Save new team
            while True:
                error = self.ui_logic.print_error_line(error)
                player_input = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()
                if player_input == GlobalConst.USER_SELECT_B: # Add team <- Add new team
                    break
                elif player_input == GlobalConst.USER_SELECT_M: # Main Menu <- Add new team
                    return player_input
                elif player_input == GlobalConst.USER_SELECT_S: # Add team <- Add new team
                    # add club to team
                    new_team.append(team_club)

                    # save team
                    self.bl_wrapper.add_team(new_team)
                    self.bl_wrapper.add_player(captain)
                    self.bl_wrapper.assign_captain(captain[1], team_name)
                    self.bl_wrapper.add_player(team_player1)
                    self.bl_wrapper.add_player(team_player2)
                    self.bl_wrapper.add_player(team_player3)
                    return self.show_add_team(competition_name)
                elif player_input == GlobalConst.USER_SELECT_C:
                    return self.show_competition_menu_organizer(competition_name)
                else:
                    error = True
                    self.display_updated_team_information(team_name, team_club, team_players, GlobalConst.MENU_OPTIONS_BMSC)
                    print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)
                
    def show_add_new_club(self, competition_name):
        """ Menu to add a new club to database.

        Args:
            competition_name (str): Name of the competition.
        """
        new_club = []

        # Display inputted information 

        self.display_updated_club_information()
        error = False
        # Club Name
        
        while True:
            error = self.ui_logic.print_error_line(error)
            club_name = input(bcolors.OKGREEN + OrganizerConst.PROMPT_CLUB_NAME + bcolors.ENDC)
            if ":" in club_name:
                error = True
                self.display_updated_club_information()
                print(bcolors.FAIL + OrganizerConst.INVALID_CLUB_NAME + bcolors.ENDC)
            elif club_name.lower() == GlobalConst.USER_SELECT_B: # Add new team <- Add new club
                return self.show_add_new_team(competition_name)
            elif club_name.lower() == GlobalConst.USER_SELECT_M: # Main Menu <- Add new club
                return club_name
            elif not self.bl_wrapper.validate_club(club_name):
                self.display_updated_club_information(club_name)
                new_club.append(club_name)
                break
            else:
                error = True
                self.display_updated_club_information()
                print(bcolors.FAIL + OrganizerConst.INVALID_CLUB_NAME_ALREADY_EXISTS + bcolors.ENDC)

        # Club Address
        
        while True:
            error = self.ui_logic.print_error_line(error)
            club_address = input(bcolors.OKGREEN + OrganizerConst.PROMPT_CLUB_ADDRESS + bcolors.ENDC)
            if club_address.lower() == GlobalConst.USER_SELECT_B: # Add new team <- Add new club
                return self.show_add_new_team(competition_name)
            elif club_address.lower() == GlobalConst.USER_SELECT_M: # Main Menu <- Add new club
                return club_address
            elif ":" in club_address:
                error = True
                self.display_updated_club_information(club_name)
                print(bcolors.FAIL + OrganizerConst.INVALID_ADDRESS + bcolors.ENDC)
            else:
                self.display_updated_club_information(club_name, club_address)
                new_club.append(club_address)
                break

        # Club Phone
        while True:
            error = self.ui_logic.print_error_line(error)
            club_phone = input(bcolors.OKGREEN + OrganizerConst.PROMPT_CLUB_PHONE + bcolors.ENDC).lower()
            if ":" in club_phone:
                error = True
                self.display_updated_club_information(club_name, club_address)
                print(bcolors.FAIL + OrganizerConst.INVALID_PHONE_NUMBER + bcolors.ENDC)
            elif self.bl_wrapper.validate_phone(club_phone):
                self.display_updated_club_information(club_name, club_address, club_phone, GlobalConst.MENU_OPTIONS_BMNC)
                new_club.append(club_phone)
                break
            elif club_phone == GlobalConst.USER_SELECT_B: # Add new team <- Add new club
                return self.show_add_new_team(competition_name)
            elif club_phone == GlobalConst.USER_SELECT_M: # Main Menu <- Add new club
                return
            else:
                error = True
                self.display_updated_club_information(club_name, club_address)
                print(bcolors.FAIL + OrganizerConst.INVALID_PHONE_NUMBER + bcolors.ENDC)

        # Display all information before continuing
        while True:
            error = self.ui_logic.print_error_line(error)
            user_input = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()
            if user_input == GlobalConst.USER_SELECT_B: # Add new team <- Add new club
                return self.show_add_new_team(competition_name)
            elif user_input == GlobalConst.USER_SELECT_M: # Main Menu <- Add new club
                return
            elif user_input == GlobalConst.USER_SELECT_N: # Add new team <- Add new club
                break
            elif user_input == GlobalConst.USER_SELECT_C: # Add new team <- Add new club
                return self.show_add_new_team(competition_name)
            else:
                error = True
                self.display_updated_club_information(club_name, club_address, club_phone, GlobalConst.MENU_OPTIONS_BMNC)
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)
        
        if new_club != None:
            self.bl_wrapper.add_club(new_club)

        return club_name

    def show_add_player(self, role: str, team_name, competition_name, captain:list = ["",""], player1:list = ["",""], player2:list = ["",""]):
        new_player = []

        self.display_updated_player_information(role)
        error = True

        # Player Name
        while True:
            error = self.ui_logic.print_error_line(error)
            player_name = input(bcolors.OKGREEN + OrganizerConst.PROMPT_PLAYER_NAME + bcolors.ENDC)

            if ":" in player_name:
                error = True
                self.display_updated_player_information(role)
                print(bcolors.FAIL + OrganizerConst.INVALID_NAME + bcolors.ENDC)
            elif player_name.lower() == GlobalConst.USER_SELECT_B: # Add new team <- Add player
                return player_name.lower()
            elif player_name.lower() == GlobalConst.USER_SELECT_M: # Main Menu <- Add player
                return player_name.lower()
            elif self.bl_wrapper.validate_names(player_name):
                self.display_updated_player_information(role, player_name)
                new_player.append(player_name)
                break
            else:
                error = True
                self.display_updated_player_information(role)
                print(bcolors.FAIL + OrganizerConst.INVALID_NAME + bcolors.ENDC)

        # Player SSN
        while True:
            error = self.ui_logic.print_error_line(error)
            player_ssn = input(bcolors.OKGREEN + OrganizerConst.PROMPT_PLAYER_SSN + bcolors.ENDC).lower()
            if ":" in player_ssn:
                error = True
                self.display_updated_player_information(role, player_name)
                print(bcolors.FAIL + OrganizerConst.INVALID_SSN + bcolors.ENDC)
            elif player_ssn == GlobalConst.USER_SELECT_B: # Add new team <- Add player
                return self.show_add_new_team(competition_name)
            elif player_ssn == GlobalConst.USER_SELECT_M: # Main Menu <- Add player
                return            
            elif (self.bl_wrapper.clean_numbers(player_ssn) == self.bl_wrapper.clean_numbers(captain[1]) 
            or self.bl_wrapper.clean_numbers(player_ssn) == self.bl_wrapper.clean_numbers(player1[1]) 
            or self.bl_wrapper.clean_numbers(player_ssn) == self.bl_wrapper.clean_numbers(player2[1])):
                if role != GlobalConst.TEAM_CAPTAIN:
                    error = True
                    self.display_updated_player_information(role, player_name)
                    print(bcolors.FAIL + OrganizerConst.INVALID_SSN_ALREADY_EXISTS + bcolors.ENDC)
                else:
                    continue
            elif self.bl_wrapper.validate_ssn(player_ssn) and self.bl_wrapper.validate_if_ssn_is_in_use(player_ssn):
                self.display_updated_player_information(role, player_name, player_ssn)
                new_player.append(player_ssn)
                break
            else:
                error = True
                self.display_updated_player_information(role, player_name)
                print(bcolors.FAIL + OrganizerConst.INVALID_SSN_ALREADY_EXISTS + bcolors.ENDC)

        # Player Email
        while True:
            error = self.ui_logic.print_error_line(error)
            player_email = input(bcolors.OKGREEN + OrganizerConst.PROMPT_PLAYER_EMAIL + bcolors.ENDC).lower()
            if ":" in player_email:
                error = True
                self.display_updated_player_information(role, player_name, player_ssn)
                print(bcolors.FAIL + OrganizerConst.INVALID_EMAIL + bcolors.ENDC)
            elif player_email == GlobalConst.USER_SELECT_B: # Add new team <- Add player
                return self.show_add_new_team(competition_name)
            elif player_email == GlobalConst.USER_SELECT_M: # Main Menu <- Add player
                return
            elif self.bl_wrapper.validate_email(player_email):
                self.display_updated_player_information(role, player_name, player_ssn, player_email)
                new_player.append(player_email)
                break
            else:
                error = True
                self.display_updated_player_information(role, player_name, player_ssn)
                print(bcolors.FAIL + OrganizerConst.INVALID_EMAIL + bcolors.ENDC)

        # Player Address
        while True:
            error = self.ui_logic.print_error_line(error)
            player_address = input(bcolors.OKGREEN + OrganizerConst.PROMPT_PLAYER_ADDRESS + bcolors.ENDC)
            if ":" in player_address:
                error = True
                self.display_updated_player_information(role, player_name, player_ssn, player_email)
                print(bcolors.FAIL + OrganizerConst.INVALID_ADDRESS + bcolors.ENDC)
            elif player_address.lower() == GlobalConst.USER_SELECT_B: # Add new team <- Add player
                return self.show_add_new_team(competition_name)
            elif player_address.lower() == GlobalConst.USER_SELECT_M: # Main Menu <- Add player
                return
            else:
                self.display_updated_player_information(role, player_name, player_ssn, player_email, player_address)
                new_player.append(player_address)
                break

        # Player GSM
        while True:
            error = self.ui_logic.print_error_line(error)
            player_gsm = input(bcolors.OKGREEN + OrganizerConst.PROMPT_PLAYER_GSM + bcolors.ENDC).lower()
            if ":" in player_gsm:
                error = True
                self.display_updated_player_information(role, player_name, player_ssn, player_email, player_address)
                print(bcolors.FAIL + OrganizerConst.INVALID_PHONE_NUMBER + bcolors.ENDC)
            elif player_gsm == GlobalConst.USER_SELECT_B: # Add new team <- Add player
                return self.show_add_new_team(competition_name)
            elif player_gsm == GlobalConst.USER_SELECT_M: # Main Menu <- Add player
                return
            elif self.bl_wrapper.validate_phone(player_gsm):
                self.display_updated_player_information(role, player_name, player_ssn, player_email, player_address, player_gsm)
                new_player.append(player_gsm)
                break
            else:
                error = True
                self.display_updated_player_information(role, player_name, player_ssn, player_email, player_address)
                print(bcolors.FAIL + OrganizerConst.INVALID_PHONE_NUMBER + bcolors.ENDC)
                

        # Player Team
        new_player.append(team_name)

        # Player Role
        new_player.append(role)

        # Player Home Phone
        while True:
            error = self.ui_logic.print_error_line(error)
            player_home_phone = input(bcolors.OKGREEN + OrganizerConst.PROMPT_PLAYER_HOME_PHONE + bcolors.ENDC).lower()
            if ":" in player_home_phone:
                error = True
                self.display_updated_player_information(role, player_name, player_ssn, player_email,
                                                player_address, player_gsm)
                print(bcolors.FAIL + OrganizerConst.INVALID_PHONE_NUMBER + bcolors.ENDC)
            elif player_home_phone == GlobalConst.USER_SELECT_B: # Add new team <- Add player
                return self.show_add_new_team(competition_name)
            elif player_home_phone == GlobalConst.USER_SELECT_M: # Main Menu <- Add player
                return
            elif self.bl_wrapper.validate_phone(player_home_phone):
                self.display_updated_player_information(role, player_name, player_ssn, player_email,
                                        player_address, player_gsm, player_home_phone, GlobalConst.MENU_OPTIONS_BMNC)
                new_player.append(player_home_phone)
                break
            else:
                error = True
                self.display_updated_player_information(role, player_name, player_ssn, player_email,
                                                player_address, player_gsm)
                print(bcolors.FAIL + OrganizerConst.INVALID_PHONE_NUMBER + bcolors.ENDC)
        
        # Display all information before continuing
        while True:
            error = self.ui_logic.print_error_line(error)
            user_input = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()
            if user_input == GlobalConst.USER_SELECT_B: # Add new team <- Add player
                return self.show_add_new_team(competition_name)
            elif user_input == GlobalConst.USER_SELECT_M: # Main Menu <- Add player
                return
            elif user_input == GlobalConst.USER_SELECT_N: # Add new team <- Add player
                break
            elif user_input == GlobalConst.USER_SELECT_C: # Add new team <- Add player
                return self.show_add_new_team(competition_name)
            else:
                error = True
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)
                self.display_updated_player_information(role, player_name, player_ssn, player_email,
                                        player_address, player_gsm, player_home_phone, GlobalConst.MENU_OPTIONS_BMNC)

        return new_player