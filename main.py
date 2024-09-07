from Icon import Icon, CreateIcon
import math

## \image html Globe.png
@CreateIcon
def Globe(self):
    self.ellipse([0, 0, self.size, self.size], fill=self.background)
    self.ellipse([self.size*2.75/10, 0, self.size*7.25/10, self.size], fill=self.background)
    self.line([self.width/2, self.size*3.5/10, self.size-self.width/2, self.size*3.5/10])
    self.line([self.width/2, self.size*6.5/10, self.size-self.width/2, self.size*6.5/10])

## \image html User.png
@CreateIcon
def User(self):
    self.ellipse([0.25*self.size, 0, 0.75*self.size, self.size/2], fill=self.background)
    self.arc([0, self.size/2-self.width, self.size, 1.5*self.size], -180, 0)
    self.line([0, self.size-self.width/2, self.size, self.size-self.width/2])

## \image html Users.png
@CreateIcon
def Users(self):
    self.load(User, self.size*2/3, self.size/3, 0)
    self.ellipse([self.size*0.25/3, self.size/3-self.width, self.size*0.75*2/3+self.width, self.size*2/3+self.width], outline=self.background, fill=self.background)
    self.ellipse([-self.width, self.size*2/3-self.width*2, self.size*2/3+self.width, self.size*1.5], outline=self.background, fill=self.background)
    self.load(User, self.size*2/3, 0, self.size/3)

## \image html Sliders.png
@CreateIcon
def Sliders(self):
    radius = self.width*1.6
    x = { 1: 1/2, 3: 5/6, 5: 1/4 }
    for i in range(1, 6, 2):
        self.line([self.width/2, self.size*i/6, self.size-self.width/2, self.size*i/6], True)
        self.ellipse([self.size*x[i]-radius, self.size*i/6-radius, self.size*x[i]+radius, self.size*i/6+radius])

## \image html Graph.png
@CreateIcon
def Graph(self):
    self.line([(self.width/2, self.width/2), (self.width/2, self.size-self.width/2), (self.size-self.width/2, self.size-self.width/2)], True)
    xpos = [self.size * x for x in [0.25, 0.45, 0.7, 0.9]]
    ypos = [self.size * y for y in [0.75, 0.35, 0.6, 0.1]]
    self.line(list(zip(xpos, ypos)), True)
    radius = self.width*0.8
    for (x, y) in zip(xpos, ypos):
        self.ellipse([x-radius, y-radius, x+radius, y+radius])

## \image html Audio.png
@CreateIcon
def Audio(self):
    self.line([(self.width/2, self.size/3), (self.width/2, self.size*2/3), (self.size/4, self.size*2/3), (self.size/2, self.size-self.width), (self.size/2, self.width), (self.size/4, self.size/3), (self.width/2, self.size/3)], True)
    self.arc([0, 0, self.size, self.size], -60, 60)
    self.arc([self.size/3, self.size/4, self.size*6.25/8, self.size*3/4], -65, 65)

## \image html Monitor.png
@CreateIcon
def Monitor(self):
    self.line([self.size/4, self.size-self.width/2, self.size*3/4, self.size-self.width/2], True)
    self.line([(self.width/2, self.size*3.6/5), (self.width/2, self.width/2), (self.size-self.width/2, self.width/2), (self.size-self.width/2, self.size*3.2/5), (self.width/2, self.size*3.2/5), (self.width/2, self.size*3.6/5), (self.size-self.width/2, self.size*3.6/5), (self.size-self.width/2, self.size/2)], True)
    self.line([(self.size/2-self.width/2, self.size-self.width/2), (self.size/2-self.width/2, self.size*3.6/5), (self.size/2+self.width/2, self.size*3.6/5), (self.size/2+self.width/2, self.size-self.width/2)], True)

## \image html Splitscreen.png
@CreateIcon
def Splitscreen(self):
    self.load(Monitor, self.size, 0, 0)
    self.line([self.size/2, 0, self.size/2, self.size*2/3])

## \image html Cap.png
## \todo Remake icon
@CreateIcon
def Cap(self):
    self.arc([self.size/5, self.size*2/3, self.size*4/5, self.size], 0, 180)
    self.line([self.size/5+self.width/2, self.size*5/6, self.size/5+self.width, self.size/2], True)
    self.line([self.size*4/5-self.width/2, self.size*5/6, self.size*4/5-self.width, self.size/2], True)
    self.line([(self.width/2, self.size*4/10), (self.size/2, self.size*7/10), (self.size-self.width/2, self.size*4/10)], fill=self.background)
    self.line([(self.size/2, self.width/2), (self.width/2, self.size*3/10), (self.size/2, self.size*6/10), (self.size-self.width/2, self.size*3/10), (self.size/2, self.width/2)], True)
    self.line([(self.size/6, self.size/2), (self.size/2, self.size/4+self.width/2), (self.size/6, self.size/2), (self.size/9, self.size*0.55), (self.size/10, self.size*0.575), (self.size/14, self.size*3/4)], True)

