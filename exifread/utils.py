"""
Misc utilities.
"""

from fractions import Fraction
from typing import Optional, Tuple


def _degrees_to_decimal(degrees: float, minutes: float, seconds: float) -> float:
    """
    Converts coordinates from a degrees minutes seconds format to a decimal degrees format.
    Reference: https://en.wikipedia.org/wiki/Geographic_coordinate_conversion
    """
    pass


def get_gps_coords(tags: dict) -> Optional[Tuple[float, float]]:
    """
    Extract tuple of latitude and longitude values in decimal degrees format from EXIF tags.
    Return None if no GPS coordinates are found.
    Handles regular and serialized Exif tags.
    """
    pass


class Ratio(Fraction):
    """
    Ratio object that eventually will be able to reduce itself to lowest
    common denominator for printing.
    """

    _numerator: Optional[int]
    _denominator: Optional[int]

    # We're immutable, so use __new__ not __init__
    def __new__(cls, numerator: int = 0, denominator: Optional[int] = None):
        try:
            self = super(Ratio, cls).__new__(cls, numerator, denominator)
        except ZeroDivisionError:
            self = super(Ratio, cls).__new__(cls)
            self._numerator = numerator
            self._denominator = denominator
        return self

    def __repr__(self) -> str:
        return str(self)

    @property
    def num(self) -> int:
        pass

    @property
    def den(self) -> int:
        pass

    def decimal(self) -> float:
        pass
