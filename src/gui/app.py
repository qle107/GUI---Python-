import PySimpleGUI as sg
import sys
try:
    import build
except ImportError:
    # If ImportError occurs, assume script is run as a module
    from . import build

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
menu_def = [['File', ['!Open', '!Save', '!Exit']],
            ['Filter', ['!Undo', '!History']],
            ['Help', ['!About', '!Manual']]]

layout = build.build_layout()
# Create the Window

def run():
    window = sg.Window('Python Project 2024', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        if event == "read_button":
            tmp_layout = build.read_file(values)
            if tmp_layout is not None:
                window.close()
                window = sg.Window('Python Project 2024', tmp_layout)

    window.close()
