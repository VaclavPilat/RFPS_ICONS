from PIL import Image, ImageDraw, ImageFont, ImageChops
import os



def CreateIcon(func, size: int = 100, width: int = 10, sampling: int|float = 5, background: list|tuple = (0,0,0,0), color: list|tuple = (255,255,255)):
    """Wrapper for creating and saving an image created in an Icon class

    Args:
        size (int, optional): Icon size. Defaults to 100.
        width (int, optional): Brush width. Defaults to 10.
        sampling (int | float, optional): Sampling multiplier. Defaults to 5.
        background (list|tuple, optional): Background color. Defaults to (0,0,0,0).
        color (list|tuple, optional): Brush color. Defaults to (255,255,255).

    Returns:
        func: Icon function
    """
    # Creating the image
    image = Image.new("RGBA", (size*sampling, size*sampling), background)
    icon = Icon(ImageDraw.Draw(image), size*sampling, width*sampling, background, color, 0, 0)
    icon.create = func
    icon.create(icon)
    image = image.resize((size, size), resample=Image.LANCZOS)
    # Getting image file path
    folder = "images"
    filepath = "{}/{}.png".format(folder, func.__name__)
    if not os.path.exists(folder):
        os.mkdir(folder)
    # Comparing older image
    if os.path.exists(filepath):
        diff = ImageChops.difference(image, Image.open(filepath))
        if not diff.getbbox():
            return func
    # Saving the image
    image.save(filepath, "PNG")
    print(filepath)
    return func



class Icon:
    """Class for encapsulating a ImageDraw with custom settings
    """

    def __init__(self, draw: ImageDraw, size: int = 100, width: int = 5, background: list|tuple = (0,0,0,0), color: list|tuple = (255,255,255), x: int = 0, y: int = 0) -> None:
        """Initializing an icon draw class

        Args:
            draw (ImageDraw): ImageDraw instance
            size (int, optional): Available image size. Defaults to 100.
            width (int, optional): Brush width. Defaults to 5.
            background (list|tuple, optional): Background color. Defaults to (0,0,0,0).
            color (list|tuple, optional): Brush color. Defaults to (255,255,255).
            x (int, optional): X offset. Defaults to 0.
            y (int, optional): Y offset. Defaults to 0.
        """
        self.draw = draw
        self.size = size
        self.width = width
        self.background = background
        self.color = color
        self.x = x
        self.y = y
    
    def create(self) -> None:
        """Drawing an image

        Raises:
            NotImplemented: Thrown if not overriden
        """
        raise NotImplemented
    
    def offset(self, points: list|tuple) -> list:
        """Offsetting provided coordinates

        Args:
            points (list|tuple): Coordinates to offset

        Returns:
            list: Ofsetted coordinates
        """
        if type(points[0]) in (int, float):
            for i in range(0, len(points), 2):
                points[i] += self.x
            for i in range(1, len(points), 2):
                points[i] += self.y
            return points
        elif type(points[0]) in (list, tuple):
            return [(point[0] + self.x, point[1] + self.y) for point in points]
    
    def load(self, func, size: int|float, x: int|float, y: int|float) -> None:
        """Draws an existing icon into this one

        Args:
            size (int | float): Icon size
            x (int | float): Icon X offset
            y (int | float): Icon Y offset
        """
        loaded = Icon(self.draw, size, self.width, self.background, self.color, x, y)
        loaded.create = func
        loaded.create(loaded)
    
    def line(self, points: list|tuple, rounded: bool = False, fill: list|tuple = None, width: int|float = None, polygon: bool = False) -> None:
        """Draws a line with rounded joints

        Args:
            points (list | tuple): List of points
            rounded (bool, optional): Rounded ends? Defaults to False.
            fill (list | tuple, optional): Fill color. Defaults to None.
            width (int | float, optional): Line width. Defaults to None.
        """
        if fill is None:
            fill = self.color
        if width is None:
            width = self.width
        if polygon:
            if type(points[0]) in (int, float):
                points += points[:2]
            elif type(points[0]) in (list, tuple):
                points.append(points[0])
        if rounded:
            if type(points[0]) in (int, float):
                points = points[2:4] + points + points[-4:-2]
            elif type(points[0]) in (list, tuple):
                points = [points[1]] + points + [points[-2]]
        self.draw.line(self.offset(points), fill=fill, width=width, joint="curve")
    
    def ellipse(self, points: list|tuple, outline: list|tuple = None, fill: list|tuple = None, width: int|float = None) -> None:
        """Draws an ellipse

        Args:
            points (list | tuple): List of points
            outline (list | tuple, optional): Outline color. Defaults to None.
            fill (list | tuple, optional): Fill color. Defaults to None.
            width (int | float, optional): Outline width. Defaults to None.
        """
        if outline is None:
            outline = self.color
        if fill is None:
            fill = self.color
        if width is None:
            width = self.width
        self.draw.ellipse(self.offset(points), fill=fill, outline=outline, width=width)
    
    def arc(self, points: list|tuple, start: int|float, end: int|float, fill: list|tuple = None, width: int|float = None) -> None:
        """Drawing an arc

        Args:
            points (list | tuple): List of points
            start (int | float): Start point in degrees
            end (int | float): End point in degrees
            fill (list | tuple, optional): Outline color. Defaults to None.
            width (int | float, optional): Outline width. Defaults to None.
        """
        if fill is None:
            fill = self.color
        if width is None:
            width = self.width
        self.draw.arc(self.offset(points), start=start, end=end, fill=fill, width=width)
    
    def rectangle(self, points: list|tuple, outline: list|tuple = None, fill: list|tuple = None, width: int|float = None, radius: int = None) -> None:
        """Drawing a rectangle

        Args:
            points (list | tuple): List of points
            outline (list | tuple, optional): Outline color. Defaults to None.
            fill (list | tuple, optional): Fill color. Defaults to None.
            width (int | float, optional): Outline width. Defaults to None.
            radius (int, optional): Corner radius. Defaults to None.
        """
        if outline is None:
            outline = self.color
        if fill is None:
            fill = self.color
        if width is None:
            width = self.width
        if radius is not None:
            self.draw.rounded_rectangle(self.offset(points), radius=radius, fill=fill, outline=outline, width=width)
        else:
            self.draw.rectangle(self.offset(points), fill=fill, outline=outline, width=width)