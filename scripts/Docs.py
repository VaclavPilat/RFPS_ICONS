# Functions for generating charts and other documentation sketches
from src import Files
import Icons
import math
from PIL import ImageFont


LIGHT = (200, 200, 200) # Light gray color
MEDIUM = (120, 120, 120) # Medium gray color
BLACK = (0, 0, 0) # Black color

BOLD = "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf" # Bold font

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
    self.rectangle((W/2-SI*H/2, (1-FO)/2*H), (W/2+SI*H/2, (H+H*BA)/2))
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

def HorizontalCurlyBracket(self, W, H, L, C, B) -> None:
    self.arc((-W/2+L/2, 0), (W/2+L/2, W), start=-90, end=0, rounded=True)
    self.line((W/2, W/2), (W/2, H/2-W/2+L))
    self.arc((W/2-L/2, H/2-W+L/2), (W*1.5-L/2, H/2+L/2), start=90, end=180, rounded=True)
    self.arc((W/2-L/2, H/2-L/2), (W*1.5-L/2, H/2+W-L/2), start=180, end=270, rounded=True)
    self.line((W/2, H-W/2), (W/2, H/2+W/2-L))
    self.arc((-W/2+L/2, H-W), (W/2+L/2, H), start=0, end=90, rounded=True)

def VerticalCurlyBracket(self, W, H, L, C, B) -> None:
    self.arc((0, -H/2+L/2), (H, H/2+L/2), start=90, end=180, rounded=True)
    self.line((H/2, H/2), (W/2-H/2+L, H/2))
    self.arc((W/2-H+L/2, H/2-L/2), (W/2+L/2, H*1.5-L/2), start=-90, end=0, rounded=True)
    self.arc((W/2-L/2, H/2-L/2), (W/2+H-L/2, H*1.5-L/2), start=180, end=270, rounded=True)
    self.line((W-H/2, H/2), (W/2+H/2-L, H/2))
    self.arc((W-H, -H/2+L/2), (W, H/2+L/2), start=0, end=90, rounded=True)

def DescribedIcon(self, W, H, L, C, B, I, T) -> None:
    self.load(I, size=(W, W))
    self.text((W/2, W+L), text=T, file=BOLD)

def ProjectPipeline(self, W, H, L, C, B, D1, *D2) -> None:
    X = W//2.7
    self.load(DescribedIcon, size=(X, 0), color=BLACK, args=(Icons.Folder, D1))
    self.load(Arrow, offset=(X+L*1.5, X/2), size=(X/2-L, 0), color=LIGHT)
    self.load(DescribedIcon, size=(X, 0), offset=(W-X, 0), color=MEDIUM, args=D2)

@Files.createImage("Docs", (630, 480), color=MEDIUM)
def Project(self, W, H, L, C, B) -> None:
    X = W/6.3
    self.load(ProjectPipeline, size=(X*2.7, 0), offset=(X*0.2, 0), args=("RFPS_MAPS/", Icons.Cube, ".BLEND"))
    self.load(ProjectPipeline, size=(X*2.7, 0), offset=(X*0.2, X*1.5), args=("RFPS_ICONS/", Icons.Cursor, ".PNG"))
    self.load(HorizontalCurlyBracket, size=(X/2, X*2.8), offset=(X*3, 0), color=LIGHT)
    self.load(ProjectPipeline, size=(X*2.7, 0), offset=(X*3.6, X*0.9), args=("RFPS/", Icons.Unity, ".EXE"))
    self.load(VerticalCurlyBracket, size=(X, X/2), offset=(X*1.9, X*2.9), color=LIGHT)
    self.load(ProjectPipeline, size=(X*2.7, 0), offset=(X*1.9, X*3.5), args=("RFPS_THESIS/", Icons.Book, ".PDF"))

def Key(self, W, H, L, C, B, K, D) -> None:
    self.rectangle((0, 0), (W, H), fill=LIGHT)
    self.text((W/2, H*3/7 ), text=K, anchor="mm", fill=MEDIUM, file=BOLD, size=3.5*L)
    self.text((W/2, H-L*1.5), text=D, anchor="ms", fill=BLACK, file=BOLD)

@Files.createImage("Docs", (100, 100))
def Keyboard(self, W, H, L, C, B) -> None:
    self.load(Key, args=("A", "LEFT"))