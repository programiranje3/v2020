#
# Create the FlightService enumeration that defines the following items (services):
# (free) snack, (free) refreshments, (free) meal, priority boarding,
# (free) onboard wifi, and an item for cases when services are not specified.
#




#
# Modify the Passenger class from Lab5 as follows:
#
# In addition to the *name* and *passport* attributes, the class should also have
# the following attributes:
# - *air_miles* - the number of air miles the passenger has accumulated
# - *checked_in* - a boolean indicator, true if the passenger has checked in
# - *services* - a class attribute defining the list of services available to all
#   passengers of a particular class (category); available services for various categories
#   of passengers should be defined as elements of the FlightService enumeration.
#   For the Passenger class, services are unspecified as they depend on the passenger
#   category (will be defined in the subclasses).
# Note that the attribute *is_business* (from Lab 5 version of the Passenger class) is dropped,
# as the passenger category will be handled through (Python) class hierarchy.
#
# The following methods of the Passenger class need to be revised:
#
# - constructor (__init__()) - it should receive 4 input arguments, one for
#   each attribute; only the arguments for the passenger's name and passport
#   have to be specified; the argument for *air_miles* has None as its default value,
#   while False is the default value for *checked_in*.
#
# - a method that returns a string representation of a given Passenger object (__str__())
#   so that it describes a passenger with the extended set of attributes.
#
# Finally, the following new methods should be added:
#
# - get and set methods (using appropriate decorators) for the *air_miles* attribute;
#   the set method should assure that a non-negative integer value is assigned to this attribute
#
# - a class method (available_services()) that returns a list of strings describing services
#   available to the passengers; this list is created based on the *services* class attribute.
#


class Passenger:

    def __init__(self, name, passport, business=False):
        self.name = name
        self.passport = passport
        self.is_business = business

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, value):
        if (isinstance(value, str)) and (len(value) == 6) and (all([ch.isdigit() for ch in value])):
            self.__passport = value
        elif (isinstance(value, int)) and (len(str(value)) == 6):
            self.__passport = str(value)
        else:
            print("Error! Incorrect passport number! Setting passport to None")
            self.__passport = None


    def __str__(self):
        passenger_str = f"passenger {self.name}, passport number: " + (self.passport if self.passport else "unknown")
        return "Business class " + passenger_str if self.is_business else ("Economy class " + passenger_str)


    def __eq__(self, other):
        if isinstance(other, Passenger):
            if self.passport and other.passport:
                return (self.name == other.name) and (self.passport == other.passport)
            else:
                print(f"Cannot determine equality since at least one of the passengers does not have passport number")
                return False
        else:
            print("The other object is not of the Passenger type")
            return False


#
# Create the EconomyPassenger class that extends the Passenger class and has:
#
# - method candidate_for_upgrade that checks if the passenger is a candidate for an upgrade
#   and returns an appropriate boolean value; a passenger is a candidate for an upgrade if
#   their current air miles exceed the given threshold (input parameter) and the passenger
#   has checked in
#
# - changed value for the *services* class attribute so that it includes snack and refreshments
#   (as elements of the FlightServices enum)
#
# - overridden __str__ method so that it first prints "Economy class passenger" and then
#   the available information about the passenger
#





#
# Create class BusinessPassenger that extends the Passenger class and has:
#
# - changed value for the services class attribute, so that it includes:
#   priority boarding, meal, digital entertainment, and onboard wifi
#
# - overridden __str__ method so that it first prints "Business class passenger" and then
#   the available information about the passengers
#





if __name__ == '__main__':

    pass

    # jim = EconomyPassenger("Jim Jonas", '123456', air_miles=1000)
    # # jim.services = [FlightService.onboard_wifi, FlightService.meal]
    # print(jim)
    # print(jim.__dict__)
    # print(jim.available_services())
    # print()
    #
    # bob = EconomyPassenger("Bob Jones", '987654', checked_in=True)
    # print(bob)
    # bob.air_miles = '20200'
    # print(bob.__dict__)
    # print(bob.available_services())
    # print()
    #
    # mike = BusinessPassenger("Mike Stone", '234567', air_miles=2000)
    # print(mike)
    # print(mike.__dict__)
    # print(mike.available_services())