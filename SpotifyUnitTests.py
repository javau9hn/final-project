import spotipy
import unittest
from unittest.mock import patch
from io import StringIO
from spotifyAPIConnect import (
    initialize_spotify_oauth,
    authenticate_with_spotify,
    create_spotify_client,
    retrieve_user_playlists,
    get_songs_in_playlists,
)

class TestMySpotifyProgram(unittest.TestCase):

    
    def test_initialize_spotify_oauth(self, mock_spotify_oauth, mock_input):
        # Test if initialize_spotify_oauth returns a SpotifyOAuth instance
        client_id = 'YOUR_CLIENT_ID'
        client_secret = 'YOUR_CLIENT_SECRET'
        redirect_uri = 'YOUR_REDIRECT_URI'
        scope = 'user-library-read playlist-read-private'

        sp_oauth = initialize_spotify_oauth(client_id, client_secret, redirect_uri, scope)
        self.assertIsInstance(sp_oauth, mock_spotify_oauth)

    
    def test_authenticate_with_spotify(self, mock_spotify_oauth):
        sp_oauth = mock_spotify_oauth.return_value
        sp_oauth.get_cached_token.return_value = False
        auth_url = 'mocked_auth_url'

        with patch('builtins.input', return_value='mocked_response'), patch('builtins.print') as mock_print:
            authenticate_with_spotify(sp_oauth)
            sp_oauth.get_authorize_url.assert_called_once()
            mock_print.assert_called_with(f'Please visit this URL to authorize the application: {auth_url}')

    
    def test_create_spotify_client(self, mock_spotify_oauth):
        sp_oauth = mock_spotify_oauth.return_value
        mock_spotify_client = spotipy.Spotify
        sp = create_spotify_client(sp_oauth)
        self.assertIsInstance(sp, mock_spotify_client)

    
    def test_retrieve_user_playlists(self, mock_spotify):
        sp = mock_spotify.return_value
        mock_playlists = {'items': [{'id': '123', 'name': 'Playlist 1'}, {'id': '456', 'name': 'Playlist 2'}]}
        sp.current_user_playlists.return_value = mock_playlists
        playlists = retrieve_user_playlists(sp)
        self.assertEqual(playlists, mock_playlists)


if __name__ == '__main__':
    unittest.main()