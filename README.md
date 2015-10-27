# Fresh Tomatoes Movie Site Generator

To generate the site with your own movies first find the movie page on IMDB. The link should be something like this:

```
http://www.imdb.com/title/tt3659388/?ref_=fn_al_tt_1
```

The component we want is the `tt_______`

The movie codes go in the `code` dictionary contained in `main.py`. An example of a completed `code` dictionary:

```python
codes = {
        "The Martian": "tt3659388",
        "Star Wars VII": "tt2488496",
        "Mad Max: Fury Road": "tt1392190",
        "Hunger Games: Catching Fire": "tt1951264",
        "The Imitation Game": "tt2084970",
        "The Grand Budapest Hotel": "tt2278388"
        }
```

The name keys in this dictionary exist solely for the programmer, to make keeping track of, adding, and removing movies easier. You should use something that identifies the movie, but it doesn't have to be perfect. For the actual page content the program will use the title scraped from IMDB.

Once all the movies you want have been added, run the `main.py` file which will generate and open the site.
