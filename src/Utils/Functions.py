## \file
# Various math function
import math



def sin(degrees: int|float) -> float:
    """A shorter syntax for calculating sinus

    Args:
        degrees (int | float): Amount of degrees

    Returns:
        float: Value between 0 and 1
    """
    return math.sin(math.radians(degrees))



def cos(degrees: int|float) -> float:
    """A shorter syntax for calculating cosinus

    Args:
        degrees (int | float): Amount of degrees

    Returns:
        float: Value between 0 and 1
    """
    return math.cos(math.radians(degrees))