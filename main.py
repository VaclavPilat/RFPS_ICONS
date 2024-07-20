from PIL import Image, ImageDraw

def icon() -> None:
    def wrap(func) -> None:
        image = Image.new("RGBA", (100, 100), (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)
        func(draw)
        image.save("{}.png".format(func.__name__), "PNG")
    return wrap

@icon()
def Singleplayer(draw: ImageDraw) -> None:
    pass