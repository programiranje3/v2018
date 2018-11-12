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