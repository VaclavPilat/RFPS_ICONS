## \file
# Decorators for wrapping Canvas methods and providing default setting values
from types import FunctionType


# noinspection PyTypeChecker
def defaultDrawSettings(*names) -> FunctionType:
    """Decorator for passing default settings to draw methods

    Returns:
        FunctionType: Wrapper for a drawing method
    """
    # noinspection PyTypeChecker
    def wrapper(method: FunctionType) -> FunctionType:
        def wrapped(self, *points, transform: bool = True, **settings) -> None:
            values = {k: v for k, v in {
                "width": self.width,
                "outline": self.color,
                "fill": self.color,
                "start": 0,
                "end": 180,
                "joint": "curve",
                "radius": self.width,
                "corners": (True, True, True, True),
                "rounded": False,
            }.items() if k in names}
            values.update(settings)
            if transform:
                points = self.transform(points)
            method(self, *points, **values)
        return wrapped
    return wrapper


# noinspection PyTypeChecker
def defaultLoadSettings(method: FunctionType) -> FunctionType:
    """Decorator for providing default settings to an image loading method

    Args:
        method (FunctionType): Method being wrapped

    Returns:
        FunctionType: Wrapped method
    """
    def wrapped(self, function: FunctionType, **settings) -> None:
        values = {
            "size": self.size,
            "offset": (0, 0),
            "color": self.color,
            "background": self.background,
            "width": self.width,
        }
        values.update(settings)
        method(self, function, **values)
    return wrapped