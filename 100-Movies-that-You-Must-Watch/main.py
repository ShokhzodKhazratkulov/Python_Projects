import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
response.raise_for_status()
web_html = response.text

soup = BeautifulSoup(web_html, "html.parser")
all_titles = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
formatted_title_list = [title.getText() for title in all_titles[::-1]]
# print(formatted_title_list)
with open("Top 100 best movies.txt", mode="w") as data_file:
    for i in formatted_title_list:
        data = data_file.write(f"{i}\n")




