# Create the FlightService enumeration that defines the following items (services):
# snack, free e-journal, priority boarding, selection of food and drinks,
# free onboard wifi, and an item for cases when services are not specified.
#
# Create the Passenger class with the following attributes:
# - name - passenger name and surname
# - passport - passenger's passport number (as string); private attribute
# - air_miles - the number of miles the passenger has made with the given air company;
#   zero if not specified
# - checked_in - a boolean indicator variable, true if the passenger has checked in;
#   False if not specified
# - services - a class attribute defining the list of services available to all
#   passengers of a particular class (category); available services for various categories
#   of passengers should be defined as elements of the FlightService enumeration.
#   For this class, services are undefined (FlightService.UNDEFINED), as they depend on
#   the passenger's class and will be defined in the subclasses.
#
# In addition, the Passenger class should implement the following methods:
# - constructor (__init__()) - only name and passport have to be specified
# - get and set methods for the passport attribute (using appropriate decorators);
#   designate it as a private attribute and assure that it is a string of length 6,
#   consisting of digits only.
# - a method that returns a string representation of a Passenger object (__str__())
# - a method (available_services()) that returns a list of strings describing services
#   available to the passengers (a class method); this list is created based on the
#   services attribute.
#
# Create class EconomyPassenger that extends the Passenger class and has:
# - method candidate_for_upgrade that check if the passenger is a candidate for an upgrade
#   and returns an appropriate boolean value; a passenger is a candidate for upgrade if their
#   their current air miles exceed the given threshold (input parameter) and the passenger
#   has checked in
# - changed value for the services class attribute, which includes the following elements of
#   the FlightServices enum: snack, free e-journal
# - overridden __str__ method so that it first prints "Economy class passenger" and then
#   the available information about the passenger
#
# Create class BusinessPassenger that extends the Passenger class and has:
# - changed value for the services class attribute, so that it includes the following elements of
#   the FlightServices enum: priority boarding, selection of food and drinks, free onboard wifi
# - overridden __str__ method so that it first prints "Business class passenger" and then
#   the available information about the passengers

from enum import Enum

class FlightService(Enum):
    """snack, free e-journal, priority boarding, selection of food and drinks,
    free onboard wifi, and an item for cases when services are not specified.
    """
    SNACK = "Snack"
    FREE_EJOURNAL = "Free e-journal"
    PRIORITY_BOARDING = "Priority boarding"
    FOOD_AND_DRINKS = "Selection of food and drinks"
    ONBOARD_WIFI = "Free onboard wifi"
    UNDEFINED = "undefined"

class Passenger:
    services = [FlightService.UNDEFINED]

    def __init__(self, name, passport, air_miles=0, checked_in=False):
        self.name = name
        self.passport = passport
        self.air_miles = air_miles
        self.checked_in = checked_in

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        if not isinstance(passport, str):
            passport = str(passport)
        if self.passport_format_ok(passport):
            self.__passport = passport
        else:
            print("Error! Passport has to consist of 6 digits exactly")
            self.__passport = "unknown"

    @staticmethod
    def passport_format_ok(passport):
        if len(passport) != 6:
            return False
        all_digits = [ch.isdigit() for ch in passport]
        return all(all_digits)

    @classmethod
    def available_services(cls):
        return [service.value for service in cls.services]

    def __str__(self):
        passenger_str = self.name
        passenger_str += "\nPassport: " + self.passport
        passenger_str += "\nAir miles: " + str(self.air_miles)
        passenger_str += "\nCompleted check-in: " + ("YES" if self.checked_in else "NO")
        passenger_str += "\nServices: " + ", ".join(self.available_services())
        return passenger_str


class EconomyPassenger(Passenger):

    services = [FlightService.SNACK, FlightService.FREE_EJOURNAL]

    def candidate_for_upgrade(self, min_miles):
        return self.checked_in and self.air_miles > min_miles

    def __str__(self):
        return "Economy class passenger:\n" + super().__str__()


class BusinessPassenger(Passenger):

    services = [FlightService.FOOD_AND_DRINKS, FlightService.PRIORITY_BOARDING,
                FlightService.ONBOARD_WIFI]

    def __str__(self):
        return "Business class passenger:\n" + super().__str__()


if __name__ == "__main__":

    bob = EconomyPassenger("Bob", "123456", 2500, True)
    print(bob)
    print()

    mike = EconomyPassenger("Mike", "123987")
    print(mike)
    print()

    print(bob.candidate_for_upgrade(2000))
    print(mike.candidate_for_upgrade(2000))

    jane = BusinessPassenger("Jane", "345678", checked_in=True)
    print(jane)