# Task 1
# Write a function that asks the user for a number, and depending on whether
# the number is even or odd, prints out an appropriate message.

def odd_or_even():
    number_str = input("Please enter a whole number\n")

    # Option 1:
    # if int(number_str) % 2 == 0:
    #     print("EVEN number")
    # else:
    #     print("ODD number")

    result = "EVEN" if int(number_str) % 2 == 0 else "ODD"
    print("Number", number_str, "is", result)


# Task 2
# Write a function to calculate the factorial of a number.
# The function accepts the number (a non-negative integer)
# as an argument. The computed factorial value should be
# printed to the console.

def factorial(number):
    result = 1
    for i in range(1, number+1):
        result *= i
    print("Factorial of number", number, "is", result)


# Task 3
# Write a function that returns n-th lowest value of an iterable
# (1st input parameter). The function return the lowest
# value if n (2nd input parameter) is greater than the number of
# elements in the iterable.

def nth_lowest(iterable, n):
    if len(iterable) < n:
        return min(iterable)
    return sorted(iterable)[n-1]


# Task 4
# Write a function that receives a list of numbers and returns
# a tuple with the following elements:
# - the list element with the smallest absolute value
# - the list element with the largest absolute value
# - the sum of all positive elements in the list
# - the product of all negative elements in the list

def list_stats(numbers):
    abs_numbers = list()
    sum_pos = 0
    prod_neg = 1
    for number in numbers:
        abs_numbers.append(abs(number))
        if number > 0: sum_pos += number
        elif number < 0: prod_neg *= number

    return min(abs_numbers), max(abs_numbers), sum_pos, prod_neg



# Task 5
# Write a function that receives a list of numbers and a
# threshold value (number). The function:
# - makes a new list that has unique elements from the input list
#   that are below the threshold
# - prints the number of elements in the new list
# - sorts the elements in the new list in the descending order,
#   and prints them, one element per line

def list_operations(numbers, threshold):
    unique_nums = list()
    for num in set(numbers):
        if num < threshold: unique_nums.append(num)

    print("The new list has", len(unique_nums), "elements")

    unique_nums.sort(reverse=True)
    for i, num in enumerate(unique_nums):
        print(str(i+1) + ". " + str(num))



# Task 6
# Write a function that receives two strings and checks if they
# are anagrams. The function returns appropriate boolean value.
# Note: An anagram is a word or phrase formed by rearranging the
# letters of a different word or phrase, typically using all the
# original letters exactly once

def anagrams(s1, s2):
    s1_list = list()
    s2_list = list()
    for ch in s1:
        if ch.isalpha(): s1_list.append(ch.lower())
    for ch in s2:
        if ch.isalpha(): s2_list.append(ch.lower())

    # s1_list.sort()
    # s2_list.sort()
    # return s1_list == s2_list
    return sorted(s1_list) == sorted(s2_list)



# Task 7
# Write a function that receives a string and checks if the
# string is palindrome. The function returns appropriate boolean value.
# Note: a palindrome is a word, phrase, or sequence that reads the same
# backwards as forwards, e.g. "madam" or "nurses run".

def palindrome(string):
    alpha_num = list()
    for ch in string:
        if ch.isalnum(): alpha_num.append(ch.lower())

    return alpha_num == list(reversed(alpha_num))




# Task 8
# Write a function to play a guessing game: to guess a number between 1 to 9.
# Scenario: user is prompted to enter a guess. If the user guesses wrongly,
# the prompt reappears; the user can try to guess max 3 times;
# on successful guess, user should get a "Well guessed!" message,
# and the function terminates. If when guessing, the user enters a number
# that is out of the bounds (less than 1 or greater than 9), or a character
# that is not a number, he/she should be informed that only single digit
# values are allowed.
#
# Hint: use function randint from random package to generate a number to
# be guessed in the game

def guessing_game():
    from random import randint
    hidden_number = randint(1,9)

    trial = 1
    while(trial <= 3):
        trial += 1
        guess = input("Make a guess (number between 1 and 9)\n")
        if (len(guess)) > 1 or (guess.isdigit() == False):
            print("Only digits between 1 and 9 are allowed. Try again")
            continue
        if int(guess) == hidden_number:
            print("Well guessed! Congrats!")
            return
        else:
            print("Wrong! Try again")

    print("No more trials left. More luck next time")





if __name__ == '__main__':

    # odd_or_even()

    # factorial(9)

    # a = [31, 72, 13, 41, 5, 16, 87, 98, 9]
    # print(nth_lowest(a, 3))
    # print(nth_lowest(['f', 'r', 't', 'a', 'b', 'y', 'j', 'd', 'c'], 6))
    # print(nth_lowest('today', 2))

    # print(list_stats([1.2, 3.4, 5.6, -4.2, -5.6, 9, 11.3, -23.45, 81]))

    # print_new_list([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 9)

    # print(anagrams('School master', 'The classroom'))
    # print(anagrams('Dormitory', 'Dirty room'))
    # print(anagrams('Conversation', 'Voices rant on'))
    # print(anagrams('Bob', 'Bill'))

    # print(palindrome("madam"))
    # print(palindrome("nurses run"))
    # print(palindrome("nurse run"))

    guessing_game()