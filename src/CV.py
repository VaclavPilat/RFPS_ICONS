## \file
# Functions for generating images for my CV
from Utils.Files import createImage
from Icons import Cap, Home
import math



## \defgroup cv Generated CV icons
# <div>
# \link Education()
# \image html CV/Education.png
# \endlink
# \link Pin()
# \image html CV/Pin.png
# \endlink
# \link Code()
# \image html CV/Code.png
# \endlink
# \link Email()
# \image html CV/Email.png
# \endlink
# \link Residence()
# \image html CV/Residence.png
# \endlink
# \link Phone()
# \image html CV/Phone.png
# \endlink
# </div>



@createImage("CV", color=(0, 0, 0))
## \image html CV/Education.png
def Education(self, W, H, L, C, B) -> None:
    self.load(Cap)

@createImage("CV", color=(0, 0, 0))
## \image html CV/Pin.png
def Pin(self, W, H, L, C, B) -> None:
    R = W*0.35
    A = 30
    self.arc((W/2-R, 0), (W/2+R, R*2), rounded=True, start=180-A, end=360+A)
    self.ellipse((W/2-R/3, R-R/3), (W/2+R/3, R+R/3))
    points = []
    for angle in [180-A, 360+A]:
        sin, cos = (function(math.radians(angle)) for function in (math.sin, math.cos))
        points.append((W/2+cos*(R-L/2), R+sin*(R-L/2)))
    points.insert(1, (W/2, H-L/2))
    self.line(*points, rounded=True)

@createImage("CV", color=(0, 0, 0))
## \image html CV/Code.png
def Code(self, W, H, L, C, B) -> None:
    for i in [-1, 1]:
        self.line((W/2+i*W*0.2, H*0.35), (W/2+i*(W/2-L/2), H/2), (W/2+i*W*0.2, H*0.65), rounded=True)
    self.line((W*0.4, H*0.85), (W*0.6, H*0.15), rounded=True)

@createImage("CV", color=(0, 0, 0))
## \image html CV/Email.png
def Email(self, W, H, L, C, B) -> None:
    self.arc((0, 0), (W, H), start=60, end=360, rounded=True)
    self.arc((W*0.275, H*0.275), (W*0.725, H*0.725), start=0, end=360)
    self.line((W*0.725-L/2, H*0.275+L/2), (W*0.725-L/2, H/2), rounded=True)
    self.arc((W*0.725-L, H*0.275+L/2), (W, H*0.725), rounded=True)

@createImage("CV", color=(0, 0, 0))
## \image html CV/Residence.png
def Residence(self, W, H, L, C, B) -> None:
    self.load(Home)

@createImage("CV", color=(0, 0, 0))
## \image html CV/Phone.png
def Phone(self, W, H, L, C, B) -> None:
    R = W*0.35
    self.arc((0, 0), (R*2, R*2), start=135, end=225, rounded=True)
    self.arc((W-R*2, H-R*2), (W, H), start=45, end=135, rounded=True)
    self.line(
        (R+math.cos(math.radians(135))*(R-L/2), R+math.sin(math.radians(135))*(R-L/2)),
        (W-R+math.cos(math.radians(135))*(R-L/2), H-R+math.sin(math.radians(135))*(R-L/2))
    )
    self.line(
        (R+math.cos(math.radians(225))*(R-L/2), R+math.sin(math.radians(225))*(R-L/2)),
        (R+math.cos(math.radians(225))*(R-L/2)+W/5, R+math.sin(math.radians(225))*(R-L/2)+H/5),
        (R+math.cos(math.radians(225))*(R-L/2)+W/10, R+math.sin(math.radians(225))*(R-L/2)+H*0.3),
        (W-R+math.cos(math.radians(45))*(R-L/2)-W*0.3, H-R+math.sin(math.radians(45))*(R-L/2)-H/10),
        (W-R+math.cos(math.radians(45))*(R-L/2)-W/5, H-R+math.sin(math.radians(45))*(R-L/2)-H/5),
        (W-R+math.cos(math.radians(45))*(R-L/2), H-R+math.sin(math.radians(45))*(R-L/2)),
        rounded=True
    )