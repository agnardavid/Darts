from ui.organizer_ui import OrganizerUI
from ui.team_captain_ui import TeamCaptainUI
from ui.user_ui import UserUI
from ui.display_UI import DisplayUI,bcolors
from ui.constants import GlobalConst,MenuConst
class MenuUI:
    """ Class only to run and print the main menu """
    
    def __init__(self):
        self.organizer_ui = OrganizerUI()
        self.team_captain_ui = TeamCaptainUI()
        self.user_ui = UserUI()
        self.ui_logic = DisplayUI()

    def menu_output(self):
        """Print for the main menu"""
        header = MenuConst.HEADER_WELCOME
        menu_options = MenuConst.MENU_OPTIONS_OTP
        input_options = MenuConst.INPUT_OPTIONS_QUIT

        
        self.ui_logic.print_ui(menu_options, input_options, header)

    def input_prompt(self):
        """Displays the main menu with 3 available login options, 
            1. organizer
            2. team captain
            3. public
        """
        error = False
        while True:
            self.menu_output()
            error = self.ui_logic.print_error_line(error)
            ui_input = input(bcolors.OKGREEN + 
                             GlobalConst.PROMPT_CHOICE + 
                             bcolors.ENDC).lower()
            if ui_input == GlobalConst.USER_SELECT_Q:
                print(MenuConst.QUIT_MSG)
                break 
            elif ui_input == GlobalConst.USER_SELECT_1: #  Main menu -> Organizer menu
                self.organizer_ui.show_organizer_menu()
            elif ui_input == GlobalConst.USER_SELECT_2: # Main menu -> Team Captain menu
                self.team_captain_ui.show_competition_list(GlobalConst.TEAM_CAPTAIN)
            elif ui_input == GlobalConst.USER_SELECT_3: # Main menu -> Public menu
                self.user_ui.show_competition_list(GlobalConst.PUBLIC)
            else:
                error = True
                print(bcolors.FAIL + 
                      GlobalConst.INVALID_INPUT + 
                      bcolors.ENDC)

