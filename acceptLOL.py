import argparse
import sys
import pyautogui
import pyscreeze
import time

# Global Definition
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False
random_x = None
random_y = None

# Arguments
parser = argparse.ArgumentParser(epilog='Example of script call: acceptLOL.py -c Annie -ec Ekko -b Kassadin -eb Yasuo')
OptionalNamedArgs = parser.add_argument_group('Arguments')
OptionalNamedArgs.add_argument( "--champion", "-c", help="Provide the champion that you wanna to play.",)
OptionalNamedArgs.add_argument( "--ban", "-b", default="Zed", help="Provide the champion that you want to ban.")
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
    while True:
        choose_session = pyscreeze.locateOnScreen('./image/choose_session.png')

        if choose_session is not None:
            print('Selecting %s...'%args.champion )

            write_location = pyscreeze.locateOnScreen('./image/write_select.png')
            writePoint = pyautogui.center(write_location)
            write_x, write_y = writePoint

            pyautogui.moveTo(write_x, write_y)
            pyautogui.click()
            pyautogui.write(args.champion)

            pyautogui.moveTo(random_x, random_y)
            pyautogui.click()

            time.sleep(1)

            confirm_button = pyscreeze.locateOnScreen('./image/confirm_button.png')

            confirmPoint = pyautogui.center(confirm_button)
            confirm_x, confirm_y = confirmPoint

            pyautogui.moveTo(confirm_x, confirm_y)
            pyautogui.click()

            break

def banChampion():
    while True:
        ban_session = pyscreeze.locateOnScreen('./image/ban_session.png')

        if ban_session is not None:
            print('Banning %s...'%args.ban )

            write_location = pyscreeze.locateOnScreen('./image/write_ban.png')
            writePoint = pyautogui.center(write_location)
            write_x, write_y = writePoint

            pyautogui.moveTo(write_x, write_y)
            pyautogui.click()
            pyautogui.write(args.ban)

            pyautogui.moveTo(random_x, random_y)
            pyautogui.click()

            time.sleep(1)

            ban_button = pyscreeze.locateOnScreen('./image/ban_button.png')
            banPoint = pyautogui.center(ban_button)
            ban_x, ban_y = banPoint

            pyautogui.moveTo(ban_x, ban_y)
            pyautogui.click()

            break

def randomChamionPosition():
    while True:
        random_button = pyscreeze.locateOnScreen('./image/random_champion.png')
        if random_button is not None:
            randomPoint = pyautogui.center(random_button)
            return randomPoint

if __name__ == '__main__':
    print("acceptLOL.py is running!")
    searchingAcceptButton()
    random_x, random_y = randomChamionPosition()
    banChampion()
    selectChampion()
    print("Enjoy your game!")