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

    def __init__(self, title, year, director='', reviews=None):
        self.title = title
        self.year = year
        self.director = director
        self.reviews = reviews

        self.__i = 0                # iterator counter

    def __str__(self):
        m = self.title + '\n'
        m += '\tyear: ' + str(self.year) if self.year else '' + '\n'
        m += '\tdirected by: ' + self.director + '\n' if self.director else 'unknown' + '\n'
        m += '\treviews\n'
        m += '\t\t\n'.join([str(r) for r in self.reviews]) if self.reviews else ''
        return m

    def __iter__(self):
        return self

    def __next__(self):
        if self.__i < len(self.reviews):
            r = self.reviews[self.__i]
            self.__i += 1
            return r
        else:
            raise StopIteration


class MovieReview:

    def __init__(self, rating, comment):
        self.rating = rating
        self.comment = comment

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        self.__rating = rating if rating in range(1, 6) \
            else print('Error: rating must be between 1 and 5')

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment):
        self.__comment = comment if isinstance(comment, str) else 'no comment yet'

    def __str__(self):
        return '\tReview: ' + str(self.rating) + ', ' + self.comment


if __name__ == '__main__':

    r1 = MovieReview(3, 'Not bad')
    r2 = MovieReview(4, 'Good')

    print(r1)
    # r2.rating = 8

    a_star_is_born = Movie("A Star is Born", 2018, "Bradley Cooper", [r1, r2])
    print(a_star_is_born)
    print()

    # for r in a_star_is_born:
    #     print(r)

    print(next(a_star_is_born))
    print(next(a_star_is_born))
    print(next(a_star_is_born))



