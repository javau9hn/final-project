import spotipy
from spotipy.oauth2 import SpotifyOAuth

def initialize_spotify_oauth(client_id, client_secret, redirect_uri, scope):
    """
    Initialize the Spotify OAuth2 client for user authorization.

    Parameters:
        - client_id (str): Your Spotify Developer App's client ID.
        - client_secret (str): Your Spotify Developer App's client secret.
        - redirect_uri (str): The redirect URI you've registered with your Spotify Developer App.
        - scope (str): The requested scopes for user authorization.

    Returns:
        SpotifyOAuth: The initialized SpotifyOAuth instance.
    """
    sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
    return sp_oauth

def authenticate_with_spotify(sp_oauth):
    """
    Check if a valid access token exists. If not, guide the user through the authorization process.

    Parameters:
        sp_oauth (SpotifyOAuth): The initialized SpotifyOAuth instance.
    """
    if not sp_oauth.get_cached_token():
        auth_url = sp_oauth.get_authorize_url()
        print(f'Please visit this URL to authorize the application: {auth_url}')
        response = input('Enter the URL you were redirected to: ')
        sp_oauth.token_info = sp_oauth.get_access_token(response)

def create_spotify_client(sp_oauth):
    """
    Create a Spotify client using the authorized access token.

    Parameters:
        sp_oauth (SpotifyOAuth): The initialized SpotifyOAuth instance.

    Returns:
        spotipy.Spotify: The initialized Spotify client.
    """
    sp = spotipy.Spotify(auth_manager=sp_oauth)
    return sp

def retrieve_user_playlists(sp):
    """
    Retrieve the playlists of the authenticated user.

    Parameters:
        sp (spotipy.Spotify): The initialized Spotify client.

    Returns:
        dict: User's playlists information.
    """
    playlists = sp.current_user_playlists()
    return playlists

def get_songs_in_playlists(sp, playlists):
    """
    Retrieve the songs in the specified playlists.

    Parameters:
        sp (spotipy.Spotify): The initialized Spotify client.
        playlists (list): List of playlists to retrieve songs from.

    Returns:
        list: List of songs in the playlists.
    """
    songs_in_playlists = []

    for playlist in playlists['items']:
        playlist_id = playlist['id']
        playlist_name = playlist['name']

        # Get the tracks from the playlist
        results = sp.playlist_tracks(playlist_id)
        tracks = results['items']

        for track in tracks:
            song = track['track']
            songs_in_playlists.append(f"{playlist_name} - {song['name']} by {', '.join([artist['name'] for artist in song['artists']])}")

    return songs_in_playlists

def main():
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    redirect_uri = 'YOUR_REDIRECT_URI'
    scope = 'user-library-read playlist-read-private'

    sp_oauth = initialize_spotify_oauth(client_id, client_secret, redirect_uri, scope)
    authenticate_with_spotify(sp_oauth)
    sp = create_spotify_client(sp_oauth)
    playlists = retrieve_user_playlists(sp)
    songs_in_playlists = get_songs_in_playlists(sp, playlists)

    for song in songs_in_playlists:
        print(song)

if __name__ == '__main__':
    main()