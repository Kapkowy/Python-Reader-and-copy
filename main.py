import PySimpleGUI as Sg
from discordwebhook import Discord
discord = Discord(url="your url here!")

while True:
    k2 = Sg.popup_get_text('Your Name', icon='icon.ico', no_titlebar=True)
    if k2 != '':
        break
layout = [[Sg.Button("test")],
          [Sg.Checkbox('Do you want to copy?', key='3232')],
          [Sg.Text(visible=False, key='lood')],
          [[Sg.In(key='l'), Sg.FileBrowse(key='32', file_types=(("Text Files", "*.txt"),))]]]
# Create the window
window = Sg.Window('Test', layout, icon='icon.ico')
# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == Sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == 'test' and values['l'] != "":
        f = open(values['32'], "r")
        f2 = f.read().upper()
        if values['3232']:
            Sg.clipboard_set(f2)
            Sg.popup("SKOOPIOWANO")
            print('coped')
        else:
            print('lat?')
            Sg.popup('NIESKOPIOWANO DANYCH. WYSYLAM INFORMACJE NA DISCORD')
            discord.post(content=k2 + " nie skopiowal danych")
        window['lood'].update(f2, visible=True)
window.close()
