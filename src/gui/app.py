import json

import PySimpleGUI as sg
import src.Controller.data as dta

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
menu_def = [['File', ['!Open', '!Save', '!Exit']],
            ['Filter', ['!Undo', '!History']],
            ['Help', ['!About', '!Manual']]]

layout = [[sg.Menu(menu_def)],
          [[sg.Text('Some text on Row 1')],
           [sg.Text('Enter something on Row 2'), sg.InputText()],
           [sg.Button('Ok'), sg.Button('Cancel')]]
          ]
layout_r = [
    [sg.Text("Select a JSON file:")],
    [sg.InputText(key="file_path", enable_events=True), sg.FileBrowse()],
    [sg.Table(values=[], headings=[], auto_size_columns=True, justification='right', key='table')],

    # [sg.Multiline(key="json_output", size=(60, 10), disabled=True)],
    [sg.Button("Read JSON", key="read_button")]
]

# Create the Window
window = sg.Window('Python Project 2024', layout_r)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    if event == "read_button":
        file_path = values["file_path"]
        if file_path:
            json_data = dta.load_data(file_path, 'json')
            if json_data is not None:
                table_data = json_data.values.tolist()
                table_headings = json_data.columns.tolist()
                window['table'].update(values=table_data)
                # window["json_output"].update(json_data)
                # window["json_output"].update(json.dumps(json_data, indent=2))
                window.close()
                window = sg.Window('test', [
                    [sg.Table(values=table_data, headings=table_headings, auto_size_columns=True, justification='right', key='table')],
                    ])
window.close()
