from operator import itemgetter


# Task 1
# Write a function that creates a dictionary from the two given lists.
# Assure the lists are of equal length.
# Print the dictionary sorted based on the element values.
# (hint: use itemgetter() f. from the operator module)
#
# Example: a list of countries and a list of the countries' national dishes
# should be turned into a dictionary where keys are country names and values
# are the corresponding dishes.

def lists_to_dict(l1, l2):

    if len(l1) != len(l2):
        print(f"Lists are not of equal size; the first {min(len(l1), len(l2))} elements of both lists will be used")

    # Option 1
    # d = dict(zip(l1, l2))
    # for key, val in sorted(d.items(), key=itemgetter(1)):
    #     print(f"{key}: {val}")

    # Option 2
    elem_cnt = min(len(l1), len(l2))
    d = {l1[i]:l2[i] for i in range(elem_cnt)}

    for key, val in sorted(d.items(), key=itemgetter(1)):
        print(f"{key}: {val}")



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

def token_frequency(text):

    # Option 1
    from collections import defaultdict
    token_freq_dict = defaultdict(int)
    for token in text.split():
        token = token.rstrip(',.;:!?').lstrip()
        if len(token) > 2:
            token_freq_dict[token.lower()] += 1

    for token, freq in sorted(sorted(token_freq_dict.items()), key=itemgetter(1), reverse=True):
        print(f"{token}: {freq}")

    # Option 2
    # from collections import Counter
    # tokens = [token.strip(',.;:!?').lower() for token in text.split()]
    # tokens_counter = Counter([t for t in tokens if len(t) > 2])
    # for token, freq in sorted(sorted(tokens_counter.items()), key=itemgetter(1), reverse=True):
    #     print(f"{token}: {freq}")



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

def password_check(passwords):

    # Option 1
    # from string import ascii_lowercase, ascii_uppercase, digits
    # valid_passwords = []
    # for pword in [p.strip() for p in passwords.split(",")]:
    #     if any([ch in ascii_lowercase for ch in pword]) and \
    #         any([ch in ascii_uppercase for ch in pword]) and \
    #         any([ch.isdigit() for ch in pword]) and \
    #         any([ch in '$#@' for ch in pword]) and \
    #         6 <= len(pword) <= 12: valid_passwords.append(pword)
    #
    # print(", ".join(valid_passwords))

    # Option 2
    valid_passwords = list()

    to_check = [p.strip() for p in passwords.split(',')]
    for pword in to_check:
        valid = [False] * 5
        if any([(ch.isalpha() and ch.islower()) for ch in pword]): valid[0] = True
        if any([ch.isdigit() for ch in pword]): valid[1] = True
        if any([(ch.isalpha() and ch.isupper()) for ch in pword]): valid[2] = True
        if any([ch in '$#@' for ch in pword]): valid[3] = True
        if 6 <= len(pword) <= 12: valid[4] = True
        if all(valid):
            valid_passwords.append(pword)

    print(", ".join(valid_passwords))



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

# def get_member_score(member_data):
#     return member_data['score']

get_member_score = lambda member_data: member_data['score']

def collect_team_data():

    print("""
    You'll be prompted to enter name, age, and score for each team member.
    Each member's data should be entered in a single line, separated by a comma.
    To terminate the data entry enter "done".
    """)

    members = list()
    while(True):
        entry = input("Data for the next member:\n")
        if entry.lower() == 'done': break
        member_data = entry.split(",")
        if len(member_data) != 3:
            print("Irregular entry; please try again")
            continue
        name, age, score = member_data
        members.append({'name': name, 'age': int(age), 'score': float(score)})

    # alternative
    # for member in sorted(members, key=itemgetter('score'), reverse=True):
    for member in sorted(members, key=get_member_score, reverse=True):
        name, age, score = member.values()
        print(f"{name}, {age} years old, scored {score}")

    return members



# Task 5
# Write a function that takes as its input the list of dictionaries created by the previous
# function and computes and prints the following statistics:
# - the average (mean) age of the team members
# - median, first and third quartile for the team's score
# - name of the player with the highest score among those under 21 years of age
#
# Hint: the 'statistics' module provides functions for the required computations

def team_stats(team_members):
    from statistics import mean, quantiles

    mean_age = mean([member['age'] for member in team_members])
    print(f"Team members are {mean_age} years old, on average")

    scores = [member['score'] for member in team_members]
    q1, q2, q3 = quantiles(scores, n=4)
    print(f"Team's median score is {q2}, whereas the interquartile range is [{q1:.2f}, {q3:.2f}]")

    # Option 1 for max_player
    # max_player = team_members[0]
    # for player in [member for member in team_members if member['age'] < 21]:
    #     if player['score'] > max_player['score']:
    #         max_player = player

    # Option 2 for max_player
    # max_player = max([member for member in team_members if member['age'] < 21], key=get_member_score)

    # Option 2.1 for max_player
    max_player = max([member for member in team_members if member['age'] < 21], key=itemgetter('score'))

    print(f"{max_player['name']} is the best player among those under 21 years of age")



# Task 6
# Write a function to count the total number of students per class. The function receives
# a list of tuples of the form (<class>,<stud_count>). For example:
# [('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1)]
# The function creates a dictionary of classes and their student numbers; it then
# prints the classes and their sizes in the decreasing order of the class size.
#
# After testing the function, try writing it using the Counter class from
# the collections module.

def classroom_stats(class_data):
    from collections import Counter
    # from collections import defaultdict
    #
    # classes_dict = defaultdict(int)
    # for cls_label, cls_count in class_data:
    #     classes_dict[cls_label] += cls_count
    #
    # for cls_label, cls_size in sorted(classes_dict.items(), key=itemgetter(1), reverse=True):
    #     print(f"Class {cls_label} has {cls_size} students")

    classes_list = []
    for cls_label, cls_count in class_data:
        classes_list.extend([cls_label] * cls_count)

    classes_counts = Counter(classes_list)
    for cls_label, cls_size in sorted(classes_counts.items(), key=itemgetter(1), reverse=True):
        print(f"Class {cls_label} has {cls_size} students")



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

    # collect_team_data()

    # team = [{'name': 'Bob', 'age': 18, 'score': 50.0},
    #         {'name': 'Tim', 'age': 17, 'score': 84.0},
    #         {'name': 'Jim', 'age': 19, 'score': 94.0},
    #         {'name': 'Joe', 'age': 19, 'score': 85.5}]
    # team_stats(team)

    # l = [('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1)]
    # classroom_stats(l)
