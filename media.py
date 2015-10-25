from lxml import html
from lxml import etree
import requests

class Movie(object):
    """Contains content used for displaying a single movie

    Attributes:
        title (str): Full title of the movie
        description (str): Description from IMDB
        poster_image_url (str/url): URL to cover art/poster image
        trailer_id (str/url): IMDB Video ID
    """

    def __init__(self):
        self.title = "Not found"
        self.description = "Not found"
        self.poster_image_url = None
        self.trailer_id = None

    @classmethod
    def from_code(cls, imdb_code):
        """Using an imdb movie code (eg. tt3659388) this pulls the xml,
        scrapes the relevant data, and returns a new Movie instance using it"""

        imdb_url = "http://www.imdb.com/title/"
        movie_url = imdb_url + imdb_code

        # Fetch the page and generate lxml tree
        page = requests.get(movie_url)
        tree = html.fromstring(page.text)

        movie = Movie()

        # Title
        title_xpath = '//*[@id="overview-top"]/h1/span[1]//text()'
        movie.title = tree.xpath(title_xpath)[0]

        # Description
        description_xpath = '//*[@id="overview-top"]/p[2]'
        description_tree = tree.xpath(description_xpath)[0]
        etree.strip_tags(description_tree, 'a')
        movie.description = description_tree.text

        # Poster URL
        poster_xpath = '//*[@id="img_primary"]/div[1]/a/img'
        movie.poster_image_url = tree.xpath(poster_xpath)[0].attrib['src']

        # Trailer URL
        trailer_xpath = '//*[@id="overview-bottom"]/a'
        movie.trailer_id = tree.xpath(trailer_xpath)[0].attrib['data-video']

        return movie

