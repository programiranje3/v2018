# Task 1
# Write a function that receives a piece of text and computes the frequency of
# the tokens appearing in the text (a token is a string of contiguous characters
# between two spaces, or between a space and punctuation marks).
# Tokens and their frequencies are to be stored in a dictionary. The function
# prints tokens and their frequencies after sorting the tokens alphanumerically.
#
# After testing the function, alter it so that the dictionary entries are printed
# in the decreasing order of the tokens' frequencies.
# (hint: use itemgetter() f. from the operator module)




# Task 2
# Write a function that accepts a sequence of comma separated passwords
# and checks their validity using the following criteria:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# 5. Minimum length: 6
# 6. Maximum length: 12
# Passwords that match the criteria should be printed in one row
# separated by a comma.




# Task 3
# Write a function that prompts the user for name, age, and height (in cm) of a couple of
# people (e.g. members of a sports team) and stores the input values as a list of tuples of
# the form (name, age, height), where name is string, whereas age and height are numbers.
# After entering these data items for one person, the user is asked if he/she wants to
# continue or not. When the entry is finished the function sorts and prints the list
# based on name, then height and finally age (so, the following sorting criteria should
# be applied: 1) name, 2) height, 3) age).





# Task 4
# Write a function that prompts the user for name, age, height (in meters), weight (in kg), and
# competition score (0-100) of members of a sports team. All data items for one member should be
# entered in a single line, separated by a comma (e.g. Bob, 19, 1.78, 75, 55). The entry stops
# when the user enters 'done'.
# The function stores the data for each team member as a dictionary, such as
# {name:Bob, age:19, height: 1.78, weight:75, score:55}
# where name is string, age is integer, and the other 3 attributes are real values.
# The data for all team members should form a list of dicitonaries; this list is the return
# value of the function.





# Task 5
# Write a function that takes as its input the list of dictionaries created by the previous function
# and computes and prints the following statistics:
# - the average (mean) age, height, and weight of the team members
# - the team's median score
# - name of the player with the highest score among those under 21 years of age
#
# Hint: the 'statistics' module provides functions for the required computations





# Task 6
# Write a function that creates a dictionary from the two given lists.
# Assure the lists are of equal length. Print the dictionary sorted based on
# the key values.
# Example: a list of countries and a list of the countries' national dishes
# should be turned into a dictionary where keys are country names and values
# are the corresponding dishes.





# Task 7
# Write a function to count the total number of students per class. The function receives
# a list of tuples of the form (<class>,<stud_count>). For example:
# [('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1)]
# The function creates a dictionary of classes and their student numbers; it then
# prints the classes and their sizes in the decreasing order of the class size.
#
# Hint: consider using defaultdict from the collections module





# if __name__ == '__main__':

    # for_token_freq = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

    # passwords = ["ABd1234@1, a F1#, 2w3E*, 2We3345"]


    # team = [{'name': 'Bob', 'age': 18, 'height': 1.77, 'weight': 79.0, 'score': 50.0},
    #              {'name': 'Tim', 'age': 17, 'height': 1.78, 'weight': 80.0, 'score': 84.0},
    #              {'name': 'Jim', 'age': 19, 'height': 1.98, 'weight': 90.0, 'score': 94.0}]


    # dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
    # countries = ["Italy", "Germany", "Spain", "USA"]

