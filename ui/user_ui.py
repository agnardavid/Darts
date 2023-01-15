from bl.bl_wrapper import BusinessLogicWrapper
from ui.display_UI import DisplayUI,bcolors
from ui.constants import GlobalConst,UserUIConst, DisplayConst

class UserUI():
    """ Class for the public functions and functions that every login has access to. """
    def __init__(self):
        self.bl_wrapper = BusinessLogicWrapper()
        self.ui_logic = DisplayUI()
        self.UI_MAX_LEN = GlobalConst.UI_MAX_LEN
        
    
    def show_competition_list(self, user: str):
        """ First menu shown for public access displaying a list of registered competitions.

        Args:
            user (str): The type of user displaying the list.
        """
        
        # Get competition list from file
        competition_list = self.bl_wrapper.get_competition_list()
        
        # print menu with competitions
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
        while True:
            error = self.ui_logic.print_error_line(error)
            user_input = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()

            for count, opt in enumerate(range(len(competition_list)), 1):
                if user_input != GlobalConst.USER_SELECT_P:
                    if user_input.isdigit():
                        if int(user_input) == count: # If user selects one of the listed options
                            return self.show_competition_menu(competition_list[opt].name) # List of competitions -> Competition menu
            if user_input == GlobalConst.USER_SELECT_M: # Main Menu <- List of competitions
                return
            elif user_input == GlobalConst.USER_SELECT_B: # Main Menu <- List of competitions
                break
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

        return

    def show_competition_menu(self, competition_name: str):
        """ Shows the menu for the selected competition, with the options to 
            print a list of teams and their players, show finished and unfinished 
            matches and get the score for the competition

        Args:
            competition_name (str): Name of the selected competition.
        """
        
        error = False
        
        selected_competition = self.bl_wrapper.get_competition_info(competition_name)
            
        self.ui_logic.print_ui(UserUIConst.MENU_OPTIONS_LA_LU_LF_OW, 
                                GlobalConst.MENU_OPTIONS_BMNP, 
                                UserUIConst.HEADER_COMP_SELECTED.format(
                                    selected_competition.name[:self.UI_MAX_LEN]))
        while True:
            
            error = self.ui_logic.print_error_line(error)
            user_selection = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()
        
            if user_selection == GlobalConst.USER_SELECT_M: # Main Menu <- Competition menu
                return
            elif user_selection == GlobalConst.USER_SELECT_B: # List of competitions <- Competition menu
                return self.show_competition_list(GlobalConst.PUBLIC)
            elif user_selection == GlobalConst.USER_SELECT_1: # Competition menu -> List of all teams
                return self.show_teams(selected_competition.name)
            elif user_selection == GlobalConst.USER_SELECT_2: # Competition menu -> List of unfinished matches
                return self.show_unfinished_matches(selected_competition.name, GlobalConst.PUBLIC)
            elif user_selection == GlobalConst.USER_SELECT_3: # Competition menu -> List of finished matches
                return self.show_finished_matches(selected_competition.name, GlobalConst.PUBLIC)
            elif user_selection == GlobalConst.USER_SELECT_4: # Competition menu -> Competition score overview
                return self.show_competition_standing(selected_competition.name, GlobalConst.PUBLIC)
            else:
                error = True
                self.ui_logic.print_ui(UserUIConst.MENU_OPTIONS_LA_LU_LF_OW, 
                                GlobalConst.MENU_OPTIONS_BMNP, 
                                UserUIConst.HEADER_COMP_SELECTED.format(
                                    selected_competition.name[:self.UI_MAX_LEN]))
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)

