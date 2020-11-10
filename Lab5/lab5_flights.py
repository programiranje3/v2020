# Create the Passenger class with the following methods:
#
# - a constructor (__init__()) that receives three input arguments
#   that are used to initialise the following 3 attributes:
#   - name - the passenger's name and surname
#   - passport - the passenger's passport number
#   - is_business - a boolean indicator variable (true if the passenger is in the business class);
#     the default value of this argument is False
#
# - get and set methods for the *passport* attribute (using appropriate decorators);
#   designate this attribute as private and assure that it is a string of length 6,
#   consisting of digits only
#
# - a method that returns a string representation of a Passenger object (__str__())
#
# - a method that checks for equality of the given Passenger object and another object
#   that is passed to the method as its input parameter (__eq__()); two passenger objects
#   are considered the same if they have the same name and passport number









# Create the Flight class with the following elements:
#
# - class attribute *departure_format* representing the expected format for
#   the departure date and time; its value should be "%Y-%m-%d %H:%M"
#   (for datetime formatting codes, check this table:
#   https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
#
# - a constructor (__init__()) that receives two input parameters and uses them
#   to initialise *flight_num* (flight number) and *departure* (departure date and time)
#   attributes; it also initialises the *passengers* attribute (list of objects of
#   the Passenger class) to an empty list
#
# - get and set methods for the *departure* attribute (using appropriate decorators);
#   make this attribute private and assure that it is a datetime object and refers to
#   a moment in the future
#
# - a method for adding a passenger to the *passengers* list; the method adds a new
#   passenger only if the input parameter is really of the Passenger class and if the
#   passenger is not already in the list
#
# - a method that returns a string representation of the given Flight object (__str__())
#
# - a method that returns the time left till departure as a tuple of the form (days, hours, mins)
#
# - methods for turning the given Flight object into an iterator (__iter__(), __next__())
#   over the flight passengers (that is, elements of the *passengers* list)






if __name__ == '__main__':

    pass

    # bob = Passenger("Bob Smith", "123456", True)
    # john = Passenger("John Smith", 987656, False)
    # jane = Passenger("Jane Smith", '987659')
    #
    # print(bob)
    # print(john)
    # print(jane)
    #
    # print("Checking if 'bob' and 'john' refer to the same passenger")
    # print(bob == john)
    # print(f"Checking if 'john' refers to the passenger 'Joe Smith', with passport number: 987656")
    # print(john == Passenger("Joe Smith", "987656"))


    # lh1411 = Flight('LF1411', '2020-12-05 6:50')
    # lh992 = Flight('LH992', '2020-11-25 12:20')
    # print()
    # print(lh1411)
    # print()
    # print(lh992)
    #
    # print()
    #
    # lh1411.add_passenger(bob)
    # lh1411.add_passenger(john)
    # lh1411.add_passenger(jane)
    # lh1411.add_passenger(Passenger("Jimmy Smith", "987658", False))
    # print()
    #
    # print(f"After adding passengers to flight {lh1411.flight_num}:")
    # print(lh1411)
    #
    # print()
    #
    # days, hours, mins = lh1411.time_to_departure()
    # print(f"Time till departure of the flight {lh1411.flight_num}: {days} days, {hours} hours, and {mins} minutes")
    #
    # print()
    #
    # print("Passengers on flight lh1411:")
    # for passenger in lh1411:
    #     print(passenger)
