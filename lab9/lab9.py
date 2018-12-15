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
from sys import stderr

def get_content_from_url(url):
    '''
    Returns the content of the web page with the given URL
    '''

    def response_ok(r):
        # print(r.headers)
        content_type = r.headers['Content-Type']
        return (r.status_code == 200) and ('html' in content_type)

    with closing(requests.get(url)) as response:
        return response.text if response_ok(response) else None


def get_mathematicians_names(url):
    '''
    Retrieves the web page with a list of well known mathematicians
    and returns a list of the mathematicians' names
    '''

    names = []

    page_content = get_content_from_url(url)
    if page_content:
        page_soup = BeautifulSoup(page_content, 'html.parser')
        ol_tags = page_soup.find_all('ol')
        for ol_tag in ol_tags:
            a_tags = ol_tag.find_all('a')
            # for a_tag in a_tags:
            #     names.append(a_tag.text)
            names.extend([a_tag.text for a_tag in a_tags])

    else:
        stderr.write("Failed to retrieve mathematicians' names")

    return names


def get_pageview_counts(name):
    '''
    Receives the name of a mathematician (or, in general, of any person).
    Returns the number of hits (page views) that the
    mathematician's Wikipedia page received in the last 60 days,
    as an int value.
    '''

    def page_views_tag(tag):
        return (tag.name == 'a') and (tag.has_attr('href')) and \
               ('latest-60' in tag['href'])

    url = "https://xtools.wmflabs.org/articleinfo/en.wikipedia.org/" + name
    page_content = get_content_from_url(url)
    if page_content:
        page_soup = BeautifulSoup(page_content, 'html.parser')
        views_tag = page_soup.find(page_views_tag)
        if views_tag:
            views_count = views_tag.text.replace(',','')
            try:
                return int(views_count)
            except ValueError as val_err:
                stderr.write(str(val_err))
                return None

    stderr.write("Failed to retrieve page views for {}\n".format(name))
    return None


def clean_names(names):
    """
    The function is intended for dealing with the diversity of name formats
    (e.g. Hermann G. Grassmann, Hermann K. H. Weyl, M. E. Camille Jordan),
    that is, name formats that cannot be directly used for collecting page
    view stats. The names are 'cleaned' so that they consists of only
    name and surname.
    """
    cleaned_names = []
    for name in names:
        name_parts = [name_part for name_part in name.split() if '.' not in name_part]
        cleaned_names.append(" ".join(name_parts))
    return cleaned_names



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

    print("Collecting mathematicians' names...")
    mathematicians_url = "http://www.fabpedigree.com/james/greatmm.htm"
    names = get_mathematicians_names(mathematicians_url)
    print("...done")

    mathematicians = []
    no_result = []
    print("Collecting page views data ...")
    for name in names:
        page_views = get_pageview_counts(name)
        if page_views:
            mathematicians.append((name, page_views))
        else:
            no_result.append(name)

    cleaned_names = clean_names(no_result)
    no_result = []
    for name in cleaned_names:
        page_views = get_pageview_counts(name)
        if page_views:
            mathematicians.append((name, page_views))
        else:
            no_result.append(name)

    mathematicians = sorted(mathematicians, key=lambda item:item[1], reverse=True)

    top_mathematicians = mathematicians[:10] if len(mathematicians) > 10 else mathematicians
    print("Top mathematicians based on Wikipedia page views in the last 2 months:")
    for num, mathematican in enumerate(top_mathematicians):
        print("{}. {} with {} page views".format(num+1, *mathematican))



if __name__ == '__main__':

    find_most_popular_mathematicians()
    # mathematicians_url = "http://www.fabpedigree.com/james/greatmm.htm"
    # # print(get_mathematicians_names(mathematicians_url))
    # print(get_pageview_counts("Isaac Newton"))
