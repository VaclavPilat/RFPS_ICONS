# Functions for creating variations and remixes of already created icons
from src import Files
import Icons, inspect, math


icons = tuple(i for i in inspect.getmembers(Icons, inspect.isfunction) if getattr(i[1], "decorated", False))
cols = 8
rows = math.ceil(len(icons) / cols)
@Files.createImage("Variations", (100*cols+10*(cols+1), 100*rows+10*(rows+1)), color=(100, 100, 100), width=10)
def Icons(self, W, H, L, C, B) -> None:
    X = int(W/(cols+(cols+1)/10))
    for i in range(rows+1):
        self.line((0, (X+L)*i+L/2), (W, (X+L)*i+L/2), fill=(255, 0, 0))
    for i in range(cols+1):
        self.line(((X+L)*i+L/2, 0), ((X+L)*i+L/2, H), fill=(255, 0, 0))
    for index, (name, function) in enumerate(icons):
        row = index // cols
        col = index % cols
        self.load(function, size=(X, X), offset=(L+X*1.1*col, L+X*1.1*row))