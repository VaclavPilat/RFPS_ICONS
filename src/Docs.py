## \file
# Functions for generating charts and other documentation sketches
from Utils import Files, Math


## \defgroup documentation Generated documentation images
# <div>
# \link Strafing()
# \image html Docs/Strafing.png
# \endlink
# \link NoStrafing()
# \image html Docs/NoStrafing.png
# \endlink
# </div>


## Light gray color
LIGHT = (200, 200, 200)
## Medium gray color
MEDIUM = (150, 150, 150)
## Black color
BLACK = (0, 0, 0)


def Arrows(self, W, H, L, C, B) -> None:
    self.line((W/2, L/2), (W/2, H-L/2), rounded=True)
    self.line((L/2, H/2), (W-L/2, H/2), rounded=True)
    self.line((W/2-L*1.5, L*2), (W/2, L/2), (W/2+L*1.5, L*2), rounded=True)
    self.line((W/2-L*1.5, H-L*2), (W/2, H-L/2), (W/2+L*1.5, H-L*2), rounded=True)
    self.line((L*2, H/2-L*1.5), (L/2, H/2), (L*2, H/2+L*1.5), rounded=True)
    self.line((W-L*2, H/2-L*1.5), (W-L/2, H/2), (W-L*2, H/2+L*1.5), rounded=True)

## Forward speed
FO = 1
## Side speed
SI = 0.6 * FO
## Backward speed
BA = 0.4 * FO
## Diagonal forward speed
FS = (FO + SI) / 2
## Diagonal backward speed
BS = (BA + SI) / 2

def BasicDots(self, W, H, L, C, B) -> None:
    self.dot((W/2, (1-FO)/2*H+L/2))
    self.dot((W/2, (H+H*BA)/2-L/2))
    self.dot((W/2-SI*H/2+L/2, H/2))
    self.dot((W/2+SI*H/2-L/2, H/2))

@Files.createImage("Docs", (300, 300), color=MEDIUM)
## \image html Docs/Strafing.png
def Strafing(self, W, H, L, C, B) -> None:
    self.load(Arrows, color=LIGHT)
    self.roundedRectangle((W/2-SI*H/2, (1-FO)/2*H), (W/2+SI*H/2, (H+H*BA)/2), fill=None)
    self.load(BasicDots, color=BLACK)
    self.dot((W/2-SI*H/2+L/2, (1-FO)/2*H+L/2), outline=BLACK)
    self.dot((W/2+SI*H/2-L/2, (1-FO)/2*H+L/2), outline=BLACK)
    self.dot((W/2-SI*H/2+L/2, (H+H*BA)/2-L/2), outline=BLACK)
    self.dot((W/2+SI*H/2-L/2, (H+H*BA)/2-L/2), outline=BLACK)

@Files.createImage("Docs", (300, 300), color=MEDIUM)
## \image html Docs/NoStrafing.png
def NoStrafing(self, W, H, L, C, B) -> None:
    self.load(Arrows, color=LIGHT)
    self.arc((W/2-FO*H/2, (1-FO)/2*H), (W/2+FO*H/2, (H+H*FO)/2), start=180, end=360, rounded=True)
    self.arc((W/2-SI*H/2, (1-SI)/2*H), (W/2+SI*H/2, (H+H*SI)/2), start=0, end=360)
    self.arc((W/2-BA*H/2, (1-BA)/2*H), (W/2+BA*H/2, (H+H*BA)/2), start=0, end=180, rounded=True)
    self.arc((W/2-FS*H/2, (1-FS)/2*H), (W/2+FS*H/2, (H+H*FS)/2), start=180, end=360, rounded=True)
    self.arc((W/2-BS*H/2, (1-BS)/2*H), (W/2+BS*H/2, (H+H*BS)/2), start=0, end=180, rounded=True)
    self.load(BasicDots, color=BLACK)
    for speed, angle in ((FS, -45), (FS, -135), (BS, 45), (BS, 135)):
        self.dot((W/2+Math.cos(angle)*(speed*H/2-L/2), H/2+Math.sin(angle)*(speed*H/2-L/2)), outline=BLACK)