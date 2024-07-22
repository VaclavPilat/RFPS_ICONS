from Icon import Icon, CreateIcon

@CreateIcon
class Globe(Icon):
    def create(self):
        self.ellipse([0, 0, self.size, self.size])
        self.ellipse([self.size*2.75/10, 0, self.size*7.25/10, self.size])
        self.line([self.width/2, self.size*3.5/10, self.size-self.width/2, self.size*3.5/10])
        self.line([self.width/2, self.size*6.5/10, self.size-self.width/2, self.size*6.5/10])

@CreateIcon
class User(Icon):
    def create(self):
        self.ellipse([0.25*self.size, 0, 0.75*self.size, self.size/2])
        self.arc([0, self.size/2-self.width, self.size, 1.5*self.size], -180, 0)
        self.line([0, self.size-self.width/2, self.size, self.size-self.width/2])

@CreateIcon
class Users(Icon):
    def create(self):
        self.load(User, self.size*2/3, self.size/3, 0)
        self.ellipse([self.size*0.25/3, self.size/3-self.width, self.size*0.75*2/3+self.width, self.size*2/3+self.width], True, self.background)
        self.ellipse([-self.width, self.size*2/3-self.width*2, self.size*2/3+self.width, self.size*1.5], True, self.background)
        self.load(User, self.size*2/3, 0, self.size/3)

@CreateIcon
class Sliders(Icon):
    def create(self):
        radius = self.width*1.6
        x = { 1: 1/2, 3: 5/6, 5: 1/4 }
        for i in range(1, 6, 2):
            self.line([self.width/2, self.size*i/6, self.size-self.width/2, self.size*i/6], True)
            self.ellipse([self.size*x[i]-radius, self.size*i/6-radius, self.size*x[i]+radius, self.size*i/6+radius], True)

@CreateIcon
class Graph(Icon):
    def create(self):
        self.line([self.width/2, self.width/2, self.width/2, self.size-self.width/2, self.size-self.width/2, self.size-self.width/2], True)
        self.line([(self.size*i/4-self.width/2, self.size*[4/5, 2/5, 3/5, 1/5][i-1]) for i in range(1, 5)], True)

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

"""
#@icon()
def General(draw: ImageDraw, size: int, outline: tuple, fill: tuple, width: float) -> None:
    def line(points: tuple) -> None:
        draw.line(points + points[:], outline, width, joint="curve")
    def cog(size: int, x: float, y: float):
        line([size/2+x, width/2+y, size/2+x, size-width/2+y])
        line([size*1/8+x, size*3/10+y, size*7/8+x, size*7/10+y])
        line([size*1/8+x, size*7/10+y, size*7/8+x, size*3/10+y])
        draw.ellipse([0.12*size+x, 0.12*size+y, 0.88*size+x, 0.88*size+y], (0,0,0,0), outline, width)
        draw.ellipse([0.12*size+x, 0.12*size+y, 0.88*size+x, 0.88*size+y], fill, outline, width)
    cog(size*3/5, 0, size*2/5)
    cog(size*3/5, size*2/5, 0)

#@icon()
def Tutorials(draw: ImageDraw, size: int, outline: tuple, fill: tuple, width: float) -> None:
    draw.arc([size/5, size*2/3, size*4/5, size], 0, 180, outline, width)
    draw.ellipse([size/5, size*5/6-width/2, size/5+width, size*5/6+width/2], outline, None, width*2)
    draw.ellipse([size*4/5-width, size*5/6-width/2, size*4/5, size*5/6+width/2], outline, None, width*2)
    draw.line([size/5+width/2, size*5/6, size/5+width, size/2], outline, width, joint="curve")
    draw.line([size*4/5-width/2, size*5/6, size*4/5-width, size/2], outline, width, joint="curve")
    draw.line([(width/2, size*4/10), (size/2, size*7/10), (size-width/2, size*4/10)], (0,0,0,0), width)
    def polygon(points):
        draw.line(points + points[:2], outline, width, joint="curve")
    polygon([(size/2, width/2), (width/2, size*3/10), (size/2, size*6/10), (size-width/2, size*3/10)])
    draw.line([(size/6, size/4+size*2.5/10), (size/2, size/4+width/2), (size/6, size/4+size*2.5/10), (size/9, size/4+size*3/10), (size/10, size/4+size*3.25/10), (size/14, size/4+size*5/10)], outline, width, joint="curve")

#@icon()
def Input(draw: ImageDraw, size: int, outline: tuple, fill: tuple, width: float) -> None:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size/4.3)
    def polygon(points: tuple):
        draw.line(points + points[:2], outline, width, joint="curve")
    def rectangle(start: tuple, end: tuple, letter: str):
        polygon([(start[0]+width/2, start[1]+width/2), (end[0]-width/2, start[1]+width/2), (end[0]-width/2, end[1]-width/2), (start[0]+width/2, end[1]-width/2)])
        draw.rectangle([start[0]+width, start[1]+width, end[0]-width, end[1]-width], outline)
        delta = end[0] - start[0]
        draw.text((start[0]+(end[0]-start[0])/2, start[1]+(end[1]-start[1])/2), letter, fill=(0,0,0,0), anchor="mm", font=font)
    length = (size-width)/3
    rectangle((size/2-length*3/4, size/2-width/4 - length), (size/2+length*1/4, size/2-width/4), "W")
    rectangle((0, size/2+width/4), (length, size/2+width/4 + length), "A")
    rectangle((size/2-length/2, size/2+width/4), (size/2+length/2, size/2+width/4 + length), "S")
    rectangle((size-length, size/2+width/4), (size, size/2+width/4 + length), "D")
"""