#----------------------------------------------------------------------------- show teams / show players
    def show_teams(self, comp_name: str, user=GlobalConst.PUBLIC):
        """ Prints a list of teams in the selected competition, and gives the option to select
            a team to see its players.

        Args:
            comp_name (str): Name of the competition.
            user (str, optional): The type of user using the function. Defaults to GlobalConst.PUBLIC.
        """
        
        competition_teams = self.bl_wrapper.get_competition_teams(comp_name)

        current_opt = 1
        option_list = list()
        for team in competition_teams:
            option_list.append(DisplayConst.MENU_TEAM_LIST.format(current_opt, team.name, team.club))
            current_opt += 1
        lower_boundary = 0
        upper_boundary = 12
        self.ui_logic.print_ui(self.get_list_boundary(option_list), 
                               GlobalConst.MENU_OPTIONS_BMNP, 
                               UserUIConst.HEADER_COMP_SELECTED.format(comp_name[:self.UI_MAX_LEN]),
                               body_header=DisplayConst.HEADER_TEAM_LIST)
        error = False
        while True:
            error = self.ui_logic.print_error_line(error)
            user_input = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()
            for count, opt in enumerate(range(len(competition_teams)), 1):
                if user_input.isdigit():
                    if int(user_input) == count: # If user selects one of the listed options
                        return self.show_players(competition_teams[opt].name, comp_name, user)
            if user_input == GlobalConst.USER_SELECT_M:  # Main Menu <- List of all teams
                return user_input
            elif user_input == GlobalConst.USER_SELECT_B:  # Competition menu <- List of all teams
                if user == GlobalConst.ORGANIZER or user == GlobalConst.TEAM_CAPTAIN: # Competition menu (team captain or organizer) <- List of all teams
                    return user_input 
                else:  
                    return self.show_competition_menu(comp_name) # Competition menu <- List of all teams
            elif user_input == GlobalConst.USER_SELECT_N or user_input == GlobalConst.USER_SELECT_P: # Turns pages back and forth if there are more than one
                lower_boundary, upper_boundary, error = self._page_turn_display(user_input, lower_boundary,
                                                                                upper_boundary,
                                                                                option_list,
                                                                    GlobalConst.MENU_OPTIONS_BMNP, 
                                                                    UserUIConst.HEADER_COMP_SELECTED.format(comp_name),
                                                                    body_header=DisplayConst.HEADER_TEAM_LIST)
            else:
                error = True
                self.ui_logic.print_ui(self.get_list_boundary(option_list, 
                                                              lower_boundary,
                                                              upper_boundary),
                                       GlobalConst.MENU_OPTIONS_BMNP,
                                       UserUIConst.HEADER_COMP_SELECTED.format(comp_name[:self.UI_MAX_LEN]),
                                       body_header=DisplayConst.HEADER_TEAM_LIST)
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)

    def show_players(self, team_name:str, comp_name:str, user=GlobalConst.PUBLIC):
        """ Prints a list of the players in the selected team.

        Args:
            team_name (str): Name of the team.
            comp_name (str): Name of the competition.
            user (str, optional): The type of user using the function. Defaults to GlobalConst.PUBLIC.
        """
    
        team_players = self.bl_wrapper.get_players(team_name)
        option_list = []
        for player in team_players:
            option_list.append(DisplayConst.MENU_PLAYER_LIST.format(player.name, player.social_id, player.gsm_number))
        # We will allow switching pages if in later updates a team is allowed to have more than 4 players
        lower_boundary = 0
        upper_boundary = 12
        self.ui_logic.print_ui(self.get_list_boundary(option_list), 
                               GlobalConst.MENU_OPTIONS_BMNP,
                               team_name[:self.UI_MAX_LEN],
                               body_header=DisplayConst.HEADER_PLAYER_LIST)
        error = False

        while True:
            error = self.ui_logic.print_error_line(error)
            user_input = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC)
            if user_input == GlobalConst.USER_SELECT_B: # List of all teams <- List of all players
                return self.show_teams(comp_name, user)
            elif user_input == GlobalConst.USER_SELECT_M: # Main Menu <- List of all players
                return GlobalConst.USER_SELECT_M
            elif user_input == GlobalConst.USER_SELECT_N or user_input == GlobalConst.USER_SELECT_P: # Turns pages back and forth if there are more than one
                lower_boundary, upper_boundary, error = self._page_turn_display(user_input, 
                                                                    lower_boundary, 
                                                                    upper_boundary, 
                                                                    option_list, 
                                                                    GlobalConst.MENU_OPTIONS_BMNP, 
                                                                    team_name,
                                                                    body_header=DisplayConst.HEADER_PLAYER_LIST)
            else:
                error = True
                self.ui_logic.print_ui(self.get_list_boundary(option_list, 
                                                              lower_boundary, 
                                                              upper_boundary), 
                                       GlobalConst.MENU_OPTIONS_BMNP,
                                       team_name[:self.UI_MAX_LEN],
                                       body_header=DisplayConst.HEADER_PLAYER_LIST)
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)

