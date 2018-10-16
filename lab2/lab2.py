from string import ascii_lowercase


# Task 1:
# Write a function that receives an integer value (n) and
# generates and prints a dictionary with entries in the
# form x:x*x, where x is a number between 1 and n.

def create_dictionary(n):
    a_dict = dict()
    for x in range(1,n+1):
        a_dict[x] = x*x
    # print(a_dict.items())
    for key, val in a_dict.items():
        print("{0}:{1}".format(key, val))



# Task 2:
# Write a function that receives a string as its input parameter and
# calculates the number of digits and letters in this string.
# The function returns the dictionary with the computed values.

def letters_digits_dict(a_string):
    a_dict = {"digits":0, "letters":0}
    for ch in a_string:
        if ch.isdigit():
            a_dict['digits'] += 1
        if ch.isalpha():
            a_dict['letters'] += 1
    return a_dict



# Task 3:
# Write a function that receives two lists and returns a list that contains
# only those elements (without duplicates) that appear in both input lists.

def common_elements(l1, l2):
    # s1 = set(l1)
    # s2 = set(l2)
    # return list(s1.intersection(s2))
    return list(set(l1).intersection(set(l2)))



# Task 4:
# Write a function that receives two strings and checks if
# the second string when reversed is equal to the first one.
# The comparison should be based on letters and digits only
# (alphanumerics) and should not be case sensitive.
# The function returns appropriate boolean value.

# def same_when_reversed(s1, s2):
#     str1 = []
#     for ch in s1.lower():
#         if ch.isalnum(): str1.append(ch)
#     str2 = []
#     for ch in s2.lower():
#         if ch.isalnum(): str2.append(ch)
#     # print(list(reversed(str2)))
#     # print(str1)
#     return str1 == list(reversed(str2))

def same_when_reversed(s1, s2):
    str1 = [ch for ch in s1.lower() if ch.isalnum()]
    str2 = [ch for ch in reversed(s2.lower()) if ch.isalnum()]
    return str1 == str2



# Task 5:
# Write a function that asks the user for a string and prints out
# whether this string is a palindrome or not.

# def palindrom():
#     an_input = input("Please enter a string to check if it is a palindrome:\n")
#     str1 = []
#     for ch in an_input.lower():
#         if ch.isalpha(): str1.append(ch)
#     str2 = []
#     for ch in reversed(an_input.lower()):
#         if ch.isalpha(): str2.append(ch)
#     if str1 == str2:
#         print("'{0}' is palindrome".format(an_input))
#     else:
#         print("'{0}' is NOT palindrome".format(an_input))


def palindrom():
    an_input = input("Please enter a string to check if it is a palindrome:\n")
    str1 = [ch.lower() for ch in an_input if ch.isalpha()]
    str2 = [ch.lower() for ch in reversed(an_input) if ch.isalpha()]
    result = "palindrome" if str1 == str2 else "NOT palindrome"
    print("'{0}' is {1}".format(an_input, result))



# Task 6:
# Write a function to check whether a given string is a pangram or not.
# Pangrams are sentences containing every letter of the alphabet at least once.
# (e.g.: "The quick brown fox jumps over the lazy dog")
#
# Hint: use ascii_lowercase from the string module to get all letters

# Option 1:
# def pangram(a_string):
#     for ch in ascii_lowercase:
#         if ch not in a_string:
#             return False
#     return True


# Option 2: using all()
def pangram(a_string):
    letters = [ch for ch in a_string.lower() if ch.isalpha()]
    return all([(ch in letters) for ch in ascii_lowercase])



# Task 7:
# Write a function that finds numbers between 100 and 400 (both included)
# where each digit of a number is even. The numbers that match this criterion
# should be printed in a comma-separated sequence.

def all_even_digits():
    all_even = []
    for num in range(100, 401):
        digits = [int(d) for d in str(num)]
        # print(digits)
        all_are_even = True
        for d in digits:
            if d % 2 != 0:
                all_are_even = False
                break
        if all_are_even:
            all_even.append(num)
    print(all_even)



# Task 8:
# Write a function that accepts a string input and returns slices of that
# string according to the following rules:
# - if the input string is less than 3 characters long, returns a list
#   with the input string as the only element
# - otherwise, returns a list with all string slices more than 1 character long
# Examples:
# input: 'are'
# result: ['ar', 'are', 're']
# input: 'table'
# result: ['ta', 'tab', 'tabl', 'table', 'ab', 'abl', 'able', 'bl', 'ble', 'le']

def string_slices(a_string):
    if len(a_string) < 3:
        return [a_string]
    result = []
    for i in range(0, (len(a_string)-1)):
        for j in range(i+1, len(a_string)):
            result.append(a_string[i:(j+1)])
    return result



if __name__ == "__main__":
    # create_dictionary(5)
    # print(letters_digits_dict("Today is Oct 16, 2018"))
    # a = [1,3, 5,11, 1, 32, 5,7,12, 3, 3]
    # b = [3, 5, 81, 34, 12, 3]
    # print(common_elements(a,b))
    # print(same_when_reversed("the 1st day", "yad,ts1,eht "))
    # print(same_when_reversed("ana", "hana"))
    # palindrom()
    print(pangram("The quick brown fox jumps over the lazy dog"))
    print(pangram("The quick brown fox jumps over the lazy cat"))
    # all_even_digits()
    # print(string_slices('are'))
    # print(string_slices('table'))