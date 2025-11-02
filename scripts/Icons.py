# Functions for generating icons
from src import Files, Math


@Files.createImage("Icons")
def Globe(self, W, H, L, C, B) -> None:
    self.arc((0, 0), (W, H))
    self.arc((W*0.275, 0), (W*0.725, H))
    for i in (-1, 1):
        self.line((L, H/2 + i*H*0.15), (W-L, H/2 + i*H*0.15))

@Files.createImage("Icons")
def User(self, W, H, L, C, B) -> None:
    self.arc((0.25*W, 0), (0.75*W, H/2))
    self.arc((0, H/2-L), (W, 1.5*H), start=-180, end=0, rounded=True)
    self.line((L/2, H-L/2), (W-L/2, H-L/2), rounded=True)

def User2(self, W, H, L, C, B) -> None:
    self.arc((0.25*W, 0), (0.75*W, H/2))
    self.arc((0, H/2-L), (W, 1.5*H), start=-180, end=-57)
    self.line((W/2+L/2, H-L/2), (L/2, H-L/2), (W/2+L/2, H-L/2))

@Files.createImage("Icons")
def Users(self, W, H, L, C, B) -> None:
    self.load(User, size=(W*3/5, H*3/5), offset=(W*2/5, H/5))
    self.load(User2, size=(W*3/5, H*3/5), offset=(0, H/5))

@Files.createImage("Icons")
def Sliders(self, W, H, L, C, B) -> None:
    for y, x in {H/6: W/2, H/2: W-L/2, 5/6*H: W/4}.items():
        self.line((L/2, y), (W-L/2, y))
        self.rectangle((x-L, y-L), (x+L, y+L), outline=B, fill=B)
        self.line((x, y-L*3/4), (x, y+L*3/4), rounded=True)

@Files.createImage("Icons")
def Graph(self, W, H, L, C, B) -> None:
    self.line((L/2, L/2), (L/2, H-L/2), (W-L/2, W-L/2), rounded=True)
    P = ((0.2*W, 0.8*H), (0.45*W, 0.35*H), (0.7*W, 0.6*H), (W-L/2, L/2))
    self.line(*P, rounded=True)

@Files.createImage("Icons")
def Audio(self, W, H, L, C, B) -> None:
    self.line((L/2, H/3), (L/2, H*2/3), (W/4, H*2/3), (W/2, H-L), (W/2, L), (W/4, H/3), (L/2, H/3), rounded=True)
    self.arc((0, 0), (W, H), start=-55, end=55, rounded=True)
    self.arc((W/3+L/3, H/4), (W*6.25/8+L/3, H*3/4), start=-60, end=60, rounded=True)

@Files.createImage("Icons")
def Monitor(self, W, H, L, C, B) -> None:
    self.roundedRectangle((0, L/2), (W, H*3/4), fill=None)
    self.line((W*0.3, H-L), (W*0.7, H-L), rounded=True)
    self.line((W/2, H*3/4), (W/2, H-L))

@Files.createImage("Icons")
def Splitscreen(self, W, H, L, C, B) -> None:
    self.load(Monitor)
    self.line((W/2, L), (W/2, H-L))

@Files.createImage("Icons")
def Cap(self, W, H, L, C, B) -> None:
    self.line((W/2, H/10+L/2), (W-L/2, H*0.35), (W/2, H*0.6), (L/2, H*0.35), (W/2, H/10+L/2), rounded=True)
    for i in (-1, 1):
        self.line((W/2+i*W/4, H/2), (W/2+i*W/4, H*0.7), rounded=True)
    self.arc((W/4-L/2, H/2), (W*3/4+L/2, H*0.9), start=0, end=180)
    self.line((L, H*0.35), (L, H*0.6), rounded=True)

