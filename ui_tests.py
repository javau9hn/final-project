import unittest
from unittest.mock import patch, Mock
import tkinter as tk
from PIL import Image, ImageTk
from ui import SpotifyDownloaderApp
import sys

class TestSpotifyDownloaderApp(unittest.TestCase):
    def setUp(self):
        """set up the tests
        Driver: Javaughn
        Navigator: Tommy"""
        self.root = tk.Tk()

    def tearDown(self):
        """after each test case, destory the environment"""
        self.root.destroy()

    @patch('subprocess.run')
    def test_run_app_py(self, mock_subprocess_run):
        """test run app.py. verifies app calls subprocess run
        Driver: Beka
        Navigator: Tommy"""
        app = SpotifyDownloaderApp(self.root)
        app.run_app_py()
        mock_subprocess_run.assert_called_once_with([sys.executable, "app.py"], check=True)

    @patch('subprocess.run')
    def test_run_logic_py(self, mock_subprocess_run):
        """test run logic. verifies playlist logic was made
        Driver: Javaughn
        Navigator: Tommy"""
        app = SpotifyDownloaderApp(self.root)
        app.run_logic_py()
        mock_subprocess_run.assert_called_once_with([sys.executable, "logic.py"], check=True)

    def test_create_button(self):
        """test run create button. verifies buttons were made
        Driver: Beka
        Navigator: Tommy"""
        app = SpotifyDownloaderApp(self.root)
        parent = tk.Frame(self.root)

        # Use 'spotify_icon.png' for the first button
        button1 = app.create_button(parent, "spotify_icon.png", lambda: None, "Spotify Button")
        self.assertTrue(button1.image is not None)

        # Use 'mnotes.jpeg' for the second button
        button2 = app.create_button(parent, "mnotes.jpeg", lambda: None, "MNotes Button")
        self.assertTrue(button2.image is not None)

    # Add more test cases as needed for other aspects of the class

if __name__ == "__main__":
    unittest.main()
