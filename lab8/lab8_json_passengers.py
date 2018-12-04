# The starting point for this task is the module lab6_passengers, that is,
# the Passenger class and its subclasses BusinessPassenger and EconomyPassenger.
# Your task is to create functions for
# - serialising (writing) objects of the class Passenger and its subclasses
#   into a .json file
# - deserializing (reconstructing) objects of the class Passenger and its subclasses
#   from a .json file (created using the previous function)


from lab6.lab6_passengers import Passenger, BusinessPassenger, EconomyPassenger
import json
from sys import stderr

known_classes = {
    'Passenger' : Passenger,
    'BusinessPassenger' : BusinessPassenger,
    'EconomyPassenger' : EconomyPassenger
}

def serialise_to_json(obj):

    obj_type = type(obj).__name__

    if obj_type in known_classes.keys():
        obj_dict = {'__classname__': obj_type}
        obj_dict.update(vars(obj))
        return obj_dict
    else:
        known_types = ", ".join(known_classes.keys())
        raise TypeError("Error! Cannot serialise objects of type '{}'. "
                        "Can only serialise objects "
                        "of these types: {}".format(obj_type, known_types))


def deserialise_from_json(json_obj):

    try:
        cls_name = json_obj['__classname__']
    except KeyError as key_err:
        stderr.write("Error! No '__classname__ key':\n{}".format(key_err))
        return json_obj

    if cls_name in known_classes.keys():
        cls = known_classes[cls_name]
        obj = cls.__new__(cls)
        for key, val in json_obj.items():
            setattr(obj, key, val)
        return obj
    else:
        stderr("Error! Cannot deserialise objects of type {}".format(cls_name))
        return json_obj



if __name__ == '__main__':

    bob = BusinessPassenger("Bob Smith", "123456", air_miles=1000, checked_in=True)
    # print(bob)
    # print(bob.__dict__)

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

    # with open("passengers.json", 'w') as f:
    #     json.dump(passengers, f, default=serialise_to_json, indent=4)

    with open('passengers.json', 'r') as f:
        passengers_copy = json.load(f, object_hook=deserialise_from_json)
        for p in passengers_copy:
            print(p)
            print()