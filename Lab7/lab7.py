from pathlib import Path
from sys import stderr
import csv
import pickle
import shelve

#
# Task 1
#
# Write a function that reads in the content of the given text file, sorts it,
# and writes the (sorted) content to new textual files.
# Assume that the content of the given file consists of file names, some
# of which have an extension ('hello.txt'), others do not ('results').
# Each file name is given in a separate line.
# Sorting should be case insensitive and done in the ascending alphabetical
# order, as follows:
# - for files with extension: first based on the extension and then based
#   on the file name,
# - for files without extension, based on the file name.
# After sorting, file names with extension should be writen in one textual
# document (e.g., "task1_files_with_extension.txt") and file names without
# an extension in another text file (e.g. "task1_files_no_extension.txt")
# Include appropriate try except blocks to prevent program from crushing
# in case of a non existing file, or any other problem occurring while
# reading from / writing to a file.

# Use the file 'data/file_names_sample.txt'

def get_data_dir():
    data_dir = Path.cwd() / 'data'
    if not data_dir.exists(): data_dir.mkdir()
    return data_dir

def get_results_dir():
    results_dir = Path('results')
    results_dir.mkdir(exist_ok=True)
    return results_dir

def write_to_txt_file(data_sequence, fpath):

    try:
        with open(fpath, 'w') as fobj:
            for item in data_sequence:
                fobj.write(item + "\n")

    except OSError as err:
        stderr.write(f"Error ocurred while trying to write to file {fpath}:\n{err}\n")


def read_sort_write(fpath):

    def with_ext_sort_order(fname):
        name, ext = fname.rsplit('.', maxsplit=1)
        return ext.lower(), name.lower()

    with_ext = []
    no_ext = []

    try:
        with open(fpath, 'r') as fobj:
            for line in [l.rstrip() for l in fobj.readlines()]:
                if line.find('.') == -1:
                    no_ext.append(line)
                else:
                    with_ext.append(line)
    except FileNotFoundError:
        stderr.write(f"Error! File {fpath} does not exist! Cannot proceed!\n")
    except OSError as err:
        stderr.write(f"Error ocurred while trying to read from file {fpath}:\n{err}\n")
    else:
        no_ext.sort(key=lambda fname: fname.lower())
        with_ext.sort(key=with_ext_sort_order)

        write_to_txt_file(with_ext, get_results_dir() / 'task1_files_with_extension.txt')
        write_to_txt_file(no_ext, get_results_dir() / 'task1_files_no_extension.txt')



#
# Task 2
#
# The file cities_and_times.txt contains city names and time data.
# More precisely, each line contains the name of a city, followed by
# abbreviated weekday (e.g. "Sun"), and the time in the form "hh:mm".
# Read in the file and create an alphabetically ordered list of the form:
# [('Amsterdam', 'Sun', datetime.time(8, 52)),
# ('Anchorage', 'Sat', datetime.time(23, 52)), ...].
# Note that the hour and minute data are used to create an object of
# the type datetime.time.
# Having created this list:
# - serialise it in a file, as a list object (using the pickle module)
# - write its content into a csv file, in the format:
#   city; weekday; time
#   where time is represented in the format '%H:%M:%S'
# Include appropriate try except blocks to prevent program from crushing
# in the case of a non existing file, or a problem while reading from /
# writing to a file, or transforming data values.
#
# Note: for a list of things that can be pickled, see this page:
# https://docs.python.org/3/library/pickle.html#pickle-picklable
#
# Bonus 1: try using named tuple (collections.namedtuple) to represent and
# then manipulate the data read from the text file
#
# Bonus 2: in the "main section" ('__name__ == __main__'), use csv.DictReader
# to read in and print the content of the csv file

from collections import namedtuple

CityData = namedtuple('CityData', ('city', 'weekday', 'time'))

def serialise_obj_to_file(obj, fpath):

    try:
        with open(fpath, 'wb') as fobj:
            pickle.dump(obj, fobj)
    except pickle.PicklingError as perr:
        stderr.write(f"Error while serialising cities list to file {fpath}:\n{perr}\n")


def process_city_data(fpath):

    from datetime import time

    def write_to_csv(fpath):

        try:
            with open(fpath, 'w') as fobj:
                csv_writer = csv.writer(fobj, delimiter=';')
                csv_writer.writerow(CityData._fields)
                for city_data in cities_data:
                    csv_writer.writerow((city_data.city, city_data.weekday, time.strftime(city_data.time, "%H:%M:%S")))
        except csv.Error as csv_err:
            stderr.write(f"Error while writing city data to the csv file {fpath}:\n{csv_err}\n")

    cities_data = list()

    try:
        with open(fpath, 'r') as fobj:
            for line in [l.rstrip() for l in fobj.readlines()]:
                city, wday, t = line.rsplit(maxsplit=2)
                hour, min = t.split(':')
                try:
                    cd = CityData(city=city, weekday=wday, time=time(int(hour), int(min)))
                    cities_data.append(cd)
                except ValueError as verr:
                    stderr.write(f"An error occurred while trying to parse time data into int:\n{verr}\n")

    except FileNotFoundError:
        stderr.write(f"Error! File {fpath} does not exist! Cannot proceed!\n")
    except OSError as err:
        stderr.write(f"Error ocurred while trying to read from file {fpath}:\n{err}\n")
    else:
        cities_data.sort(key=lambda city_data: city_data.city.lower())

        serialise_obj_to_file(cities_data, get_results_dir() / 'task2_serialised_city_data.pkl')
        write_to_csv(get_results_dir() / 'task2_cities_data.csv')


