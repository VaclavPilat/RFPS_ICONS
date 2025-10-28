# Functions for creating variations and remixes of already created icons
from src import Files
from Icons import Home, Cursor, Audio, Flag, Search, Globe, Monitor, Cogs, Stopwatch, Cap, Crosshair, Star, Book


@Files.createImage("Variations", (550, 50), color=(128, 128, 128), width=5)
def Icons(self, W, H, L, C, B) -> None:
    icons = (Home, Cogs, Star, Globe, Flag, Audio, Cursor, Search, Cap, Stopwatch, Monitor)
    size = self.size[1]
    # noinspection PyShadowingNames
    for i, function in enumerate(icons):
        self.load(function, size=(size, size), offset=(i*size, 0))

def rename(name: str):
    """Creating a decorator for changing the __name__ of the provided type.
    Used for renaming functions and classes.

    Args:
        name (str): New type name

    Returns:
        Decorator for changing type name
    """
    # noinspection PyShadowingNames
    def decorator(function):
        function.__name__ = name
        return function
    return decorator

import Icons, inspect
for name, function in inspect.getmembers(Icons, inspect.isfunction):
    @Files.createImage("Variations", (50, 50), color=(0, 0, 0), width=5)
    @rename(f"Mini{name}")
    def Miniature(self, *args) -> None:
        self.load(function)