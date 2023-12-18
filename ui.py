import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys

class SpotifyDownloaderApp:
    """
    GUI Application for downloading
    Driver: Javaughn
    Navigator: Tommy
    Class creates a windows with buttons

    Attributes:
        master(tk): The main window of the application
    """
    def __init__(self, master):
        """
        Initialize application with a main window
        Driver: Beka
        Navigator: Tommy

        Attributes: 
            master(tk): The main window of the application
        """
        self.master = master
        master.title("Spotify Web Downloader")
        master.geometry("300x200")

        frame = tk.Frame(master)
        frame.pack(padx=20, pady=20)

        spotify_icon_button = self.create_button(frame, "spotify_icon.png", self.run_app_py, "Log into Spotify")
        spotify_icon_button.pack(side=tk.LEFT, padx=10)

        mnotes_icon_button = self.create_button(frame, "mnotes.jpeg", self.run_logic_py, "Generate Playlist")
        mnotes_icon_button.pack(side=tk.RIGHT, padx=10)

    def run_app_py(self):
        """
        Run the app.py file - Spotify login
        Driver: Mitch
        Navigator: Beka

        Handles and prints errors
        """
        try:
            subprocess.run([sys.executable, "app.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running app.py: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def run_logic_py(self):
        """
        Run the logic.py file - Generates Playlist
        Driver: Beka
        Navigator Tommy

        Prints any errors that occur
        """
        try:
            subprocess.run([sys.executable, "logic.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running logic.py: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def create_button(self, parent, image_file, command, title):
        """
        Create a button with an image and text
        Driver: Javaughn
        Navigator: Tommy

        Returns:
            tk.Button - the created button widget
        """
        image = Image.open(image_file)
        photo = ImageTk.PhotoImage(image)
        button = tk.Button(parent, image=photo, command=command, compound=tk.TOP)
        button.image = photo
        button.title = title  # Set button title
        button.config(text=title, font=("Arial", 12))  # Set text on top of the button
        return button

def main():
    """
    Main function to start the application

    Creates the main application window
    """
    root = tk.Tk()
    app = SpotifyDownloaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