#----------------------------------------------------------------------------- show finished og unfinished
    def show_unfinished_matches(self, comp_name, back_user: str, user:str=GlobalConst.PUBLIC):
        """ Prints a list of unfinished matches in the selected competition.

        Args:
            comp_name (str): Name of the competition
            back_user (str): Current user access.
            user (str, optional): The type of user using the function. Defaults to GlobalConst.PUBLIC.
        """
        unfinished_matches = self.bl_wrapper.get_unplayed_matches(comp_name)

        current_opt = 1
        option_list = list()
        for match in unfinished_matches:
            option_list.append(DisplayConst.MENU_UNFINISHED_MATCH_LIST.format(match.date,
                                                                           match.home_team,
                                                                           match.away_team))
            current_opt += 1
        lower_boundary = 0
        upper_boundary = 12
        self.ui_logic.print_ui(option_list,
                               GlobalConst.MENU_OPTIONS_BMNP,
                               UserUIConst.HEADER_COMP_UNFINISHED.format(comp_name[:self.UI_MAX_LEN]),
                               body_header=DisplayConst.HEADER_UNFINISHED_MATCH_LIST)
        error = False
    
        while True:
            error = self.ui_logic.print_error_line(error)
            user_selection = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()
            if user_selection == GlobalConst.USER_SELECT_M: # Main Menu <- List of unfinished matches
                return user_selection
            elif user_selection == GlobalConst.USER_SELECT_B: 
                if back_user == GlobalConst.PUBLIC:  # Competition menu <- List of unfinished matches
                    return self.show_competition_menu(comp_name)
                else:
                    return GlobalConst.USER_SELECT_B # Competition menu <- List of unfinished matches (Team captain and Organizer)
            elif user_selection == GlobalConst.USER_SELECT_N or user_selection == GlobalConst.USER_SELECT_P: # Turns pages back and forth if there are more than one
                lower_boundary, upper_boundary, error = self._page_turn_display(user_selection, 
                                                                    lower_boundary, 
                                                                    upper_boundary, 
                                                                    option_list, 
                                                                    GlobalConst.MENU_OPTIONS_BMNP, 
                                                                    UserUIConst.HEADER_COMP_UNFINISHED.format(comp_name),
                                                                    body_header=DisplayConst.HEADER_UNFINISHED_MATCH_LIST)
            else:
                error = True
                self.ui_logic.print_ui(self.get_list_boundary(option_list, 
                                                              lower_boundary, 
                                                              upper_boundary), 
                                       GlobalConst.MENU_OPTIONS_BMNP,
                                       UserUIConst.HEADER_COMP_UNFINISHED.format(comp_name[:self.UI_MAX_LEN]),
                                       body_header=DisplayConst.HEADER_UNFINISHED_MATCH_LIST)
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)

    def show_finished_matches(self, comp_name, back_user: str, user=GlobalConst.PUBLIC):
        """ Prints a list of finished matches in the selected competition.

        Args:
            comp_name (str): Name of the competition.
            back_user (str): Current user access.
            user (str, optional): The type of user using the function. Defaults to GlobalConst.PUBLIC.
        """
        finished_matches = self.bl_wrapper.get_played_matches(comp_name)

        current_opt = 1
        option_list = list()
        for match in finished_matches:
            option_list.append(DisplayConst.MENU_FINISHED_MATCH_LIST.format(match.home_team,
                                                                         match.score_board[0],
                                                                         match.score_board[1],
                                                                         match.away_team))
            current_opt += 1
        lower_boundary = 0
        upper_boundary = 12
        self.ui_logic.print_ui(option_list,
                               GlobalConst.MENU_OPTIONS_BMNP,
                               UserUIConst.HEADER_COMP_FINISHED.format(comp_name[:self.UI_MAX_LEN]),
                               body_header=DisplayConst.HEADER_FINISHED_MATCH_LIST_HEADER)

        error = False
        while True:
            error = self.ui_logic.print_error_line(error)
            user_selection = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()
            if user_selection == GlobalConst.USER_SELECT_M: # Main Menu <- List of finished matches
                return user_selection
            elif user_selection == GlobalConst.USER_SELECT_B:
                if back_user == GlobalConst.PUBLIC: # Competition menu <- List of finished matches
                    return self.show_competition_menu(comp_name)
                else:
                    return user_selection # Competition menu <- List of finished matches (team captain or Organizer)
            elif user_selection == GlobalConst.USER_SELECT_N or user_selection == GlobalConst.USER_SELECT_P: # Turns pages back and forth if there are more than one
                lower_boundary, upper_boundary, error = self._page_turn_display(user_selection, 
                                                                                lower_boundary,
                                                                                upper_boundary,
                                                                                option_list,
                                                                    GlobalConst.MENU_OPTIONS_BMNP, 
                                                                    UserUIConst.HEADER_COMP_FINISHED.format(comp_name),
                                                                    body_header=DisplayConst.HEADER_FINISHED_MATCH_LIST_HEADER)
            else:
                error = True
                self.ui_logic.print_ui(self.get_list_boundary(option_list, 
                                                              lower_boundary, 
                                                              upper_boundary), 
                                       GlobalConst.MENU_OPTIONS_BMNP,
                                       UserUIConst.HEADER_COMP_FINISHED.format(comp_name[:self.UI_MAX_LEN]),
                                       body_header=DisplayConst.HEADER_FINISHED_MATCH_LIST_HEADER)
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)
#----------------------------------------------------------------------------- comp standing
    
    def show_competition_standing(self, competition_name: str, back_user: str, user=GlobalConst.PUBLIC):
        """ Prints out overview of the standing in the selected competition.

        Args:
            competition_name (str): Name of the competition.
            back_user (str): Current user access.
            user (str, optional): The type of user using the function. Defaults to GlobalConst.PUBLIC.
        """
        comp_standings = self.bl_wrapper.get_competition_standing(competition_name)

        option_list = list()
        standing = 1
        for team in comp_standings:
            option_list.append(DisplayConst.MENU_COMP_STANDINGS_LIST.format(standing,
                                                                            team["team"],
                                                                            team["wins"],
                                                                            team["won legs"]))
            standing += 1
        lower_boundary = 0
        upper_boundary = 12
        self.ui_logic.print_ui(option_list,
                               GlobalConst.MENU_OPTIONS_BMNP, 
                               UserUIConst.HEADER_COMP_STANDING.format(competition_name[:self.UI_MAX_LEN]),
                               body_header=DisplayConst.HEADER_COMPETITION_STANDINGS_LIST)
    
        error = False
        while True:
            error = self.ui_logic.print_error_line(error)
            user_selection = input(bcolors.OKGREEN+ GlobalConst.PROMPT_CHOICE + bcolors.ENDC).lower()
            if user_selection == GlobalConst.USER_SELECT_M: # Main Menu <- Competition score overview
                return user_selection
            elif user_selection == GlobalConst.USER_SELECT_B: 
                if back_user == GlobalConst.PUBLIC: # Competition menu <- Competition score overview
                    return self.show_competition_menu(competition_name)
                else:
                    return GlobalConst.USER_SELECT_B # Competition menu <- Competition score overview (Team captain or Organizer)
            elif user_selection == GlobalConst.USER_SELECT_N or user_selection == GlobalConst.USER_SELECT_P: # Turns pages back and forth if there are more than one
                lower_boundary, upper_boundary, error = self._page_turn_display(user_selection, lower_boundary,
                                                                                upper_boundary,
                                                                                option_list,
                                                            GlobalConst.MENU_OPTIONS_BMNP,
                                                            UserUIConst.HEADER_COMP_STANDING.format(competition_name),
                                                            body_header=DisplayConst.HEADER_COMPETITION_STANDINGS_LIST)
            else:
                error = True
                self.ui_logic.print_ui(self.get_list_boundary(option_list, lower_boundary, upper_boundary),
                                       GlobalConst.MENU_OPTIONS_BMNP,
                                       UserUIConst.HEADER_COMP_STANDING.format(competition_name[:self.UI_MAX_LEN]),
                                       DisplayConst.HEADER_COMPETITION_STANDINGS_LIST)
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)

