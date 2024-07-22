from PIL import Image, ImageDraw, ImageFont

def CreateIcon(cls):
    """Wrapper for creating and saving an image created in an Icon class

    Args:
        cls: Icon class to wrap

    Returns:
        Wrapped Icon class
    """
    print(cls.__name__)
    size: int = 100
    width: int = 10
    sampling: int|float = 5
    background: list|tuple = (0,0,0,0)
    color: list|tuple = (255,255,255)
#def CreateIcon(size: int = 100, width: int = 10, sampling: int|float = 5, background: tuple = (0,0,0,0), color: tuple = (255,255,255)) -> None:
    #class Wrapper:
    #    def __init__(self) -> None:
    image = Image.new("RGBA", (size*sampling, size*sampling), background)
    cls(ImageDraw.Draw(image), size*sampling, width*sampling, color, 0, 0)
    image = image.resize((size, size), resample=Image.LANCZOS)
    image.save("{}.png".format(cls.__name__), "PNG")
    return cls

class Icon:
    def __init__(self, draw: ImageDraw, size: int = 100, width: int = 5, color: tuple = (255,255,255), x: int = 0, y: int = 0) -> None:
        """Initializing an icon draw class
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

@CreateIcon
class Globe(Icon):
    def create(self):
        self.ellipse([0, 0, self.size, self.size])
        self.ellipse([self.size*2.75/10, 0, self.size*7.25/10, self.size])
        self.line([self.width/2, self.size*3.5/10, self.size-self.width/2, self.size*3.5/10])
        self.line([self.width/2, self.size*6.5/10, self.size-self.width/2, self.size*6.5/10])