def Cog(self):
    self.line([(self.size/2, self.width/2), (self.size/2, self.size-self.width/2)], True)
    self.line([(self.width/2, self.size/2), (self.size-self.width/2, self.size/2)], True)
    self.line([(self.size*0.2, self.size*0.2), (self.size*0.8, self.size*0.8)], True)
    self.line([(self.size*0.2, self.size*0.8), (self.size*0.8, self.size*0.2)], True)
    self.ellipse([0.15*self.size, 0.15*self.size, 0.85*self.size, 0.85*self.size], fill=self.background)

## \image html Cogs.png
@CreateIcon
def Cogs(self):
    self.load(Cog, self.size*0.55, 0, self.size*0.365)
    self.load(Cog, self.size*0.55, self.size*0.45, self.size*0.085)

## \image html Keyboard.png
@CreateIcon
def Keyboard(self):
    length = (self.size-self.width*1.5)/3
    gap = self.width*1.5/2
    self.rectangle([(length, self.size/2-length-gap/2), (length*2, self.size/2-gap/2)], radius=self.width/2)
    for i in range(3):
        self.rectangle([(length*i+gap*i, self.size/2+gap/2), (length*(i+1)+gap*i, self.size/2+gap/2+length)], radius=self.width/2)

## \image html Play.png
## \todo Tweak icon
@CreateIcon
def Play(self):
    self.ellipse([0, 0, self.size, self.size], fill=self.background)
    height = self.size/2
    length = math.sqrt(2)/2*height
    self.line([(self.size/2-length/2+self.width*2/3, self.size/2-height/2), (self.size/2-length/2+self.width*2/3, self.size/2+height/2), (self.size/2+length/2+self.width*2/3, self.size/2), (self.size/2-length/2+self.width*2/3, self.size/2-height/2)], True)

