
class GlobalConst:
    # User selections
    USER_SELECT_1 = "1"
    USER_SELECT_2 = "2"
    USER_SELECT_3 = "3"
    USER_SELECT_4 = "4"
    USER_SELECT_5 = "5"
    USER_SELECT_6 = "6"
    USER_SELECT_7 = "7"
    USER_SELECT_8 = "8"
    USER_SELECT_9 = "9"
    USER_SELECT_10 = "10"
    
    USER_SELECT_B = "b"
    USER_SELECT_Q = "q"
    USER_SELECT_M = "m"
    USER_SELECT_N = "n"
    USER_SELECT_P = "p"
    USER_SELECT_S = "s"
    USER_SELECT_C = "c"
    USER_SELECT_Y = "y"
    
    # Headers
    HEADER_LIST_ALL_COMP = "List of All Competitions"    
    
    # Menu Options
    MENU_OPTIONS_B = "[B]ACK"
    MENU_OPTIONS_C = "[C]ANCEL"
    MENU_OPTIONS_BM = "[B]ACK  [M]AIN MENU"
    MENU_OPTIONS_BMNP = "[B]ACK  [M]AIN MENU  [N]EXT  [P]REV"
    MENU_OPTIONS_BMSC = "[B]ACK  [M]AIN MENU  [S]AVE  [C]ANCEL"
    MENU_OPTIONS_BMNC = "[B]ACK  [M]AIN MENU  [N]EXT  [C]ANCEL"
    
    # Prompts, errors and other
    PROMPT_CHOICE = "Enter your choice: "
    INVALID_INPUT = "Invalid input, try again."
    ORGANIZER = "Organizer"
    TEAM_CAPTAIN = "Team Captain"
    PLAYER2 = "Player 2"
    PLAYER3 = "Player 3"
    PLAYER4 = "Player 4"
    PUBLIC = "Public"
    UI_MAX_LEN = 30
    CENTERED = "centered"
    LEFT = "left"
    COLON = "colon"
    DOT = "."
    SPACES = " "
    LINE = "-"
    COMMA = ","
    DARTS = "Darts"
    O_BRACE = "{"
    EQUAL = "="
    LE_BRACKET = "<"
    ASTRO = "'"
    
class DisplayConst:
    # Headers
    HEADER_PLAYER_LIST = ["Name","SSN","GSM"]
    HEADER_TEAM_LIST = ["Team","Club"]
    HEADER_UNFINISHED_MATCH_LIST = ["Date","Match"]
    HEADER_FINISHED_MATCH_LIST_HEADER = ["Home Team","Score","Away Team"]
    HEADER_COMPETITION_STANDINGS_LIST = ["Team","Wins","Won Legs"]

    MENU_PLAYER_LIST = "{:<30}{:^15}{:>10}"
    MENU_TEAM_LIST = "{}. {:<28}{:<17}"
    MENU_UNFINISHED_MATCH_LIST = "{:^21}{} VS {}"
    MENU_FINISHED_MATCH_LIST = "{:<22}{} - {:<11}{}"
    MENU_COMP_STANDINGS_LIST = "{}. {:<23}{:<16}{}"
    
    #"-              Name                            SSN             GSM                   -"
    HEADER_MENU_PLAYER_LIST = "{:<1}{:<14}{:<30}{:^15}{:>10}{:<15}{:>1}"
    #"-                     Team                        Club                               -"
    HEADER_MENU_TEAM_LIST = "{:<1}{:<21}{:<28}{:<17}{:<18}{:>1}"
    #"-                     Date            Match                                          -"
    HEADER_MENU_UNFINISHED_MATCH_LIST = "{:<1}{:<21}{:<16}{:<20}{:<27}{:>1}"
    # "-                Home Team             Score          Away Team                      -"
    HEADER_MENU_FINISHED_MATCH_LIST = "{:<1}{:<16}{:<22}{:<15}{:<9}{:<22}{:>1}"
    #"-                     Team                 Wins            Won Legs                  -"
    HEADER_MENU_COMP_STANDINGS_LIST = "{:<1}{:<23}{:<23}{:<16}{:<16}{:<6}{:>1}"

    # Prompts, errors and other
    UI_WIDTH = 84
    NAME = "Name"
    SSN = "SSN"
    GSM = "GSM"
    TEAM = "Team"
    CLUB = "Club"
    MATCH = "Match"
    DATE = "Date"
    HOME_TEAM = "Home Team"
    SCORE = "Score"
    AWAY_TEAM = "Away Team"
    WINS = "Wins"
    WON_LEGS = "Won Legs"


class MenuConst:
    # Constants
    HEADER_WELCOME = "Welcome to Darts"
    MENU_OPTIONS_OTP = ["1. Organizer",
                        "2. Team Captain",
                        "3. Public"]
    INPUT_OPTIONS_QUIT = "[Q]UIT"
    QUIT_MSG = "Thank you, good bye."

    

