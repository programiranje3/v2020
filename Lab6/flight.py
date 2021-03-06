# Modify the Flight class from Lab5 as follows:
#
# In addition to the flight_num, departure, and passengers attributes,
# the class should also have the following attributes:
# - *route* - the route of the flight as a tuple of the form (origin, destination)
# - *operated_by* - the company that operates the flight
#
# The following methods of the Flight class need to be revised:
#
# - the constructor (__init__()) - it should receive 4 input arguments, one for
#   each attribute, but only the arguments for the flight number and the departure
#   have to be specified; *route* and *operator* arguments have default value None.
#
# - the set method for the *departure* attribute, so that it properly handles situations
#   when departure date and time are given as a string in an unknown format (that is, in the
#   format other than the *departure_format*)
#
# - the method that returns a string representation of the given Flight object (__str__())
#   so that it describes the flight with the extended set of attributes
#
# Finally, the following new methods should be added:
#
# - get and set methods (using appropriate decorators) for the *route* attribute; the set method
#   should allow for different ways of setting the route, that is, it should be able to handle input
#   value given as a list or a tuple (of two elements) or a string with the origin and destination
#   separated by a comma (Belgrade, Rome), a hyphen (Belgrade - Rome), or a '>' char (Belgrade > Roma)
#   (Hint: consider using split method from the re (regular expressions) module)
#
# - the class method from_Belgrade_to_Frankfurt() for creating flights from Belgrade to Frankfurt
#   (alternative constructor); the method receives flight number and the scheduled departure date and time.
#
# - a class method for creating a Flight object (alternative constructor) out of the flight-related
#   data provided as a dictionary with the following keys: fl_num, origin, destination, departure,
#   operator. Consider that the input value might not contain the expected dictionary elements, that is,
#   dictionary keys might not match the expected ones.
#
# - a generator method that generates a sequence of passengers who have not yet checked in;
#   at the end - after yielding all those who haven't checked in - the method prints the number of
#   such passengers
#
# - a generator method that generates a sequence of candidate passengers for an upgrade to
#   the business class; those are the passengers of the economy class whose air miles
#   exceed the given threshold (input parameter) and who have checked in for the flight;
#   the generated sequence should consider the passengers air miles, so that those with more
#   air miles are first offered the upgrade option.

from datetime import datetime
from sys import stderr
from Lab6.passengers import Passenger, EconomyPassenger, BusinessPassenger

class Flight:

    departure_format = "%Y-%m-%d %H:%M"

    def __init__(self, fl_num, departure, route=None, operator=None):
        self.flight_num = fl_num
        self.departure = departure
        self.route = route
        self.operator = operator

        self.passengers = list()


    @property
    def departure(self):
        return self.__departure

    @departure.setter
    def departure(self, value):
        self.__departure = None

        if isinstance(value, datetime) and (value > datetime.today()):
            self.__departure = value
        elif isinstance(value, str):
            try:
                value_dt = datetime.strptime(value, self.departure_format)
                if value_dt > datetime.today():
                    self.__departure = value_dt
                else:
                    print("Error! The departure has to be a date and time in the future")
            except ValueError as err:
                stderr.write(f"Error while processing departure input: {err}\n")
        else:
            print(f"Error in setting the departure date and time")


    @property
    def route(self):
        return self.__route

    @route.setter
    def route(self, value):
        import re

        if isinstance(value, (list, tuple)) and (len(value) == 2):
            self.__route = tuple(value)
        elif isinstance(value, str) and (len(re.split('[,->]', value)) == 2):
            origin, destination = re.split('[,->]', value)
            self.__route = origin.rstrip(), destination.lstrip()
        else:
            print("Error! Route value cannot be interpreted")
            self.__route = None


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

        if self.route:
            origin, dest = self.route
            flight_str += f"\nFlying from {origin if origin else '[unknown]'} to {dest if dest else '[unknown]'}"
        else:
            flight_str += "Flying route not set"

        flight_str += f"\nFlight operated by {self.operator if self.operator else '[unknown]'}"

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


    @classmethod
    def from_Belgrade_to_Frankfurt(cls, flight_num, departure_dt):
        return cls(flight_num, departure_dt, 'Belgrade, Frankfurt')


    @classmethod
    def from_dict(cls, flight_dict):
        # fl_num, origin, destination, departure, operator
        try:
            return cls(flight_dict['fl_num'], flight_dict['departure'],
                       (flight_dict['origin'], flight_dict['destination']),
                       flight_dict['operator'])
        except KeyError as err:
            stderr.write(f"An error occurred while reading from the flight-related dictionary:\nErroneous key:{err}\n")
            stderr.write("Creating a Flight object with the available valid data\n")

            return cls(cls.value_or_None(flight_dict, 'fl_num'),
                       cls.value_or_None(flight_dict, 'departure'),
                       (cls.value_or_None(flight_dict, 'origin'), cls.value_or_None(flight_dict, 'destination')),
                       cls.value_or_None(flight_dict, 'operator'))

    @staticmethod
    def value_or_None(d, key):
        return d[key] if key in d.keys() else None


    def not_checked_in(self):
        not_checked_in_count = 0
        for p in self.passengers:
            if not p.checked_in:
                not_checked_in_count += 1
                yield p

        print(f"{not_checked_in_count} passengers have not checked in yet")


    def candidates_for_upgrade(self, min_air_miles):
        candidates = (p for p in self.passengers
                      if isinstance(p, EconomyPassenger) and p.candidate_for_upgrade(min_air_miles))
        for c in sorted(candidates, key=lambda c: c.air_miles, reverse=True):
            yield c



if __name__ == '__main__':


    lh1411 = Flight('LH1411', '2020-12-10 6:50', 'Belgrade > Munich')
    print(lh1411)
    print()

    lh992 = Flight.from_Belgrade_to_Frankfurt('LH992', '2020-11-29 12:20')
    lh992.operator = "Lufthansa"
    print(lh992)
    print()

    lh1514_dict = {'fl_num':'lh1514',
                   'departure': '2020-11-30 16:30',
                   'operator': 'Lufthansa',
                   'from': 'Paris',
                   'to': 'Berlin'}

    lh1514 = Flight.from_dict(lh1514_dict)
    print(lh1514)
    print()

    bob = BusinessPassenger("Bob Smith", "123456", air_miles=1000, checked_in=True)
    john = EconomyPassenger("John Smith", "987654")
    bill = EconomyPassenger("Billy Stone", "917253", 5000, True)
    dona = EconomyPassenger("Dona Stone", "917251", air_miles=2500)
    kate = EconomyPassenger("Kate Fox", "114252", 3500, checked_in=True)

    for p in [bob, john, bill, dona, kate]:
        lh992.add_passenger(p)

    print(f"After adding passengers to flight {lh992.flight_num}:\n")
    print(lh992)
    print()

    print("Last call to passengers who have not yet checked in!")
    for passenger in lh992.not_checked_in():
        print(passenger)

    print()
    print("An alternative way to iterate through passengers who have not checked in:")
    g = lh992.not_checked_in()
    try:
        while True:
            print(next(g))
    except StopIteration:
        print("--- end of check-in report ---")


    print()
    print("Passengers offered an upgrade opportunity:")
    for ind, passenger in enumerate(lh992.candidates_for_upgrade(2000)):
        print(f"{ind+1}. {passenger}")


    print()
    print("Candidates for upgrade to business class:")
    g = lh992.candidates_for_upgrade(1000)
    try:
        while True:
            print(next(g))
    except StopIteration:
        print("--- end of candidates list ---")