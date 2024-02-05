import unittest
import src.Controller.data as data
import os


class UnitTestForDataController(unittest.TestCase):
    def test_read_csv(self):
        content = data.load_data('./resources/example.csv')
        self.assertTrue(len(content), 3)  # Ensure that it only contains 3 items
        self.assertTrue({'Name': 'John', 'Age': '25', 'Location': 'New York'} in content)

    def test_save_csv(self):
        user_home = os.path.expanduser("~")
        file_path = os.path.join(user_home, 'Downloads', 'output_file.csv')
        content = data.load_data('./resources/example.csv')
        self.assertFalse(isinstance(data.save_data(content, file_path, 'csv'),FileNotFoundError))
        self.assertFalse(isinstance(data.save_data(content, file_path, 'csv'),Exception))

if __name__ == '__main__':
    unittest.main()
