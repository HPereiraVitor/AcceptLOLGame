import pyautogui

while True:
    # Encontre a posição do botão na tela
    button_location = pyautogui.locateOnScreen('image/button_aceitar.png')
    # Verifique se o botão foi encontrado
    if button_location is not None:
        print('BUTTON FOUND...')

        # Obtenha as coordenadas do centro do botão
        button_x, button_y, button_width, button_height = pyautogui.center(button_location)

        # Mova o cursor do mouse para o centro do botão
        pyautogui.moveTo(button_x, button_y)

        # Clique no botão
        pyautogui.click()

        break
    else:
        print('SEARCHING...')
