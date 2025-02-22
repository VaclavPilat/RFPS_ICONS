## \file
# Functions for generating charts and other documentation sketches
from Utils.Files import createImage
from Utils.Functions import sin, cos



## \defgroup documentation Generated documentation images
# <div>
# \link Strafing()
# \image html Docs/Strafing.png
# \endlink
# \link NoStrafing()
# \image html Docs/NoStrafing.png
# \endlink
# </div>



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

@createImage("Docs", (300, 300), color=(150, 150, 150))
## \image html Docs/Strafing.png
def Strafing(self, W, H, L, C, B) -> None:
    self.load(Arrows, color=(200, 200, 200))
    self.roundedRectangle((W/2-SI*H/2, (1-FO)/2*H), (W/2+SI*H/2, (H+H*BA)/2), fill=None)
    self.load(BasicDots, color=(0, 0, 0))
    self.dot((W/2-SI*H/2+L/2, (1-FO)/2*H+L/2), outline=(0, 0, 0))
    self.dot((W/2+SI*H/2-L/2, (1-FO)/2*H+L/2), outline=(0, 0, 0))
    self.dot((W/2-SI*H/2+L/2, (H+H*BA)/2-L/2), outline=(0, 0, 0))
    self.dot((W/2+SI*H/2-L/2, (H+H*BA)/2-L/2), outline=(0, 0, 0))

@createImage("Docs", (300, 300), color=(150, 150, 150))
## \image html Docs/NoStrafing.png
def NoStrafing(self, W, H, L, C, B) -> None:
    self.load(Arrows, color=(200, 200, 200))
    self.arc((W/2-FO*H/2, (1-FO)/2*H), (W/2+FO*H/2, (H+H*FO)/2), start=180, end=360, rounded=True)
    self.arc((W/2-SI*H/2, (1-SI)/2*H), (W/2+SI*H/2, (H+H*SI)/2), start=0, end=360)
    self.arc((W/2-BA*H/2, (1-BA)/2*H), (W/2+BA*H/2, (H+H*BA)/2), start=0, end=180, rounded=True)
    self.arc((W/2-FS*H/2, (1-FS)/2*H), (W/2+FS*H/2, (H+H*FS)/2), start=180, end=360, rounded=True)
    self.arc((W/2-BS*H/2, (1-BS)/2*H), (W/2+BS*H/2, (H+H*BS)/2), start=0, end=180, rounded=True)
    self.load(BasicDots, color=(0, 0, 0))
    for speed, angle in ((FS, -45), (FS, -135), (BS, 45), (BS, 135)):
        self.dot((W/2+cos(angle)*(speed*H/2-L/2), H/2+sin(angle)*(speed*H/2-L/2)), outline=(0, 0, 0))