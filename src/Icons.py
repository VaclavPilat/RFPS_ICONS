## \file
# Functions for generating icons
from Utils.Files import createImage
import math



## \defgroup icons Generated icon images (inverted)
# <div class="inverted">
# \link Globe()
# \image html Icons/Globe.png
# \endlink
# \link User()
# \image html Icons/User.png
# \endlink
# \link Users()
# \image html Icons/Users.png
# \endlink
# \link Sliders()
# \image html Icons/Sliders.png
# \endlink
# \link Graph()
# \image html Icons/Graph.png
# \endlink
# \link Audio()
# \image html Icons/Audio.png
# \endlink
# \link Monitor()
# \image html Icons/Monitor.png
# \endlink
# \link Splitscreen()
# \image html Icons/Splitscreen.png
# \endlink
# \link Cap()
# \image html Icons/Cap.png
# \endlink
# \link Cogs()
# \image html Icons/Cogs.png
# \endlink
# \link Keyboard()
# \image html Icons/Keyboard.png
# \endlink
# \link Play()
# \image html Icons/Play.png
# \endlink
# \link Warehouse()
# \image html Icons/Warehouse.png
# \endlink
# \link Shutdown()
# \image html Icons/Shutdown.png
# \endlink
# \link Home()
# \image html Icons/Home.png
# \endlink
# \link Search()
# \image html Icons/Search.png
# \endlink
# \link Flag()
# \image html Icons/Flag.png
# \endlink
# \link Cursor()
# \image html Icons/Cursor.png
# \endlink
# \link Book()
# \image html Icons/Book.png
# \endlink
# \link Circle()
# \image html Icons/Circle.png
# \endlink
# \link Plus()
# \image html Icons/Plus.png
# \endlink
# \link Trash()
# \image html Icons/Trash.png
# \endlink
# \link Metro()
# \image html Icons/Metro.png
# \endlink
# \link Babel()
# \image html Icons/Babel.png
# \endlink
# \link Stopwatch()
# \image html Icons/Stopwatch.png
# \endlink
# \link Crosshair()
# \image html Icons/Crosshair.png
# \endlink
# </div>



@createImage("Icons")
## <div class="inverted">
# \image html Icons/Globe.png
# </div>
def Globe(self, W, H, L, C, B) -> None:
    self.ellipse((0, 0), (W, H), fill=None)
    self.ellipse((W*0.275, 0), (W*0.725, H), fill=None)
    for i in (-1, 1):
        self.line((L, H/2 + i*H*0.15), (W-L, H/2 + i*H*0.15))

