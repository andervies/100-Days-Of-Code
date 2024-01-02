import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

# with open("movies.txt", "w") as file:
movie_list = soup.find_all(name="div", class_="jsx-1913936986")
print(movie_list)







