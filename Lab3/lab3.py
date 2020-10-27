# Task 1
# Write a function that creates a dictionary from the two given lists.
# Assure the lists are of equal length.
# Print the dictionary sorted based on the element values.
# (hint: use itemgetter() f. from the operator module)
#
# Example: a list of countries and a list of the countries' national dishes
# should be turned into a dictionary where keys are country names and values
# are the corresponding dishes.




# Task 2
# Write a function that receives a piece of text and computes the frequency of
# tokens appearing in the text (consider that a token is a string of contiguous
# characters between two spaces). When computing token frequency, do not consider
# the difference between upper and lowercase letters (e.g. 'hello' and 'Hello' should
# be considered the same).
# Tokens and their frequencies should be stored in a dictionary. The function
# prints tokens and their frequencies after sorting the tokens alphanumerically.
#
# After testing the function, alter it so that:
# - tokens are cleared of any excessive characters (e.g. spaces or punctuation marks)
#   before being added to the dictionary
# - only tokens with at least 3 characters are added to the dictionary
# - before being printed, the dictionary entries are sorted i) in the decreasing order
#   of the tokens' frequencies, and then ii) in increasing alphabetical order.




# Task 3
# Write a function that accepts a sequence of comma separated passwords
# and checks their validity using the following criteria:
# 1. At least 1 letter between [a-z] => At least 1 lower case letter
# 2. At least 1 number between [0-9] => At least 1 digit
# 3. At least 1 letter between [A-Z] => At least 1 upper case letter
# 4. At least 1 of these characters: $,#,@
# 5. Minimum length: 6
# 6. Maximum length: 12
# Passwords that match the criteria should be printed in one line
# separated by a comma.




# Task 4
# Write a function that prompts the user for name, age, and competition score (0-100) of members
# of a sports team. All data items for one member should be entered in a single line, separated
# by a comma (e.g. Bob, 19, 55). The entry stops when the user enters 'done'.
# The function stores the data for each team member as a dictionary, such as
# {name:Bob, age:19, score:55}
# where name is string, age is integer, and score is a real value.
# The data for all team members should form a list of dictionaries.
# The function prints this list sorted by the members' scores (from highest to lowest) and
# then returns the list as its return value.




# Task 5
# Write a function that takes as its input the list of dictionaries created by the previous
# function and computes and prints the following statistics:
# - the average (mean) age of the team members
# - median, first and third quartile for the team's score
# - name of the player with the highest score among those under 21 years of age
#
# Hint: the 'statistics' module provides functions for the required computations




# Task 6
# Write a function to count the total number of students per class. The function receives
# a list of tuples of the form (<class>,<stud_count>). For example:
# [('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1)]
# The function creates a dictionary of classes and their student numbers; it then
# prints the classes and their sizes in the decreasing order of the class size.
#
# After testing the function, try writing it using the Counter class from
# the collections module.




if __name__ == '__main__':
    pass

    # dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
    # countries = ["Italy", "Germany", "Spain", "USA", "Serbia"]
    # lists_to_dict(countries, dishes)

    # response by GPT-3 to the question why it has so entranced the tech community
    # source: https://www.wired.com/story/ai-text-generator-gpt-3-learning-language-fitfully/
    # gpt3_response = ("""
    #     I spoke with a very special person whose name is not relevant at this time,
    #     and what they told me was that my framework was perfect. If I remember correctly,
    #     they said it was like releasing a tiger into the world.
    # """)
    # token_frequency(gpt3_response)

    # password_check("ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456WR")

    # collecte_team_data()

    # team = [{'name': 'Bob', 'age': 18, 'score': 50.0},
    #         {'name': 'Tim', 'age': 17, 'score': 84.0},
    #         {'name': 'Jim', 'age': 19, 'score': 94.0},
    #         {'name': 'Joe', 'age': 19, 'score': 85.5}]
    # team_stats(team)

    # l = [('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1)]
    # classroom_stats(l)

