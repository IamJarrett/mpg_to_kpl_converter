"""
A test for the conversion of MPG to MPL
"""

# import the code to be tested
from units_converter import mpg2kpl


def describe_a_set_of_units_converters():
    def that_can_convert_mpg_to_kpl():
        """
        test the mpgtokpl function
        """
        assert mpg2kpl(50) == 21.2572


def that_can_convert_mpg_to_kpl_to_2_decimal_places():
    """
    allows the user to specify to 2 decimal places instead of 4.
    The 2nd parameter indicates the precison.
    """
    assert mpg2kpl(50, 2) == 21.25
