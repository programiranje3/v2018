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
