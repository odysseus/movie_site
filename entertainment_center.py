from media import Movie
from fresh_tomatoes import open_movies_page

def generate_and_run():
    codes = {
            "The Martian": "tt3659388",
            "Star Wars VII": "tt2488496",
            "Mad Max: Fury Road": "tt1392190",
            "Hunger Games: Catching Fire": "tt1951264"
            }

    movies = []
    for k, v in codes.iteritems():
        movies.append(Movie.from_code(v))

    open_movies_page(movies)
