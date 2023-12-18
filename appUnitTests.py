import unittest
from unittest.mock import MagicMock
from app import app, create_spotify_oauth

class TestSpotifyApp(unittest.TestCase):
    """Unit tests for the Spotify Flask app."""

    def setUp(self):
        """Set up test environment.
        Driver: Tommy
        Navigator: Beka
        """
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        """Tear down test environment.
        Driver: Tommy
        Navigator: Javaughn"""
        pass

    def test_login_redirects_to_spotify(self):
        """Test if the login endpoint redirects to Spotify's authorization page.
        Driver: Tommy
        Navigator: Javaughn
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)  
        self.assertIn('accounts.spotify.com', response.headers['Location'])  

    def test_authorize_redirects_to_get_tracks(self):
        """Test if the authorize endpoint redirects to the getTracks endpoint after authorization.
        Driver: Tommy
        Navigator: Beka
        """
        with app.test_request_context('/authorize?code=mock_code'):
            response = self.app.get('/authorize')
            self.assertEqual(response.status_code, 302)  
            self.assertEqual(response.headers['Location'], '/getTracks')  

    def test_logout_clears_session(self):
        """Test if the logout endpoint clears the session.
        Driver: Tommy
        Navigator: Javaughn
        """
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['some_key'] = 'some_value'
            client.get('/logout')
            with client.session_transaction() as sess:
                self.assertNotIn('some_key', sess)  

   

if __name__ == '__main__':
    unittest.main()