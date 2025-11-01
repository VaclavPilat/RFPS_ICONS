## \file
# Decorators for wrapping Canvas methods and providing default setting values
from PIL import ImageFont


# noinspection PyTypeChecker
def defaultDrawSettings(*names):
    """Decorator for passing default settings to draw methods

    Returns:
        Wrapper for a drawing method
    """
    # noinspection PyTypeChecker
    def wrapper(method):
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
                "text": "Hello world",
                "font": ImageFont.load_default(self.width*2),
                "anchor": "mt",
            }.items() if k in names}
            values.update(settings)
            if transform:
                points = self.transform(points)
            method(self, *points, **values)
        return wrapped
    return wrapper


# noinspection PyTypeChecker
def defaultLoadSettings(method):
    """Decorator for providing default settings to an image loading method

    Args:
        method: Method being wrapped

    Returns:
        FunctionType: Wrapped method
    """
    def wrapped(self, function, **settings) -> None:
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