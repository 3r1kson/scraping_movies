import requests

from bs4 import BeautifulSoup

class Billboard:
    def __init__(self):
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
        self.songs_list = []

    def get_billboard_list(self, date):
        try:
            response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}", headers=self.header)
            soup = BeautifulSoup(response.text, "html.parser")
            song_list = soup.select(selector="li ul li h3")
            self.songs_list = [song.getText().strip() for song in song_list]
        finally:
            return self.songs_list
