from Icon import Icon, CreateIcon
import math

@CreateIcon
class Globe(Icon):
    def create(self):
        self.ellipse([0, 0, self.size, self.size], fill=self.background)
        self.ellipse([self.size*2.75/10, 0, self.size*7.25/10, self.size], fill=self.background)
        self.line([self.width/2, self.size*3.5/10, self.size-self.width/2, self.size*3.5/10])
        self.line([self.width/2, self.size*6.5/10, self.size-self.width/2, self.size*6.5/10])

@CreateIcon
class User(Icon):
    def create(self):
        self.ellipse([0.25*self.size, 0, 0.75*self.size, self.size/2], fill=self.background)
        self.arc([0, self.size/2-self.width, self.size, 1.5*self.size], -180, 0)
        self.line([0, self.size-self.width/2, self.size, self.size-self.width/2])

@CreateIcon
class Users(Icon):
    def create(self):
        self.load(User, self.size*2/3, self.size/3, 0)
        self.ellipse([self.size*0.25/3, self.size/3-self.width, self.size*0.75*2/3+self.width, self.size*2/3+self.width], outline=self.background, fill=self.background)
        self.ellipse([-self.width, self.size*2/3-self.width*2, self.size*2/3+self.width, self.size*1.5], outline=self.background, fill=self.background)
        self.load(User, self.size*2/3, 0, self.size/3)

@CreateIcon
class Sliders(Icon):
    def create(self):
        radius = self.width*1.6
        x = { 1: 1/2, 3: 5/6, 5: 1/4 }
        for i in range(1, 6, 2):
            self.line([self.width/2, self.size*i/6, self.size-self.width/2, self.size*i/6], True)
            self.ellipse([self.size*x[i]-radius, self.size*i/6-radius, self.size*x[i]+radius, self.size*i/6+radius])

@CreateIcon
class Graph(Icon):
    def create(self):
        self.line([(self.width/2, self.width/2), (self.width/2, self.size-self.width/2), (self.size-self.width/2, self.size-self.width/2)], True)
        xpos = [self.size * x for x in [0.25, 0.45, 0.7, 0.9]]
        ypos = [self.size * y for y in [0.75, 0.35, 0.6, 0.1]]
        self.line(list(zip(xpos, ypos)), True)
        radius = self.width*0.8
        for (x, y) in zip(xpos, ypos):
            self.ellipse([x-radius, y-radius, x+radius, y+radius])

@CreateIcon
class Audio(Icon):
    def create(self):
        self.line([(self.width/2, self.size/3), (self.width/2, self.size*2/3), (self.size/4, self.size*2/3), (self.size/2, self.size-self.width), (self.size/2, self.width), (self.size/4, self.size/3), (self.width/2, self.size/3)], True)
        self.arc([0, 0, self.size, self.size], -60, 60)
        self.arc([self.size/3, self.size/4, self.size*6.25/8, self.size*3/4], -65, 65)

@CreateIcon
class Monitor(Icon):
    def create(self):
        self.line([self.size/4, self.size-self.width/2, self.size*3/4, self.size-self.width/2], True)
        self.line([(self.width/2, self.size*3.6/5), (self.width/2, self.width/2), (self.size-self.width/2, self.width/2), (self.size-self.width/2, self.size*3.2/5), (self.width/2, self.size*3.2/5), (self.width/2, self.size*3.6/5), (self.size-self.width/2, self.size*3.6/5), (self.size-self.width/2, self.size/2)], True)
        self.line([(self.size/2-self.width/2, self.size-self.width/2), (self.size/2-self.width/2, self.size*3.6/5), (self.size/2+self.width/2, self.size*3.6/5), (self.size/2+self.width/2, self.size-self.width/2)], True)

@CreateIcon
class Splitscreen(Icon):
    def create(self):
        self.load(Monitor, self.size, 0, 0)
        self.line([self.size/2, 0, self.size/2, self.size*2/3])

