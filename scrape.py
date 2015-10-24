from lxml import html
from lxml import etree
import requests

# URL prefix for movie pages
IMDB_URL = "http://www.imdb.com/title/"

# Test Cases
martian = "tt3659388"
star_wars = "tt2488496"

# Code for an individual movie
imdb_code = star_wars

movie_url = IMDB_URL + imdb_code

page = requests.get(movie_url)
tree = html.fromstring(page.text)

title_xpath = '//*[@id="overview-top"]/h1/span[1]//text()'
title = tree.xpath(title_xpath)[0]

description_xpath = '//*[@id="overview-top"]/p[2]'
description_tree = tree.xpath(description_xpath)[0]
etree.strip_tags(description_tree, 'a')
description = description_tree.text

poster_xpath = '//*[@id="img_primary"]/div[1]/a/img'
poster_url = tree.xpath(poster_xpath)[0].attrib['src']
