# Functions for creating miniatures of already created icons
from src import Files
import Icons, inspect


icons = tuple(i for i in inspect.getmembers(Icons, inspect.isfunction) if getattr(i[1], "decorated", False))

def rename(name):
    def wrapper(func):
        func.__name__ = name
        return func
    return wrapper

for name, function in icons:
    @Files.createImage("Miniatures", (50, 50), color=(0, 0, 0), width=5)
    @rename(f"Mini{name}")
    def Miniature(self, W, H, L, C, B):
        self.load(function)