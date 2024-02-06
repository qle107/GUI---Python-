import PySimpleGUI as sg
# import src.Controller.data as dta
import pandas.core.frame as frame

try:
    from ..Controller import data as dta
except ImportError:
    # If ImportError occurs, assume script is run as a module
    from Controller import data as dta


def create_table(data, meta_data):
    right_click_menu = ['Edit',['Insert column left', 'Insert column right', 'Filter']]

    if isinstance(data, list) and isinstance(meta_data, list):
        return_layout = [
            [sg.Text("Select a file:")],
            [sg.InputText(key="file_path",
                          enable_events=True), sg.FileBrowse()],
            [sg.Table(values=data,
                      headings=meta_data,
                      auto_size_columns=True,
                      justification='right',
                      key='table',
                      enable_click_events=True,
                      enable_events=True,
                      right_click_menu=right_click_menu,
                      hide_vertical_scroll=True)],
            [sg.Button("Load file", key="read_button")]
        ]
        return return_layout
    else:
        sg.popup("ERROR: To create a new table, the input of data and metadata should be in 'list' format")


def build_layout():
    return_layout = [
        [sg.Text("Select a file:")],
        [sg.InputText(key="file_path", enable_events=True), sg.FileBrowse()],
        [sg.Button("Load file", key="read_button")]
    ]
    return return_layout


def read_file(values):
    file_path = values["file_path"]
    data = None
    if file_path and file_path.endswith('.json'):
        data = dta.load_data(file_path)
    elif file_path and file_path.endswith('.csv'):
        data = dta.load_data(file_path)
    elif file_path and file_path.endswith('.xml'):
        data = dta.load_data(file_path)
    else:
        sg.popup('Can not detect file\'s format')
    if data is not None and isinstance(data, frame.DataFrame):
        table_data = data.values.tolist()
        table_headings = data.columns.tolist()
        layout = create_table(table_data, table_headings)
        return layout
    elif isinstance(data, dict):
        sg.popup(data['error'])
        return None
    else:
        sg.popup('Verify your file and try again')
        return None


def extract_columns(values):
    file_path = values["file_path"]
    data = None
    if file_path and file_path.endswith('.json'):
        data = dta.load_data(file_path)
    elif file_path and file_path.endswith('.csv'):
        data = dta.load_data(file_path)
    elif file_path and file_path.endswith('.xml'):
        data = dta.load_data(file_path)
    else:
        sg.popup('Can not detect file\'s format')
    if data is not None and isinstance(data, frame.DataFrame):
        table_headings = data.columns.tolist()
        return table_headings
    elif isinstance(data, dict):
        sg.popup(data['error'])
        return None
    else:
        sg.popup('Verify your file and try again')
        return None
