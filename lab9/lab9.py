# This task is based on the example from the "Practical Introduction to
# Web Scraping in Python" tutorial, available at:
# https://realpython.com/python-web-scraping-practical-introduction/

# The task is to write a Python program (script) that among the
# hundred greatest mathematicians of the past
# (http://www.fabpedigree.com/james/greatmm.htm)
# finds and prints 10 currently most popular mathematicians based
# on the level of attention they are receiving by the Web users.
# The popularity is approximated by the number of page views that
# the mathematicians' Wikipedia pages have received in the last 60 days;
# these (and many other) stats about Wikipedia pages can be obtained
# from the Wikipedia’s XTools (https://xtools.wmflabs.org/).

# Some useful links:
# - requests developer interface (aka API)
# http://docs.python-requests.org/en/master/api/
# - tutorial + documentation for BeautifulSoup:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc


import requests
from bs4 import BeautifulSoup
from contextlib import closing

def get_content_from_url(url):
    '''
    Returns the content of the web page with the given URL
    '''

    pass



def get_mathematicians_names(url):
    '''
    Retrieves the web page with a list of well known mathematicians
    and returns a list of the mathematicians' names
    '''

    pass



def get_pageview_counts(name):
    '''
    Receives the name of a mathematician (or, in general, of any person).
    Returns the number of hits (page views) that the
    mathematician's Wikipedia page received in the last 60 days,
    as an int value.
    '''

    pass



def clean_names(names):
    """
    The function is intended for dealing with the diversity of name formats
    (e.g. Hermann G. Grassmann, Hermann K. H. Weyl, M. E. Camille Jordan),
    that is, name formats that cannot be directly used for collecting page
    view stats. The names are 'cleaned' so that they consists of only
    name and surname.
    """
    pass



def find_most_popular_mathematicians():
    '''
    The function puts all parts together; namely, it
    - obtains a list of mathematicians' names
    - iterates over the list to get the number of 'hits'
    for each name
    - cleans the names that didn't get through and tries
    once again to obtain 'hits' for them
    - sorts the names by 'popularity' (hits)
    - prints top 10 based on the popularity
    - prints names for which hits could not have been pulled
    '''

    pass




if __name__ == '__main__':

    find_most_popular_mathematicians()

