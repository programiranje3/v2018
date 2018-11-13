# Create the Flight class with the following attributes:
# - flight_num - flight number
# - departure - the date and time of the departure
# - origin - the location the flight departs from
# - destination - the destination of the flight
# - operated_by - the company that operates the flight
# - passengers - list of passengers, that is, instances of the Passenger class
#
# The Flight class should implement the following methods:
# - constructor (__init__()) - only flight number and departure have to be specified
#
# - get and set methods (using appropriate decorators) for the following attributes:
#   - departure - make it a private attribute and assure that it is a datetime object of the format:
#     "%Y-%m-%d %H:%M"; consider defining this format as a class attribute (departure_format)
#   - flight_num - make it a private attribute and assure that the flight number consist of
#     two letters followed by 3-4 digits
#   - passengers - make it a private attribute and assure that only objects of the type Passenger
#     can be added to the passengers list; if None is passed to the setter, create an empty
#     passengers list
#
# - method that returns a string representation of the given Flight object (__str__())
#
# - class method from_Frankfurt_by_Lufthansa() that creates flights that fly from Frankfurt and
#   are operated by Lufthansa (alternative constructor); the method receives flight number and
#   the scheduled departure date and time
#
# - a generator method that generates a sequence of passengers who have not yet checked in
#
# - a generator method that generates a sequence of candidate passengers for an upgrade to
#   the business class; those are the passengers of the economy class whose air miles
#   exceed the given threshold (input parameter) and who have checked in for the flight;
#   the generated sequence should consider the passengers air miles, so that those with more
#   air miles are first offered the upgrade option

from lab6.lab6_passengers import Passenger, BusinessPassenger, EconomyPassenger
from datetime import datetime

class Flight:
    departure_format = "%Y-%m-%d %H:%M"

    def __init__(self, flight_num, departure, origin="unknown",
                 destination="unknown", operated_by="unknown", passengers=None):
        self.flight_num = flight_num
        self.departure = departure
        self.origin = origin
        self.destination = destination
        self.operated_by = operated_by
        self.passengers = passengers

    @property
    def departure(self):
        return self.__departure

    @departure.setter
    def departure(self, departure_str):
        try:
            self.__departure = datetime.strptime(departure_str, self.departure_format)
        except ValueError as err:
            print("Error: " + err)
            self.__departure = "unknown"

    @property
    def flight_num(self):
        return self.__flight_num

    @flight_num.setter
    def flight_num (self,flight_num):
        if self.pomocna(flight_num):
            self.__flight_num=flight_num

    @staticmethod
    def pomocna(flight_num):

        if len(flight_num) > 6 or len(flight_num) < 5:
            return False

        list=[False]*len(flight_num)
        if flight_num[0].isalpha():
            list[0]=True
        if flight_num[1].isalpha():
            list[1]=True
        for p, ch in enumerate(flight_num[2:]):
            if ch.isdigit(): list[p] = True
        return all(list)

    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self, passengers_list):
        self.__passengers = list()
        if passengers_list is not None:
            for index, passenger in enumerate(passengers_list):
                if isinstance(passenger, Passenger):
                    self.__passengers.append(passenger)
                else:
                    print("Error! {}. element of the input list is not Passenger".format(index+1))



