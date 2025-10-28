# Functions for generating charts and other documentation sketches
from src import Files, Math
import math


LIGHT = (200, 200, 200) # Light gray color
MEDIUM = (150, 150, 150) # Medium gray color
BLACK = (0, 0, 0) # Black color

def Arrow(self, W, H, L, C, B) -> None:
    self.line((0, 0), (W, H), rounded=True)
    degrees = math.degrees(math.atan2(-H, -W))
    for i in (-45, +45):
        radians = math.radians(degrees + i)
        self.line((W, H), (W+math.cos(radians)*3*L, H+math.sin(radians)*3*L), rounded=True)

def Arrows(self, W, H, L, C, B) -> None:
    for i in (-1, 1):
        self.load(Arrow, offset=(W/2, H/2), size=(i*(W/2-L/2), 0))
        self.load(Arrow, offset=(W/2, H/2), size=(0, i*(H/2-L/2)))

FO = 1 # Forward speed
SI = 0.6 * FO # Side speed
BA = 0.4 * FO # Backward speed
FS = (FO + SI) / 2 # Diagonal forward speed
BS = (BA + SI) / 2 # Diagonal backward speed

def BasicDots(self, W, H, L, C, B) -> None:
    self.dot((W/2, (1-FO)/2*H+L/2))
    self.dot((W/2, (H+H*BA)/2-L/2))
    self.dot((W/2-SI*H/2+L/2, H/2))
    self.dot((W/2+SI*H/2-L/2, H/2))

@Files.createImage("Docs", (300, 300), color=MEDIUM)
def Strafing(self, W, H, L, C, B) -> None:
    self.load(Arrows, color=LIGHT)
    self.roundedRectangle((W/2-SI*H/2, (1-FO)/2*H), (W/2+SI*H/2, (H+H*BA)/2), fill=None)
    self.load(BasicDots, color=BLACK)
    self.dot((W/2-SI*H/2+L/2, (1-FO)/2*H+L/2), outline=BLACK)
    self.dot((W/2+SI*H/2-L/2, (1-FO)/2*H+L/2), outline=BLACK)
    self.dot((W/2-SI*H/2+L/2, (H+H*BA)/2-L/2), outline=BLACK)
    self.dot((W/2+SI*H/2-L/2, (H+H*BA)/2-L/2), outline=BLACK)

@Files.createImage("Docs", (300, 300), color=MEDIUM)
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