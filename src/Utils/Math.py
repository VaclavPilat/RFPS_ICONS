## \file
# Various math functions
import math


def sin(degrees: float) -> float:
    """A shorter syntax for calculating sinus

    Args:
        degrees (float): Angle size in degrees

    Returns:
        float: Value between 0 and 1
    """
    return math.sin(math.radians(degrees))


def cos(degrees: float) -> float:
    """A shorter syntax for calculating cosinus

    Args:
        degrees (float): Angle size in degrees

    Returns:
        float: Value between 0 and 1
    """
    return math.cos(math.radians(degrees))