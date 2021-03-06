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
            print("Error: " + str(err))
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

        # return all([ch.isalpha() for ch in flight_num[0:2]]) and \
        #        all([ch.isdigit() for ch in flight_num[2:]])

        list=[False]*len(flight_num)
        if flight_num[0].isalpha():
            list[0]=True
        if flight_num[1].isalpha():
            list[1]=True
        for p, ch in enumerate(flight_num[2:]):
            if ch.isdigit(): list[p+2] = True
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


    def __str__(self):
        flight_str = "Flight number: " + self.flight_num
        flight_str += "\nDeparture: " + self.format_departure(self.departure)
        flight_str += "\nOrigin: " + self.origin
        flight_str += "\nDestination: " + self.destination
        flight_str += "\nOperated by: " + self.operated_by

        if len(self.passengers) == 0:
            flight_str += "\nNo passenger yet registered."
        else:
            flight_str += "\n\n"
            flight_str += "\n\n".join([str(p) for p in self.passengers])

        return flight_str


    @staticmethod
    def format_departure(departure):
        if isinstance(departure, str):
            return departure

        try:
            return datetime.strftime(departure, "%Y/%m/%d %H/%M")
        except TypeError as err:
            print("Error while formatting departure:\n{}".format(err))
            return "undefined"

    @classmethod
    def from_Frankfurt_by_Lufthansa(cls, flight_num, departure):
        return cls(flight_num, departure, origin="Frankfurt", operated_by="Lufthansa")


    def generate_non_checkedin_list(self):
        for p in self.passengers:
            if not p.checked_in:
                yield p


    def generate_upgrade_candidates(self, min_miles):
        candidates = [p for p in self.passengers
                       if isinstance(p, EconomyPassenger) and p.candidate_for_upgrade(min_miles)]
        candidates = sorted(candidates, key=lambda passenger: passenger.air_miles, reverse=True)
        for candidate in candidates:
            yield candidate


if __name__ == '__main__':

    lh1411 = Flight('LH1411', '2018-11-03 6:50', origin='Belgrade', destination='Frankfurt')
    print(lh1411)
    print()

    lh992 = Flight.from_Frankfurt_by_Lufthansa('LH992', '2018-11-03 12:20')
    # lh992.destination = "Amsterdam"
    print(lh992)
    # print()

    # bob = BusinessPassenger("Bob Smith", "123456", air_miles=1000, checked_in=True)
    # john = EconomyPassenger("John Smith", "987654", checked_in=False)
    # bill = EconomyPassenger("Billy Stone", "917253", air_miles=5000, checked_in=True)
    # dona = EconomyPassenger("Dona Stone", "917253", air_miles=2500, checked_in=False)
    # kate = EconomyPassenger("Kate Fox", "114252", air_miles=3500, checked_in=True)
    #
    # lh992.passengers.extend([bob, john, bill, dona, kate])

    # print(f"After adding passengers to flight {lh992.flight_num}:\n")
    # print(lh992)

    # print("Last call to passengers who have not yet checked in!")
    # for passenger in lh992.generate_non_checkedin_list():
    #     print(passenger)
    #     print()

    # print("Passengers offered an upgrade opportunity:")
    # for ind, passenger in enumerate(lh992.generate_upgrade_candidates(2000)):
    #     print(str(ind+1) + ".\n" + str(passenger))