class OrganizerConst:
    # Headers
    HEADER_ORGANIZER = "Organizer"
    HEADER_CREATE_COMP = "Create competition"
    HEADER_FIND_COMPETITION = "Find competition"
    HEADER_COMPETITION = "Competition: {}"
    HEADER_ADD_NEW_TEAM = "Add New Team"
    HEADER_ADD_TEAM = "Add Team"
    HEADER_CREATE_CLUB = "Create club"
    HEADER_CREATE_TEAM = "Create Team"
    HEADER_TEAM_ADD_PLAYERS = "Team {} - Add player {}"
    HEADER_MATCH_DATE = "Current date {}"
    HEADER_ADD_COMP = "Add new competition"
    HEADER_CHANGE_DATE = "Game: {} VS {}, Change Date"
    HEADER_SET_START_DATE = "Competition: {}, Set Start Date"
    HEADER_SET_END_DATE = "Competition: {}, Set End Date"
    HEADER_SELECT_CLUB =  "Select Club for '{}'"
    HEADER_ADD_ROLE = "Add {}"
    HEADER_ADD_NEW_CLUB = "Add New Club"
    HEADER_COMP_ADD_TEAM = "{} | Add team"
    
    # Menu options
    MENU_OPTIONS_SCL_CNP = ["1. Show Competition List",
                            "2. Create New Competition"]
    MENU_OPTIONS_ECN_LOC =["1. Enter competition name: ",
                           "2. List of competitions"]
    MENU_OPTIONS_TL_CT = ["1. Team List",
                          "2. Create Team"]
    MENU_OPTIONS_STC_CNC = ["1. Select team club",
                            "2. Create new club"]
    MENU_OPTIONS_AM_AT_SM_DC = ["1. Add Match",
                                "2. Add Teams",
                                "3. Show Matches",
                                "4. Display Competition stats"]
    MENU_SEL_COMP = "{}. {}"
    MENU_OPTIONS_SHOW_COMP = ["1. Add teams",
                              "2. Generate match schedule",
                              "3. Edit match results",
                              "4. Delay match",
                              "5. List of all teams and their players",
                              "6. List of unfinished matches",
                              "7. List of finished matches",
                              "8. Overview of competition score"]

    MENU_OPTIONS_SHOW_COMP_2 = ["1. Edit match results",
                                "2. Delay match",
                                "3. List of all teams and their players",
                                "4. List of unfinished matches",
                                "5. List of finished matches",
                                "6. Overview of competition score"]
    MENU_COMP_NAME = "Name: {}"
    MENU_ORG_NAME = "Organizer: {}"
    MENU_PHONE = "Phone: {}"
    MENU_START_DATE = "Start date: {}"
    MENU_END_DATE = "End date: {}"
    MENU_ROUNDS = "Rounds: {}"
    MENU_CLUB_NAME = "Club Name: {}"
    MENU_HOME_ADDRESS = "Home Address: {}"
    MENU_PHONE = "Phone Number: {}"
    MENU_TEAM_CLUB = "Team Club: {}"
    MENU_TEAM_NAME = "Team name: {}"
    MENU_TEAM_CAPTAIN = "Team Captain: {}"
    MEANU_TEAM_PLAYER2 = "Team Player: {}"
    MEANU_TEAM_PLAYER3 = "Team Player: {}"
    MEANU_TEAM_PLAYER4 = "Team Player: {}"
    MENU_PLAYER_NAME = "Player Name: {}"
    MENU_PLAYER_HOME = "Player Home Address: {}"
    MENU_PLAYER_PHONE = "Player Home Phone: {}"
    MENU_PLAYER_MOBILE = "Player Mobile Phone: {}"
    MENU_PLAYER_EMAIL = "Player Email: {}"
    MENU_PLAYER_SSN = "Player SSN: {}"
    MENU_PLAYER_TC = "Team Captain( y/n ): {}"
    MENU_YEAR = "Year: {}"
    MENU_MONTH = "Month: {}"
    MENU_DAY = "Day: {}"
    

    # Prompts, errors and other
    PROMPT_HOME_SCORE = "Enter new home team score: "
    PROMPT_AWAY_SCORE = "Enter new away team score: "
    PROMPT_DATE_MATCH = "Enter new date for match: "
    PROMPT_YEAR = "Enter year (YYYY): "
    PROMPT_MONTH = "Enter month (MM): "
    PROMPT_DAY = "Enter day (DD): "
    PROMPT_COMP_NAME = "Enter competition name: "
    PROMPT_ORG_NAME = "Enter organizer name: "
    PROMPT_COMP_PHONE = "Enter organizer phone number: "
    PROMPT_ROUNDS = "Enter rounds: "
    PROMPT_TEAM_NAME = "Enter team name: "
    PROMPT_CLUB_NAME = "Enter club name: "
    PROMPT_CLUB_ADDRESS = "Enter club address: "
    PROMPT_CLUB_PHONE = "Enter club phone number: "
    PROMPT_PLAYER_NAME = "Enter player name: "
    PROMPT_PLAYER_SSN = "Enter player ssn: "
    PROMPT_PLAYER_EMAIL = "Enter player email: "
    PROMPT_PLAYER_ADDRESS = "Enter player address: "
    PROMPT_PLAYER_GSM = "Enter player gsm: "
    PROMPT_PLAYER_HOME_PHONE = "Enter player home number: "
    PROMPT_CONFIRM = "Are you sure you want to generate matches? Press (Y)es to generate: "
    INVALID_YEAR = "Year invalid!"
    INVALID_MONTH = "Month invalid!"
    INVALID_DAY = "Day invalid!"
    INVALID_DATE = "Date invalid!"
    INVALID_COMP_NAME = "Invalid competition name"
    INVALID_COMP_NAME_ALREADY_EXISTS = "Competition name already exists!"
    INVALID_NAME = "Name invalid!"
    INVALID_PHONE_NUMBER = "Phone number invalid!"
    INVALID_START_DATE = "The end date cannot be before the start date"
    INVALID_ROUNDS = "Rounds must be higher than zero!"
    INVALID_TEAM_NAME = "Team name invalid!"
    INVALID_TEAM_NAME_ALREADY_EXISTS = "Team name already exists!"
    INVALID_CLUB_NAME = "Club name invalid!"
    INVALID_CLUB_NAME_ALREADY_EXISTS = "Club name already exists!"
    INVALID_ADDRESS = "Invalid address!"
    INVALID_SSN = "Invalid SSN!"
    INVALID_SSN_ALREADY_EXISTS = "Invalid SSN or player already registered!"
    INVALID_EMAIL = "Invalid email!"
    DATE_OUT_OF_RANGE = "Date not within competition timeline"
    SELECTIOM_ADD_NEW_TEAM = "{}. Add new team"
    SELECTIOM_ADD_NEW_CLUB = "{}. Add new club"
    CURRENT_DATE = "Current date: {}"
    SELECTED_DATE_START_END = "{} - : - {}"
