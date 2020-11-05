# Task 1
# Write a function that receives an arbitrary number of numeric values
# and computes their product. The function also receives a named argument
# "absolute" with the default value False, which determines if the numeric
# values should be used as given or their absolute value should be used instead.
#
# Implement the function in two different ways:
# 1) using a for loop
# 2) using the reduce() f. from the functools module together with an appropriate lambda f.
#   for an example and explanation of reduce() f. check, for example, this article
#   https://realpython.com/python-reduce-function/ or this one:
#   https://www.python-course.eu/python3_lambda.php

def compute_product(*numbers, absolute=False):
    if absolute:
        numbers = [abs(number) for number in numbers]

    # Option 1
    # product = 1
    # for number in numbers:
    #     product *= number
    # return product

    # Option 2
    from functools import reduce
    return reduce(lambda a,b: a*b, numbers)



# Task 2
# Write a function that receives an arbitrary number of strings and returns a list
# of those strings where the first and the last character are the same (case-insensitive)
# and the total number of unique characters is above the given threshold. The threshold
# is given as a named argument with the default value of 3.
#
# Implement the function in three different ways:
# 1) using the for loop
# 2) using list comprehension
# 3) using the filter() f. together with an appropriate lambda f.

def select_strings(*strings, threshold=3):
    # Option 1
    # selection = list()
    # for s in [s.lower() for s in strings]:
    #     if (s[0] == s[-1]) and (len(set(s)) > threshold):
    #         selection.append(s)
    #
    # return selection

    # Option 2
    # return [s for s in strings if (s.lower()[0] == s.lower()[-1]) and (len(set(s.lower())) > threshold)]

    # Option 3
    check_string = lambda s: (s.lower()[0] == s.lower()[-1]) and (len(set(s.lower())) > threshold)
    return list(filter(check_string, strings))


# Task 3
# Write a function that receives a list of product orders, where each order is a 4-tuple
# of the form (order_id, product_name, quantity, price_per_item). The function returns
# a list of 2-tuples of the form (order_id, total_price) where total price (in USD) for
# an order is the product of the quantity and the price per item (in USD).
# The function also receives two named arguments that may affect the computed total price:
# - discount - the discount, expressed in percentages, to be applied to the total price;
#   the default value of this argument is 0
# - shipping - the shipping cost to be added to orders with total price less than 100 USD.
#   default value of this argument is 10 (USD).
#
# Implement the function in three different ways:
# 1) using the for loop
# 2) using list comprehension
# 3) using the map() f. together with an appropriate lambda f.

def process_product_orders(orders, shipping=10, discount=0):
    # Option 1
    # processed_orders = list()
    # for order in orders:
    #     id, pname, quantity, pprice = order
    #     tot_price = quantity * pprice * (1-discount/100)
    #     processed_orders.append((id, tot_price if tot_price >= 100 else tot_price+shipping))
    # return processed_orders

    # Option 2
    # processed_orders = [(id, quantity*pprice*(1-discount/100)) for id, pname, quantity, pprice in orders]
    #
    # return [(pid, tot_price) if tot_price > 100 else (pid, tot_price + shipping)
    #         for pid, tot_price in processed_orders]

    # Option 3
    # processed_orders = map(lambda order: (order[0], order[2]*order[3]*(1-discount/100)), orders)
    # return list(map(lambda porder: porder if porder[1] > 100 else (porder[0], porder[1] + shipping), processed_orders))

    # Option 4
    def process_order(order):
        id, pname, quantity, pprice = order
        tot_price = quantity * pprice * (1 - discount / 100)
        return (id, tot_price) if tot_price > 100 else (id, tot_price + shipping)

    return list(map(process_order, orders))



# Task 4
# Create a decorator that measures the time a function takes to execute
# and prints the duration to the console.
#
# Hint 1: use the decorator-writing pattern:
# import functools
# def decorator(func):
#     @functools.wraps(func)			                # preserves func's identity after it's decorated
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator
#
# Hint 2: to measure the time of function execution, use the perf_counter() f.
# from the time module (it returns a float value representing time in seconds).

import functools
def timer(func):
    from time import perf_counter

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):

        start_time = perf_counter()

        value = func(*args, **kwargs)

        duration = perf_counter() - start_time
        print(f"The executation time of function {func.__name__} was {duration:.4f} seconds")

        return value
    return wrapper_timer



