## \file
# Functions for creating variations and remixes of already created icons
from icons import Files
from Icons import Home, Cursor, Audio, Flag, Search, Globe, Monitor, Cogs, Stopwatch, Cap, Crosshair, Star, Book


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
# \image html Variations/MiniBook.png
# \endlink
# </div>


@Files.createImage("Variations", (550, 50), color=(128, 128, 128), width=5)
## \image html Variations/Icons.png
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

for function in (Cursor, Audio, Crosshair, Home, Book):
    @Files.createImage("Variations", (50, 50), color=(0, 0, 0), width=5)
    @rename(f"Mini{function.__name__}")
    ## \image html Variations/MiniCursor.png
    # \image html Variations/MiniAudio.png
    # \image html Variations/MiniCrosshair.png
    # \image html Variations/MiniHome.png
    # \image html Variations/MiniBook.png
    def Miniature(self, W, H, L, C, B) -> None:
        self.load(function)