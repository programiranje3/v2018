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


