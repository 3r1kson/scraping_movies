import os
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from dotenv import load_dotenv
from scraping_music.classes.billboard import Billboard

load_dotenv()

class Spotipy(Billboard):
    def __init__(self):
        super().__init__()
        self.client_id = os.getenv("spotify_client_id")
        self.client_secret = os.getenv("spotify_client_secret")
        self.authentication = ""
        self.spotify_id = ""
        self.songs_uri = []
        self.playlist_id = ""

    def auth(self):
        self.authentication = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri="http://example.com",
                client_id=self.client_id,
                client_secret=self.client_secret,
                show_dialog=True,
                cache_path="token.txt",
                username="Erikson",
                )
            )
        self.spotify_id = self.authentication.current_user()['id']

    def search_song(self, date):
        self.create_playlist(date)
        year = date.split("-")[0]
        for song in self.songs_list:
            result = self.authentication.search(q=f"track:{song} year:{year}", type="track")
            try:
                self.songs_uri.append(result["tracks"]["items"][0]["uri"])
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")

        self.save_songs_playlist()

    def create_playlist(self, date):
        playlist = self.authentication.user_playlist_create(user=self.spotify_id, name=f"{date} Billboard 100", public=False)
        self.playlist_id = playlist["id"]

    def save_songs_playlist(self):
        try:
            self.authentication.playlist_add_items(playlist_id=self.playlist_id, items=self.songs_uri)
        finally:
            print("- List saved on Spotify")