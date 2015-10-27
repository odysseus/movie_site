from media import Movie


def generate_movies(codes):
    """Takes a dictionary of IMDB movie codes, generates their associated movie
    objects and generates the Fresh Tomatoes site with that data.

    Args:
        codes (dict): A dictionary of codes with the following format
            "Movie Name": "imdb_code",
            "The Martian": "tt3659388"

    Returns:
        A list of movie objects
    """
    movies = []
    for k, v in codes.iteritems():
        movies.append(Movie.from_code(v))

    return movies
