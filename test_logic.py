import random
import unittest
from unittest.mock import patch
import logic  
import ast  

class TestSpotifyPlaylistGenerator(unittest.TestCase):

    def test_load_data(self):

        test_data = [["Song1", "['Pop', 'Rock']"], ["Song2", "['Jazz']"]]
        with patch('builtins.open', unittest.mock.mock_open(read_data="Name,Genres\nSong1,['Pop', 'Rock']\nSong2,['Jazz']")):
            data = logic.load_data("dummy_path.csv")
            formatted_data = [[row[0], str(ast.literal_eval(row[1]))] for row in data]
            self.assertEqual(formatted_data, test_data)

    def test_get_songs_by_genre(self):
        test_songs = [["Song1", "['Pop', 'Rock']"], ["Song2", "['Jazz']"]]
        expected_songs = ["Song1"]
        filtered_songs = logic.get_songs_by_genre(test_songs, 'Pop')
        self.assertEqual(filtered_songs, expected_songs)

    @patch('random.choice')
    @patch('random.shuffle')
    def test_playlist_generation_conditions(self, mock_shuffle, mock_choice):
        test_songs = [["Song1", "['Pop', 'Rock']"], ["Song2", "['Jazz', 'Blues']"], ["Song3", "[]"]]
        def choice_side_effect(seq):
            if seq:
                return seq[0]
            raise StopIteration
        mock_choice.side_effect = choice_side_effect
        mock_shuffle.side_effect = lambda x: x.reverse()  

        logic.songs_data = test_songs.copy()
        logic.playlist = []
        logic.min_songs = 1
        while len(logic.playlist) < logic.min_songs:
            if not logic.songs_data:
                break

            logic.songs_data.append(logic.songs_data.pop(0))  

            try:
                random_genres = ast.literal_eval(logic.songs_data[-1][1])
            except (ValueError, SyntaxError):
                continue

            if not random_genres:
                continue

            selected_genre = mock_choice(random_genres)
            logic.playlist.extend(song for song in logic.get_songs_by_genre(logic.songs_data, selected_genre) 
                                  if song != logic.songs_data[-1][0] and song not in logic.playlist)

            if len(logic.playlist) >= logic.min_songs:
                random.shuffle(logic.playlist)
                logic.playlist = logic.playlist[:logic.min_songs]
                break

        self.assertTrue(len(logic.playlist) >= logic.min_songs)

if __name__ == '__main__':
    unittest.main()
