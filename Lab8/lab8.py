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


def get_content_from_url(url):
    '''
        Returns the content of the web page with the given URL or None
        if the page content cannot be retrieved
    '''




def get_athletes_names(url):
    '''
        Retrieves the web page with a list of top athletes
        and returns a list of the athletes' names
    '''





def retrieve_country_of_origin(name):
    '''
        Receives the full name of an athlete.
        Returns the country of birth of the athlete extracted from his/her
        Wikipedia page (or None if the information is not available).
    '''






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

    # athletes_names = list()
    # try:
    #     with open(Path.cwd() / 'athletes_names.txt', 'r') as fobj:
    #         for line in fobj.readlines():
    #             athletes_names.append(line.rstrip('\n'))
    # except OSError as err:
    #     stderr.write(f"An error occurred while reading athletes' names from file:\n{err}\n")
    #
    #
    # print("\nCollecting data about the athletes' country origins...")
    # athletes_dict = dict()
    # not_found = list()
    # for name in athletes_names:
    #     country = retrieve_country_of_origin(name)
    #     if country:
    #         athletes_dict[name] = country
    #     else:
    #         not_found.append(name)
    # print('...done')
    #
    # for athlete, origin in athletes_dict.items():
    #     print(f"{athlete}: {origin}")
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
    most_represented_countries()
