# Create the MovieReview class with the following methods:
#
# - a constructor (__init__()) that receives two input parameters that are used to initialise
#   attributes *rating* and *comment*, respectively. Default value for the 2nd input parameter
#   is an empty string. The constructor also sets the value of the *timestamp* attribute to the
#   current date and time.
#
# - get and set methods for the *rating* and *comment* attributes (using appropriate decorators);
#   designate both attributes as private; valid values for these two attributes are as follows:
#   - for *rating*: int values between 1 and 5, including 1 and 5
#   - for *comment*: any string value
#
# - a method that returns a string representation of a MovieReview object (__str__())

from datetime import datetime

class MovieReview:

    def __init__(self, rating, comment=""):
        self.rating = rating
        self.comment = comment
        self.timestamp = datetime.today()

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if isinstance(value, int) and 1 <= value <= 5:
            self.__rating = value
        elif isinstance(value, str) and (len(value) == 1) and (value in '12345'):
            self.__rating = int(value)
        else:
            print(f"Invalid value ({value}) passed for movie rating")
            self.__rating = None

    @property
    def comment(self):
        return self.__comment if self.__comment else ""

    @comment.setter
    def comment(self, value):
        if isinstance(value, str):
            self.__comment = value
        else:
            print(f"Error! String value expected, received {type(value)} instead. Coercing the input to a string")
            self.__comment = str(value)

    def __str__(self):
        s = f"{self.rating} stars; " if self.rating else "Rating not available; "
        s += f"comment: '{self.comment}'" if self.comment else "no comment left"
        s += f"(received {datetime.strftime(self.timestamp, '%b %d, %Y %H:%M')})"
        return s


# Create the Movie class with the following methods:
#
# - a constructor (__init__()) that receives three input parameters to be used to initialise
#   attributes *title*, *year*, and *director*, respectively. Default value for the 3rd input
#   parameter is None. The constructor also initializes the *reviews* attribute
#   (a list of MovieReview objects) to an empty list.
#
# - a method that returns a string representation of the given Movie object (__str__())
#
# - a method for adding a new review to the Movie objects, that is, to the *reviews* list.
#   The review to be added is passed as the input argument; it is added to the list, only
#   if it is an object of the MovieReview class and the review is not older than 1 year.
#   (a useful StackOverflow entry:
#   https://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python)
#
# - a method (__eq__()) for checking for equality of the given Movie object and another
#   object that is passed to the method as its input parameter. Two Movie objects are
#   considered the same if they have the same title and director, or, if the director is
#   unknown, then the same title and year.
#
# - methods for turning the given Movie object into an iterator (__iter__(), __next__())
#   over the movie reviews (that is, elements of the *reviews* list)
#

class Movie:

    def __init__(self, title, year, director=None):
        self.title = title
        self.year = year
        self.director = director
        self.reviews = list()


    def __str__(self):
        movie_str = f"Movie '{self.title}' from {self.year}"
        movie_str += f" directed by {self.director}" if self.director else " (director unknown)"
        if len(self.reviews) > 0:
            movie_str += "\nReviews:\n" + "\n".join([str(mr) for mr in self.reviews])
        else:
            movie_str += ", no reviews yet"
        return movie_str


    def add_review(self, review):
        if isinstance(review, MovieReview):
            time_diff = datetime.today() - review.timestamp
            time_diff_sec = time_diff.total_seconds()
            secs_in_year = 365*24*60*60
            time_diff_year = time_diff_sec // secs_in_year # integer division
            if time_diff_year < 1:
                self.reviews.append(review)
            else:
                print("An outdated review")
        else:
            print("Not an object of MovieReview class; cannot be added")


    def __eq__(self, other):
        if isinstance(other, Movie):
            if self.director and other.director:
                return (self.title == other.title) and (self.director == other.director)
            else:
                print("Director(s) unknown; checking for equality based on the title-year pair")
                return (self.title == other.title) and (self.year == other.year)
        else:
            print("The other object is not a Movie")
            return False


    def __iter__(self):
        self.__review_counter = 0
        return self

    def __next__(self):
        if self.__review_counter == len(self.reviews):
            raise StopIteration

        current_review = self.reviews[self.__review_counter]
        self.__review_counter += 1
        return current_review


if __name__ == '__main__':

    mr_1 = MovieReview(5, "Superb!")
    mr_2 = MovieReview(5, "The best ever!")
    mr_3 = MovieReview(3, "Expected more...")

    # print(mr_1)
    # print(mr_2)
    # print(mr_3)

    godfather = Movie("The Godfather", year=1972, director="Francis Ford Coppola")
    print(godfather)

    print()

    godfather_2 = Movie("The Godfather: part II", 1974, "Francis Ford Coppola")
    print(godfather_2)

    print()

    if godfather == godfather_2:
        print("No difference observed!")
    else:
        print("Different movies!")

    print()

    for mr in (mr_1, mr_2, mr_3):
        godfather_2.add_review(mr)

    print("Printing movie data after adding reviews")
    print(godfather_2)

    print("\nReviews for the Godfather 2 movie:")
    for review in godfather_2:
        print(review)