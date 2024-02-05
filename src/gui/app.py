import PySimpleGUI as sg
import sys
import Controller.util as util
import Controller.data as dta

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
    columns_list = []
    dataframe = None
    window = sg.Window('Python Project 2024', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        if event == "read_button":
            tmp_layout = build.read_file(values)
            tmp_columns = build.extract_columns(values)
            dataframe = dta.load_data(values["file_path"])
            if tmp_columns is not None:
                columns_list = tmp_columns
                tmp_columns = None
            if tmp_layout is not None:
                window.close()
                window = sg.Window('Python Project 2024', tmp_layout)
        if event[0] == "table" and event[2][0] == -1:
            sg.popup(util.calculate_list(dataframe[columns_list[event[2][1]]].to_list()))
    window.close()
