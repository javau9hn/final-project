import os
import requests
import random

# SoundCloud OAuth2 credentials
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'

# OAuth2 token request
def get_oauth_token():
    auth_url = 'https://api.soundcloud.com/oauth2/token'
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials',
    }
    
    response = requests.post(auth_url, data=data)
    
    if response.status_code == 200:
        token_data = response.json()
        return token_data['access_token']

# API request with OAuth2 token
def get_user_data(access_token):
    headers = {
        'Authorization': f'person {access_token}',
    }
    
    user_url = 'https://api.soundcloud.com/me'
    response = requests.get(user_url, headers=headers)
    
    if response.status_code == 200:
        user_data = response.json()
        return user_data

# Sample recommendation function (simplified)
def generate_recommendations(user_data):
    # In this simplified example, we randomly select tracks from user's liked tracks
    liked_tracks = user_data.get('track_likes', [])
    recommendations = random.sample(liked_tracks, min(5, len(liked_tracks)))
    return recommendations

if __name__ == '__main__':
    # Authenticate and obtain an access token
    access_token = get_oauth_token()
    
    if access_token:
        # Fetch user data using the access token
        user_data = get_user_data(access_token)
        
        if user_data:
            # Process and use the user data as needed
            print(f'User ID: {user_data["id"]}, Username: {user_data["username"]}')
            
            # Generate recommendations (simplified example)
            recommendations = generate_recommendations(user_data)
            
            if recommendations:
                print('Recommended Tracks:')
                for track in recommendations:
                    print(f'Track ID: {track["id"]}, Title: {track["title"]}, Artist: {track["user"]["username"]}')