class TeamCaptainConst:
    # Headers
    HEADER_COMP_CAPTAIN_MATCHES = "Competition {}: Your unfinished matches"
    
    # Menu Options
    HEADER_COMPETITION = "Competition: {}"
    MENU_OPTIONS_SHOW_COMP = ["1. Add results",
                              "2. List of all teams and their players",
                              "3. List of unfinished matches",
                              "4. List of finished matches",
                              "5. Overview of competition score"]
    
    # Prompt and errors and other
    INSIDE_TEAM_CAPTAIN = "Inside Team Captain"
    PROMPT_SSN = "Enter your ssn: "
    ADD_NEW_RESULT = "1. Add new results"
    LIST_TEAMS_PLAYERS = "2. List of all teams and their players"
    LIST_UNFINISHED = "3. List of unfinished matches"
    LIST_FINISHES = "4. List of finished matches"
    OVERVIEW_COMP = "5. Overview of competition score"
    HOME_TEAM_SCORE = "Home Team Score: "
    AWAY_TEAM_SCORE = "Away Team Score: "
    INVALID_SCORE = "Score must be 0, 1 or 2!"
    INVALID_SCORE_SUM = "Only best out of 3!"
    PRESS_S_SAVE = "Do you want to [S]ave scorecard? "
    INVALID_SSN = "SSN does not exist"
    INVALID_CAPTAIN_SSN = "SSN is not team captain!"


class UserUIConst:
    # Headers
    HEADER_COMP_SELECTED = "Competition {}"
    HEADER_COMP_UNFINISHED = "Competition {}: Unfinished matches"
    HEADER_COMP_FINISHED = "Competition {}: Finished matches"
    HEADER_COMP_STANDING = "Competition {}: Standings"

    HEADER_PLAYER_LIST = "{:<30}{:^10}{:>10}"
    
    # Menu Options
    MENU_OPTIONS_LA_LU_LF_OW = ["1. List of all teams and their players",
                                "2. List of unfinished matches",
                                "3. List of finished matches",
                                "4. Overview of competition score"]
    MENU_OPTIONS_SEL_HOME_AWAY = "{}. {} VS {}"
    MENU_OPTIONS_SEL_HOME_AWAY_CURRENT_DATE = "{}. {} VS {} | Current date: {}"
    MENU_OPTIONS_TEAM_STANDING = "{} - {}"

    # Scorecard
    SCORECARD_SINGLE_501 = "{}. {:<20}{} | 501 | {:<14}{:<10}"
    SCORECARD_DOUBLE_301 = "{}. {:<20}{} | 301 | {:14}{:<10}"
    SCORECARD_CRICKET = "{}. {:<20}{} |  C  | {:<14}{:<10}"
    SCORECARD_QUAD_501 = "{}. {:<20}{} | 501 | {:<14}{:<10}"
    SCORECARD_BLANK_LINE = "   {:<20}- | --- | -             {:<14}"
    
    # Prompts, errors and other
 