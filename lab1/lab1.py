# Write a function that asks the user for a number, and depending on whether
# the number is even or odd, prints out an appropriate message.

def odd_or_even():
    number = input("Please enter a number:\n")
    number = int(number)
    if number % 2 == 0:
        print("This number is EVEN")
    else:
        print("This number is ODD")


# Write a function to calculate the factorial of a number.
# The function accepts the number (a non-negative integer)
# as an argument.

def factorial(n):
    '''This function computes the factorial of number n'''
    f = 1
    for i in range(n, 1, -1):
        f *= i
    return f


# Write a function that returns nth lowest value of a list
# (or an iterable in general). Return the lowest if n (2nd argument)
# is greater than the number of elements in the iterable.

def nth_lowest(a_list, n):
    a_set = set(a_list)
    sorted_set = sorted(a_set, reverse=True)
    if n > len(sorted_set):
        n = 1
    print(sorted_set)
    return sorted_set[n-1]


# Write a function that receives a list of numbers and returns
# a tuple with the following elements:
# - the list element with the smallest absolute value
# - the list element with the largest absolute value
# - the sum of all positive elements in the list
# - the product of all negative elements in the list

def list_stats(a_list):
    sum_pos = 0
    prod_neg = 1
    min_abs = max_abs = abs(a_list[0])
    # max_abs = abs(a_list[0])
    for i in a_list:
        if i > 0:
            sum_pos += i
        elif i < 0:
            prod_neg *= i
        if abs(i) > max_abs:
            max_abs = abs(i)
        elif abs(i) < min_abs:
            min_abs = abs(i)
    return sum_pos, prod_neg, min_abs, max_abs



# Write a function that receives a list of numbers and a
# threshold value (number). The function:
# - makes a new list that has unique elements from the input list
#   that are less than the given number
# - prints the number of elements in the new list
# - sorts the elements in the list and prints them, an element per line

def create_new_list(a_list, threshold):
    new_list = []
    for item in set(a_list):
        if item < threshold:
            new_list.append(item)
    print("The new list has", str(len(new_list)), "elements")
    sorted_list = sorted(new_list, reverse=True)
    for item in sorted_list:
        print(item)




if __name__ == "__main__":
    # odd_or_even()
    # print(factorial(7))
    l = [2, 8, -12, -98, 8, 2, 12, 81]
    l1 = ['a', 'f', 'r', 'hi', 'nice']
    l2 = 'today'
    # print(nth_lowest(l2, 2))
    # print(list_stats(l))
    create_new_list(l, 5)