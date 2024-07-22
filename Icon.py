from PIL import Image, ImageDraw, ImageFont



def CreateIcon(cls, size: int = 100, width: int = 10, sampling: int|float = 5, background: tuple = (0,0,0,0), color: tuple = (255,255,255)):
    """Wrapper for creating and saving an image created in an Icon class

    Args:
        size (int, optional): Icon size. Defaults to 100.
        width (int, optional): Brush width. Defaults to 10.
        sampling (int | float, optional): Sampling multiplier. Defaults to 5.
        background (tuple, optional): Background color. Defaults to (0,0,0,0).
        color (tuple, optional): Brush color. Defaults to (255,255,255).

    Returns:
        cls: Icon class
    """
    image = Image.new("RGBA", (size*sampling, size*sampling), background)
    cls(ImageDraw.Draw(image), size*sampling, width*sampling, color, 0, 0)
    image = image.resize((size, size), resample=Image.LANCZOS)
    image.save("{}.png".format(cls.__name__), "PNG")
    return cls



class Icon:
    def __init__(self, draw: ImageDraw, size: int = 100, width: int = 5, color: tuple = (255,255,255), x: int = 0, y: int = 0) -> None:
        """Initializing an icon draw class

        Args:
            draw (ImageDraw): ImageDraw instance
            size (int, optional): Available image size. Defaults to 100.
            width (int, optional): Brush width. Defaults to 5.
            color (tuple, optional): Brush color. Defaults to (255,255,255).
            x (int, optional): X offset. Defaults to 0.
            y (int, optional): Y offset. Defaults to 0.
        """
        self.draw = draw
        self.size = size
        self.width = width
        self.color = color
        self.x = x
        self.y = y
        self.create()
    
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
        if type(points[0]) in (list, tuple):
            return [(point[0] + self.x, point[1] + self.y) for point in points]
    
    def line(self, points: list|tuple) -> None:
        """Drawing a line

        Args:
            points (list|tuple): List of points
        """
        self.draw.line(self.offset(points), fill=self.color, width=self.width, joint="curve")
    
    def ellipse(self, points: list|tuple) -> None:
        """Drawing an ellipse

        Args:
            points (list | tuple): List of points
        """
        self.draw.ellipse(self.offset(points), outline=self.color, width=self.width)
    
    def arc(self, points: list|tuple, start: int|float, end: int|float) -> None:
        """Drawing an arc

        Args:
            points (list | tuple): List of points
            start (int | float): Arc start in degrees
            end (int | float): Arc end in degrees
        """
        self.draw.arc(self.offset(points), start=start, end=end, fill=self.color, width=self.width)