# Task 4.1
# Write a function that for each number x in the range 1..n (n is the input parameter)
# computes the sum: S(x) = 1 + 2 + ... + x-1 + x, and returns the sum of all S(x).
# Decorate the function with the timer decorator.
#
# Write the function in a few different ways - e.g. (1) using a loop; (2) using list comprehension;
# (3) using the map f. - and decorate each one with the timer to compare their performance

@timer
def compute_sum_loop(n):
    tot_sum = 0
    for x in range(1, n+1):
        tot_sum += sum(range(1, x+1))
    return tot_sum

@timer
def compute_sum_lc(n):
    return sum([sum(range(1, x+1)) for x in range(1, n+1)])

@timer
def compute_sum_map(n):
    return sum(map(lambda x: sum(range(1, x+1)), range(1, n+1)))



# Task 4.2
# Write a function that creates a list by generating n random numbers (integers)
# between 1 and k (n and k are input parameters). After generating and adding each
# number to the list, the function computes and prints the difference
# between mean and median of the list elements. Decorate the function with
# the timer decorator.
#
# Bonus: assure that each function invocation produces the same results

@timer
def mean_median_diff(k, n):
    from random import randint, seed
    from statistics import mean, median

    numbers = []
    print("Printing mean - median difference")
    seed(1)
    for i in range(n):
        numbers.append(randint(1, k))
        print(f"After adding {i+1} element: {abs(mean(numbers) - median(numbers)):.4f}")



# Task 5
# Create a decorator that standardizes (= z-transforms) a list of numbers
# before passing the list to a function for further computations.
# The decorator also rounds the computation result to 4
# digits before returning it (as its return value).
#
# Bonus: before calling the wrapped function, print, to the console,
# its name with the list of input parameters (after standardisation)

def standardiser(func):
    @functools.wraps(func)
    def wrapper_standardiser(*args, **kwargs):

        from statistics import mean, stdev
        m = mean(args)
        sd = stdev(args)
        args = [(a-m)/sd for a in args]

        print(f"Calling function {func.__name__} with")
        print("- positional arguments: " + ", ".join([str(round(a, 4)) for a in args]))
        print("- keyword arguments: " + ", ".join([key + "=" + str(val) for key, val in kwargs.items()]))

        value = func(*args, **kwargs)

        return round(value, 4)
    return wrapper_standardiser


# Task 5.1
# Write a function that receives an arbitrary number of int values
# and for each value (x) computes the following sum:
# S(x) = 1 + x + x**2 + x**3 + ... + x**n
# where n is the keyword argument with default value 10.
# The function returns the sum of S(x) of all received int values.
# Decorate the function with the standardise decorator.

@standardiser
def sum_of_sums(*numbers, n=10):
    return sum(map(lambda x: sum([x**y for y in range(n+1)]), numbers))


if __name__ == '__main__':

    pass

    # print(compute_product(1,-4,13,2))
    # print(compute_product(1, -4, 13, 2, absolute=True))

    # # calling the compute_product function with a list
    # num_list = [2, 7, -11, 9, 24, -3]
    # # this is NOT a way to make the call:
    # print("Calling the function by passing a list as input argument")
    # print(compute_product(num_list))
    # print()
    # # instead, this is how it should be done:
    # print("Calling the function by passing an 'unpacked' list as input argument")
    # print(compute_product(*num_list)) # the * operator is 'unpacking' the list

    # str_list = ['yellowy', 'Bob', 'lovely', 'yesterday', 'too']
    # print(select_strings(*str_list))

    # orders = [("34587", "Learning Python, Mark Lutz", 4, 40.95),
    #           ("98762", "Programming Python, Mark Lutz", 5, 56.80),
    #           ("77226", "Head First Python, Paul Barry", 3, 32.95),
    #           ("88112", "Einführung in Python3, Bernd Klein", 3, 24.99)]
    #
    # print(process_product_orders(orders))
    # print()
    # print("The same orders with discount of 10%")
    # print(process_product_orders(orders, discount=10))

    # print(compute_sum(10000))
    # print()
    # print(compute_sum_v2(10000))
    # print()
    # print(compute_sum_v3(10000))

    # mean_median_diff(100, 250)

    # print(sum_of_sums(1,3,5,7,9,11,13, n=7))