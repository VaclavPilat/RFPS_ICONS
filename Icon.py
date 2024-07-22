from PIL import Image, ImageDraw, ImageFont

class Icon:
    def __init__(self, draw: ImageDraw, size: int = 100, width: int = 5, color: tuple = (255,255,255), x: int = 0, y: int = 0) -> None:
        """Initializing an icon draw class
        """
        self.draw = draw
        self.size = size
        self.color = color
        self.x = x
        self.y = y
    
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
        self.draw.line(self.offset(points), outline=self.color, width=self.width)