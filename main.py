import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
moviesHTML = response.text


def listToString(s):
    emptyString = ' '
    return emptyString.join(s)


soup = BeautifulSoup(moviesHTML, "html.parser")
movies = soup.find_all(name="h3", class_="title")
listMovie = []
for movie in movies:
    listMovie.append(movie.getText())

newListMovie = []
for movie in listMovie:
    temp = movie.split()
    newListMovie.append(temp)


for movie in newListMovie:
    temp = movie.pop(0)

finalListMovie = []
for movie in newListMovie:
    temp = listToString(movie)
    finalListMovie.append(temp)

print(finalListMovie)

with open("movies.txt", "a") as file:
    count = 1
    for movie in finalListMovie:
        emptyString = f"{count}) {movie}\n"
        file.write(emptyString)
        count += 1



