from lxml import html
from lxml import etree
import requests

class Movie(object):
    """Contains content used for displaying a single movie

    Attributes:
        title (str): Full title of the movie
        description (str): Description from IMDB
        poster_image_url (str/url): URL to cover art/poster image
        trailer_url (str/url): URL to trailer
    """

    def __init__(self):
        """All init properties should be changed after instantiation, defaults
        exist only to prevent null errors"""

        self.title = "Not found"
        self.description = "Not found"
        self.poster_image_url = "http://lmvoa.com/widget/image/placeholder.png"
        self.trailer_youtube_url = "https://www.youtube.com/embed/RDfjXj5EGqI"

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
        trailer_id = tree.xpath(trailer_xpath)[0].attrib['data-video']
        movie.trailer_url = "http://www.imdb.com/video/imdb/{trailer_id!s}/imdb/embed?autoplay=false&width=640".format(**locals())

        return movie

# Test Cases
martian = "tt3659388"
star_wars = "tt2488496"

mov = Movie.from_code(star_wars)

print mov.title
print mov.description
print mov.poster_image_url
print mov.trailer_url
