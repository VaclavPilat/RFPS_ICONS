from PIL import Image, ImageDraw, ImageChops
import os



class V2:
    """Class for a 2D vector
    """

    def __init__(self, x: int|float = 0, y: int|float = 0) -> None:
        """Initialising a point

        Args:
            x (int | float, optional): X value. Defaults to 0.
            y (int | float, optional): Y value. Defaults to 0.
        """
        ## X value
        self.x = x
        ## Y value
        self.y = y
    
    def __iter__(self):
        """Getting an iterator
        """
        return iter([self.x, self.y])



def defaultSettings(*names) -> "func":
    """Decorator for passing some default settings through and allowing their updates

    Returns:
        func: Wrapper for a drawing method
    """
    def wrapper(method: "func") -> "func":
        def wrapped(self, *args, **kwargs) -> None:
            values = {k: v for k, v in {
                "width": self.line,
                "outline": self.color,
                "fill": None,
            }.items() if k in names}
            values.update(kwargs)
            method(self, *args, **values)
        return wrapped
    return wrapper



class Canvas:
    """Class for creating an image using simple shapes
    """

    def __init__(self, draw: ImageDraw, size: V2 = V2(100, 100), offset: V2 = V2(), color: tuple = (255, 255, 255), background: tuple = (0, 0, 0, 0), line: int|float = 10) -> None:
        """Initialising and Image instance

        Args:
            draw (PIL.ImageDraw): ImageDraw instance
            size (V2, optional): Image size. Defaults to V2(100, 100).
            offset (V2, optional): Image offset point. Defaults to V2().
            color (tuple, optional): Foreground color. Defaults to (255, 255, 255).
            background (tuple, optional): Background color. Defaults to (0, 0, 0, 0).
            line (int | float, optional): Line width. Defaults to 10.
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
        self.line = line
    
    def transform(self, points: list) -> list:
        """Transforming vector points to tuples that Pillow accepts

        Args:
            points (list): List of V2 points

        Returns:
            list: List of ofsetted coordinate tuples
        """
        return [(point.x + self.offset.x, point.y + self.offset.y) for point in points]
    
    @defaultSettings("fill", "outline", "width")
    def ellipse(self, *points, **settings) -> None:
        """Drawing an ellipse
        """
        self.draw.ellipse(self.transform(points), **settings)



image = Image.new("RGBA", (100, 100), (0,0,0,0))
draw = Canvas(ImageDraw.Draw(image))
draw.ellipse(V2(), V2(100, 50))
image.save("image.png", "PNG")