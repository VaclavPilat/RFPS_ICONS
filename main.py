## \file
# Functions for generating icons
from Image import createImage



## \defgroup icons Generated icon images
# \image html Globe.png
# \image html User.png
# \image html Users.png
# \image html Sliders.png
# \image html Graph.png
# \image html Audio.png
# \image html Monitor.png
# \image html Splitscreen.png
# \image html Cap.png
# \image html Cogs.png
# \image html Keyboard.png
# \image html Play.png
# \image html Warehouse.png
# \image html Shutdown.png
# \image html Home.png
# \image html Search.png
# \image html Flag.png
# \image html Cursor.png
# \image html Book.png
# \image html Circle.png
# \image html Plus.png
# \image html Trash.png
# \image html Metro.png
# \image html Babel.png
# \image html Stopwatch.png
# \image html Crosshair.png



## \image html Globe.png
@createImage()
def Globe(self, W, H, L, C, B) -> None:
    self.ellipse((0, 0), (W, H), fill=None)
    self.ellipse((W*0.275, 0), (W*0.725, H), fill=None)
    for i in (-1, 1):
        self.line((L, H/2 + i*H*0.15), (W-L, H/2 + i*H*0.15))

## \image html User.png
@createImage()
def User(self, W, H, L, C, B) -> None:
    self.ellipse((0.25*W, 0), (0.75*W, H/2), fill=None)
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
        self.line((L/2, H*y/6), (W-L/2, H*y/6), rounded=True)
        self.ellipse((W*x-1.5*L, H*y/6-1.5*L), (W*x+1.5*L, H*y/6+1.5*L), outline=B, width=L//2)

## \image html Graph.png
@createImage()
def Graph(self, W, H, L, C, B) -> None:
    self.line((L/2, L/2), (L/2, H-L/2), (W-L/2, W-L/2), rounded=True)
    points = ((0.25*W, 0.75*H), (0.45*W, 0.35*H), (0.7*W, 0.6*H), (0.9*W, 0.1*H))
    self.line(*points)
    for x, y in points:
        self.ellipse((x-L*0.8, y-L*0.8), (x+L*0.8, y+L*0.8))

## \image html Audio.png
@createImage()
def Audio(self, W, H, L, C, B) -> None:
    self.line((L/2, H/3), (L/2, H*2/3), (W/4, H*2/3), (W/2, H-L), (W/2, L), (W/4, H/3), (L/2, H/3), rounded=True)
    self.arc((0, 0), (W, H), start=-60, end=60)
    self.arc((W/3, H/4), (W*6.25/8, H*3/4), start=-65, end=65)

## \image html Monitor.png
@createImage()
def Monitor(self, W, H, L, C, B) -> None:
    self.line((W/4, H-L/2), (W*3/4, H-L/2), rounded=True)
    self.line((L/2, H*3.6/5), (L/2, L/2), (W-L/2, L/2), (W-L/2, H*3.2/5), (L/2, H*3.2/5), (L/2, H*3.6/5), (W-L/2, H*3.6/5), (W-L/2, H/2), rounded=True)
    self.line((W/2-L/2, H-L/2), (W/2-L/2, H*3.6/5), (W/2+L/2, H*3.6/5), (W/2+L/2, H-L/2), rounded=True)

## \image html Splitscreen.png
@createImage()
def Splitscreen(self, W, H, L, C, B) -> None:
    self.load(Monitor, (W, H), (0, 0))
    self.line((W/2, 0), (W/2, H))