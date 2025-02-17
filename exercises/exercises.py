from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/show")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
article_upvotes = soup.find_all("span", class_="score")
articles_data = [
    [i.getText(), i.a["href"], int(article_upvotes[idx].getText().replace(" points", ""))]
    for idx, i in enumerate(articles)]

max_votes_article = max(articles_data, key=lambda x: x[2])
print(max_votes_article)


# with open("website.html") as file:
#     for i in file:
#         contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
#
# all_anchor_tags = soup.find_all(name="a")
#
# h3_heading = soup.find_all("h3", class_="heading")
#
# company_url = soup.select_one(selector="p a")
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)