#---------------------------------------------------------------------------- Setting list boundaries

    def get_list_boundary(self, option_list:list = [], lower_boundary:int=0, upper_boundary:int=10):
        """ Sets the boundary of the list for the display.

        Args:
            option_list (list, optional): _description_. Defaults to [].
            lower_boundary (int, optional): _description_. Defaults to 0.
            upper_boundary (int, optional): _description_. Defaults to 10.

        Returns:
            _type_: _description_
        """

        if len(option_list) + 1 < upper_boundary:
            return option_list[lower_boundary:]
        else:
            return option_list[lower_boundary:upper_boundary]

    def display_score_card(self, match, match_dict, match_games):
        header = f"Game: {match.home_team} VS {match.away_team}"
        scorecard_list = [
        UserUIConst.SCORECARD_SINGLE_501.format("1", match_dict['501 1'][0], match_games[0][0], match_games[0][1], match_dict['501 1'][1]),
        UserUIConst.SCORECARD_SINGLE_501.format("2", match_dict['501 2'][0], match_games[1][0], match_games[1][1], match_dict['501 2'][1]),
        UserUIConst.SCORECARD_SINGLE_501.format("3", match_dict['501 3'][0], match_games[2][0], match_games[2][1], match_dict['501 3'][1]),
        UserUIConst.SCORECARD_SINGLE_501.format("4", match_dict['501 4'][0], match_games[3][0], match_games[3][1], match_dict['501 4'][1]),
        UserUIConst.SCORECARD_DOUBLE_301.format("5", match_dict['301 HomeTeam'][0], match_games[4][0], match_games[4][1], match_dict['301 AwayTeam'][0]),
        UserUIConst.SCORECARD_BLANK_LINE.format(match_dict['301 HomeTeam'][1], match_dict['301 AwayTeam'][1]),
        UserUIConst.SCORECARD_CRICKET.format("6", match_dict['Cricket HomeTeam'][0], match_games[5][0], match_games[5][1], match_dict['Cricket AwayTeam'][0]),
        UserUIConst.SCORECARD_BLANK_LINE.format(match_dict['Cricket HomeTeam'][1], match_dict['Cricket AwayTeam'][1]),
        UserUIConst.SCORECARD_QUAD_501.format("7", match_dict['501 HomeTeam'][0], match_games[6][0], match_games[6][1], match_dict['501 AwayTeam'][0]),
        UserUIConst.SCORECARD_BLANK_LINE.format(match_dict['501 HomeTeam'][1], match_dict['501 AwayTeam'][1]),
        UserUIConst.SCORECARD_BLANK_LINE.format(match_dict['501 HomeTeam'][2], match_dict['501 AwayTeam'][2]),
        UserUIConst.SCORECARD_BLANK_LINE.format(match_dict['501 HomeTeam'][3], match_dict['501 AwayTeam'][3])]

        self.ui_logic.print_ui(scorecard_list, GlobalConst.MENU_OPTIONS_BM, header)

