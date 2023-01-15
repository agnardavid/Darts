from ui.user_ui import UserUI
from ui.display_UI import DisplayUI,bcolors
from bl.bl_wrapper import BusinessLogicWrapper
from ui.constants import GlobalConst, TeamCaptainConst, UserUIConst


class TeamCaptainUI(UserUI):
    """ Class for team captain functions """
    def __init__(self):
        self.user_ui = UserUI()
        self.bl_wrapper = BusinessLogicWrapper()
        self.ui_logic = DisplayUI()
        self.UI_MAX_LEN = GlobalConst.UI_MAX_LEN

    def show_competition_list(self, user: str):
        """ Prints list of competitions in database.

        Args:
            user (str): Display that the user is team captain:
        """
        # Display competition list

        competition_list = self.bl_wrapper.get_competition_list()

        current_opt = 1
        option_list = list()
        for competition in competition_list:
            option_list.append(f"{current_opt}. {competition.name}")
            current_opt += 1
        lower_boundary = 0
        upper_boundary = 12
        self.ui_logic.print_ui(self.get_list_boundary(option_list), 
                               GlobalConst.MENU_OPTIONS_BMNP, 
                               GlobalConst.HEADER_LIST_ALL_COMP)
        error = False
        # User selection
        while True:
            error = self.ui_logic.print_error_line(error)
            user_input = input(bcolors.OKGREEN + GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()
            for count, opt in enumerate(range(len(competition_list)), 1):  # SELECTION IN LIST
                if user_input.isdigit():
                    if int(user_input) == count: # If user selects one of the listed options
                        return self.show_competition_menu_team_captain(competition_list[opt].name)
            if user_input == GlobalConst.USER_SELECT_M:  # Main Menu <- Competition list
                return
            elif user_input == GlobalConst.USER_SELECT_B:  # Main Menu <- Competition list
                break
            elif user_input == GlobalConst.USER_SELECT_N or user_input == GlobalConst.USER_SELECT_P: # Turns pages back and forth if there are more than one
                lower_boundary, upper_boundary, error = self._page_turn_display(user_input, 
                                                                    lower_boundary, 
                                                                    upper_boundary, 
                                                                    option_list, 
                                                                    GlobalConst.MENU_OPTIONS_BMNP, 
                                                                    GlobalConst.HEADER_LIST_ALL_COMP)
            else:
                print(GlobalConst.INVALID_INPUT)
                self.ui_logic.print_ui(self.get_list_boundary(option_list, 
                                                              lower_boundary, 
                                                              upper_boundary), 
                                       GlobalConst.MENU_OPTIONS_BMNP, 
                                       GlobalConst.HEADER_LIST_ALL_COMP)
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)
                error = True    

    def show_competition_menu_team_captain(self, competition_name: str):
        """ Show competition menu options for team captain.

        Args:
            competition_name (str): Name of the competition.
        """

        selected_competition = self.bl_wrapper.get_competition_info(competition_name)
        error = False
        # Print Team Captain Options
        self.ui_logic.print_ui(TeamCaptainConst.MENU_OPTIONS_SHOW_COMP,
                        GlobalConst.MENU_OPTIONS_BMNP,
                        TeamCaptainConst.HEADER_COMPETITION.format(selected_competition.name))
        # User selection
        while True:
            
            # Print Team Captain Options

            error = self.ui_logic.print_error_line(error)

            user_selection = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()

            if user_selection == GlobalConst.USER_SELECT_M: # Main Menu <- Competition menu
                return
            elif user_selection == GlobalConst.USER_SELECT_B: # Competition list
                return self.show_competition_list(GlobalConst.TEAM_CAPTAIN)
            elif user_selection == GlobalConst.USER_SELECT_1: # Competition menu -> Captain matches
                captain_ssn = input(bcolors.OKGREEN + TeamCaptainConst.PROMPT_SSN + bcolors.ENDC).lower()
                if self.bl_wrapper.validate_ssn(captain_ssn):
                    if self.bl_wrapper.validate_ssn_of_team_captain(captain_ssn):
                        return self.show_captain_matches(selected_competition.name, captain_ssn)
                    else:
                        error = True
                        self.ui_logic.print_ui(TeamCaptainConst.MENU_OPTIONS_SHOW_COMP,
                                        GlobalConst.MENU_OPTIONS_BMNP,
                                        TeamCaptainConst.HEADER_COMPETITION.format(selected_competition.name))
                        print(bcolors.FAIL + TeamCaptainConst.INVALID_CAPTAIN_SSN + bcolors.ENDC)
                        continue
                elif captain_ssn == GlobalConst.USER_SELECT_M: # Main Menu <- Competition menu
                    return
                elif captain_ssn == GlobalConst.USER_SELECT_B: # Competition list <- Competition menu
                    continue
                else:
                    error = True
                    self.ui_logic.print_ui(TeamCaptainConst.MENU_OPTIONS_SHOW_COMP,
                                    GlobalConst.MENU_OPTIONS_BMNP,
                                    TeamCaptainConst.HEADER_COMPETITION.format(selected_competition.name))
                    print(bcolors.FAIL + TeamCaptainConst.INVALID_SSN + bcolors.ENDC)
                    continue
            elif user_selection == GlobalConst.USER_SELECT_2: # Competition menu -> List of all teams
                user_input = self.show_teams(selected_competition.name, GlobalConst.TEAM_CAPTAIN)
                if user_input == GlobalConst.USER_SELECT_M: # Main Menu <- List of all teams
                    return
                self.ui_logic.print_ui(TeamCaptainConst.MENU_OPTIONS_SHOW_COMP,
                                       GlobalConst.MENU_OPTIONS_BMNP,
                                       TeamCaptainConst.HEADER_COMPETITION.format(selected_competition.name))

            elif user_selection == GlobalConst.USER_SELECT_3: # Competition menu -> List of unfinished matches
                user_input = self.show_unfinished_matches(selected_competition.name, GlobalConst.TEAM_CAPTAIN)
                if user_input == GlobalConst.USER_SELECT_M: # Main Menu <- List of unfinished matches
                    return
                self.ui_logic.print_ui(TeamCaptainConst.MENU_OPTIONS_SHOW_COMP,
                                       GlobalConst.MENU_OPTIONS_BMNP,
                                       TeamCaptainConst.HEADER_COMPETITION.format(selected_competition.name))

            elif user_selection == GlobalConst.USER_SELECT_4: # Competition menu -> List of finished matches
                user_input = self.show_finished_matches(selected_competition.name, GlobalConst.TEAM_CAPTAIN)
                if user_input == GlobalConst.USER_SELECT_M: # Main Menu -> List of finished matches
                    return
                self.ui_logic.print_ui(TeamCaptainConst.MENU_OPTIONS_SHOW_COMP,
                                       GlobalConst.MENU_OPTIONS_BMNP,
                                       TeamCaptainConst.HEADER_COMPETITION.format(selected_competition.name))
            elif user_selection == GlobalConst.USER_SELECT_5: # Competition menu -> Competition score overview
                user_input = self.show_competition_standing(selected_competition.name, GlobalConst.TEAM_CAPTAIN)
                if user_input == GlobalConst.USER_SELECT_M: # Main Menu <- Competition score overview
                    return
                self.ui_logic.print_ui(TeamCaptainConst.MENU_OPTIONS_SHOW_COMP,
                                       GlobalConst.MENU_OPTIONS_BMNP,
                                       TeamCaptainConst.HEADER_COMPETITION.format(selected_competition.name))
            else:
                error = True
                self.ui_logic.print_ui(TeamCaptainConst.MENU_OPTIONS_SHOW_COMP,
                        GlobalConst.MENU_OPTIONS_BMNP,
                        TeamCaptainConst.HEADER_COMPETITION.format(selected_competition.name))
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)
            

    def show_captain_matches(self, competition_name, captain_ssn):
        """ Show only captain's home team matches that are unfinished

        Args:
            competition_name (str): Name of the competition.
            captain_ssn (str): Social security number of team captain.
        """
        captains_matches = self.bl_wrapper.get_captain_matches(competition_name, captain_ssn)

        # Display match list
        current_opt = 1
        option_list = list()
        for match in captains_matches:
            option_list.append(UserUIConst.MENU_OPTIONS_SEL_HOME_AWAY_CURRENT_DATE.format(current_opt,
                                                                                          match.home_team,
                                                                                          match.away_team,
                                                                                          match.date))
            current_opt += 1

        lower_boundary = 0
        upper_boundary = 12
        self.ui_logic.print_ui(option_list,
                               GlobalConst.MENU_OPTIONS_BMNP,
                               TeamCaptainConst.HEADER_COMP_CAPTAIN_MATCHES.format(competition_name))
        error = False
        # User Selection
        while True:
            error = self.ui_logic.print_error_line(error)
            user_input = input(bcolors.OKGREEN + GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()

            for count, opt in enumerate(range(len(captains_matches)), 1):  # SELECTION IN LIST
                if user_input.isdigit():
                    if int(user_input) == count: # If user selects one of the listed options
                        return self.show_add_results(captains_matches[opt], competition_name, captain_ssn)

            if user_input == GlobalConst.USER_SELECT_M:  # Main Menu <- Captain matches
                return
            elif user_input == GlobalConst.USER_SELECT_B:  # Competition menu <- Captain matches
                return self.show_competition_menu_team_captain(competition_name)
            elif user_input == GlobalConst.USER_SELECT_N or user_input == GlobalConst.USER_SELECT_P:  # Turns pages back and forth if there are more than one
                lower_boundary, upper_boundary, error = self._page_turn_display(user_input, lower_boundary, upper_boundary,
                                                                         option_list, GlobalConst.MENU_OPTIONS_BMNP,
                                                                         TeamCaptainConst.HEADER_COMP_CAPTAIN_MATCHES.format
                                                                         (competition_name))
            else:
                error = True
                self.ui_logic.print_ui(option_list, GlobalConst.MENU_OPTIONS_BMNP,
                                       TeamCaptainConst.HEADER_COMP_CAPTAIN_MATCHES.format
                                       (competition_name))
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC) # INVALID


    def show_add_results(self, match, competition_name, captain_ssn):
        """ Show add result to game menu, team captain enters won legs for each game

        Args:
            match (str): The match to add results to.
            competition_name (str): Name of the competition.
            captain_ssn (str): Social security number of team captain.
        """
        match_dict = match.games
        match_games = [["x","x"], ["x","x"], ["x","x"], ["x","x"], ["x","x"], ["x","x"], ["x","x"]]

        # Add results
        for i in range(7):
            self.display_score_card(match, match_dict, match_games)

            # Home team score input
            error = False
            while True:
                error = self.ui_logic.print_error_line(error)
                home_team_score = input(bcolors.OKGREEN+ TeamCaptainConst.HOME_TEAM_SCORE + bcolors.ENDC)
                if home_team_score == GlobalConst.USER_SELECT_M: # Main Menu <- Add results
                    self.bl_wrapper.reset_match_data(match.id)
                    return home_team_score
                elif home_team_score == GlobalConst.USER_SELECT_B: # Captain matches <- Add results
                    return home_team_score
                elif self.bl_wrapper.validate_game_score(home_team_score):
                    break
                else:
                    error = True
                    self.display_score_card(match, match_dict, match_games)
                    print(bcolors.FAIL + TeamCaptainConst.INVALID_SCORE + bcolors.ENDC)

            match_games[i][0] = home_team_score
            print(home_team_score)
            self.display_score_card(match, match_dict, match_games)

            # Away team score input
            while True:
                error = self.ui_logic.print_error_line(error)
                away_team_score = input(bcolors.OKGREEN+ TeamCaptainConst.AWAY_TEAM_SCORE + bcolors.ENDC)
                if away_team_score == GlobalConst.USER_SELECT_M: # Main Menu <- Add results
                    self.bl_wrapper.reset_match_data(match.id)
                    return away_team_score
                elif away_team_score == GlobalConst.USER_SELECT_B: # Captain matches <- Add results
                    return away_team_score                
                elif self.bl_wrapper.validate_game_score(away_team_score):
                    if self.bl_wrapper.validate_combined_game_score(home_team_score, away_team_score):
                        break

                    else:
                        error = True
                        self.display_score_card(match, match_dict, match_games)
                        print(bcolors.FAIL + TeamCaptainConst.INVALID_SCORE_SUM + bcolors.ENDC)
                else:
                    error = True
                    self.display_score_card(match, match_dict, match_games)
                    print(bcolors.FAIL + TeamCaptainConst.INVALID_SCORE + bcolors.ENDC)

            match_games[i][1] = away_team_score
            print(away_team_score)
            self.bl_wrapper.add_result(match.match_id, home_team_score, away_team_score) # Update in file

        self.display_score_card(match, match_dict, match_games)

        save_scorecard = input(bcolors.OKGREEN + TeamCaptainConst.PRESS_S_SAVE + bcolors.ENDC)
        self.bl_wrapper.edit_match(match.match_id, match_games)
        return self.show_captain_matches(competition_name, captain_ssn)
