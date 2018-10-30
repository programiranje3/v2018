from functools import reduce, wraps
from collections import defaultdict
from statistics import mean, median
from random import seed, randint

# Task 1
# Write a function that receives an arbitrary number of numeric values
# and computes their product. The function also receives a named argument
# "absolute" with the default value False, which determines if absolute
# value of the product is to be returned or not.
# Implement the function in two different ways:
#
# 1) using a for loop
# 2) using the reduce() f. from the functools package together with an appropriate lambda f.

# def product(*numbers, absolute=False):
#     result = 1
#     for number in numbers:
#         result *= number;
#     if absolute:
#         result = abs(result)
#     return result


def product(*numbers, absolute=False):
    result = reduce(lambda x,y: x*y, numbers)
    return result if not absolute else abs(result)

# Task 2
# Write a function that receives an arbitrary number of strings and returns a list
# of those strings where the first and the last character are the same and the
# total number of unique characters is above the given threshold. The threshold
# is given as a named argument with the default value of 3.
#
# Implement the function in two different ways:
# 1) using a for loop
# 2) using the filter() f. together with an appropriate lambda f.

# def select_strings(*strings, threshold=3):
#     selection = []
#     for s in strings:
#         if (s[0].lower() == s[-1].lower()) and (len(set(s)) > threshold):
#             selection.append(s)
#     return selection

# def select_strings(*strings, threshold=3):
#     return [s for s in strings if (s[0].lower() == s[-1].lower()) and (len(set(s)) > threshold)]

def select_strings(*strings, threshold=3):
    f = lambda s: (s[0].lower() == s[-1].lower()) and (len(set(s)) > threshold)
    return list(filter(f, strings))


# Task 3
# Write a function that receives a list of product orders, where each order is a 4-tuple
# of the form (order_id, product_name, quantity, price_per_item). The function returns
# a list of 2-tuples of the form (order_id, total_price) where total price (in USD) for
# an order is the product of the quantity and the price per item (in USD) plus the shipping
# cost for orders with total value less than 100 USD. The shipping cost is given as the
# value of the input argument 'shipping' with default value of 10 (USD).
#
# Implement the function in two different ways:
# 1) using a for loop
# 2) using the map() f. together with an appropriate lambda f.

# def process_orders(orders, shipping=10):
#     orders_dict = defaultdict(float)
#     for order_id, prod_name, quantity, item_price in orders:
#         orders_dict[order_id] += quantity * item_price
#     for order_id, tot_value in orders_dict.items():
#         if tot_value < 100:
#             orders_dict[order_id] += shipping
#     return [(order_id, tot_value) for order_id, tot_value in orders_dict.items()]

def process_orders(orders, shipping=10):
    processed_orders = map(lambda order: (order[0], order[2]*order[3]), orders)
    processed_orders = map(lambda order: order if order[1] >= 100
                            else (order[0], order[1]+shipping), processed_orders)
    return list(processed_orders)

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
# Hint 2: to measure the time a function takes, use the perf_counter() function from the time module.

def stopwatch(f):
    from time import perf_counter

    @wraps(f)
    def wrapper_stopwatch(*args):
        start_time = perf_counter()
        result = f(*args)
        end_time = perf_counter()
        print("Function {0} was running for {1:.4f} seconds".format(f.__name__, end_time-start_time ))
        return result

    return wrapper_stopwatch

# Write a function that for each number x in the range 1..n (n is the input parameter)
# computes the sum: S(x) = 1 + 2 + ... + x-1 + x, and returns the sum of all S(x).
# Decorate the function with the stopwatch decorator.

@stopwatch
def sum_of_sums(n):
    result = 0
    for x in range(1, n+1):
        result += sum(range(1, x+1))
    return result


# Write a function that creates a list by generating n random numbers between
# 1 and k (n and k are input parameters). After generating and adding each
# number to the list, the function determines and prints the difference
# between mean and median of the list elements. Decorate the function with
# the stopwatch decorator.

@stopwatch
def random_numbers(n, k):
    numbers = []
    seed(1)
    for _ in range(n):
        number = randint(1,k)
        numbers.append(number)
        diff = mean(numbers) - median(numbers)
        print("After adding {0}, the difference between mean and median is {1:.4f}".format(number, diff))


# Task 5
# Create a decorator that standardizes a list of numbers
# before passing it to a function for further computations.
# The decorator also rounds the computation results to 4
# digits before returning it (as its return value).
#
# Bonus: before calling the wrapped function, print, to the console,
# its name with the list of input parameters (after standardisation)




# Write a function that receives an arbitrary number of int values
# and for each value (x) computes the following sum:
# S(x) = x + x**2 + x**3 + ... + x**n
# where n is the keyword argument with default value 10.
# The function returns the sum of S(x) of all received int values.
# Decorate the function with the standardise decorator.



if __name__ == '__main__':

    # print(product(1,-4,13,2))
    # print()
    # print(product(1, -4, 13, 2, absolute=True))

    # calling the product function with a list
    # num_list = [2, 7, -11, 9, 24, -3]
    # this is NOT a way to make the call:
    # print(product(num_list))
    # instead, this is how it should be done:
    # print(product(*num_list))

    # str_list = ['Yellowy', 'Bob', 'lovely', 'yesterday', 'too']
    # print(select_strings(*str_list, threshold=2))

    # orders = [("34587", "Learning Python, Mark Lutz", 4, 40.95),
    #           ("98762", "Programming Python, Mark Lutz", 5, 56.80),
    #           ("77226", "Head First Python, Paul Barry", 3, 32.95),
    #           ("88112", "Einführung in Python3, Bernd Klein", 3, 24.99)]
    #
    # print(process_orders(orders))

    # print(sum_of_sums(10000))
    random_numbers(100, 250)

    # print(sum_of_powered_args(1,3,5,7,9, n=5))


