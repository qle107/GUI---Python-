import src.Controller.data as data
import os
content = data.load_data('./resources/example.yaml', 'xml')
print(content)
# user_home = os.path.expanduser("~")
# file_path = os.path.join(user_home, 'Downloads', 'output_file.csv')
# data.save_data(content, file_path, 'csv')