def Cog(self, W, H, L, C, B) -> None:
    self.arc((0.15*W, 0.15*H), (0.85*W, 0.85*H))
    for i in range(0, 360, 45):
        self.line((W/2+Math.cos(i)*W*0.35, H/2+Math.sin(i)*W*0.35), (W/2+Math.cos(i)*W*0.4, H/2+Math.sin(i)*W*0.4), rounded=True)

@Files.createImage("Icons")
def Cogs(self, W, H, L, C, B) -> None:
    self.load(Cog, size=(W*0.55, H*0.55), offset=(0, H*0.365))
    self.load(Cog, size=(W*0.55, H*0.55), offset=(W*0.45, H*0.085))

@Files.createImage("Icons")
def Keyboard(self, W, H, L, C, B) -> None:
    S = W/3-L/2
    G = L*3/4
    self.roundedRectangle((S, H/2-S-G/2), (S*2, H/2-G/2), radius=L/2, fill=None)
    for i in range(3):
        self.roundedRectangle((S*i+G*i, H/2+G/2), (S*(i+1)+G*i, H/2+G/2+S), radius=L/2, fill=None)

@Files.createImage("Icons")
def Play(self, W, H, L, C, B) -> None:
    self.arc((0, 0), (W, H))
    R = 0.25*W
    A = (0, 120, 240)
    for a, b in ((A[i-1], A[i]) for i in range(3)):
        self.line((W/2+Math.cos(a)*R, H/2+Math.sin(a)*R), (W/2+Math.cos(b)*R, H/2+Math.sin(b)*R), rounded=True)

