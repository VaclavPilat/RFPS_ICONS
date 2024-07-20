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

@icon()
def Singleplayer(draw: ImageDraw, size: int, outline: tuple, fill: tuple, width: float) -> None:
    draw.ellipse([0.25*size, 0, 0.75*size, size/2], fill, outline, width)
    draw.arc([0, size/2-width, size, 1.5*size], -180, 180, fill, width)
    draw.line([0, size-width/2, size, size-width/2], fill, width)

@icon()
def Multiplayer(draw: ImageDraw, size: int, outline: tuple, fill: tuple, width: float) -> None:
    def person(draw: ImageDraw, size: int, outline: tuple, fill: tuple, width: float, x: float, y: float):
        draw.ellipse([0.25*size+x-width, y-width, 0.75*size+x+width, size/2+y+width], (0,0,0,0), None, width*2)
        draw.arc([x-width, size/2-width+y-width, size+x+width, 1.5*size+y+width], -180, 0, (0,0,0,0), width*2)
        draw.ellipse([0.25*size+x, y, 0.75*size+x, size/2+y], fill, outline, width)
        draw.arc([x, size/2-width+y, size+x, 1.5*size+y], -180, 0, outline, width)
        draw.line([x, size-width/2+y, size+x, size-width/2+y], outline, width)
    person(draw, size*2/3, outline, fill, width, size/3, 0)
    person(draw, size*2/3, outline, fill, width, 0, size/3)

@icon()
def Settings(draw: ImageDraw, size: int, outline: tuple, fill: tuple, width: float) -> None:
    def line(points: tuple) -> None:
        draw.line(points + points[:], outline, width, joint="curve")
    def cog(size: int, x: float, y: float):
        line([size/2+x, width/2+y, size/2+x, size-width/2+y])
        line([size*1/8+x, size*3/10+y, size*7/8+x, size*7/10+y])
        line([size*1/8+x, size*7/10+y, size*7/8+x, size*3/10+y])
        draw.ellipse([0.2*size+x, 0.2*size+y, 0.8*size+x, 0.8*size+y], (0,0,0,0), outline, width)
        draw.ellipse([0.2*size+x, 0.2*size+y, 0.8*size+x, 0.8*size+y], fill, outline, width)
    cog(size*3/5, 0, size*2/5)
    cog(size*3/5, size*2/5, 0)