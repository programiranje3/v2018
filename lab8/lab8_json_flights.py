# The starting point for this task is the module lab6_flight, that is,
# the Flight class. Note that one attribute of this class is a list of flight
# passengers the elements of which are objects of the class Passenger and/or its
# subclasses BusinessPassenger and EconomyPassenger defined in the module
# lab6_passengers.
# Your task is to create functions for
# - serialising (writing) objects of the class Flight into a .json file
# - deserializing (reconstructing) objects of the class Flight from a
#   .json file (created using the previous function)

from lab6.lab6_flight import Flight
from lab6.lab6_passengers import EconomyPassenger, BusinessPassenger




if __name__ == '__main__':

    lh992 = Flight.from_Frankfurt_by_Lufthansa('LH992', '2018-11-03 12:20')
    lh992.destination = "Amsterdam"
    # print(lh992)
    # print()

    lh1411 = Flight('LH1411', '2018-11-03 6:50', origin='Belgrade', destination='Frankfurt')
    # print(lh1411)
    # print()

    bob = BusinessPassenger("Bob Smith", "123456", air_miles=1000, checked_in=True)
    john = EconomyPassenger("John Smith", "987654", checked_in=False)
    bill = EconomyPassenger("Billy Stone", "917253", air_miles=5000, checked_in=True)
    dona = EconomyPassenger("Dona Stone", "917253", air_miles=2500, checked_in=True)
    kate = EconomyPassenger("Kate Fox", "114252", air_miles=3500, checked_in=True)

    lh1411.passengers.extend([bob, john, bill, dona, kate])