@Files.createImage("Icons")
def Warehouse(self, W, H, L, C, B) -> None:
    self.line((L/2, H), (L/2, H/3), (W/2, L/2), (W-L/2, H/3), (W-L/2, H))
    self.line((L/2, H*0.4-L/2), (W-L/2, H*0.4-L/2))
    for y in range(H-L//2, H//3+L, -L*2):
        self.line((L*2, y), (W-L*2, y))

@Files.createImage("Icons")
def Shutdown(self, W, H, L, C, B) -> None:
    self.arc((L/2, L), (W-L/2, H), start=-55, end=-125, rounded=True)
    self.line((W/2, L/2), (W/2, H/2), rounded=True)

@Files.createImage("Icons")
def Home(self, W, H, L, C, B) -> None:
    self.line((W/6, H-L/2), (W*5/6, H-L/2))
    for i in (-1, 1):
        self.line((W/2+i*W*0.35, H), (W/2+i*W*0.35, H*0.4))
    self.line((L/2, H/2), (W/2, L/2), (W-L/2, H/2), rounded=True)
    self.rectangle((W/2-L*1.5, H*3/5), (W/2+L*1.5, H), fill=None)

@Files.createImage("Icons")
def Search(self, W, H, L, C, B) -> None:
    self.arc((0, 0), (W*0.7, H*0.7))
    self.line((W*0.6, H*0.6), (W-L/2, H-L/2), rounded=True)

@Files.createImage("Icons")
def Flag(self, W, H, L, C, B) -> None:
    O = (0, H*0.4)
    self.line((W-L*1.5, H*0.1+O[0]), (W-L*1.5, H*0.1+O[1]), rounded=True)
    for o in O:
        self.arc((-L/2, o), (W*2/3-L/2, H/2+o), start=-120, end=-45)
        self.arc((W/3, -L-H/5+o), (W, H*0.3-L+o), start=50, end=130)
    self.line((L*1.5, H), (L*1.5, L*0.7), (L*1.5, H))

@Files.createImage("Icons")
def Cursor(self, W, H, L, C, B) -> None:
    C = ((W*0.60, H*0.87), (W*0.4, H*0.5), (W*0.7, H*0.45), (L/2, L/2), (L/2, H*0.80), (W*0.25, H*0.58), (W*0.45, H-L/2), (W*0.60, H*0.87))
    self.line(*((x+W*0.12, y) for x, y in C), rounded=True)

@Files.createImage("Icons")
def Book(self, W, H, L, C, B) -> None:
    for i in range(3):
        self.line((L/2+i*(W/2-L/2), H*0.1), (L/2+i*(W/2-L/2), H-L))
    for i in range(2):
        for j in (0, 4):
            self.arc((-W/4+W/2*i, L*2*j+L/20), (W*3/4+W/2*i, H+L*2*j+L/20), start=-123 if i else -116, end=-64 if i else -57, rounded=True)

@Files.createImage("Icons")
def Circle(self, W, H, L, C, B) -> None:
    self.arc((W/2-L*1.5, H/2-L*1.5), (W/2+L*1.5, H/2+L*1.5))

@Files.createImage("Icons")
def Plus(self, W, H, L, C, B) -> None:
    self.line((W/2, L/2), (W/2, H-L/2), rounded=True)
    self.line((L/2, H/2), (W-L/2, H/2), rounded=True)

@Files.createImage("Icons")
def Trash(self, W, H, L, C, B) -> None:
    for i in (-1, 1):
        self.line((W/2+i*L, L*4), (W/2+i*L, H-L*2.5), rounded=True)
    self.line((W/2-L*3, L*2), (W/2-L*3, H-L/2), (W/2+L*3, H-L/2), (W/2+L*3, L*2), rounded=True)
    self.line((L, L*2), (W-L, L*2), rounded=True)
    self.line((W*1/3, L*2), (W*1/3, L/2), (W*2/3, L/2), (W*2/3, L*2), rounded=True)

@Files.createImage("Icons")
def Metro(self, W, H, L, C, B) -> None:
    for i in range(2):
        self.line((W/2, H/2), (i*W, H+L*2.5))
    self.line((0, H*0.8), (W, H*0.8), fill=B)
    self.roundedRectangle((W*0.15, 0), (W*0.85, H*0.8), fill=B)
    for i in (-1, 1):
        self.dot((W/2+i*W/6, H*0.6))
    self.line((W*0.15, H*0.45), (W*0.85, H*0.45))

@Files.createImage("Icons")
def Babel(self, W, H, L, C, B) -> None:
    for index, (left, right) in enumerate(zip(zip(range(L//2, W, L), range(H-L//2-L//4, 0, -2*L)), zip(range(W-L//2, 0, -L), range(H-L-L//2-L//4, 0, -2*L)))):
        self.line((left[0], min(left[1]+L*1.75, H)), left, right, (right[0], min(right[1]+L*2, H)))
        if index == 2:
            self.line((left[0]+L, left[1]-L/2), (left[0]+L, L/2), rounded=True)
            self.line((right[0]-L, right[1]), (right[0]-L, L/2), rounded=True)
            self.line((left[0]+L, L*1.25), (right[0]-L, L*1.25), rounded=True)
            self.line((W/2, L/2), (W/2, L*1.25), rounded=True)
            break

@Files.createImage("Icons")
def Stopwatch(self, W, H, L, C, B) -> None:
    self.line((W*0.4, L/2), (W*0.6, L/2), rounded=True)
    self.line((W/2, 0), (W/2, H*0.15))
    self.arc((W*0.075, H*0.15), (W*0.925, H))
    self.line((W/2, H*0.575), (W/2, H*0.35), rounded=True)
    self.line((W/2, H*0.575), (W/2+Math.cos(30)*W*0.15, H*0.575+Math.sin(30)*H*0.15), rounded=True)
    for i in (-45, -135):
        self.line((W/2+Math.cos(i)*W*0.45, H*0.575+Math.sin(i)*H*0.45), (W/2+Math.cos(i)*W*0.375, H*0.575+Math.sin(i)*H*0.375), rounded=True)

@Files.createImage("Icons")
def Crosshair(self, W, H, L, C, B) -> None:
    self.arc((0.1*W, 0.1*H), (0.9*W, 0.9*H))
    self.dot((W/2, H/2))
    for i in range(0, 360, 90):
        self.line((W/2+Math.cos(i)*W/4, H/2+Math.sin(i)*H/4), (W/2+Math.cos(i)*(W/2-L/2), H/2+Math.sin(i)*(H/2-L/2)), rounded=True)

@Files.createImage("Icons")
def Pin(self, W, H, L, C, B) -> None:
    R = W*0.3
    A = 20
    self.arc((W/2-R, 0), (W/2+R, R*2), rounded=True, start=180-A, end=360+A)
    self.dot((W/2, R), width=L*1.5)
    points = []
    for i in [180-A, 360+A]:
        points.append((W/2+Math.cos(i)*(R-L/2), R+Math.sin(i)*(R-L/2)))
    points.insert(1, (W/2, H-L/2))
    self.line(*points, rounded=True)

@Files.createImage("Icons")
def Code(self, W, H, L, C, B) -> None:
    for i in [-1, 1]:
        self.line((W/2+i*W*0.2, H*0.35), (W/2+i*(W/2-L/2), H/2), (W/2+i*W*0.2, H*0.65), rounded=True)
    self.line((W*0.4, H*0.85), (W*0.6, H*0.15), rounded=True)

@Files.createImage("Icons")
def Email(self, W, H, L, C, B) -> None:
    self.arc((0, 0), (W, H), start=60, end=360, rounded=True)
    self.arc((W*0.275, H*0.275), (W*0.725, H*0.725))
    self.line((W*0.725-L/2, H*0.275+L/2), (W*0.725-L/2, H/2), rounded=True)
    self.arc((W*0.725-L, H*0.275+L/2), (W, H*0.725), start=0, end=180, rounded=True)

@Files.createImage("Icons")
def Phone(self, W, H, L, C, B) -> None:
    R = W*0.4
    self.arc((0, -L), (R*2, R*2-L), start=135, end=225, rounded=True)
    self.arc((W-R*2+L, H-R*2), (W+L, H), start=45, end=135, rounded=True)
    self.line((R+Math.cos(135)*(R-L/2), R+Math.sin(135)*(R-L/2)-L), (W-R+Math.cos(135)*(R-L/2)+L, H-R+Math.sin(135)*(R-L/2)))
    self.line(
        (R+Math.cos(225)*(R-L/2), R+Math.sin(225)*(R-L/2)-L), (R+Math.cos(225)*(R-L/2)+W/5, R+Math.sin(225)*(R-L/2)+H/5-L),
        (R+Math.cos(225)*(R-L/2)+W/10, R+Math.sin(225)*(R-L/2)+H*0.3-L), (W-R+Math.cos(45)*(R-L/2)-W*0.3+L, H-R+Math.sin(45)*(R-L/2)-H/10),
        (W-R+Math.cos(45)*(R-L/2)-W/5+L, H-R+Math.sin(45)*(R-L/2)-H/5), (W-R+Math.cos(45)*(R-L/2)+L, H-R+Math.sin(45)*(R-L/2)),
        rounded=True
    )

@Files.createImage("Icons")
def Star(self, W, H, L, C, B) -> None:
    R = W/5
    for a, b, c in ((18, 54, 90), (90, 126, 162), (162, 198, 234), (234, 270, 306), (306, 342, 18)):
        self.line((W/2+Math.cos(a)*R, H/2+Math.sin(a)*R), (W/2+Math.cos(b)*(W/2-L/2), H/2+Math.sin(b)*(H/2-L/2)), (W/2+Math.cos(c)*R, H/2+Math.sin(c)*R), rounded=True)

@Files.createImage("Icons")
def Bag(self, W, H, L, C, B) -> None:
    R = W*0.2
    self.roundedRectangle((0, H*0.25), (W, H), fill=B)
    self.arc((W/2-R, 0), (W/2+R, R*2), start=180, end=360)
    for i in (-1, 1):
        self.line((W/2+i*(R-L/2), R), (W/2+i*(R-L/2), R+R/2))
    self.line((0, H*0.55), (W, H*0.55))
    self.line((W/2, H*0.5-L/3), (W/2, H*0.6+L/3), rounded=True)

@Files.createImage("Icons")
def Certificate(self, W, H, L, C, B) -> None:
    self.roundedRectangle((0, H*0.1), (W, H*0.9), fill=B)
    self.load(Star, size=(W*0.5, H*0.5), offset=(W/2-W*0.25, H/2-H*0.25))

@Files.createImage("Icons")
def Speech(self, W, H, L, C, B) -> None:
    self.arc((0, H*0.2), (W, H*0.8), start=140, end=360+100, rounded=True)
    self.line((W/2+Math.cos(140)*(W/2-L/2), H/2+Math.sin(140)*(H*0.3-L/2)), (L, H-L), (W/2+Math.cos(360+100)*(W/2-L/2), H/2+Math.sin(360+100)*(H*0.3-L/2)), rounded=True)

@Files.createImage("Icons")
def Birth(self, W, H, L, C, B) -> None:
    R = W/5
    for i in range(-90, 270, 360//5):
        self.line((W/2, H/2), (W/2+Math.cos(i)*W/3, H/2+Math.sin(i)*H/3), rounded=True)

@Files.createImage("Icons")
def Server(self, W, H, L, C, B) -> None:
    P = L
    self.roundedRectangle((P, 0), (W-P, H), fill=None)
    S = [L/2, H-L/2]
    for i in range(1, 3):
        Y = L/2+(H-L)*i/3
        self.line((L, Y), (W-L, Y))
        S.insert(len(S)-1, Y)
    for y in ((y1+y2)/2 for y1, y2 in zip(S, S[1:])):
        for i in range(2):
            self.dot((P+2*L+1.5*L*i, y))

@Files.createImage("Icons")
def Network(self, W, H, L, C, B) -> None:
    self.line((0, H/2), (W, H/2))
    self.line((W/2, H/2), (W/2, L*3))
    self.roundedRectangle((W/2-L*1.75, 0), (W/2+L*1.75, L*3.5), fill=None)
    for i in (-1, 1):
        x = W/2+i*W/4
        self.line((x, H/2), (x, H-3*L))
        self.roundedRectangle((x-L*1.75, H-L*3.5), (x+L*1.75, H), fill=None)

@Files.createImage("Icons")
def Logo(self, W, H, L, C, B) -> None:
    for a in range(30, 390, 60):
        self.line((W/2, H/2), (W/2+Math.cos(a)*(W/2-L/2), H/2+Math.sin(a)*(H/2-L/2)), rounded=True)
        self.line((W/2+Math.cos(a)*(W/2-L/2), H/2+Math.sin(a)*(H/2-L/2)), (W/2+Math.cos(a+60)*(W/2-L/2), H/2+Math.sin(a+60)*(H/2-L/2)), rounded=True)

@Files.createImage("Icons")
def Folder(self, W, H, L, C, B) -> None:
    self.line((L/2, H-L*1.5), (W/4, H/2), (W-L/2, H/2), (W-W/4, H-L*1.5), (L/2, H-L*1.5), (L/2, L*1.5), (W/3, L*1.5), (W/3+L, L*2.5), (W-W/4, L*2.5), (W-W/4, H/2-L))

@Files.createImage("Icons")
def Cube(self, W, H, L, C, B) -> None:
    self.line((W*0.6, H-L/2), (L/2, H*0.85), (L/2, H*0.3), (W*0.6, H*0.4), (W*0.6, H-L/2), (W-L/2, H*0.7), (W-L/2, H*0.15), (W*0.6, H*0.4), rounded=True)
    self.line((L/2, H*0.3), (W*0.4, L/2), (W-L/2, H*0.15), rounded=True)