#
# Task 3
#
# You are given a text file ('image_files_for_training.txt') that lists full file paths
# for a bunch of images (one image file path per line). Write a function that reads
# in the content of this text file and does the following:
# - counts the number of images in each category, and stores the computed
#   counts in a csv file in the format: category_name, image_count
# - creates and stores (in a file) a dictionary with the image category as
#   the key and a list of image names in the corresponding category as value;
#   for storage use 1) pickle and 2) shelve.
#
#
# Note: for a nice quick introduction to the shelve module, see: https://pymotw.com/3/shelve/
#
# Note 2: shelve.open function does not support pathlib.Path, so, a Path object has to be
# transformed to its string representation to be used with the shelve.open() function

def put_on_shelf(dict_obj, fpath):

    try:
        with shelve.open(fpath, 'c') as shelf:
            for item in dict_obj.items():
                key, val = item
                shelf[key] = val
    except OSError as err:
        stderr.write(f"An error occurred while storing dictionary in a shelve:\n{err}\n")


def process_image_files(fpath):

    from collections import defaultdict

    def write_dict_to_csv(fpath):

        try:
            with open(fpath, 'w') as fobj:
                csv_writer = csv.writer(fobj)
                csv_writer.writerow(('category', 'img_count'))
                for img_cat in img_categories.items():
                    cat_name, cat_files = img_cat
                    csv_writer.writerow((cat_name, len(cat_files)))
        except csv.Error as csv_err:
            stderr.write(f"An error occurred while writing image categorires dict to the csv file {fpath}:\n{csv_err}\n")


    img_categories = defaultdict(list)

    try:
        with open(fpath, 'r') as fobj:
            for line in (l.rstrip() for l in fobj.readlines()):
                the_rest, img_file = line.rsplit('/', maxsplit=1)
                _, category = the_rest.lstrip('/').split('/', maxsplit=1)
                category = category.replace('/', '_')

                img_categories[category].append(img_file)

    except FileNotFoundError:
        stderr.write(f"Error! File {fpath} does not exist! Cannot proceed!\n")
    except OSError as err:
        stderr.write(f"An error occurred while reading from file {fpath}:\n{err}\n")
    else:
        write_dict_to_csv(get_results_dir() / 'task3_category_counts.csv')
        serialise_obj_to_file(img_categories, get_results_dir() / 'task3_serialised_img_categoires.pkl')
        put_on_shelf(img_categories, str(get_results_dir() / 'task3_img_categories'))


#
# Task 4
#
# Write a function that receives two text files with lists of numbers (integers) in
# them (one number per line). The function identifies the numbers present in both
# lists and serialises them, as a (new) list of numbers, in a (new) file.
# Note: it may happen that not all lines in the input files contain numbers, so,
# after reading in the content of the files, assure that only numerical values are
# considered for comparison.
#
# To test the function use the files 'happy_numbers.txt' and 'prime_numbers.txt'
# available in the 'data' folder
#
# Note: based on this exercise:
# https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
#

def read_numbers_from_file(fpath):

    numbers = []

    try:
        with open(fpath, 'r') as fobj:
            for line in fobj.readlines():
                try:
                    numbers.append(int(line.rstrip()))
                except ValueError:
                    stderr.write(f"Could not parse '{line.rstrip()}' into an int - skipping this one\n")

    except FileNotFoundError:
        stderr.write(f"Error! File {fpath} does not exist! Cannot proceed!\n")
    except OSError as err:
        stderr.write(f"An exception occurred while reading from file {fpath}:\n{err}\n")
    finally:
        return numbers


def identify_shared_numbers(fpath1, fpath2):

    l1 = read_numbers_from_file(fpath1)
    l2 = read_numbers_from_file(fpath2)

    common_nums = [num for num in l1 if num in l2]
    serialise_obj_to_file(common_nums, get_results_dir() / 'task4_shared_numbers.pkl')



if __name__ == "__main__":

    # pass

    # Task 1:
    # read_sort_write(get_data_dir() / 'file_names_sample.txt')


    # Task 2:
    # process_city_data(get_data_dir() / "cities_and_times.txt")

    # with open(get_results_dir() / 'task2_serialised_city_data.pkl', 'rb') as fpkl:
    #     for data_item in pickle.load(fpkl):
    #         print(data_item)

    # with open(get_results_dir() / "task2_cities_data.csv") as fobj:
    #     data_as_dict_list = csv.DictReader(fobj, delimiter=';')
    #     for data_dict in data_as_dict_list:
    #         city, wday, t = data_dict.values()
    #         print(f"{city}, {wday}, {t}")


    # Task 3:
    # process_image_files(get_data_dir() / "image_files_for_training.txt")
    #
    # with open(get_results_dir() / 'task3_category_counts.csv', 'r') as csv_fobj:
    #     categories_data = csv.DictReader(csv_fobj)
    #     for category_data in categories_data:
    #         category, img_count = category_data.values()
    #         print(f"{category}: {img_count}")

    # Note: shelve.open function does not support pathlib.Path, so, we have to
    # transform the Path object to its string representation
    # with shelve.open(str(get_results_dir() / 'task3_img_categories'), 'r') as sf:
    #     for cat, img_list in sf.items():
    #         print(f"{cat}: " + ",".join(img_list))

    # with open(get_results_dir() / 'task3_serialised_img_categoires.pkl', 'rb') as fobj:
    #     loaded_data = pickle.load(fobj)
    #     for cat, img_list in loaded_data.items():
    #         print(f"{cat}: " + ",".join(img_list))


    # Task 4:
    t4_f1 = get_data_dir() / "prime_numbers.txt"
    t4_f2 = get_data_dir() / "happy_numbers.txt"
    identify_shared_numbers(t4_f1, t4_f2)

    with open(get_results_dir() / 'task4_shared_numbers.pkl', 'rb') as fobj:
        loaded_data = pickle.load(fobj)
        print(", ".join((str(num) for num in loaded_data)))