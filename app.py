#!/usr/bin/python3

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, url_for, session, request, redirect
import json
import time
import pandas as pd
import requests


"""A Flask app that interacts with the Spotify API to retrieve user's saved tracks and their respective genres.

Attributes:
    app (Flask): The Flask application.
"""
app = Flask(__name__)

app.secret_key = 'esfks'
app.config['SESSION_COOKIE_NAME'] = 'spotify-login-session'

@app.route('/')
def login():
    """Redirects the user to Spotify's authorization page for login."""
    
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    print(auth_url)
    return redirect(auth_url)



@app.route('/authorize')
def authorizePage():
    """Authorizes the user via Spotify OAuth and stores token information in the session."""
    sp_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session["token_info"] = token_info
    return redirect("/getTracks")

@app.route('/logout')
def logout():
    """Logs the user out by clearing the session."""
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')


@app.route('/getTracks')
def get_all_tracks():
    """Retrieves all of the user's saved tracks along with their respective genres and saves them to a CSV file."""
    session['token_info'], authorized = get_token()
    session.modified = True
    if not authorized:
        return redirect('/')
    sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))
    songNames = []
    songGenres = []
    iter = 0
    while True:
        offset = iter * 50
        iter += 1
        curGroup = sp.current_user_saved_tracks(limit=50, offset=offset)['items']
        for idx, item in enumerate(curGroup):
        
            track = item['track']
            songVal = track['name'] + " - " + track['artists'][0]['name']
            artistID = track['album']['artists'][0]['id']
            artist_info = sp.artist(artistID)['genres']

            songNames += [songVal]
            songGenres += [artist_info]
        if (len(curGroup) < 50):
            break
    


    df = pd.DataFrame({'song names': songNames, 'song genre': songGenres})
    df.to_csv('songs.csv', index=False)
    return "done"



def get_token():
    """Checks if the token is valid and refreshes it if expired.

    Returns:
        tuple: A tuple containing the token information and a boolean indicating if the token is valid.
    """
    token_valid = False
    token_info = session.get("token_info", {})

    # Checking if the session already has a token stored
    if not (session.get('token_info', False)):
        token_valid = False
        return token_info, token_valid

    # Checking if token has expired
    now = int(time.time())
    is_token_expired = session.get('token_info').get('expires_at') - now < 60

    # Refreshing token if it has expired
    if (is_token_expired):
        sp_oauth = create_spotify_oauth()
        token_info = sp_oauth.refresh_access_token(session.get('token_info').get('refresh_token'))

    token_valid = True
    return token_info, token_valid


def create_spotify_oauth():
    """Creates an instance of SpotifyOAuth for handling Spotify authorization.

    Returns:
        SpotifyOAuth: An instance of SpotifyOAuth.
    """

    return SpotifyOAuth(
            client_id="56d658f130c3412884d595d59ac0095d",
            client_secret="948fedf1fc4f4c1aa9d8847df9fcc641",
            redirect_uri=url_for('authorizePage', _external=True),
            scope="user-library-read")


    

if __name__ == '__main__':
    app.run(debug=True, port=8080)