## \image html Warehouse.png
@CreateIcon
def Warehouse(self):
    self.line([(self.width/2, self.size), (self.width/2, self.size/3), (self.size/2, self.width/2), (self.size-self.width/2, self.size/3), (self.size-self.width/2, self.size)])
    self.line([(self.width/2, self.size*0.4-self.width/2), (self.size-self.width/2, self.size*0.4-self.width/2)])
    for y in range(self.size-self.width//2, self.size//3+self.width, -self.width*2):
        self.line([(self.width*2, y), (self.size-self.width*2, y)])

## \image html Shutdown.png
@CreateIcon
def Shutdown(self):
    self.arc([self.width/2, self.width, self.size-self.width/2, self.size], -55, -125)
    self.line([self.size/2, self.width/2, self.size/2, self.size/2], True)

## \image html Home.png
@CreateIcon
def Home(self):
    self.line([(self.size/6, self.size-self.width/2), (self.size*5/6, self.size-self.width/2)])
    for i in [-1, 1]:
        self.line([(self.size/2+i*self.size*0.35, self.size), (self.size/2+i*self.size*0.35, self.size*0.4)])
        self.line([(self.size/2+i*self.width/2, self.size*3/5), (self.size/2+i*self.width/2, self.size)])
    self.line([(self.width/2, self.size/2), (self.size/2, self.width/2), (self.size-self.width/2, self.size/2)], True)

## \image html Search.png
@CreateIcon
def Search(self):
    self.ellipse([0, 0, self.size*0.7, self.size*0.7], fill=self.background)
    self.line([self.size*0.6, self.size*0.6, self.size-self.width/2, self.size-self.width/2], True)

## \image html Flag.png
@CreateIcon
def Flag(self):
    width = 0.35*self.size
    height = 0.55*self.size
    self.line([(self.size/2-width, self.size), (self.size/2-width, self.width/2), (self.size/2, self.width/2), (self.size/2+self.width, self.width*1.5), (self.size/2+width, self.width*1.5), (self.size/2+width, height), (self.size/2+self.width/2, height), (self.size/2-self.width/2, height-self.width), (self.size/2-width, height-self.width)], True)

## \image html Cursor.png
@CreateIcon
def Cursor(self):
    coords = [(self.size*0.60, self.size*0.87), (self.size*0.4, self.size*0.5), (self.size*0.7, self.size*0.45), (self.width/2, self.width/2), (self.width/2, self.size*0.80), (self.size*0.25, self.size*0.58), (self.size*0.45, self.size-self.width/2)]
    self.line([(c[0]+self.size*0.12, c[1]) for c in coords], True, polygon=True)

## \image html Book.png
@CreateIcon
def Book(self):
    for i in range(3):
        self.line([(self.width/2+i*(self.size/2-self.width/2), self.size*0.1), (self.width/2+i*(self.size/2-self.width/2), self.size*0.9)])
    for i in range(2):
        for j in [0, 4]:
            self.arc([(-self.size/4+self.size/2*i, self.width*2*j+self.width/20), (self.size*3/4+self.size/2*i, self.size+self.width*2*j+self.width/20)], -130, -50)

## \image html Circle.png
@CreateIcon
def Circle(self):
    self.ellipse([(self.size/5, self.size/5), (self.size*4/5, self.size*4/5)])

## \image html Plus.png
@CreateIcon
def Plus(self):
    self.line([self.size/2, self.width/2, self.size/2, self.size-self.width/2], True)
    self.line([self.width/2, self.size/2, self.size-self.width/2, self.size/2], True)

## \image html Trash.png
@CreateIcon
def Trash(self):
    for i in (-1, 1):
        self.line([(self.size/2+i*self.width, self.width*4), (self.size/2+i*self.width, self.size-self.width*2.5)], True)
    self.line([(self.size/2-self.width*3, self.width*2), (self.size/2-self.width*3, self.size-self.width/2), (self.size/2+self.width*3, self.size-self.width/2), (self.size/2+self.width*3, self.width*2)], True)
    self.line([(self.width, self.width*2), (self.size-self.width, self.width*2)], True)
    self.line([(self.size*1/3, self.width*2), (self.size*1/3, self.width/2), (self.size*2/3, self.width/2), (self.size*2/3, self.width*2)], True)

## \image html Metro.png
## \todo Tweak icon
@CreateIcon
def Metro(self):
    for i in range(2):
        self.line([(self.size/2, self.size*0.5), (i*self.size, self.size+self.width)])
    x = 0.2
    y = 0.75
    self.rectangle([(0, 0), (self.size, y*self.size+self.width)], fill=self.background, outline=self.background)
    self.line([(x*self.size, self.width/2), ((1-x)*self.size, self.width/2), ((1-x)*self.size, y*self.size), (x*self.size, y*self.size)], True, polygon=True)
    self.rectangle([(x*self.size, y*self.size-self.width*2.5), ((1-x)*self.size, y*self.size)])
    self.ellipse([(x*self.size+self.width*0.5, y*self.size-self.width*1.5), (x*self.size+self.width*1.5, y*self.size-self.width*0.5)], outline=self.background)
    self.ellipse([((1-x)*self.size-self.width*1.5, y*self.size-self.width*1.5), ((1-x)*self.size-self.width*0.5, y*self.size-self.width*0.5)], outline=self.background)

## \image html Babel.png
@CreateIcon
def Babel(self):
    x = self.width
    y = 2*self.width
    start = [self.width/2, self.size-self.width*0.8]
    end = [self.size-self.width/2, self.size-self.width*0.8-y/2]
    for i in range(3):
        self.line([(start[0], start[1]+0.85*y), start, end, (end[0], end[1]+0.85*y)], True)
        start[0] += x
        end[0] -= x
        for a in (start, end):
            a[1] -= y
    for a in (start, end):
        self.line([(a[0], a[1]+0.85*y), (a[0], self.width/2)], True)
    self.line([(start[0], self.width*1.25), (end[0], self.width*1.25)])
    self.line([(self.size/2, self.width/2), (self.size/2, self.width)], True)

## \image html Stopwatch.png
@CreateIcon
def Stopwatch(self):
    s = 0.85
    x = 0.10
    self.ellipse([((1-s)/2*self.size, (1-s)*self.size), ((s+(1-s)/2)*self.size, self.size)], fill=self.background)
    self.line([(self.size*(0.5-x), self.width/2), (self.size*(0.5+x), self.width/2)], True)
    self.line([(self.size/2, 0), (self.size/2, (1-s)*self.size)])
    c = (self.size/2, (1-s/2)*self.size)
    r = s/2*self.size-self.width/2
    ro = r+self.width*1.25
    si = math.sin(math.radians(45))
    co = math.cos(math.radians(45))
    for i in [-1, 1]:
        self.line([(c[0]+i*si*r, c[1]-co*r), (c[0]+i*si*ro, c[1]-co*ro)])
    ri = r-self.width*1.35
    rs = ri-self.width*0.65
    self.line([c, (c[0]+math.sin(math.radians(0))*ri, c[1]-math.cos(math.radians(0))*ri)], True)
    self.line([c, (c[0]+math.sin(math.radians(90))*rs, c[1]-math.cos(math.radians(90))*rs)], True)

## \image html Crosshair.png
@CreateIcon
def Crosshair(self):
    offset = self.size*0.1
    inset = offset+self.size*0.15
    self.ellipse([(offset, offset), (self.size-offset, self.size-offset)], fill=self.background)
    self.ellipse([(self.size/2-self.width/2, self.size/2-self.width/2), (self.size/2+self.width/2, self.size/2+self.width/2)])
    self.line([(self.width/2, self.size/2), (inset, self.size/2)], True)
    self.line([(self.size-self.width/2, self.size/2), (self.size-inset, self.size/2)], True)
    self.line([(self.size/2, self.width/2), (self.size/2, inset)], True)
    self.line([(self.size/2, self.size-self.width/2), (self.size/2, self.size-inset)], True)