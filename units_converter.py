"""
A converter of MPG to GPL
"""


# useful constants
KPM = 1.609344  # kilometers per mile
GPL = 0.2641720524  # gallons per liter


def mpg2kpl(mpg, precision=4):
    """
    Converts MPG to KPL to 4 decimal places
    """
    return round(mpg * KPM * GPL, 4)
