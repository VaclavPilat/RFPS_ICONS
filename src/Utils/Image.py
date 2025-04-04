## \file
# Functionality for generating images using simple shapes
from PIL import ImageDraw
# noinspection PyPackages
from .Settings import *
import math


# noinspection PyIncorrectDocstring
class Canvas:
    """Class for wrapping the functionality of the Pillow library
    """

    def __init__(self, draw: ImageDraw, size: tuple = (100, 100), offset: tuple = (0, 0),
        color: tuple = (255, 255, 255), background: tuple = (0, 0, 0, 0), width: float = 10) -> None:
        """Initialising and Image instance

        Args:
            draw (ImageDraw): ImageDraw instance
            size (tuple, optional): Image size. Defaults to (100, 100).
            offset (tuple, optional): Image offset point. Defaults to (0, 0).
            color (tuple, optional): Foreground color. Defaults to (255, 255, 255).
            background (tuple, optional): Background color. Defaults to (0, 0, 0, 0).
            width (float, optional): Line width. Defaults to 10.
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
    def load(self, function: "func", offset: tuple, **settings) -> None:
        """Loading another image into this one

        Args:
            function (func): Function to load
            offset (tuple, optional): Image offset. Defaults to (0, 0).
            size (tuple, optional): Image size. Defaults to parent image size.
            color (tuple, optional): Image foreground color. Defaults to parent image foreground color.
            background (tuple, optional): Image background color. Defaults to parent image background color.
            width (float, optional): Image line width. Defaults to parent image line width.
        """
        offset = tuple(a + b for a, b in zip(self.offset, offset))
        loaded = Canvas(self.draw, offset=offset, **settings)
        function(loaded, *settings["size"], settings["width"], settings["color"], settings["background"])
    
    @defaultDrawSettings("fill", "width", "joint", "rounded")
    def line(self, *points, rounded: bool, **settings) -> None:
        """Drawing a line

        Args:
            *points (tuple): Points representing a line
            fill (tuple, optional): Line color. Defaults to image foreground color.
            width (float, optional): Line width. Defaults to image line color.
            joint (str, optional): Line joint type. Defaults to "curve".
            rounded (bool, optional): Should the line ends be rounded? Defaults to False.
        """
        if rounded:
            points = (points[1], ) + points + (points[-2], )
        self.draw.line(points, **settings)
    
    @defaultDrawSettings("fill", "outline", "width")
    def ellipse(self, *points, **settings) -> None:
        """Drawing a full ellipse

        Args:
            *points (tuple): Top left and bottom right corner positions
            fill (tuple, optional): Ellipse fill color. Defaults to image foreground color.
            outline (tuple, optional): Ellipse border color. Defaults to image foreground color.
            width (float, optional): Ellipse border width. Defaults to image line width.
        """
        self.draw.ellipse(points, **settings)
    
    @defaultDrawSettings("start", "end", "fill", "width", "rounded")
    def arc(self, *points, rounded: bool, **settings) -> None:
        """Drawing an arc

        Args:
            *points (tuple): Top left and bottom right corner positions
            start (float, optional): Start angle in degrees. Defaults to 0.
            end (float, optional): Stop angle in degrees. Defaults to 180.
            fill (tuple, optional): Arc border color. Defaults to image foreground color.
            width (float, optional): Arc border width. Defaults to image line width.
            rounded (bool, optional): Should the ends of the arc be rounded? Defaults to False.
        """
        if rounded:
            for degrees in (settings["start"], settings["end"]):
                line = settings["width"]
                color = settings["fill"]
                sin, cos = (function(math.radians(degrees)) for function in (math.sin, math.cos))
                center = (points[0][0]/2 + points[1][0]/2, points[0][1]/2 + points[1][1]/2)
                width, height = (points[1][0]-points[0][0]-line, points[1][1]-points[0][1]-line)
                self.dot((center[0] + cos*width/2, center[1] + sin*height/2), outline=color, fill=color, transform=False)
        self.draw.arc(points, **settings)
    
    @defaultDrawSettings("fill", "outline", "width")
    def rectangle(self, *points, **settings) -> None:
        """Drawing a rectangle

        Args:
            *points (tuple): Top left and bottom right corner positions
            fill (tuple, optional): Rectangle fill color. Defaults to image foreground color.
            outline (tuple, optional): Rectangle border color. Defaults to image foreground color.
            width (float, optional): Rectangle border width. Defaults to image line width.
        """
        self.draw.rectangle(points, **settings)
    
    @defaultDrawSettings("fill", "outline", "width", "radius", "corners")
    def roundedRectangle(self, *points, **settings) -> None:
        """Drawing a rounded rectangle

        Args:
            *points (tuple): Top left and bottom right corner positions
            fill (tuple, optional): Rectangle fill color. Defaults to image foreground color.
            outline (tuple, optional): Rectangle border color. Defaults to image foreground color.
            width (float, optional): Rectangle border width. Defaults to image line width.
            radius (float, optional): Rectangle border radius. Defaults to image line width.
            corners (tuple, optional): Rectangle corner settings. Defaults to image corner settings.
        """
        self.draw.rounded_rectangle(points, **settings)
    
    @defaultDrawSettings("fill", "outline", "width")
    def polygon(self, *points, **settings) -> None:
        """Drawing a polygon

        Args:
            *points (tuple): Points representing the polygon
            fill (tuple, optional): Polygon fill color. Defaults to image foreground color.
            outline (tuple, optional): Polygon border color. Defaults to image foreground color.
            width (float, optional): Polygon border width. Defaults to image line width.
        """
        self.draw.polygon(points, **settings)
    
    @defaultDrawSettings("fill", "outline", "width")
    def dot(self, point: tuple, **settings) -> None:
        """Drawing a small circle

        Args:
            point (tuple): Point coordinates
            fill (tuple, optional): Dot fill color. Defaults to image foreground color.
            outline (tuple, optional): Dot border color. Defaults to image foreground color.
            width (float, optional): Dot diameter. Defaults to image line width.
        """
        radius = settings["width"] / 2
        self.draw.ellipse(((point[0]-radius, point[1]-radius), (point[0]+radius, point[1]+radius)), **settings)