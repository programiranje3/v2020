# Task 1:
# Write a function that receives two lists and returns a list that contains
# only those elements (without duplicates) that appear in both input lists.



# Task 2:
# Write a function that receives 2 lists of the same length and
# returns a new list obtained by concatenating the two input
# lists index-wise. Example:
# Input lists:
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# Output: ['My', 'name', 'is', 'Kelly']




# Task 3:
# Write a function that checks and returns whether a given string is a pangram or not.
# Pangrams are sentences containing every letter of the alphabet at least once.
# (e.g.: "The quick brown fox jumps over the lazy dog")
#
# Hint: ascii_lowercase from the string module can be used to get all letters




# Task 4
# Write a function that receives a string with a mix of lower and upper case letters.
# The function arranges letters in such a way that all lowercase letters come first,
# followed by all upper case letters.
# The new,'rearranged' string is the function's return value.




# Task 5
# Write a function that receives a report (as a string) on the state (up / down) of several servers.
# Each line of the report refers to one server, and has the following format:
# "Server <server_name> is <up/down>"
# Note that some lines may be empty.
# The function should process the report and print:
# - the total number of servers mentioned in the report
# - the proportion of servers that are down
# - names of servers that are down.




# Task 6:
# Write a function that receives an integer value (n) and
# generates and prints a dictionary with entries in the
# form x: (1 + 2 + ... + x), where x is a number between 1 and n.




# Task 7:
# Write a function that receives a string as its input parameter, and
# calculates the number of digits, letters, and punctuation marks (.,!?;:)
# in this string.
# The function returns a dictionary with the computed values.




# Task 8:
# Write a function that receives a list of web addresses (= website names) of various organisations.
# Compute the number of addresses for each suffix (e.g., com, org, net) encountered in the list.
# Create and return a dictionary of thus computed values (keys are website suffixes, values are
# the corresponding counts)




# Task 9:
# Write a function that finds numbers between 100 and 400 (both included)
# where each digit of a number is even. The numbers that match this criterion
# should be printed in a comma-separated sequence.





if __name__ == '__main__':
    pass

    # a = [1, 1, 2, 3, 5, 8, 13, 21, 55, 89, 5, 10]
    # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # print(common_unique_elements(a,b))

    # list1 = ["M", "na", "i", "Ke"]
    # list2 = ["y", "me", "s", "lly"]
    # print(merge_lists(list1, list2))

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

    # dict_of_sums(7)

    # print(string_stats("Today is October 19, 2020!"))

    # sample_websites = ['https://www.technologyreview.com/', 'https://www.tidymodels.org/',
    #                    'https://podcasts.google.com/', 'https://www.jamovi.org/', 'http://bg.ac.rs/']
    #
    # print(website_stats(sample_websites))

    # all_digits_even()
