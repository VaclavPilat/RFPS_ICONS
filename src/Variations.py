## \file
# Functions for creating variations and remixes of already created icons
from Utils.Files import createImage
from Icons import Home, Cursor, Audio, Flag, Search, Globe, Monitor, Cogs, Metro, Stopwatch, Cap, Crosshair
from types import FunctionType
from typing import Callable


## \defgroup variations Generated icon variations and remixes
# <div>
# \link Icons()
# \image html Variations/Icons.png
# \endlink
# \link Miniature()
# \image html Variations/MiniCursor.png
# \image html Variations/MiniAudio.png
# \image html Variations/MiniCrosshair.png
# \image html Variations/MiniHome.png
# \endlink
# </div>


@createImage("Variations", (550, 50), color=(128, 128, 128), width=5)
## \image html Variations/Icons.png
def Icons(self, W, H, L, C, B) -> None:
    icons = (Home, Cogs, Cursor, Globe, Flag, Audio, Metro, Search, Cap, Stopwatch, Monitor)
    size = self.size[1]
    # noinspection PyShadowingNames
    for i, function in enumerate(icons):
        self.load(function, size=(size, size), offset=(i*size, 0))


def rename(name: str) -> Callable[[FunctionType], FunctionType]:
    """Creating a decorator for changing the __name__ of the provided type.
    Used for renaming functions and classes.

    Args:
        name (str): New type name

    Returns:
        Callable[[FunctionType], FunctionType]: Decorator for changing type name
    """
    # noinspection PyShadowingNames
    def decorator(function: FunctionType) -> FunctionType:
        function.__name__ = name
        return function
    return decorator


for function in (Cursor, Audio, Crosshair, Home):
    @createImage("Variations", (50, 50), color=(0, 0, 0), width=5)
    @rename(f"Mini{function.__name__}")
    ## \image html Variations/MiniCursor.png
    # \image html Variations/MiniAudio.png
    # \image html Variations/MiniCrosshair.png
    # \image html Variations/MiniHome.png
    def Miniature(self, W, H, L, C, B) -> None:
        self.load(function)