class Movie(object):
    """Contains content used for displaying a single movie

    Attributes:
        title (str): Full title of the movie
        poster_image_url (str/url): URL to image with cover art
        trailer_youtube_url (str/url): URL to YouTube trailer (*must* be YouTube)
    """

    def __init__(self):
        self.title = None
        self.poster_image_url = None
        self.trailer_youtube_url = None
