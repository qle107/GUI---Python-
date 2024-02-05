import csv
import json
import xml.etree.ElementTree as ET
import pandas as pd
import os


def load_data(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    if file_extension:
        try:
            with open(file_path, 'r') as file:
                if file_extension == '.csv' and file_path.endswith('csv'):
                    return pd.read_csv(file)
                elif file_extension == '.json' and file_path.endswith('json'):
                    data = json.load(file)
                    first_key = list(data.keys())[0]
                    if first_key:
                        return pd.DataFrame(data[first_key])
                    else:
                        return list(data)
                elif file_extension == '.xml' and file_path.endswith('xml'):
                    return pd.read_xml(file)
                else:
                    return "Unsupported format or format is not correct"
        except FileNotFoundError:
            return {'error': 'file not found'}
        except Exception as error:
            return {'error': str(error)}
    else:
        return {'error': 'file extension is not exist'}


def save_data(data, file_path, file_format):
    if isinstance(data, dict):
        try:
            with open(file_path, 'w', newline='') as file:
                if file_format == 'csv':
                    if data and isinstance(data[0], dict):
                        # Use the keys from the first dictionary if data is a list of dictionaries
                        writer = csv.DictWriter(file, fieldnames=data[0].keys())
                        writer.writeheader()
                        for row in data:
                            writer.writerow(row)
                    else:
                        # Use a generic fieldnames list if data is not a list of dictionaries
                        writer = csv.writer(file)
                        writer.writerows(data)
                elif file_format == 'json':
                    json.dump(data, file, indent=2)
                elif file_format == 'xml':
                    root = ET.Element('data')
                    for entry in data:
                        item = ET.SubElement(root, 'item')
                        for key, value in entry.items():
                            sub_element = ET.SubElement(item, key)
                            sub_element.text = str(value)
                    tree = ET.ElementTree(root)
                    tree.write(file)
                else:
                    return "Unsupported format"

        ## Here in fact should handle corrupted file but im too lazy
        except PermissionError:
            return "Program doesn't have permission to create/modify"
        except FileNotFoundError:
            return "File doesn't exist or is not a file"
        except Exception as error:
            return error
