import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys
from PIL import Image
import os

def run_app_py():
    try:
        subprocess.run([sys.executable, "app.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running app.py: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def run_logic_py():
    try:
        subprocess.run([sys.executable, "logic.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running logic.py: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def create_button(parent, image_file, command):
    image = Image.open(image_file)
    photo = ImageTk.PhotoImage(image)
    button = tk.Button(parent, image=photo, command=command)
    button.image = photo  # To prevent image garbage collection
    return button

def main():
    root = tk.Tk()
    root.title("Spotify Web Downloader")
    root.geometry("800x500")

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    spotify_icon_button = create_button(frame, "spotify_icon.png", run_app_py)
    spotify_icon_button.pack(side=tk.LEFT, padx=10)

    mnotes_icon_button = create_button(frame, "mnotes.jpeg", run_logic_py)
    mnotes_icon_button.pack(side=tk.RIGHT, padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()