from scraping_music.classes.billboard import Billboard
from scraping_music.classes.spotipy_ import Spotipy

spotify = Spotipy()
spotify.auth()
billboard = Billboard()

def save_songs_spotify():
    user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    billboard.get_billboard_list(user_date)

    if len(billboard.songs_list) > 0:
        spotify.songs_list = billboard.songs_list
        spotify.search_song(user_date)

save_songs_spotify()