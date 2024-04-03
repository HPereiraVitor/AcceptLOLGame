#import pyautogui
#import tkinter
#import customtkinter
#
#def searchingAcceptButton():
#    combobox_1.get()
#    print(combobox_1.get())
#
#    while True:
#        # Encontre a posição do botão na tela
#        button_location = pyautogui.locateOnScreen('image/button_aceitar.png')
#        # Verifique se o botão foi encontrado
#        if button_location is not None:
#            print('BUTTON FOUND...')
#            # Obtenha as coordenadas do centro do botão
#            buttonPoint = pyautogui.center(button_location)
#            button_x, button_y = buttonPoint
#            # Mova o cursor do mouse para o centro do botão
#            pyautogui.moveTo(button_x, button_y)
#            # Clique no botão
#            pyautogui.click()
#            break
#
#def showResetCheckBox():
#    if radiobutton_var.get() == 1:
#        checkbox_1['state'] = 'normal'
#        checkbox_1.pack(pady=10, padx=10)
#        checkbox_1.grid(row=0, column=0)
#    else:
#        checkbox_1['state'] = 'readonly'
#        checkbox_1.grid_forget()
#
#if __name__ == '__main__':
#    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
#
#    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
#    app.geometry("400x200")
#    app.title("Accepting a match automatically")
#
#    position_text = "Are you the team leader?"
#    label = customtkinter.CTkLabel(app, text=position_text)
#    label.grid(row=0, column=0)
#
#    radiobutton_var = customtkinter.IntVar(value=1)
#
#    radiobutton_1 = customtkinter.CTkRadioButton(master=app, text="Yes", variable=radiobutton_var, value=1, command=showResetCheckBox)
#    radiobutton_var.set(2)
#    radiobutton_1.pack(pady=10, padx=10)
#    radiobutton_1.grid(row=1, column=0)
#
#    radiobutton_2 = customtkinter.CTkRadioButton(master=app, text="No", variable=radiobutton_var, value=2, command=showResetCheckBox)
#    radiobutton_2.pack(pady=10, padx=10)
#    radiobutton_2.grid(row=2, column=0)
#
#    checkbox_1 = customtkinter.CTkCheckBox(master=app, text="Want to restart search?", command=showResetCheckBox)
#
#    buttonSearch = customtkinter.CTkButton(master=app, text="Start", command=searchingAcceptButton)
#    buttonSearch.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
#
#    app.mainloop()