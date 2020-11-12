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

from datetime import datetime

class Flight:

    departure_format = "%Y-%m-%d %H:%M"

    def __init__(self, fl_num, departure):
        self.flight_num = fl_num
        self.departure = departure
        self.passengers = list()


    @property
    def departure(self):
        return self.__departure

    @departure.setter
    def departure(self, value):
        if isinstance(value, datetime) and (value > datetime.today()):
            self.__departure = value
        elif isinstance(value, str) and (datetime.strptime(value, self.departure_format) > datetime.today()):
            self.__departure = datetime.strptime(value, self.departure_format)
        else:
            print(f"Error in setting the departure date and time")
            self.__departure = None


    def add_passenger(self, p):
        if isinstance(p, Passenger):
            if p not in self.passengers:
                self.passengers.append(p)
            else: print(str(p) + " is already in the passengers list")
        else:
            print("Error - received an object that is not of the Passenger type")


    def __str__(self):
        flight_str = f"Flight number {self.flight_num} scheduled to departure at: "

        flight_str += datetime.strftime(self.departure, self.departure_format) if self.departure else "still unknown"

        if len(self.passengers) == 0:
            flight_str += "\nStill no passengers checked for the flight."
        else:
            flight_str += "\nPassengers:\n" + "\n".join([str(p) for p in self.passengers])

        return flight_str


    def time_to_departure(self):
        time_diff = self.departure - datetime.today()
        days = time_diff.days
        secs_in_hour = 60*60
        hours, remainder_secs = divmod(time_diff.seconds, secs_in_hour)
        return days, hours, remainder_secs//60


    def __iter__(self):
        self.__iter_counter = 0
        return self


    def __next__(self):
        if self.__iter_counter == len(self.passengers):
            raise StopIteration
        else:
            current_passenger = self.passengers[self.__iter_counter]
            self.__iter_counter += 1
            return current_passenger



if __name__ == '__main__':

    bob = Passenger("Bob Smith", "123456", True)
    john = Passenger("John Smith", 987656, False)
    jane = Passenger("Jane Smith", '987659')

    print(bob)
    print(john)
    print(jane)

    print("Checking if 'bob' and 'john' refer to the same passenger")
    print(bob == john)
    print(f"Checking if 'john' refers to the passenger 'Joe Smith', with passport number: 987656")
    print(john == Passenger("Joe Smith", "987656"))


    lh1411 = Flight('LF1411', '2020-12-05 6:50')
    lh992 = Flight('LH992', '2020-11-25 12:20')
    print()
    print(lh1411)
    print()
    print(lh992)

    print()

    lh1411.add_passenger(bob)
    lh1411.add_passenger(john)
    lh1411.add_passenger(jane)
    lh1411.add_passenger(Passenger("Jane Smith", "987659", False))
    print()

    print(f"After adding passengers to flight {lh1411.flight_num}:")
    print(lh1411)

    print()

    days, hours, mins = lh1411.time_to_departure()
    print(f"Time till departure of the flight {lh1411.flight_num}: {days} days, {hours} hours, and {mins} minutes")

    print()
    print("Passengers on flight lh1411:")
    flight_iter = iter(lh1411)
    try:
        print(next(flight_iter))
        print(next(flight_iter))
        print(next(flight_iter))
        print(next(flight_iter))
    except StopIteration:
        print("No more passengers")

    print()

    print("Passengers on flight lh1411 (for loop):")
    for passenger in lh1411:
        print(passenger)
