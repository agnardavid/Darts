# Agnar Davíð Halldórsson
# Daníel Guðjónsson
# Helgi Harðarson
# Hörður Daði Bergmann
# Jóhann Agnar Einarsson
# Oliver Ormar Ingvarsson

from ui.menu_ui import MenuUI
import os

def main():
    os.system("")
    ui = MenuUI()
    error = None
    try:
        while ui.input_prompt():
        # If start returns true, user logged out, should call start again to login again
            pass
    except Exception as err:
        error = err
    finally:
        # ui.quit()
        pass
    if error is not None:
        raise error

if __name__ == '__main__':
    main()