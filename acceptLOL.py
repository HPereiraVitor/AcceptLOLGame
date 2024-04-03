import argparse
import sys
import pyautogui
import pyscreeze

# Global Definition
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False
# Mandatory Arguments
parser = argparse.ArgumentParser(epilog='Example of script call: acceptLOL.py -c Annie -ec Ekko -b Kassadin -eb Yasuo')
requiredNamedArgs = parser.add_argument_group('Mandatory Arguments')
requiredNamedArgs.add_argument( "--champion", "-c", help="Provide the champion that you wanna to play.",)
requiredNamedArgs.add_argument( "--ban", "-b", default="Zed", help="Provide the champion that you want to ban.")
# Optional Arguments
OptionalNamedArgs = parser.add_argument_group('Optional Arguments')
OptionalNamedArgs.add_argument( "--extrachoice", "-ec", help="Provide an seccond champion that you wanna play.",)
OptionalNamedArgs.add_argument( "--extraban", "-eb", default="Master Yi", help="Provide an seccond champion you want to ban.")

args = parser.parse_args()

def searchingAcceptButton():
    print('Searching Game...')

    while True:
        button_location = pyscreeze.locateOnScreen('./image/game_found.png')

        if button_location is not None:
            print('Game Found...')

            # Get the coordinates of the button's center
            buttonPoint = pyautogui.center(button_location)
            button_x, button_y = buttonPoint

            pyautogui.moveTo(button_x, button_y)
            pyautogui.click()

            break

def selectChampion():
    print ('Selecting your champion...')

    while True:
        button_location = pyscreeze.locateOnScreen('./image/ban_session.png')

        if button_location is not None:
            break

def banChampion():
    while True:
        ban_session = pyscreeze.locateOnScreen('./image/ban_session.png')

        if ban_session is not None:
            print('Banning %s...'%args.ban )

            write_location = pyscreeze.locateOnScreen('./image/write.png')
            writePoint = pyautogui.center(write_location)
            write_x, write_y = writePoint

            ban_button = pyscreeze.locateOnScreen('./image/ban_button.png')
            banPoint = pyautogui.center(ban_button)
            ban_x, ban_y = banPoint

            pyautogui.moveTo(write_x, write_y)
            pyautogui.click()

            pyautogui.write(args.ban)

            # TO DO: CLICK ON THE CHAMPION

            pyautogui.moveTo(ban_x, ban_y)
            pyautogui.click()

if __name__ == '__main__':
    print("TESTE")
    searchingAcceptButton()
    banChampion()
    selectChampion()