@createImage("Icons")
## <div class="inverted">
# \image html Icons/User.png
# </div>
def User(self, W, H, L, C, B) -> None:
    self.ellipse((0.25*W, 0), (0.75*W, H/2), fill=None)
    self.arc((0, H/2-L), (W, 1.5*H), start=-180, end=0)
    self.line((0, H-L/2), (W, H-L/2))

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Users.png
# </div>
def Users(self, W, H, L, C, B) -> None:
    self.load(User, size=(W*2/3, H*2/3), offset=(W/3, 0))
    self.ellipse((W/6-L, H/3-L), (W/2+L, H*2/3+L), fill=B, outline=B)
    self.ellipse((-L, H*2/3-2*L), (W*2/3+L, H*4/3+L), fill=B, outline=B)
    self.load(User, size=(W*2/3, H*2/3), offset=(0, W/3))

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Sliders.png
# </div>
def Sliders(self, W, H, L, C, B) -> None:
    for y, x in {1: 1/2, 3: 5.1/6, 5: 1/4}.items():
        self.line((L/2, H*y/6), (W-L/2, H*y/6), rounded=True)
        self.ellipse((W*x-1.5*L, H*y/6-1.5*L), (W*x+1.5*L, H*y/6+1.5*L), outline=B, width=L//2)

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Graph.png
# </div>
def Graph(self, W, H, L, C, B) -> None:
    self.line((L/2, L/2), (L/2, H-L/2), (W-L/2, W-L/2), rounded=True)
    points = ((0.25*W, 0.75*H), (0.45*W, 0.35*H), (0.7*W, 0.6*H), (0.9*W, 0.1*H))
    self.line(*points)
    for x, y in points:
        self.ellipse((x-L*0.8, y-L*0.8), (x+L*0.8, y+L*0.8))

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Audio.png
# </div>
def Audio(self, W, H, L, C, B) -> None:
    self.line((L/2, H/3), (L/2, H*2/3), (W/4, H*2/3), (W/2, H-L), (W/2, L), (W/4, H/3), (L/2, H/3), rounded=True)
    self.arc((0, 0), (W, H), start=-55, end=55, rounded=True)
    self.arc((W/3, H/4), (W*6.25/8, H*3/4), start=-60, end=60, rounded=True)

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Monitor.png
# </div>
def Monitor(self, W, H, L, C, B) -> None:
    self.line((W/4, H-L/2), (W*3/4, H-L/2), rounded=True)
    self.line((L/2, H*3.6/5), (L/2, L/2), (W-L/2, L/2), (W-L/2, H*3.2/5), (L/2, H*3.2/5), (L/2, H*3.6/5), (W-L/2, H*3.6/5), (W-L/2, H/2), rounded=True)
    self.line((W/2-L/2, H-L/2), (W/2-L/2, H*3.6/5), (W/2+L/2, H*3.6/5), (W/2+L/2, H-L/2), rounded=True)

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Splitscreen.png
# </div>
def Splitscreen(self, W, H, L, C, B) -> None:
    self.load(Monitor)
    self.line((W/2, 0), (W/2, H))

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Cap.png
# </div>
def Cap(self, W, H, L, C, B) -> None:
    self.line((W/2, H/10+L/2), (W-L/2, H*0.35), (W/2, H*0.6), (L/2, H*0.35), (W/2, H/10+L/2), rounded=True)
    for i in [-1, 1]:
        self.line((W/2+i*W/4, H/2), (W/2+i*W/4, H*0.7), rounded=True)
    self.arc((W/4-L/2, H/2), (W*3/4+L/2, H*0.9), start=0, end=180)
    self.line((L, H*0.35), (L, H*0.6), rounded=True)

def Cog(self, W, H, L, C, B) -> None:
    self.ellipse((0.15*W, 0.15*H), (0.85*W, 0.85*H), fill=B)
    for degrees in range(0, 360, 45):
        sin, cos = (func(math.radians(degrees)) for func in (math.sin, math.cos))
        self.line((W/2+cos*W*0.35, H/2+sin*W*0.35), (W/2+cos*W*0.4, H/2+sin*W*0.4), rounded=True)

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Cogs.png
# </div>
def Cogs(self, W, H, L, C, B) -> None:
    self.load(Cog, size=(W*0.55, H*0.55), offset=(0, H*0.365))
    self.load(Cog, size=(W*0.55, H*0.55), offset=(W*0.45, H*0.085))

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Keyboard.png
# </div>
def Keyboard(self, W, H, L, C, B) -> None:
    length = W/3-L/2
    gap = L*3/4
    self.roundedRectangle((length, H/2-length-gap/2), (length*2, H/2-gap/2), radius=L/2)
    for i in range(3):
        self.roundedRectangle((length*i+gap*i, H/2+gap/2), (length*(i+1)+gap*i, H/2+gap/2+length), radius=L/2)

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Play.png
# </div>
def Play(self, W, H, L, C, B) -> None:
    self.ellipse((0, 0), (W, H), fill=B)
    height = H*0.35
    length = math.sqrt(3)/2*height
    points = [(W/2-length/2+L/2, H/2-height/2), (W/2-length/2+L/2, H/2+height/2), (W/2+length/2+L/2, H/2)]
    self.line(*points, rounded=True, closed=True)
    self.polygon(*points)

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Warehouse.png
# </div>
def Warehouse(self, W, H, L, C, B) -> None:
    self.line((L/2, H), (L/2, H/3), (W/2, L/2), (W-L/2, H/3), (W-L/2, H))
    self.line((L/2, H*0.4-L/2), (W-L/2, H*0.4-L/2))
    for y in range(H-L//2, H//3+L, -L*2):
        self.line((L*2, y), (W-L*2, y))

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Shutdown.png
# </div>
def Shutdown(self, W, H, L, C, B) -> None:
    self.arc((L/2, L), (W-L/2, H), start=-55, end=-125, rounded=True)
    self.line((W/2, L/2), (W/2, H/2), rounded=True)

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Home.png
# </div>
def Home(self, W, H, L, C, B) -> None:
    self.line((W/6, H-L/2), (W*5/6, H-L/2))
    for i in [-1, 1]:
        self.line((W/2+i*W*0.35, H), (W/2+i*W*0.35, H*0.4))
        self.line((W/2+i*L/2, H*3/5), (W/2+i*L/2, H))
    self.line((L/2, H/2), (W/2, L/2), (W-L/2, H/2), rounded=True)

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Search.png
# </div>
def Search(self, W, H, L, C, B) -> None:
    self.ellipse((0, 0), (W*0.7, H*0.7), fill=B)
    self.line((W*0.6, H*0.6), (W-L, H-L), rounded=True)
    self.line((W*0.7, H*0.7), (W-L*3/4, H-L*3/4), rounded=True, width=int(L*1.5))

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Flag.png
# </div>
def Flag(self, W, H, L, C, B) -> None:
    offsets = (0, H*0.4)
    self.line((W-L*1.5, H*0.1+offsets[0]), (W-L*1.5, H*0.1+offsets[1]), rounded=True)
    for offset in offsets:
        self.arc((-L/2, offset), (W*2/3-L/2, H/2+offset), start=-120, end=-45)
        self.arc((W/3, -L-H/5+offset), (W, H*0.3-L+offset), start=50, end=130)
    self.line((L*1.5, L*0.7), (L*1.5, H), rounded=True)

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Cursor.png
# </div>
def Cursor(self, W, H, L, C, B) -> None:
    coords = ((W*0.60, H*0.87), (W*0.4, H*0.5), (W*0.7, H*0.45), (L/2, L/2), (L/2, H*0.80), (W*0.25, H*0.58), (W*0.45, H-L/2), (W*0.60, H*0.87))
    self.line(*((x+W*0.12, y) for x, y in coords), rounded=True)

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Book.png
# </div>
def Book(self, W, H, L, C, B) -> None:
    for i in range(3):
        self.line((L/2+i*(W/2-L/2), H*0.1), (L/2+i*(W/2-L/2), H*0.9))
    for i in range(2):
        for j in [0, 4]:
            self.arc((-W/4+W/2*i, L*2*j+L/20), (W*3/4+W/2*i, H+L*2*j+L/20), start=-130, end=-50)

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Circle.png
# </div>
def Circle(self, W, H, L, C, B) -> None:
    self.ellipse((W/4, H/4), (W*3/4, H*3/4))

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Plus.png
# </div>
def Plus(self, W, H, L, C, B) -> None:
    self.line((W/2, L/2), (W/2, H-L/2), rounded=True)
    self.line((L/2, H/2), (W-L/2, H/2), rounded=True)

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Trash.png
# </div>
def Trash(self, W, H, L, C, B) -> None:
    for i in (-1, 1):
        self.line((W/2+i*L, L*4), (W/2+i*L, H-L*2.5), rounded=True)
    self.line((W/2-L*3, L*2), (W/2-L*3, H-L/2), (W/2+L*3, H-L/2), (W/2+L*3, L*2), rounded=True)
    self.line((L, L*2), (W-L, L*2), rounded=True)
    self.line((W*1/3, L*2), (W*1/3, L/2), (W*2/3, L/2), (W*2/3, L*2), rounded=True)

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Metro.png
# </div>
def Metro(self, W, H, L, C, B) -> None:
    for i in range(2):
        self.line((W/2, H*0.5), (i*W, H+L*2.5))
    self.roundedRectangle((0, 0), (W, H*0.8+L/2), outline=B, fill=B)
    self.roundedRectangle((W*0.15, 0), (W*0.85, H*0.8), fill=B)
    self.roundedRectangle((W*0.15, H*0.5), (W*0.85, H*0.8))
    for i in [-1, 1]:
        self.ellipse((W/2+i*W/5-L/2, H*0.7-L), (W/2+i*W/5+L/2, H*0.7), outline=B)

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Babel.png
# </div>
def Babel(self, W, H, L, C, B) -> None:
    for index, (left, right) in enumerate(zip(zip(range(L//2, W, L), range(H-L//2-L//4, 0, -2*L)), zip(range(W-L//2, 0, -L), range(H-L-L//2-L//4, 0, -2*L)))):
        self.line(left, right, rounded=True)
        self.line(left, (left[0], left[1]+L*1.75), rounded=True)
        self.line(right, (right[0], right[1]+L*2), rounded=True)
        if index == 2:
            self.line((left[0]+L, left[1]-L/2), (left[0]+L, L/2), rounded=True)
            self.line((right[0]-L, right[1]), (right[0]-L, L/2), rounded=True)
            self.line((left[0]+L, L*1.25), (right[0]-L, L*1.25), rounded=True)
            self.line((W/2, L/2), (W/2, L*1.25), rounded=True)
            break

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Stopwatch.png
# </div>
def Stopwatch(self, W, H, L, C, B) -> None:
    self.line((W*0.4, L/2), (W*0.6, L/2), rounded=True)
    self.line((W/2, 0), (W/2, H*0.15))
    self.ellipse((W*0.075, H*0.15), (W*0.925, H), fill=B)
    self.line((W/2, H*0.575), (W/2, H*0.35), rounded=True)
    self.line((W/2, H*0.575), (W/2+math.cos(math.radians(30))*W*0.15, H*0.575+math.sin(math.radians(30))*H*0.15), rounded=True)
    for i in [-45, -135]:
        sin, cos = (function(math.radians(i)) for function in (math.sin, math.cos))
        self.line((W/2+cos*W*0.45, H*0.575+sin*H*0.45), (W/2+cos*W*0.375, H*0.575+sin*H*0.375), rounded=True)

@createImage("Icons")
## <div class="inverted">
# \image html Icons/Crosshair.png
# </div>
def Crosshair(self, W, H, L, C, B) -> None:
    self.ellipse((0.1*W, 0.1*H), (0.9*W, 0.9*H), fill=None)
    self.ellipse((W/2-L/2, H/2-L/2), (W/2+L/2, H/2+L/2))
    for degrees in range(0, 360, 90):
        sin, cos = (func(math.radians(degrees)) for func in (math.sin, math.cos))
        self.line((W/2+cos*W/4, H/2+sin*H/4), (W/2+cos*(W/2-L/2), H/2+sin*(H/2-L/2)), rounded=True)