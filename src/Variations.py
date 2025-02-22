## \file
# Functions for creating variations and remixes of already created icons
from Utils.Files import createImage
from Icons import Home, Cursor, Audio, Flag, Search, Globe, Monitor, Cogs, Metro, Stopwatch, Cap, Crosshair



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



@createImage("Variations", (550, 50), color=(128, 128, 128), line=5)
## \image html Variations/Icons.png
def Icons(self, W, H, L, C, B) -> None:
    icons = (Home, Cogs, Cursor, Globe, Flag, Audio, Metro, Search, Cap, Stopwatch, Monitor)
    size = self.size[1]
    for i, func in enumerate(icons):
        self.load(func, size=(size, size), offset=(i*size, 0))

def rename(name: str) -> "func":
    """Creating a decorator for changing the __name__ of the provided type.
    Used for renaming functions and classes.

    Args:
        name (str): New type name

    Returns:
        func: Decorator for changing type name
    """
    def decorator(func: "func") -> "func":
        func.__name__ = name
        return func
    return decorator

for func in (Cursor, Audio, Crosshair, Home):
    @createImage("Variations", (50, 50), color=(0, 0, 0), line=5)
    @rename(f"Mini{func.__name__}")
    ## \image html Variations/MiniCursor.png
    # \image html Variations/MiniAudio.png
    # \image html Variations/MiniCrosshair.png
    # \image html Variations/MiniHome.png
    def Miniature(self, W, H, L, C, B) -> None:
        self.load(func)