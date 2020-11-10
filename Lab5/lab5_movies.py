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





if __name__ == '__main__':

    pass

    # mr_1 = MovieReview(5, "Superb!")
    # mr_2 = MovieReview(5, "The best ever!")
    # mr_3 = MovieReview(3, "Expected more...")

    # print(mr_1)
    # print(mr_2)
    # print(mr_3)

    # godfather = Movie("The Godfather", year=1972, director="Francis Ford Coppola")
    # print(godfather)
    #
    # print()
    #
    # godfather_2 = Movie("The Godfather: part II", 1974, "Francis Ford Coppola")
    # print(godfather_2)
    #
    # print()
    #
    # if godfather == godfather_2:
    #     print("No difference observed!")
    # else:
    #     print("Different movies!")
    #
    # print()
    #
    # for mr in (mr_1, mr_2, mr_3):
    #     godfather_2.add_review(mr)
    #
    # print("Printing movie data after adding reviews")
    # print(godfather_2)
    #
    # print("\nReviews of the Godfather 2 movie:")
    # for review in godfather_2:
    #     print(review)