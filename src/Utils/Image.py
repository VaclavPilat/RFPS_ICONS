## \file
# Functionality for generating images using simple shapes
from PIL import ImageDraw
import math



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



class Canvas:
    """Class for wrapping the functionality of the Pillow library
    """

    def __init__(self, draw: ImageDraw, size: tuple = (100, 100), offset: tuple = (0, 0), color: tuple = (255, 255, 255), background: tuple = (0, 0, 0, 0), width: int|float = 10) -> None:
        """Initialising and Image instance

        Args:
            draw (ImageDraw): ImageDraw instance
            size (tuple, optional): Image size. Defaults to (100, 100).
            offset (tuple, optional): Image offset point. Defaults to (0, 0).
            color (tuple, optional): Foreground color. Defaults to (255, 255, 255).
            background (tuple, optional): Background color. Defaults to (0, 0, 0, 0).
            width (int | float, optional): Line width. Defaults to 10.
        """
        ## ImageDraw instance
        self.draw = draw
        ## Image size
        self.size = size
        ## Image offset point
        self.offset = offset
        ## Default foreground color
        self.color = color
        ## Background color
        self.background = background
        ## Line width
        self.width = width
    
    def transform(self, points: list) -> list:
        """Transforming vector points to tuples that Pillow accepts

        Args:
            points (list): List of coordinate tuples

        Returns:
            list: List of ofsetted coordinate tuples
        """
        return [(point[0] + self.offset[0], point[1] + self.offset[1]) for point in points]
    
    @defaultLoadSettings
    def load(self, function: "func", **settings) -> None:
        """Loading another image into this one

        Args:
            function (func): Function to load
        """
        loaded = Canvas(self.draw, **settings)
        function(loaded, *settings["size"], settings["width"], settings["color"], settings["background"])
    
    @defaultSettings("fill", "width", "joint")
    def line(self, *points, closed: bool = False, rounded: bool = False, **settings) -> None:
        """Drawing a line

        Args:
            closed (bool, optional): Should the line be closed? Defaults to False.
            rounded (bool, optional): Should the line ends be rounded? Defaults to False.
        """
        if closed:
            points = points + (points[0], )
        if rounded:
            points = (points[1], ) + points + (points[-2], )
        self.draw.line(points, **settings)
    
    @defaultSettings("fill", "outline", "width")
    def ellipse(self, *points, **settings) -> None:
        """Drawing an ellipse
        """
        self.draw.ellipse(points, **settings)
    
    @defaultSettings("start", "end", "fill", "width")
    def arc(self, *points, rounded: bool = False, **settings) -> None:
        """Drawing an arc

        Args:
            rounded (bool, optional): Should the ends of the arc be rounded? Defaults to False.
        """
        if rounded:
            for degrees in (settings["start"], settings["end"]):
                line = settings["width"]
                color = settings["fill"]
                sin, cos = (function(math.radians(degrees)) for function in (math.sin, math.cos))
                center = (points[0][0]/2 + points[1][0]/2, points[0][1]/2 + points[1][1]/2)
                width, height = (points[1][0]-points[0][0]-line, points[1][1]-points[0][1]-line)
                self.dot((center[0] + cos*width/2, center[1] + sin*height/2), outline=color, fill=color)
        self.draw.arc(points, **settings)
    
    @defaultSettings("fill", "outline", "width")
    def rectangle(self, *points, **settings) -> None:
        """Drawing a rectangle
        """
        self.draw.rectangle(points, **settings)
    
    @defaultSettings("fill", "outline", "width", "radius", "corners")
    def roundedRectangle(self, *points, **settings) -> None:
        """Drawing a rounded rectangle
        """
        self.draw.rounded_rectangle(points, **settings)
    
    @defaultSettings("fill", "outline", "width")
    def polygon(self, *points, **settings) -> None:
        """Drawing a polygon
        """
        self.draw.polygon(points, **settings)
    
    @defaultSettings("fill", "outline", "width")
    def dot(self, point: tuple, **settings) -> None:
        """Drawing a small circle

        Args:
            point (tuple): Point coordinates
        """
        radius = settings["width"] / 2
        self.draw.ellipse(((point[0]-radius, point[1]-radius), (point[0]+radius, point[1]+radius)), **settings)