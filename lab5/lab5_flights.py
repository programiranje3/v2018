# Create the Flight class with the following attributes:
# - flight_num - flight number
# - departure - the date and time of the departure
# - origin - the location the flight departs from
# - destination - the destination of the flight
# - passengers - list of passengers, that is, instances of the Passenger class
#                (another class to be created in this task, see below)
#
# Use appropriate decorators to create get and set method for the departure attribute;
# make it a private attribute and assure that it is a datetime object of the format:
# "%Y-%m-%d %H:%M"; consider defining this format as a class attribute (departure_format)
#
# The Flight class should implement the following methods:
# - constructor (__init__())
# - method that returns a string representation of the given Flight object (__str__())
# - method that checks for equality of the given Flight object and another object
#   that is passed to the method as its input parameter (__eq__())
# - methods for turning the given Flight object into an iterator (__iter__(), __next__())

# Create the Passenger class with the following attributes:
# - name - passenger name and surname
# - passport - passenger's passport number
# - is_business - a boolean indicator variable (true if the passenger is in the business class)
#
# Use appropriate decorators to create get and set method for the passport attribute;
# designate it as a private attribute and assure that it is a string of length 6,
# consisting of digits only.
# In addition, implement the method that returns a string representation of a
# Passenger object (__str__()).


from datetime import datetime

class Flight:

    departure_format = "%Y-%m-%d %H:%M"  # a class attribute

    def __init__(self, flight_num, departure, origin = "unknown", destination = "unknown", passengers = []):
        self.flight_num = flight_num
        self.departure = departure
        self.origin = origin
        self.destination = destination
        self.passengers = passengers

        self.passenger_index = 0


    @property
    def departure(self):
        return self.__departure


    @departure.setter
    def departure(self, departure):
        """Expecting departure date and time in the form: %Y-%m-%d %H:%M"""
        try:
            self.__departure = datetime.strptime(departure, self.departure_format)
        except ValueError as error:
            print(error)
            print(f"Error! Departure expected in the format: '{self.departure_format}'")


    def __str__(self):
        flight_str = "Flight number: " + self.flight_num + \
                     "\nDeparture date/time: " + datetime.strftime(self.departure, self.departure_format) + \
                     "\nOrigin: " + self.origin + "\nDestination: " + self.destination

        if len(self.passengers) == 0:
            flight_str += "\nNo passengers registered yet"
        else:
            flight_str += "\nPassengers:\n"
            flight_str += "\n".join(["\t" + str(p) for p in self.passengers])

        return flight_str


    def __eq__(self, other):
        """Two flights are considered equal if they have the same flight number and departure date"""
        if self.__class__ != other.__class__:
            return False
        return (self.flight_num == other.flight_num) and (self.departure == other.departure)


    def __iter__(self):
        """Iterator through the passengers list"""
        return self


    def __next__(self):
        if self.passenger_index == len(self.passengers):
            raise StopIteration
        current_passenger = self.passengers[self.passenger_index]
        self.passenger_index += 1
        return current_passenger



class Passenger:

    def __init__(self, name, passport, is_business):
        self.name = name
        self.passport = passport
        self.is_business = is_business

    def __str__(self):
        passenger_str = "Passenger: " + self.name + \
                        " passport number: " + self.passport + " class: "
        passenger_str += "bussiness" if self.is_business else "economy"
        return passenger_str

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        """Passport number has to be a string of length 6, consisting of digits only"""
        if (len(passport) == 6) and self.all_digits(passport):
            self.__passport = passport
        else:
            print("Error! Passport number has to be a string of length 6, consisting of digits only")

    def all_digits(self, str_val):
        for ch in str_val:
            if not ch.isdigit():
                return False
        return True



if __name__ == '__main__':

    lh1411 = Flight('LF1411', '2018-11-03 6:50', origin='Belgrade', destination='Frankfurt')
    lh992 = Flight('LH992', '2018-11-03 12:20', origin='Frankfurt', destination='Amsterdam')
    print(lh1411)
    print()
    print(lh992)

    print()

    bob = Passenger("Bob Smith", "123456", True)
    john = Passenger("John Smith", "987654", False)
    lh1411.passengers.extend([bob, john])

    print(f"After adding passengers to flight {lh1411.flight_num}:")
    print(lh1411)