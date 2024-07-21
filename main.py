from PIL import Image, ImageDraw

def icon() -> None:
    def wrap(func) -> None:
        size = 100
        sample = 5
        image = Image.new("RGBA", (size*sample, size*sample), (255, 255, 255, 0))
        func(
            draw = ImageDraw.Draw(image),
            size = size*sample,
            outline = (255, 255, 255),
            fill = None,
            width = 10*sample,
        )
        image = image.resize((size, size), resample=Image.LANCZOS)
        image.save("{}.png".format(func.__name__), "PNG")
    return wrap

#@icon()
def Singleplayer(draw: ImageDraw, size: int, outline: tuple, fill: tuple, width: float) -> None:
    draw.ellipse([0.25*size, 0, 0.75*size, size/2], fill, outline, width)
    draw.arc([0, size/2-width, size, 1.5*size], -180, 180, fill, width)
    draw.line([0, size-width/2, size, size-width/2], fill, width)

#@icon()
def Multiplayer(draw: ImageDraw, size: int, outline: tuple, fill: tuple, width: float) -> None:
    def person(draw: ImageDraw, size: int, outline: tuple, fill: tuple, width: float, x: float, y: float):
        draw.ellipse([0.25*size+x-width, y-width, 0.75*size+x+width, size/2+y+width], (0,0,0,0), None, width*2)
        draw.arc([x-width, size/2-width+y-width, size+x+width, 1.5*size+y+width], -180, 0, (0,0,0,0), width*2)
        draw.ellipse([0.25*size+x, y, 0.75*size+x, size/2+y], fill, outline, width)
        draw.arc([x, size/2-width+y, size+x, 1.5*size+y], -180, 0, outline, width)
        draw.line([x, size-width/2+y, size+x, size-width/2+y], outline, width)
    person(draw, size*2/3, outline, fill, width, size/3, 0)
    person(draw, size*2/3, outline, fill, width, 0, size/3)

#@icon()
def Settings(draw: ImageDraw, size: int, outline: tuple, fill: tuple, width: float) -> None:
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
def Statistics(draw: ImageDraw, size: int, outline: tuple, fill: tuple, width: float) -> None:
    def polyline(points: tuple):
        draw.line([points[1]] + points + [points[-2]], outline, width, joint="curve")
    polyline([(size-width/2, size-width/2), (width/2, size-width/2), (width/2, width/2)])
    polyline([(size*1/4-width/2, size*4/5), (size*2/4-width/2, size*2/5), (size*3/4-width/2, size*3/5), (size-width/2, size*1/5)])

#@icon()
def Graphics(draw: ImageDraw, size: int, outline: tuple, fill: tuple, width: float) -> None:
    def polyline(points: tuple):
        draw.line([points[1]] + points + [points[-2]], outline, width, joint="curve")
    polyline([(size*2/8, size-width/2), (size*6/8, size-width/2)])
    polyline([(width/2, size*3.6/5), (width/2, width/2), (size-width/2, width/2), (size-width/2, size*3.2/5), (width/2, size*3.2/5), (width/2, size*3.6/5), (size-width/2, size*3.6/5), (size-width/2, size/2)])
    polyline([(size/2-width/2, size-width/2), (size/2-width/2, size*3.6/5), (size/2+width/2, size*3.6/5), (size/2+width/2, size-width/2)])

#@icon()
def Audio(draw: ImageDraw, size: int, outline: tuple, fill: tuple, width: float) -> None:
    draw.arc([0, 0, size, size], -60, 60, outline, width)
    draw.arc([size/3, size/4, size*6.25/8, size*3/4], -65, 65, outline, width)
    def polygon(points: tuple):
        draw.line(points + points[:2], outline, width, joint="curve")
    polygon([(width/2, size/3), (width/2, size*2/3), (size/4, size*2/3), (size/2, size-width), (size/2, width), (size/4, size/3)])

#@icon()
def Input(draw: ImageDraw, size: int, outline: tuple, fill: tuple, width: float) -> None:
    def polygon(points: tuple):
        draw.line(points + points[:2], outline, width, joint="curve")
    def rectangle(start: tuple, end: tuple, direction: int):
        polygon([(start[0]+width/2, start[1]+width/2), (end[0]-width/2, start[1]+width/2), (end[0]-width/2, end[1]-width/2), (start[0]+width/2, end[1]-width/2)])
        draw.rectangle([start[0]+width, start[1]+width, end[0]-width, end[1]-width], outline)
        delta = end[0] - start[0]
        if direction == 0:
            draw.polygon([(end[0]-delta/5, end[1]-delta/5), (end[0]-delta*4/5, end[1]-delta/5), (end[0]-delta/2, end[1]-delta*4/5)], (0,0,0,0))
        elif direction == 1:
            draw.polygon([(start[0]+delta/5, start[1]+delta/5), (start[0]+delta/5, start[1]+delta*4/5), (start[0]+delta*4/5, start[1]+delta/2)], (0,0,0,0))
        elif direction == 2:
            draw.polygon([(start[0]+delta/5, start[1]+delta/5), (start[0]+delta*4/5, start[1]+delta/5), (start[0]+delta/2, start[1]+delta*4/5)], (0,0,0,0))
        elif direction == 3:
            draw.polygon([(end[0]-delta/5, end[1]-delta/5), (end[0]-delta/5, end[1]-delta*4/5), (end[0]-delta*4/5, end[1]-delta/2)], (0,0,0,0))
    length = (size-width)/3
    rectangle((size/2-length/2, size/2-width/4 - length), (size/2+length/2, size/2-width/4), 0)
    rectangle((0, size/2+width/4), (length, size/2+width/4 + length), 3)
    rectangle((size/2-length/2, size/2+width/4), (size/2+length/2, size/2+width/4 + length), 2)
    rectangle((size-length, size/2+width/4), (size, size/2+width/4 + length), 1)

@icon()
def General(draw: ImageDraw, size: int, outline: tuple, fill: tuple, width: float) -> None:
    def polygon(points: tuple):
        draw.line(points + points[:2], outline, width, joint="curve")
    def dot(point: tuple):
        length = width*3.1
        draw.ellipse([point[0]-length/2, point[1]-length/2, point[0]+length/2, point[1]+length/2], outline)
    polygon([(width/2, size*1/6), (size-width/2, size*1/6)])
    dot([size/2, size/6])
    polygon([(width/2, size/2), (size-width/2, size/2)])
    dot([size*5/6, size/2])
    polygon([(width/2, size*5/6), (size-width/2, size*5/6)])
    dot([size/4, size*5/6])