# --------------------------------------------------------------------------- The logic behind turning a page
    def _page_turn_display(self, user_input:str, 
                           lower_boundary:int,
                           upper_boundary:int,
                           option_list:list,
                           menu_options:str,
                           header:str,
                           align=GlobalConst.CENTERED,
                           body_header=""):
        """ Prints the next page.

        Args:
            user_input (str): Input from user.
            lower_boundary (int): Lower boundary.
            upper_boundary (int): Upper boundary.
            option_list (list): List of options.
            menu_options (str): List of menu options.
            header (str): Page header.
            body_header (str, optional): Information for the data in list. Defaults to "".
        """
        error = False
        if user_input == GlobalConst.USER_SELECT_N:
            if lower_boundary + 12 >= len(option_list):
                error = True
                self.ui_logic.print_ui(self.get_list_boundary(option_list, 
                                       lower_boundary,
                                       upper_boundary),
                                       menu_options,
                                       header,
                                       align,
                                       body_header)
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)
            else:
                lower_boundary += 12
                upper_boundary += 12
                self.ui_logic.print_ui(self.get_list_boundary(option_list, 
                                       lower_boundary,
                                       upper_boundary),
                                       menu_options,
                                       header,
                                       align,
                                       body_header)
        elif user_input == GlobalConst.USER_SELECT_P:
            if lower_boundary - 12 < 0:
                error = True
                self.ui_logic.print_ui(self.get_list_boundary(option_list, 
                                       lower_boundary,
                                       upper_boundary),
                                       menu_options,
                                       header,
                                       align,
                                       body_header)
                print(bcolors.FAIL + GlobalConst.INVALID_INPUT + bcolors.ENDC)
            else:
                lower_boundary -= 12
                upper_boundary -= 12
                self.ui_logic.print_ui(self.get_list_boundary(option_list, 
                                       lower_boundary,
                                       upper_boundary),
                                       menu_options,
                                       header,
                                       align,
                                       body_header)

        return lower_boundary, upper_boundary, error