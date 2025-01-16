## \file
# Functions for generating icons
from Image import createImage



## \defgroup icons Generated icon images
# \image html Globe.png



## \image html Globe.png
@createImage()
def Globe(self, W: int, H: int, L: int|float) -> None:
    self.ellipse((0, 0), (W, H))
    self.ellipse((W*0.275, 0), (W*0.725, H))
    for i in (-1, 1):
        self.line((L, H/2 + i*H*0.15), (W-L, H/2 + i*H*0.15))