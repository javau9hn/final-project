import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys

class SpotifyDownloaderApp:
    def __init__(self, master):
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
        try:
            subprocess.run([sys.executable, "app.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running app.py: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def run_logic_py(self):
        try:
            subprocess.run([sys.executable, "logic.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running logic.py: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def create_button(self, parent, image_file, command, title):
        image = Image.open(image_file)
        photo = ImageTk.PhotoImage(image)
        button = tk.Button(parent, image=photo, command=command, compound=tk.TOP)
        button.image = photo
        button.title = title  # Set button title
        button.config(text=title, font=("Arial", 12))  # Set text on top of the button
        return button

def main():
    root = tk.Tk()
    app = SpotifyDownloaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()