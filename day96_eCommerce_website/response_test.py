import requests

api_key = "f23630e371240007466edc8cb63276a5"
parameters = {
    "query":"the Matrix",
    "api_key":api_key,
}

#response = requests.get("https://api.themoviedb.org/3/search/movie/discover/movie?sort_by=popularity.desc", params = parameters)
response = requests.get("https://api.themoviedb.org/3/search/movie", params=parameters)
print(response.raise_for_status())
movie_data = response.json()
print(len(movie_data["results"]))
# for data in movie_data["results"]:
#     print(f"{data['original_title']}-{data['release_date']}")

# parameters2 = {
#     "api_key": api_key,
#     "language": "en-US"
# }
# response2 = requests.get("https://api.themoviedb.org/3/movie/603",params=parameters2)
# movie_data2 = response2.json()
# print(movie_data2)
# print(movie_data2["release_date"][:4])
# print(movie_data2["title"])
# img_url = "https://image.tmdb.org/t/p/w500" +  movie_data2["poster_path"]
# print(img_url)
# print(movie_data2["overview"])