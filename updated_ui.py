import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
# Custom styling for the buttons
BUTTON_STYLE = {
    'font': ('Helvetica', 14),
    'borderwidth': '1',
    'relief': 'flat'
}

# You can adjust colors to your liking for a modern look
COLORS = {
    'background': '#333333',
    'foreground': '#FFFFFF',
    'button_background': '#5C6BC0',
    'button_foreground': '#FFFFFF',
    'button_hover': '#7986CB'
}


class Recommender:
    """
    This class represents a Soundcloud and Spotify Recommender application.


    Methods:
        create_button(parent, text, image, command=None): Create a styled button with text, image, and optional command.
        create_ui(): Create the user interface for the application.
        style_buttons(): Apply custom styling to buttons.

    """

    def __init__(self, root):
        """
        Initialize the Recommender class.

        Args:
            root (tk.Tk): The root window for the application.

        """
        self.root = root
        self.root.geometry("800x500")
        self.root.title("Soundcloud and Spotify Recommender")
        self.root.configure(bg=COLORS['background'])
        self.create_ui()

    def create_button(self, parent, text, image, command=None):
        """
        Create a styled button with text, image, and an optional command.

        Args:
            parent: The parent widget for the button.
            text (str): The text to display on the button.
            image: The image to display on the button.
            command: The function to be called when the button is clicked.     """

        button = ttk.Button(parent, text=text, image=image,
                            compound='top', command=command)
        button.image = image
        return button

    def create_ui(self):
        """
        Create the user interface for the application. Create our buttons for our generat playlist, spotify, and soundcloud

        """
        title_font = ("Helvetica", 16, "bold")
        welcome_msg = tk.Label(self.root, text="Welcome to our recommender! Hope you enjoy the playlist we make you!",
                               font=title_font, fg=COLORS['foreground'], bg=COLORS['background'])
        welcome_msg.pack(pady=20)

        button_frame = tk.Frame(self.root, bg=COLORS['background'])
        button_frame.pack(expand=True)

        music_icons = MusicIcons()

        playlist_icon = music_icons.playlist_icon()

        playlist_button = self.create_button(
            button_frame, "Generate Playlist After Logging In", playlist_icon, )
        playlist_button.pack(side="right", padx=10, pady=10)

        spotify_icon = music_icons.spotify_icon()

        spotify_button = self.create_button(
            button_frame, "Login to Spotify", spotify_icon, command=self.open_spotify)
        spotify_button.pack(side="left", padx=10, pady=10)

        soundcloud_icon = music_icons.soundcloud_icon()

        soundcloud_button = self.create_button(
            button_frame, "Login to SoundCloud", soundcloud_icon, command=self.open_soundcloud)
        soundcloud_button.pack(side="right", padx=10, pady=10)

        self.style_buttons()

    def open_spotify(self):
        webbrowser.open('https://accounts.spotify.com/en/login')

    def open_soundcloud(self):
        webbrowser.open('https://soundcloud.com/signin')

    def login_spotify(self):
        sp_oauth = SpotifyOAuth(
            '05df772d434d44e4bcdbd360a7b2b34f',
            'd97d683e553a4c948b9104a598676ad3',
            'http://localhost:8888/callback'
        )
        auth_url = sp_oauth.get_authorize_url()
        import webbrowser
        webbrowser.open(auth_url)

    def style_buttons(self):
        """
        Apply custom styling to the buttons.

        """
        style = ttk.Style(self.root)
        style.configure('TButton', **BUTTON_STYLE)
        style.map('TButton',
                  background=[('active', COLORS['button_hover'])],
                  foreground=[('active', COLORS['button_foreground'])])


class MusicIcons:
    """
    This class provides methods to load and create image icons for each button.

    Methods:
        load_image(image_name, size=(55, 55)): Load and resize an image.
        spotify_icon(): returns spotify icon
        soundcloud_icon(): returns soundcloud icon
        playlist_icon(): returns playlist icon

    """

    def load_image(self, image_name, size=(55, 55)):
        """
        Load and resize an image.

        Args:
            image_name (str): The name of the image file.
            size (tuple): The desired size for the image."""
        try:
            image = Image.open(image_name)
            # Use LANCZOS for antialiasing
            image = image.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(image)
        except FileNotFoundError:
            print(
                f"Error: The image '{image_name}' was not found. Please check the file's existence and path.")
            return None

    def spotify_icon(self):
        """
        Load and return the Spotify icon image.

        Returns:
            Spotify icon or none

        """
        return self.load_image("spotify_icon.png")

    def soundcloud_icon(self):
        """
        Load and return the SoundCloud icon image.

        Returns:
            Soundcloud icon or none

        """
        return self.load_image("Soundcloud-icon.png")

    def playlist_icon(self):
        """
        Load and return the playlist icon image.

        Returns:
            Playlist icon or none

        """
        return self.load_image("mnotes.jpeg")


def main():
    """
    Entry point of the application. Creates the root window and starts the Recommender.

    """
    root = tk.Tk()
    app = Recommender(root)
    root.mainloop()


if __name__ == "__main__":
    main()
