import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    "imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres"
)

search = input("What movie do you want to search for? ")
url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search)

resp = requests.get(url)
resp.raise_for_status()

movie_data = resp.json()
movie_list = movie_data.get('hits')

# movies = []
# for md in movie_list:
#     m = MovieResult(
#         imdb_code=md.get('imdb_code'),
#         title=md.get('title'),
#         duration=md.get('duration'),
#         director=md.get('director'),
#         year=md.get('year', 0.0),
#         rating=md.get('rating', 0.0),
#         imdb_score=md.get('imdb_score', 0.0),
#         keywords=md.get('keywords'),
#         genres=md.get('genres'),
#     )
#     movies.append(m)

# movies = []
# for md in movie_list:
#     # use keyword argument shortcut ** if keywords exactly match up with the keys
#     m = MovieResult(**md)
#     movies.append(m)

# meand the same thing as the above blocks of code
movies = [
    MovieResult(**md)
    for md in movie_list
]

for m in movies:
    print("{} -- {}".format(m.year, m.title))
