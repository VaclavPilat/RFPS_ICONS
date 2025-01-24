## \file
# Decorators for wrapping Canvas methods and providing default setting values



def defaultSettings(*names) -> "func":
    """Decorator for passing some default settings through and allowing their updates

    Returns:
        func: Wrapper for a drawing method
    """
    def wrapper(method: "func") -> "func":
        def wrapped(self, *points, **settings) -> None:
            values = {k: v for k, v in {
                "width": self.width,
                "outline": self.color,
                "fill": self.color,
                "start": 0,
                "end": 180,
                "joint": "curve",
                "radius": self.width,
                "corners": (True, True, True, True),
            }.items() if k in names}
            values.update(settings)
            method(self, *self.transform(points), **values)
        return wrapped
    return wrapper



def defaultLoadSettings(method: "func") -> "func":
    """Decorator for providing default settings for loaded image functions

    Args:
        method (func): Method being wrapped

    Returns:
        func: Wrapped method
    """
    def wrapped(self, function: "func", **settings) -> None:
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