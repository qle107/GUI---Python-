import src.Controller.data as data
import src.Controller.util as util
import os
content = data.load_data('./resources/example.json')
# print(content)
# user_home = os.path.expanduser("~")
# file_path = os.path.join(user_home, 'Downloads', 'output_file.csv')
# data.save_data(content, file_path, 'csv')
tmp = content['age'].to_list()
# print(content['name'].to_list())

# print(util.calculate_list(tmp))

print(util.get_columns_from_dataframe(content))