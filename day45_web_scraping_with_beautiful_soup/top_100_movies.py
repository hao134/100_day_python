from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_web_page = response.text

soup = BeautifulSoup(movie_web_page, "html.parser")
print(soup.title)

all_movies = soup.find_all(name="h3", class_="title")

with open("top_100_movies.txt","w") as f:
    for movie in all_movies[::-1]:
        f.write(movie.getText()+"\n")
# print(all_movies)