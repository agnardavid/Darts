from bl.bl_wrapper import BusinessLogicWrapper
from ui.constants import GlobalConst,DisplayConst,UserUIConst
import copy

class DisplayUI():

    def __init__(self):
        self.bl_wrapper = BusinessLogicWrapper()
        self.SPACES = GlobalConst.SPACES
        self.DOT = GlobalConst.DOT
        self.LINE = GlobalConst.LINE
        self.COMMA = GlobalConst.COMMA
        self.ASTRO = GlobalConst.ASTRO
        self.DARTS = GlobalConst.DARTS
        self.O_BRACE = GlobalConst.O_BRACE
        self.EQUAL = GlobalConst.EQUAL
        self.LE_BRACKET = GlobalConst.LE_BRACKET


    def print_ui(self, option_list:list,
                 input_options:str,
                 header:str,
                 align:str = GlobalConst.CENTERED,
                 body_header:str = "") -> None:
        '''Prints the menu in correct format'''
        self.print_darts()
        print(bcolors.OKGREEN + self.center_string(header) + bcolors.ENDC)
        print(bcolors.OKGREEN + "-"*86 + bcolors.ENDC)
        
        # Main body headers
        if body_header == DisplayConst.HEADER_PLAYER_LIST:
            self.main_body_header_player_list()
        elif body_header == DisplayConst.HEADER_TEAM_LIST:
            self.main_body_header_team_list()
        elif body_header == DisplayConst.HEADER_UNFINISHED_MATCH_LIST:
            self.main_body_header_unfinished_match_list()
        elif body_header == DisplayConst.HEADER_FINISHED_MATCH_LIST_HEADER:
            self.main_body_header_finished_match_list()
        elif body_header == DisplayConst.HEADER_COMPETITION_STANDINGS_LIST:
            self.main_body_header_competition_standings_list()
        else:
            print(bcolors.OKGREEN +
                  f"{self.LINE:<3}{self.SPACES:<80}{self.LINE:>3}" +
                  bcolors.ENDC)
        
        # Main body content
        self.print_option(option_list, align)

        print(bcolors.OKGREEN + "-"*86 + bcolors.ENDC)
        print(bcolors.OKGREEN + self.center_string(input_options) + bcolors.ENDC)
        self.print_darts()

    def print_darts(self):
        """ Prints the darts on the menu """
        
        print(bcolors.OKGREEN + self.LINE * 86 + bcolors.ENDC)
        print(bcolors.OKGREEN + self.SPACES*48 + "/" + self.ASTRO*11 + "\\" + 
              bcolors.ENDC)
        print(bcolors.OKGREEN + self.DARTS + self.SPACES*11 + self.LINE*6 + "=" + 
              self.O_BRACE*14 + "}" + self.LE_BRACKET*4 + self.EQUAL*5 + "<" + 
              self.LINE*13 + ">" + self.SPACES*19 + self.DARTS + bcolors.ENDC)
        print(bcolors.OKGREEN + self.SPACES*48 + "\\" + self.COMMA*11 + "/" + 
              bcolors.ENDC)
        print(bcolors.OKGREEN + self.LINE*86 + bcolors.ENDC)


    def main_body_header_player_list(self):
        '''prints out correct headers for list view'''
        print(bcolors.OKGREEN + 
              DisplayConst.HEADER_MENU_PLAYER_LIST.format(self.LINE,
                                                          self.SPACES,
                                                          DisplayConst.NAME,
                                                          DisplayConst.SSN, 
                                                          DisplayConst.GSM,
                                                          self.SPACES,
                                                          self.LINE)
              + bcolors.ENDC)        


    def main_body_header_team_list(self):
        '''prints out correct headers for list view'''
        print(bcolors.OKGREEN + 
              DisplayConst.HEADER_MENU_TEAM_LIST.format(self.LINE,
                                                        self.SPACES,
                                                        DisplayConst.TEAM,
                                                        DisplayConst.CLUB,
                                                        self.SPACES,
                                                        self.LINE)
              + bcolors.ENDC) 
        

    
    def main_body_header_unfinished_match_list(self):
        '''prints out correct headers for list view'''
        print(bcolors.OKGREEN + 
              DisplayConst. HEADER_MENU_UNFINISHED_MATCH_LIST.format(self.LINE,
                                                                   self.SPACES,
                                                                   DisplayConst.DATE,
                                                                   DisplayConst.MATCH,
                                                                   self.SPACES,
                                                                   self.LINE)
              + bcolors.ENDC) 

    
    def main_body_header_finished_match_list(self):
        '''prints out correct headers for list view'''
        print(bcolors.OKGREEN + 
              DisplayConst.HEADER_MENU_FINISHED_MATCH_LIST.format(self.LINE,
                                                                self.SPACES,
                                                                DisplayConst.HOME_TEAM,
                                                                DisplayConst.SCORE, 
                                                                DisplayConst.AWAY_TEAM,
                                                                self.SPACES,
                                                                self.LINE)
              + bcolors.ENDC)                


    def main_body_header_competition_standings_list(self):
        '''prints out correct headers for list view'''
        print(bcolors.OKGREEN + 
              DisplayConst.HEADER_MENU_COMP_STANDINGS_LIST.format(self.LINE,
                                                                  self.SPACES,
                                                                  DisplayConst.TEAM,
                                                                  DisplayConst.WINS, 
                                                                  DisplayConst.WON_LEGS,
                                                                  self.SPACES,
                                                                  self.LINE)
              + bcolors.ENDC)                


    def center_string(self, text_to_display:str):
        '''Takes in a text and returns it centered within the set character 
        parameters (86 characters)'''
        return text_to_display.center(86)


    def print_option(self, option_list:list, align:str = GlobalConst.CENTERED):
        '''takes in a list and prints out all contents of the list, given 
        that its length 
        is equal or less than 10'''
        popped_list = copy.deepcopy(option_list)
        popped_list.reverse()
        line = GlobalConst.LINE
        
        if align == GlobalConst.CENTERED:
            ui_width = DisplayConst.UI_WIDTH
            length,leading,trailing = self.bl_wrapper.ui_menu_option_width(option_list, 
                                                                           ui_width)
            
            for _ in range(12):
                if len(popped_list) != 0:
                    option = popped_list.pop()
                    print(bcolors.OKGREEN + 
                          f"{line:<1}{self.SPACES:<{leading}}{option:<{length}}{self.SPACES:<{trailing}}{line:>1}" + bcolors.ENDC)
                else:
                    print(bcolors.OKGREEN + f"{line*1:<3}{self.SPACES:<80}{line*1:>3}" + bcolors.ENDC)
                    
        if align == GlobalConst.LEFT:
            for _ in range(12):
                if len(popped_list) != 0:
                    option = popped_list.pop()
                    if self.is_len_of_string_within_constraints(option):
                        print(bcolors.OKGREEN + f"{line:<3}{option:^80}{line:>3}" + bcolors.ENDC)
                    else:
                        full_word = option[0:77].strip() + 3*self.DOT
                        print(bcolors.OKGREEN + f"{line:<3}{full_word:<80}{line:>3}" + bcolors.ENDC)
                else:
                    print(bcolors.OKGREEN + f"{line:<3}{self.SPACES:<80}{line:>3}" + bcolors.ENDC)
        
        if align == GlobalConst.COLON:
            for _ in range(12):
                if len(popped_list) != 0:
                    option = popped_list.pop()
                    option1,option2 = self.bl_wrapper.ui_menu_option_center_colon(option)
                    if self.is_len_of_string_within_constraints(option):
                        print(bcolors.OKGREEN + f"{line:<3}{option1:>33}{option2:<47}{line:>3}" + bcolors.ENDC)
                else:
                    print(bcolors.OKGREEN + f"{line:<3}{self.SPACES:<80}{line:>3}" + bcolors.ENDC)

    def is_len_of_string_within_constraints(self, text_to_check:str) -> None:
        '''Checks the length of the given text and returns True if it's within bounds (<= 40 characters)'''
        if len(text_to_check) > 80:
            return False
        else:
            return True


    def print_list(self, a_list:list = []) -> None:
        """ Prints given list """ 
        for line in a_list:
            print(line.strip("\n"))


    def display_score_card(self, match, match_dict, match_games): # match_games iare lists in a list?, match_dict is a dict, match is an object
        """ Prints the scoreboard """
        print(f"Game: {match} VS {match}")
        print(f"1. {match_dict['501 1'][0]:<10}{match_games[0][0]}| 501 |{match_games[0][1]:<10}{match_dict['501 1'][1]}")
        print(f"2. {match_dict['501 2'][0]:<10}{match_games[1][0]}| 501 |{match_games[1][1]:<10}{match_dict['501 2'][1]}")
        print(f"3. {match_dict['501 3'][0]:<10}{match_games[2][0]}| 501 |{match_games[2][1]:<10}{match_dict['501 3'][1]}")
        print(f"4. {match_dict['501 4'][0]:<10}{match_games[3][0]}| 501 |{match_games[3][1]:<10}{match_dict['501 4'][1]}")
        print(f"5. {match_dict['301 HomeTeam'][0]:<10}{match_games[4][0]}| 301 |{match_games[4][1]:<10}{match_dict['301 AwayTeam'][0]}")
        print(f"   {match_dict['301 HomeTeam'][1]:<11} --- {match_dict['301 AwayTeam'][1]:>14}")
        print(f"6. {match_dict['Cricket HomeTeam'][0]:<11}{match_games[5][0]}| C |{match_games[5][1]:<11}{match_dict['Cricket AwayTeam'][0]}")
        print(f"   {match_dict['Cricket HomeTeam'][1]:<11} --- {match_dict['Cricket AwayTeam'][1]:>16}")
        print(f"7. {match_dict['501 HomeTeam'][0]:<10}{match_games[6][0]}| 501 |{match_games[6][1]:<10}{match_dict['501 AwayTeam'][0]}")
        print(f"   {match_dict['501 HomeTeam'][1]:<11} --- {match_dict['501 AwayTeam'][1]:>16}")
        print(f"   {match_dict['501 HomeTeam'][2]:<11} --- {match_dict['501 AwayTeam'][2]:>17}")
        print(f"   {match_dict['501 HomeTeam'][3]:<11} --- {match_dict['501 AwayTeam'][3]:>15}")

    def print_error_line(self, error:bool) -> bool:
        '''prints a line if the error parameter is False, and returns False regardless of the parameter'''
        if error == False:
            print()
        return False

class bcolors():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'