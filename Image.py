## \file
# Functionality for generating images using simple shapes
from PIL import Image, ImageDraw, ImageChops
import os



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
    """Class for wrapping the functionality of the Pillow library
    """

    def __init__(self, draw: ImageDraw, size: tuple = (100, 100), offset: tuple = (0, 0), color: tuple = (255, 255, 255), background: tuple = (0, 0, 0, 0), line: int|float = 10) -> None:
        """Initialising and Image instance

        Args:
            draw (ImageDraw): ImageDraw instance
            size (tuple, optional): Image size. Defaults to (100, 100).
            offset (tuple, optional): Image offset point. Defaults to (0, 0).
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
            points (list): List of coordinate tuples

        Returns:
            list: List of ofsetted coordinate tuples
        """
        return [(point[0] + self.offset[0], point[1] + self.offset[1]) for point in points]
    
    @defaultSettings("fill", "outline", "width")
    def ellipse(self, *points, **settings) -> None:
        """Drawing an ellipse
        """
        self.draw.ellipse(self.transform(points), **settings)



def createImage(size: tuple = (100, 100), sampling: float = 5, line: int|float = 10, background: tuple = (0, 0, 0, 0), color: tuple = (255, 255, 255)) -> "func":
    """Decorator for creating an image and saving it to a file

    Args:
        size (tuple, optional): Image size. Defaults to (100, 100).
        sampling (float, optional): Sampling multiplier. Defaults to 5.
        line (int | float, optional): Default line width. Defaults to 10.
        background (tuple, optional): Background color. Defaults to (0, 0, 0, 0).
        color (tuple, optional): Default foreground color. Defaults to (255, 255, 255).

    Returns:
        func: Wrapper for image creation
    """
    def wrapper(function: "func") -> "func":
        # Calculating sampled sizes
        scaledSize = (size[0] * sampling, size[1] * sampling)
        scaledLine = line * sampling
        # Creating an image
        image = Image.new("RGBA", scaledSize, background)
        canvas = Canvas(ImageDraw.Draw(image), scaledSize, (0, 0), color, background, scaledLine)
        # Calling the function
        function(canvas, *scaledSize, scaledLine)
        image = image.resize(size, resample=Image.LANCZOS)
        # Getting image file path
        folder = "images"
        filepath = f"{folder}/{function.__name__}.png"
        if not os.path.exists(folder):
            os.mkdir(folder)
        # Comparing older image
        if os.path.exists(filepath):
            diff = ImageChops.difference(image, Image.open(filepath))
            if not diff.getbbox():
                return
        # Saving the image
        image.save(filepath, "PNG")
        print(filepath)
    return wrapper