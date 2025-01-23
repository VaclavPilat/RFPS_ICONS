## \file
# Functions for generating charts and other documentation sketches
from Image import createImage
import math



## \defgroup documentation Generated documentation images
# \image html Strafing.png
# \image html NoStrafing.png



def Axis(self, W, H, L, C, B) -> None:
    self.line((W/2, L/2), (W/2, H-L/2), fill=(200, 200, 200), rounded=True)
    self.line((L/2, H/2), (W-L/2, H/2), fill=(200, 200, 200), rounded=True)

FORWARD = 1
SIDES = 0.6 * FORWARD
BACKWARD = 0.4 * FORWARD

def BasicDots(self, W, H, L, C, B) -> None:
    self.dot((W/2, (1-FORWARD)/2*H+L/2))
    self.dot((W/2, (H+H*BACKWARD)/2-L/2))
    self.dot((W/2-SIDES*H/2+L/2, H/2))
    self.dot((W/2+SIDES*H/2-L/2, H/2))

@createImage((300, 300), color=(0, 0, 0))
## \image html Strafing.png
def Strafing(self, W, H, L, C, B) -> None:
    self.load(Axis, (W, H), (0, 0))
    self.roundedRectangle((W/2-SIDES*H/2, (1-FORWARD)/2*H), (W/2+SIDES*H/2, (H+H*BACKWARD)/2), fill=None, outline=(150, 150, 150))
    self.load(BasicDots, (W, H), (0, 0))
    self.dot((W/2-SIDES*H/2+L/2, (1-FORWARD)/2*H+L/2))
    self.dot((W/2+SIDES*H/2-L/2, (1-FORWARD)/2*H+L/2))
    self.dot((W/2-SIDES*H/2+L/2, (H+H*BACKWARD)/2-L/2))
    self.dot((W/2+SIDES*H/2-L/2, (H+H*BACKWARD)/2-L/2))

FRONTSIDE = (FORWARD + SIDES) / 2
BACKSIDE = (BACKWARD + SIDES) / 2

@createImage((300, 300), color=(0, 0, 0))
## \image html NoStrafing.png
def NoStrafing(self, W, H, L, C, B) -> None:
    self.load(Axis, (W, H), (0, 0))
    self.arc((W/2-FORWARD*H/2, (1-FORWARD)/2*H), (W/2+FORWARD*H/2, (H+H*FORWARD)/2), start=180, end=360, fill=(150, 150, 150), rounded=True)
    self.arc((W/2-SIDES*H/2, (1-SIDES)/2*H), (W/2+SIDES*H/2, (H+H*SIDES)/2), start=0, end=360, fill=(150, 150, 150))
    self.arc((W/2-BACKWARD*H/2, (1-BACKWARD)/2*H), (W/2+BACKWARD*H/2, (H+H*BACKWARD)/2), start=0, end=180, fill=(150, 150, 150), rounded=True)
    self.arc((W/2-FRONTSIDE*H/2, (1-FRONTSIDE)/2*H), (W/2+FRONTSIDE*H/2, (H+H*FRONTSIDE)/2), start=180, end=360, fill=(150, 150, 150), rounded=True)
    self.arc((W/2-BACKSIDE*H/2, (1-BACKSIDE)/2*H), (W/2+BACKSIDE*H/2, (H+H*BACKSIDE)/2), start=0, end=180, fill=(150, 150, 150), rounded=True)
    self.load(BasicDots, (W, H), (0, 0))
    for angle in [-45, -135]:
        self.dot((W/2+math.cos(math.radians(angle))*(FRONTSIDE*H/2-L/2), H/2+math.sin(math.radians(angle))*(FRONTSIDE*H/2-L/2)))
    for angle in [45, 135]:
        self.dot((W/2+math.cos(math.radians(angle))*(BACKSIDE*H/2-L/2), H/2+math.sin(math.radians(angle))*(BACKSIDE*H/2-L/2)))