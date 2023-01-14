import math

class ShowLogic:

    def ui_menu_option_width(self, option_list:list, width:int) -> tuple:
        '''gets list of menu options and width to calculate spaces to 
        center menu based on the longest line'''
        
        length = 0
        for _ in option_list:
            if len(_) > length:
                length = len(_)
        spaces = width - length
        leading = math.floor(spaces/2)
        trailing = math.ceil(spaces/2)
        
        return length,leading,trailing

    def ui_menu_option_center_colon(self,option) -> tuple:
        '''gets a menu option with colon, splits in two on colon and returns'''
        
        option1,option2 = option.split(":")
        option1 = option1 + ":"
        
        return option1,option2