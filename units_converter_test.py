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
        assert mpg2kpl(50) == 21.2571854
