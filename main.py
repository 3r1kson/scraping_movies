import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
movies_response = response.text

soup = BeautifulSoup(movies_response, "html.parser")
list = [i.getText() for i in
             soup.find_all(name="h3", class_="title")]
list.reverse() # or list[::-1]

with open("movies.txt", mode="a") as file:
    for i in list:
        file.writelines(i + "\n")
