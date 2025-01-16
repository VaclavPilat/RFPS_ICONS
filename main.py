## \file
# Functions for generating icons
from Image import createImage



## \defgroup icons Generated icon images
# \image html Globe.png
# \image html User.png
# \image html Users.png
# \image html Sliders.png



## \image html Globe.png
@createImage()
def Globe(self, W, H, L, C, B) -> None:
    self.ellipse((0, 0), (W, H))
    self.ellipse((W*0.275, 0), (W*0.725, H))
    for i in (-1, 1):
        self.line((L, H/2 + i*H*0.15), (W-L, H/2 + i*H*0.15))

## \image html User.png
@createImage()
def User(self, W, H, L, C, B) -> None:
    self.ellipse((0.25*W, 0), (0.75*W, H/2))
    self.arc((0, H/2-L), (W, 1.5*H), start=-180, end=0)
    self.line((0, H-L/2), (W, H-L/2))

## \image html Users.png
@createImage()
def Users(self, W, H, L, C, B) -> None:
    self.load(User, (W*2/3, H*2/3), (W/3, 0))
    self.ellipse((W/6-L, H/3-L), (W/2+L, H*2/3+L), fill=B, outline=B)
    self.ellipse((-L, H*2/3-2*L), (W*2/3+L, H*4/3+L), fill=B, outline=B)
    self.load(User, (W*2/3, H*2/3), (0, W/3))

## \image html Sliders.png
@createImage()
def Sliders(self, W, H, L, C, B) -> None:
    for y, x in {1: 1/2, 3: 5.1/6, 5: 1/4}.items():
        self.line((L/2, H*y/6), (W-L/2, H*y/6), joint=True)
        self.ellipse((W*x-1.5*L, H*y/6-1.5*L), (W*x+1.5*L, H*y/6+1.5*L), fill=C, outline=B, width=L//2)