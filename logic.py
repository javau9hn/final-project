import csv
import random

# Load CSV file
file_path = 'songs.csv'  

# Function to load data from CSV
def load_data(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            data.append(row)
    return data

# Function to filter songs by genre
def get_songs_by_genre(songs, selected_genre):
    filtered_songs = []
    for song in songs:
        if selected_genre in eval(song[1]):
            filtered_songs.append(song[0])
    return filtered_songs

# Load data from CSV
songs_data = load_data(file_path)

# Initialize variables
playlist = []
min_songs = 5

while len(playlist) < min_songs:
    # Select a random song
    random_song = random.choice(songs_data)
    random_genres = eval(random_song[1])

    # Select a random genre from the random song
    selected_genre = random.choice(random_genres)

    # Get songs that share the selected genre
    playlist = get_songs_by_genre(songs_data, selected_genre)

    # Remove the randomly selected song from the playlist
    if random_song[0] in playlist:
        playlist.remove(random_song[0])

    # Check if there are enough songs with the selected genre
    if len(playlist) >= min_songs:
        playlist = random.sample(playlist, min_songs)
        break

# Display the playlist
if len(playlist) >= min_songs:
    print("Generated Playlist:")
    for index, song in enumerate(playlist, start=1):
        print(f"{index}. {song}")
else:
    print(f"Not enough songs with the selected genre after trying multiple genres.")