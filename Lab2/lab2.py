# Task 1:
# Write a function that receives two lists and returns a list that contains
# only those elements (without duplicates) that appear in both input lists.

def common_elements(l1, l2):
    # Option 1
    # l3 = list()
    # for item in set(l1):
    #     if item in l2: l3.append(item)
    # return l3

    # Option 2
    return [item for item in set(l1) if item in l2]



# Task 2:
# Write a function that receives 2 lists of the same length and
# returns a new list obtained by concatenating the two input
# lists index-wise. Example:
# Input lists:
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# Output: ['My', 'name', 'is', 'Kelly']

def concat_index_wise(l1, l2):
    # Option 1
    # l3 = list()
    # for i in range(len(l1)):
    #     l3.append(l1[i] + l2[i])
    # return l3

    # Option 2
    return [l1_elem + l2_elem for l1_elem, l2_elem in zip(l1, l2)]



# Task 3:
# Write a function that checks and returns whether a given string is a pangram or not.
# Pangrams are sentences containing every letter of the alphabet at least once.
# (e.g.: "The quick brown fox jumps over the lazy dog")
#
# Hint: ascii_lowercase from the string module can be used to get all letters

def pangram(string):
    from string import ascii_lowercase
    # Option 1
    # for letter in ascii_lowercase:
    #     if letter not in string.lower():
    #         return False
    # return True

    # Option 2
    return all([(letter in string) for letter in ascii_lowercase])



# Task 4
# Write a function that receives a string with a mix of lower and upper case letters.
# The function arranges letters in such a way that all lowercase letters come first,
# followed by all upper case letters.
# The new,'rearranged' string is the function's return value.

def first_lower_then_upper(string):
    # Option 1
    # lowercase = []
    # uppercase = []
    # for ch in string:
    #     if ch.islower(): lowercase.append(ch)
    #     elif ch.isupper(): uppercase.append(ch)
    # all_letters = lowercase + uppercase
    # return "".join(all_letters)

    # Option 2
    # lowercase = [ch for ch in string if ch.islower()]
    # uppercase = [ch for ch in string if ch.isupper()]
    # return "".join(lowercase) + "".join(uppercase)

    # Option 3
    new_indices = [i for i, ch in enumerate(string) if ch.islower()]
    new_indices.extend([i for i, ch in enumerate(string) if ch.isupper()])
    return "".join([string[i] for i in new_indices])



# Task 5
# Write a function that receives a report (as a string) on the state (up / down) of several servers.
# Each line of the report refers to one server, and has the following format:
# "Server <server_name> is <up/down>"
# Note that some lines may be empty.
# The function should process the report and print:
# - the total number of servers mentioned in the report
# - the proportion of servers that are down
# - names of servers that are down.

def server_status(report):
    total = 0
    down_servers = []
    for line in [row.lstrip() for row in report.split('\n') if row.lstrip() != ""]:
        total += 1
        # Option 1
        # words = line.split()
        # if words[-1] == "down": down_servers.append(words[1])
        # Option 2
        _, server_name, _, status = line.split()
        if status == "down": down_servers.append(server_name)

    print(f"Total number of servers {total}")
    print(f"Proportion of down servers: {len(down_servers)/total}")
    print("Servers that are down:" + ", ".join(down_servers))



# Task 6:
# Write a function that receives an integer value (n) and
# generates and prints a dictionary with entries in the
# form x: (1 + 2 + ... + x), where x is a number between 1 and n.

def numeric_dict(n):
    d = {}
    for x in range(1, n+1):
        d[x] = sum(range(1, x+1))

    for key, val in d.items():
        print(f"{key}: {val}")


# Task 7:
# Write a function that receives a string as its input parameter, and
# calculates the number of digits, letters, and punctuation marks (.,!?;:)
# in this string.
# The function returns a dictionary with the computed values.

def string_stats(string):
    # Option 1
    # digits_cnt = 0
    # letters_cnt = 0
    # punct_cnt = 0
    # for ch in string:
    #     if ch.isdigit(): digits_cnt += 1
    #     elif ch.isalpha(): letters_cnt += 1
    #     elif ch in '?!,.:;': punct_cnt += 1
    # return {'digits': digits_cnt, 'letters': letters_cnt, 'punctuation': punct_cnt}

    # Option 2
    # digits_cnt = sum([x.isdigit() for x in string])
    # letters_cnt = sum([x.isalpha() for x in string])
    # punct_cnt = sum([x in ',.!?;:' for x in string])
    # return {'digits': digits_cnt, 'letters': letters_cnt, 'punct': punct_cnt}

    # Option 3
    d = {'digits': 0, 'letters': 0, 'punct': 0}
    for ch in string:
        if ch.isalpha(): d['letters'] += 1
        elif ch.isdigit(): d['digits'] += 1
        elif ch in '.,!?;:': d['punct'] += 1
    return d



# Task 8:
# Write a function that receives a list of web addresses (= website names) of various organisations.
# Compute the number of addresses for each suffix (e.g., com, org, net) encountered in the list.
# Create and return a dictionary of thus computed values (keys are website suffixes, values are
# the corresponding counts)

def website_stats(website_names):
    # Option 1
    # d = dict()
    # for name in website_names:
    #     # extension = name.rsplit('.', maxsplit=1)[1].rstrip('/')
    #     _, extension = name.rsplit('.', maxsplit=1)
    #     extension = extension.rstrip('/')
    #     if extension in d.keys():
    #         d[extension] += 1
    #     else:
    #         d[extension] = 1
    #
    # return d

    # Option 2
    from collections import defaultdict
    d = defaultdict(int)
    for name in website_names:
        # Option 2.1
        # extension = name.rsplit('.', maxsplit=1)[1].rstrip('/')
        # Option 2.2
        _, extension = name.rsplit('.', maxsplit=1)
        d[extension.rstrip('/')] += 1

    return dict(d)



# Task 9:
# Write a function that finds numbers between 100 and 400 (both included)
# where each digit of a number is even. The numbers that match this criterion
# should be printed in a comma-separated sequence.

def all_digits_even():
    # Option 1
    # result = list()
    # for number in range(100, 401):
    #     all_even = True
    #     for dig in str(number):
    #         if int(dig) % 2 != 0:
    #             all_even = False
    #             break
    #     if all_even: result.append(number)
    #
    # print(", ".join([str(num) for num in result]))

    # Option 2
    result = list()
    for number in range(100, 401):
        all_digits = all([(digit in '02468') for digit in str(number)])
        if all_digits: result.append(number)

    print(", ".join([str(num) for num in result]))



if __name__ == '__main__':

    # a = [1, 1, 2, 3, 5, 8, 13, 21, 55, 89, 5, 10]
    # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # print(common_elements(a,b))

    # list1 = ["M", "na", "i", "Ke", "hi"]
    # list2 = ["y", "me", "s", "lly"]
    # print(concat_index_wise(list1, list2))

    # print(pangram("The quick brown fox jumps over the lazy dog"))
    # print(pangram("The quick brown fox jumps over the lazy cat"))

    # print(first_lower_then_upper("PyNaTive"))

    # sample_input = '''
    #     Server abc01 is up
    #     Server abc02 is down
    #     Server xyz01 is down
    #     Server xyz02 is up
    #     '''
    # server_status(sample_input)

    # numeric_dict(7)

    # print(string_stats("Today is October 22, 2020!"))

    # sample_websites = ['https://www.technologyreview.com/', 'https://www.tidymodels.org/',
    #                    'https://podcasts.google.com/', 'https://www.jamovi.org/', 'http://bg.ac.rs/']
    #
    # print(website_stats(sample_websites))

    all_digits_even()