@CreateIcon
class Cap(Icon):
    def create(self):
        self.arc([self.size/5, self.size*2/3, self.size*4/5, self.size], 0, 180)
        self.line([self.size/5+self.width/2, self.size*5/6, self.size/5+self.width, self.size/2], True)
        self.line([self.size*4/5-self.width/2, self.size*5/6, self.size*4/5-self.width, self.size/2], True)
        self.line([(self.width/2, self.size*4/10), (self.size/2, self.size*7/10), (self.size-self.width/2, self.size*4/10)], fill=self.background)
        self.line([(self.size/2, self.width/2), (self.width/2, self.size*3/10), (self.size/2, self.size*6/10), (self.size-self.width/2, self.size*3/10), (self.size/2, self.width/2)], True)
        self.line([(self.size/6, self.size/2), (self.size/2, self.size/4+self.width/2), (self.size/6, self.size/2), (self.size/9, self.size*0.55), (self.size/10, self.size*0.575), (self.size/14, self.size*3/4)], True)

class Cog(Icon):
    def create(self):
        self.line([(self.size/2, self.width/2), (self.size/2, self.size-self.width/2)], True)
        self.line([(self.width/2, self.size/2), (self.size-self.width/2, self.size/2)], True)
        self.line([(self.size*0.2, self.size*0.2), (self.size*0.8, self.size*0.8)], True)
        self.line([(self.size*0.2, self.size*0.8), (self.size*0.8, self.size*0.2)], True)
        self.ellipse([0.15*self.size, 0.15*self.size, 0.85*self.size, 0.85*self.size], fill=self.background)

@CreateIcon
class Cogs(Icon):
    def create(self):
        self.load(Cog, self.size*0.55, 0, self.size*0.365)
        self.load(Cog, self.size*0.55, self.size*0.45, self.size*0.085)

@CreateIcon
class Keyboard(Icon):
    def create(self):
        length = (self.size-self.width*1.5)/3
        gap = self.width*1.5/2
        self.rectangle([(length, self.size/2-length-gap/2), (length*2, self.size/2-gap/2)], radius=self.width/2)
        for i in range(3):
            self.rectangle([(length*i+gap*i, self.size/2+gap/2), (length*(i+1)+gap*i, self.size/2+gap/2+length)], radius=self.width/2)

@CreateIcon
class Play(Icon):
    def create(self):
        self.ellipse([0, 0, self.size, self.size], fill=self.background)
        height = self.size/2
        length = math.sqrt(2)/2*height
        self.line([(self.size/2-length/2+self.width*2/3, self.size/2-height/2), (self.size/2-length/2+self.width*2/3, self.size/2+height/2), (self.size/2+length/2+self.width*2/3, self.size/2), (self.size/2-length/2+self.width*2/3, self.size/2-height/2)], True)

@CreateIcon
class Warehouse(Icon):
    def create(self):
        self.line([(self.width/2, self.size), (self.width/2, self.size/3), (self.size/2, self.width/2), (self.size-self.width/2, self.size/3), (self.size-self.width/2, self.size)])
        self.line([(self.width/2, self.size*0.4-self.width/2), (self.size-self.width/2, self.size*0.4-self.width/2)])
        for y in range(self.size-self.width//2, self.size//3+self.width, -self.width*2):
            self.line([(self.width*2, y), (self.size-self.width*2, y)])

@CreateIcon
class Shutdown(Icon):
    def create(self):
        self.arc([self.width/2, self.width, self.size-self.width/2, self.size], -55, -125)
        self.line([self.size/2, self.width/2, self.size/2, self.size/2], True)

@CreateIcon
class Home(Icon):
    def create(self):
        self.line([(self.size/6, self.size-self.width/2), (self.size*5/6, self.size-self.width/2)])
        for i in [-1, 1]:
            self.line([(self.size/2+i*self.size*0.35, self.size), (self.size/2+i*self.size*0.35, self.size*0.4)])
            self.line([(self.size/2+i*self.width/2, self.size*3/5), (self.size/2+i*self.width/2, self.size)])
        self.line([(self.width/2, self.size/2), (self.size/2, self.width/2), (self.size-self.width/2, self.size/2)], True)

@CreateIcon
class Search(Icon):
    def create(self):
        self.ellipse([0, 0, self.size*0.7, self.size*0.7], fill=self.background)
        self.line([self.size*0.6, self.size*0.6, self.size-self.width/2, self.size-self.width/2], True)
