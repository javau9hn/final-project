import csv
import random
import pandas as pd

def load_data(file_path):
    """Loads data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: List of data from the CSV file.

    Driver: Mitch
    Navagator: Tommy
    """
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for row in reader:
            data.append(row)
    return data

def get_songs_by_genre(songs, selected_genre):
    """Filters songs by a selected genre.

    Args:
        songs (list): List of songs data.
        selected_genre (str): The selected genre to filter by.

    Returns:
        list: Filtered songs by the selected genre.

    Driver: Tommy
    Navagator: Mitch
    """
    filtered_songs = []
    for song in songs:
        if selected_genre in eval(song[1]):
            filtered_songs.append(song[0])
    return filtered_songs

def list_to_csv(data_list):
    """Writes a list to a CSV file.

    Args:
        data_list (list): The list to be written to the CSV file.

    Returns:
        str: Message indicating success or failure.
    """
    filename = 'NewPlaylist.csv'
    try:
        df = pd.DataFrame(data_list)
        df.to_csv(filename, index=False)
        return f"CSV file '{filename}' created successfully!"
    except Exception as e:
        return f"Failed to create CSV file: {str(e)}"

def main():
    
    file_path = 'songs.csv'  
    songs_data = load_data(file_path)
    playlist = []
    min_songs = 5

    while len(playlist) < min_songs:
        random_song = random.choice(songs_data)
        random_genres = eval(random_song[1])

        selected_genre = random.choice(random_genres)

        while (selected_genre == None):
            selected_genre = random.choice(random_genres)

        playlist = get_songs_by_genre(songs_data, selected_genre)

        if random_song[0] in playlist:
            playlist.remove(random_song[0])

        if len(playlist) >= min_songs:
            playlist = random.sample(playlist, min_songs)
            break

    if len(playlist) >= min_songs:
        list_to_csv(playlist)
    else:
        print(f"Not enough songs with the selected genre after trying multiple genres.")

if __name__ == '__main__':
    main()