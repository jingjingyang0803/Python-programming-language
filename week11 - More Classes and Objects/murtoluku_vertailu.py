"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 11.6 - Comparisons of fractions:


Learning Goals:
Getting acquainted with the comparison methods (__lt__, __le__ jne.)
 presented in Python documentation.
"""

class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def __lt__(self, other):
        """
        Returns True if the fraction is less than another fraction, False
        otherwise.

        :param other: Fraction, the fraction to be compared with
        """
        difference = self.deduct(other)
        return difference.__numerator * difference.__denominator < 0

    def __gt__(self, other):
        """
        Returns True if the fraction is greater than another fraction, False
        otherwise.

        :param other: Fraction, the fraction to be compared with
        """
        difference = self.deduct(other)
        return difference.__numerator * difference.__denominator > 0

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        """
        Simplifies the fraction by dividing both the numerator and the
         denominator by their greatest common divisor.
        """
        common_divisor = greatest_common_divisor(self.__numerator,
                                                 self.__denominator)

        # Update the numerator and denominator
        # Covert float from division operation into int before assigning
        self.__numerator = int(self.__numerator / common_divisor)
        self.__denominator = int(self.__denominator / common_divisor)

    def complement(self):
        """
        Return the complement of the fraction.

        :returns: Fraction, the complement of the fraction.
        """
        numerator = self.__numerator * -1
        denominator = self.__denominator
        return Fraction(numerator, denominator)

    def reciprocal(self):
        """
        Return the reciprocal of the fraction.
        """
        # Swapping the numerator and denominator to get the reciprocal of
        # the fraction.
        return Fraction(self.__denominator, self.__numerator)

    def multiply(self, other_fraction):
        """
        Return the multiplication of the fraction with another fraction.

        :param other_fraction: Fraction, the fraction to be multiplied with

        :returns: Fraction,
                  the multiplication of the fraction with another fraction
        """
        # Multiply the numerators and denominators together
        numerator=self.__numerator * other_fraction.__numerator
        denominator=self.__denominator * other_fraction.__denominator
        return Fraction(numerator, denominator)

    def divide(self, other_fraction):
        """
        Return the divisor of the fraction with another fraction.

        :param other_fraction: Fraction, the fraction to be divided with

        :returns: Fraction,
                  the divisor of the fraction with another fraction
        """
        # Dividing by a fraction is the same as multiplying with its
        # reciprocal.
        other_fraction_reciprocal=other_fraction.reciprocal()
        return self.multiply(other_fraction_reciprocal)

    def add(self, other_fraction):
        """
        Return the sum of the fraction with another fraction.

        :param other_fraction: Fraction, the fraction to be added to the
        current fraction.

        :returns: Fraction,
                  the sum of the fraction with another fraction
        """
        common_denominator = self.__denominator * other_fraction.__denominator
        numerator = (self.__numerator * other_fraction.__denominator
                             + other_fraction.__numerator * self.__denominator)
        denominator = common_denominator
        return Fraction(numerator, denominator)

    def deduct(self, other_fraction):
        """
        Returns the deduction of the fraction with another fraction.

        :param other_fraction: Fraction, the fraction to be deduced from the
        current fraction.

        :returns: Fraction,
                  the deduction of the fraction with another fraction
        """
        common_denominator = self.__denominator * other_fraction.__denominator
        numerator = (self.__numerator * other_fraction.__denominator
                             - other_fraction.__numerator * self.__denominator)
        denominator = common_denominator
        return Fraction(numerator, denominator)


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a

