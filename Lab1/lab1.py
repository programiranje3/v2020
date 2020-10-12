# Task 1
# Write a function that asks the user for a number, and depending on whether
# the number is even or odd, prints out an appropriate message.




# Task 2
# Write a function to calculate the factorial of a number.
# The function accepts the number (a non-negative integer)
# as an argument. The computed factorial value should be
# printed to the console.




# Task 3
# Write a function that returns n-th lowest value of an iterable
# (1st input parameter). The function return the lowest
# value if n (2nd input parameter) is greater than the number of
# elements in the iterable.




# Task 4
# Write a function that receives a list of numbers and returns
# a tuple with the following elements:
# - the list element with the smallest absolute value
# - the list element with the largest absolute value
# - the sum of all positive elements in the list
# - the product of all negative elements in the list





# Task 5
# Write a function that receives a list of numbers and a
# threshold value (number). The function:
# - makes a new list that has unique elements from the input list
#   that are below the threshold
# - prints the number of elements in the new list
# - sorts the elements in the new list in the descending order,
#   and prints them, one element per line





# Task 6
# Write a function that receives two strings and checks if they
# are anagrams. The function returns appropriate boolean value.
# Note: An anagram is a word or phrase formed by rearranging the
# letters of a different word or phrase, typically using all the
# original letters exactly once





# Task 7
# Write a function that receives a string and checks if the
# string is palindrome. The function returns appropriate boolean value.
# Note: a palindrome is a word, phrase, or sequence that reads the same
# backwards as forwards, e.g. "madam" or "nurses run".






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





if __name__ == '__main__':

    pass

    # odd_or_even()

    # print(factorial(7))

    # a = [31, 72, 13, 41, 5, 16, 87, 98, 9]
    # print(nth_lowest_v2(a, 3))
    # print(nth_lowest_v2(['f', 'r', 't', 'a', 'b', 'y', 'j', 'd', 'c'], 6))
    # print(nth_lowest_v2('today', 6))

    # print(list_stats([1.2, 3.4, 5.6, -4.2, -5.6, 9, 11.3, -23.45, 81]))
    # print(list_stats_v2([1.2, 3.4, 5.6, -4.2, -5.6, 9, 11.3, -23.45, 81]))

    # print_new_list([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 9)

    # print(anagrams('School master', 'The classroom'))
    # print(anagrams('Dormitory', 'Dirty room'))
    # print(anagrams('Bob', 'Bill'))

    # print(palindrome("madam"))
    # print(palindrome("nurses run"))
    # print(palindrome("nurse run"))

    # guess_number()