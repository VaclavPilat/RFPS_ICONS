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