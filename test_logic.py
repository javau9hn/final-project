import unittest
import os
from tempfile import NamedTemporaryFile
from logic import load_data, list_to_csv

class TestLoadData(unittest.TestCase):

    def setUp(self):
        """Set up the test environment.
            Driver: Tommy
            Navigator: Javaughn
        """
        self.test_data = [
            ["Song1", "['Rock', 'Pop']"],
            ["Song2", "['Pop', 'R&B']"],
            ["Song3", "['Hip Hop', 'Rap']"],
        ]
        self.temp_file = NamedTemporaryFile(mode='w', delete=False, newline='', encoding='utf-8')
        self.temp_file_name = self.temp_file.name
        self.temp_file.write("Title,Genres\n")
        for song in self.test_data:
            self.temp_file.write(f"{song[0]},{song[1]}\n")
        self.temp_file.close()

    def tearDown(self):
        """Tear down the test environment.
            Driver: Tommy
            Navigator: Javaughn
        """
        os.unlink(self.temp_file_name)

    def test_load_data(self):
        """Test the load_data function.
            Driver: Tommy
            Navigator: Javaughn
            """
        loaded_data = load_data(self.temp_file_name)
        self.assertEqual(len(loaded_data), len(self.test_data))
        self.assertEqual(loaded_data, self.test_data)

class TestListToCSV(unittest.TestCase):
    

    def test_list_to_csv_success(self):
        """Test list_to_csv function on successful CSV creation.
            Driver: Tommy
            Navigator: Javaughn
        """
        test_data = [
            ["Song1", "Rock"],
            ["Song2", "Pop"],
            ["Song3", "Hip Hop"],
        ]
        temp_file_name = 'test_playlist.csv'
        result = list_to_csv(test_data, filename=temp_file_name)
        self.assertEqual(result, f"Playlist: '{temp_file_name}' created successfully!")
        os.unlink(temp_file_name)

    def test_list_to_csv_failure(self):
        """Test list_to_csv function on failure during CSV creation.
            Driver: Tommy
            Navigator: Javaughn
        """
        test_data = [
            ["Song1", "Rock"],
            ["Song2", "Pop"],
            ["Song3", "Hip Hop"],
        ]
        temp_file_name = 'non_existent_folder/test_playlist.csv'
        result = list_to_csv(test_data, filename=temp_file_name)
        self.assertTrue(result.startswith("Failed to create CSV file"))

if __name__ == '__main__':
    unittest.main()