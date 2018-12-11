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
from datetime import datetime
import json

known_classes = {
    'Flight' : Flight,
    'EconomyPassenger': EconomyPassenger,
    'BusinessPassenger': BusinessPassenger
}

def serialise_to_json(obj):

    obj_type = type(obj).__name__

    if obj_type not in known_classes.keys():
        known_types = ", ".join(known_classes.keys())
        raise TypeError("Error! Unknown class! "
                        "Can only serialise objects of types: {}".format(known_types))

    obj_dict = {'__classname__':obj_type}
    obj_dict.update(vars(obj))

    if obj_type == 'Flight':
        dv = '_Flight__departure'
        obj_dict[dv] = datetime.strftime(obj_dict[dv], Flight.departure_format)

    return obj_dict

def deserialise_from_json(json_obj):

    try:
        cls_name = json_obj['__classname__']
    except KeyError:
        print("Error! Unknown key: __classname__")
        return json_obj

    if cls_name in known_classes.keys():
        cls = known_classes[cls_name]
        obj = cls.__new__(cls)
        for key, value in json_obj.items():
            if key == '__classname__': continue
            setattr(obj, key, value)
        return obj

    print("Error! Unknown class!")
    return json_obj

if __name__ == '__main__':

    lh992 = Flight.from_Frankfurt_by_Lufthansa('LH992', '2018-11-03 12:20')
    lh992.destination = "Amsterdam"
    print(lh992.__dict__)
    # print()

    # lh1411 = Flight('LH1411', '2018-11-03 6:50', origin='Belgrade', destination='Frankfurt')
    # # print(lh1411)
    # # print()

    bob = BusinessPassenger("Bob Smith", "123456", air_miles=1000, checked_in=True)
    john = EconomyPassenger("John Smith", "987654", checked_in=False)
    bill = EconomyPassenger("Billy Stone", "917253", air_miles=5000, checked_in=True)
    dona = EconomyPassenger("Dona Stone", "917253", air_miles=2500, checked_in=True)
    kate = EconomyPassenger("Kate Fox", "114252", air_miles=3500, checked_in=True)

    lh992.passengers.extend([bob, john, bill, dona, kate])

    # with open("flight_lh992.json", "w") as jsonf:
    #     json.dump(lh992, jsonf, default=serialise_to_json, indent=4)

    with open("flight_lh992.json", "r") as jsonf:
        lh992_copy = json.load(jsonf, object_hook=deserialise_from_json)
        print(lh992_copy)