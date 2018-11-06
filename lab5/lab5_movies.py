# Create the Movie class with the following attributes: title, year, director, reviews.
# The first three attributes are self-explanatory, whereas the reviews represents a list
# of MovieReview objects (another class to be created in this task, see below).
# Implement the following methods of the Movie class:
# - constructor (__init__())
# - method that returns a string representation of the given Movie object (__str__())
# - method for checking for equality of the given Movie object and another object
#   that is passed to the method as its input parameter (__eq__())
# - methods for turning the given Movie object into an iterator (__iter__(), __next__())
#
# Create the MovieReview class with two private attributes: rating and comment.
# Valid values for these two attributes are as follows:
# - for rating: values between 1 and 5, including 1 and 5
# - for comment: any string value
# Use appropriate decorators to create get and set methods for these attributes.
# In addition, implement the method that returns a string representation of a
# MovieReview object (__str__()).

class Movie:

    def __init__(self, title, year, director = "unknown", reviews = []):
        self.title = title
        self.year = year
        self.director = director
        self.reviews = reviews

        self.rev_index = 0

    def __str__(self):
        movie_str = self.title + "\n release year: " + str(self.year) + "\n director: " + self.director

        if len(self.reviews) == 0:
            movie_str += "\n reviews: no reviews so far"
        else:
            movie_str += "\n reviews:\n\t"
            movie_str += "\n\t".join([str(review) for review in self.reviews])

        return movie_str


    def __eq__(self, other):
        """Two Movie objects are considered equal if they have the same title and release year."""
        if self.__class__ != other.__class__:
            return False
        return (self.title == other.title) and (self.year == other.year)


    def __iter__(self):
        return self


    def __next__(self):
        if self.rev_index == len(self.reviews):
            raise StopIteration
        current_review = self.reviews[self.rev_index]
        self.rev_index += 1
        return current_review



class MovieReview:

    def __init__(self, rating, comment = ""):
        self.rating = rating        # calling the setter for self.__rating
        self.comment = comment      # calling the setter for self.__comment

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        if 1 <= rating <=5:
            self.__rating = rating
        else:
            print('Error in setting the rating value; values 1-5 only')

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment):
        if isinstance(comment, str):
            self.__comment = comment
        else:
            print('Error in setting the comment value; string values only')


    def __str__(self):
        if self.comment != "":
            return "rating: " + str(self.rating) + "; comment: " + self.comment
        else:
            return "rating: " + str(self.rating) + "; no comment provided"



if __name__ == '__main__':

    godfather = Movie("The Godfather", year=1972, director="Francis Ford Coppola")
    print(godfather)

    print()

    godfather_2 = Movie("The Godfather: part II", year=1974, director="Francis Ford Coppola")
    print(godfather_2)

    print()

    # if godfather == godfather_2:
    #     print("No difference observed!")
    # else:
    #     print("Different movies!")

    mr_1 = MovieReview(5, "Superb!")
    mr_2 = MovieReview(5, "The best ever!")
    godfather.reviews = [mr_1, mr_2]

    print("Reviews of the Godfather movie:")
    godfather_reviews = iter(godfather)
    print(next(godfather_reviews))
    print(next(godfather_reviews))