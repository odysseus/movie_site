from entertainment_center import generate_movies
from fresh_tomatoes import open_movies_page

codes = {
        "The Martian": "tt3659388",
        "Star Wars VII": "tt2488496",
        "Mad Max: Fury Road": "tt1392190",
        "Hunger Games: Catching Fire": "tt1951264",
        "The Imitation Game": "tt2084970",
        "The Grand Budapest Hotel": "tt2278388"
        }


def main():
    """Taking the list of codes from above, generates the movie objects and uses
    those to generate the Fresh Tomatoes page"""
    movies = generate_movies(codes)
    open_movies_page(movies)


if __name__ == "__main__":
    main()
