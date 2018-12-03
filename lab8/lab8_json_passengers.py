# The starting point for this task is the module lab6_passengers, that is,
# the Passenger class and its subclasses BusinessPassenger and EconomyPassenger.
# Your task is to create functions for
# - serialising (writing) objects of the class Passenger and its subclasses
#   into a .json file
# - deserializing (reconstructing) objects of the class Passenger and its subclasses
#   from a .json file (created using the previous function)


from lab6.lab6_passengers import Passenger, BusinessPassenger, EconomyPassenger



if __name__ == '__main__':

    bob = BusinessPassenger("Bob Smith", "123456", air_miles=1000, checked_in=True)
    # print(bob)
    # print()

    john = EconomyPassenger("John Smith", "987654", checked_in=False)
    # print(john)
    # print()

    bill = EconomyPassenger("Billy Stone", "917253", air_miles=5000, checked_in=True)
    # print(bill)
    # print()

    dona = EconomyPassenger("Dona Stone", "917253", air_miles=2500, checked_in=True)
    # print(dona)
    # print()

    passengers = [bob, john, bill, dona]