# Functions for generating charts and other documentation sketches
from src import Files
import Icons
import math
from PIL import ImageFont


LIGHT = (200, 200, 200) # Light gray color
MEDIUM = (150, 150, 150) # Medium gray color
BLACK = (0, 0, 0) # Black color

def Arrow(self, W, H, L, C, B) -> None:
    self.line((0, 0), (W, H), rounded=True)
    degrees = math.degrees(math.atan2(-H, -W))
    for i in (-45, +45):
        radians = math.radians(degrees + i)
        self.line((W, H), (W+math.cos(radians)*2*L, H+math.sin(radians)*2*L), rounded=True)

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
        radians = math.radians(angle)
        self.dot((W/2+math.cos(radians)*(speed*H/2-L/2), H/2+math.sin(radians)*(speed*H/2-L/2)), outline=BLACK)

def CurlyBracket(self, W, H, L, C, B) -> None:
    self.arc((-W/2+L/2, 0), (W/2+L/2, W), start=-90, end=0, rounded=True)
    self.line((W/2, W/2), (W/2, H/2-W/2+L))
    self.arc((W/2-L/2, H/2-W+L/2), (W*1.5-L/2, H/2+L/2), start=90, end=180, rounded=True)
    self.arc((W/2-L/2, H/2-L/2), (W*1.5-L/2, H/2+W-L/2), start=180, end=270, rounded=True)
    self.line((W/2, H-W/2), (W/2, H/2+W/2-L))
    self.arc((-W/2+L/2, H-W), (W/2+L/2, H), start=0, end=90, rounded=True)

def DescribedIcon(self, W, H, L, C, B, I, T) -> None:
    self.load(I, size=(W, W))
    self.text((W/2, W+L), text=T, font=ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 2*L))

def ProjectPipeline(self, W, H, L, C, B, D1, *D2) -> None:
    self.load(DescribedIcon, size=(W//3, 0), color=BLACK, args=(Icons.Folder, D1))
    self.load(Arrow, offset=(W/3+L*1.5, W/6), size=(W/3-3*L, 0), color=LIGHT)
    self.load(DescribedIcon, size=(W//3, 0), offset=(W/3*2, 0), color=MEDIUM, args=D2)

@Files.createImage("Docs", (700, 280), color=MEDIUM)
def Project(self, W, H, L, C, B) -> None:
    X = W/7
    self.load(ProjectPipeline, size=(X*3, 0), offset=(L*2, 0), args=("RFPS_MAPS/", Icons.Cube, ".BLEND"))
    self.load(ProjectPipeline, size=(X*3, 0), offset=(L*2, X*1.5), args=("RFPS_ICONS/", Icons.Cursor, ".PNG"))
    self.load(CurlyBracket, size=(X-4*L, H), offset=(X*3+L*3, 0), color=LIGHT)
    self.load(ProjectPipeline, size=(X*3, H/2), offset=(X*4, H/2-X/2), args=("RFPS/", Icons.Logo, ".EXE"))