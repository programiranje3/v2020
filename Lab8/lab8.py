#
# The task is to write a Python program (script) that determines which countries
# gave the largest number of athletes who are considered to be among the 100 greatest
# sport stars ever.
# To that end, the program should do the following:
# - collect names of the "100 Greatest Sport Stars Ever" from:
#   https://ivansmith.co.uk/?page_id=475
# - for each athlete, determine his/her country of birth by scraping the relevant
#   data (birthplace) from his/her Wikipedia page
# - stores the data about athletes and their country of origin in a json file
# - prints a sorted list of identified countries and for each country, the number
#   of greatest athletes it gave
#
# Note: to retrieve web page content, we will use the *requests* library
# Quick start guide is available at: https://requests.readthedocs.io/en/master/user/quickstart/
#
# Documentation for BeautifulSoup is available at:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/


import json
from pathlib import Path
from sys import stderr
import requests
from bs4 import BeautifulSoup


def get_content_from_url(url):
    '''
        Returns the content of the web page with the given URL or None
        if the page content cannot be retrieved
    '''

    def response_OK(r):
        contet_type = r.headers['content-type']
        return (r.status_code == requests.codes.ok) and contet_type and ('html' in contet_type)

    try:
        with requests.get(url, headers={'User-Agent':'P3_FON'}) as response:
            return response.text if response_OK(response) else None
    except requests.RequestException as rerr:
        stderr.write(f"An error occurred while tryng to retrieve page from {url}:\n{rerr}\n")
        return None


def get_str_from_element(element):
    if element.string:
        return element.string.strip()

    if element.strings:
        return " ".join(s for s in element.stripped_strings)

    return ""


def get_athletes_names(url):
    '''
        Retrieves the web page with a list of top athletes
        and returns a list of the athletes' names
    '''

    names = list()

    web_page = get_content_from_url(url)
    if web_page is None:
        stderr.write(f"Cannot retrieve data from {url}. Cannot proceed!\n")
        return names

    page_soup = BeautifulSoup(web_page, 'html.parser')
    if page_soup is None:
        stderr.write(f"Cannot parse page from {url}. Cannot proceed!\n")
        return names

    olist = page_soup.find('ol')
    for litem in olist.find_all('li'):
        strong = litem.find('strong')
        strong_str = get_str_from_element(strong)
        if strong_str != "":
            names.append(strong_str)

    return names


def extract_country_of_origin(element):

    def is_reference(s):
        return (len(s) >= 3) and (s[0]=='[') and (s[-1] ==']')

    if element.string:
        return element.string.rsplit(',', maxsplit=1)[-1].lstrip()

    if element.strings:
        born_str = " ".join([s for s in element.stripped_strings if not is_reference(s)])
        return born_str.rsplit(',', maxsplit=1)[-1].lstrip()

    return None


def is_disambiguation_page(page_soup):
    return page_soup.find(name='table', id="disambigbox") is not None


def retrieve_country_of_origin(name):
    '''
        Receives the full name of an athlete.
        Returns the country of birth of the athlete extracted from his/her
        Wikipedia page (or None if the information is not available).
    '''

    url = f"https://en.wikipedia.org/wiki/{name.replace(' ', '_')}"
    wiki_page = get_content_from_url(url)
    if wiki_page is None:
        stderr.write(f"Cannot retrieve Wikipedia page for {name}\n")
        return None

    wiki_soup = BeautifulSoup(wiki_page, 'html.parser')
    if wiki_soup is None:
        stderr.write(f"Cannot parse Wikipedia page for {name}\n")
        return None

    info_table = wiki_soup.find(name='table', class_=lambda val: ('infobox' in val) and ('vcard' in val))
    if info_table is None:
        if is_disambiguation_page(wiki_soup):
            print(f"Reached disambiguation page for {name}")
        return None

    th_born = info_table.find(name='th', string=lambda val: val and (val.startswith('Born') or val=='Place of birth'))
    if th_born:
        td_born = th_born.find_next_sibling(name='td')
        if td_born:
            return extract_country_of_origin(td_born)

    bold_born = info_table.find(name='b', string=lambda val: val and val.startswith('Born'))
    if bold_born:
        td_born = bold_born.find_parent(name='td')
        if td_born:
            return extract_country_of_origin(td_born)

    print(f"Could not retrieve country for {name}")
    return None


def collect_athletes_data(athletes_url):
    '''
        The function puts several parts together:
        - obtains a list of athletes' names
        - iterates over the list of (cleaned) names to retrieve the country
        for each athlete by 'consulting' his/her Wikipedia page
        - stores the collected data in a json file
        - prints names of athletes whose birthplace data could not have
        been collected
    '''

    # print("Putting together a list of athletes' names...")
    # athletes_names = get_athletes_names(athletes_url)
    # print('...done')
    # print(f'Gathered names for {len(athletes_names)} athletes.')

    # Store athletes' names so that we do not pull the content from page each time
    # the program runs
    # try:
    #     with open(Path.cwd() / 'athletes_names.txt', 'w') as fobj:
    #         for name in athletes_names:
    #             fobj.write(name + "\n")
    # except OSError as err:
    #     stderr.write(f"An error occurred while writing athletes' names to file:\n{err}\n")

    athletes_names = list()
    try:
        with open(Path.cwd() / 'athletes_names.txt', 'r') as fobj:
            for line in fobj.readlines():
                athletes_names.append(line.rstrip('\n'))
    except OSError as err:
        stderr.write(f"An error occurred while reading athletes' names from file:\n{err}\n")


    print("\nCollecting data about the athletes' country origins...")
    athletes_dict = dict()
    not_found = list()
    for name in athletes_names:
        country = retrieve_country_of_origin(name)
        if country:
            athletes_dict[name] = country
        else:
            not_found.append(name)
    print('...done')

    for athlete, origin in athletes_dict.items():
        print(f"{athlete}: {origin}")
    #
    # with open(Path.cwd() / "athletes.json", "w") as jsonf:
    #     json.dump(athletes_dict, jsonf, indent=4)
    #
    # print(f"\nInformation about country of origin was not found for the following {len(not_found)} athletes:")
    # print(", ".join(not_found))


def create_country_labels_mapping():
    '''
        Creates a mapping between a country and different ways it was referred to
        in the collected data.
        :returns a dictionary with countries as the keys and the different terms used
        to refer to them as values
    '''
    country_lbls_dict = dict()

    country_lbls_dict['USA'] = ['California', 'New York', 'United States', 'Florida', 'Oklahoma', 'US', 'U.S.',
                                'Pennsylvania', 'Ohio', 'Mississippi', 'Alabama', 'Indian Territory', 'Maryland']
    country_lbls_dict['Germany'] = ['West Germany']
    country_lbls_dict['Australia'] = ['Victoria', 'Western Australia', 'New South Wales']
    country_lbls_dict['UK'] = ['England', 'UK', 'British Leeward Islands', 'United Kingdom']

    return country_lbls_dict



def most_represented_countries():
    '''
        Creates and prints a list of countries based on how well they
        are represented in the collected athletes data.
    '''

    



if __name__ == '__main__':

    top_athletes_url = 'https://ivansmith.co.uk/?page_id=475'
    collect_athletes_data(top_athletes_url)
    # most_represented_countries()
