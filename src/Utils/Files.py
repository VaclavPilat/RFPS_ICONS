## \file
# Functionality for creating and saving generated images into files
from PIL import Image, ImageDraw, ImageChops
# noinspection PyPackages
from .Image import Canvas
import os


def createImage(folder: str = ".", size: tuple = (100, 100), sampling: float = 5, width: float = 10, background: tuple = (0, 0, 0, 0), color: tuple = (255, 255, 255)) -> "func":
    """Decorator for creating an image and saving it to a file

    Args:
        folder (str, optional): Output folder name. Defaults to ".".
        size (tuple, optional): Image size. Defaults to (100, 100).
        sampling (float, optional): Sampling multiplier. Defaults to 5.
        width (float, optional): Default line width. Defaults to 10.
        background (tuple, optional): Background color. Defaults to (0, 0, 0, 0).
        color (tuple, optional): Default foreground color. Defaults to (255, 255, 255).

    Returns:
        func: Wrapper for image creation
    """
    def wrapper(function: "func") -> "func":
        # Calculating sampled sizes
        scaledSize = (size[0] * sampling, size[1] * sampling)
        scaledWidth = width * sampling
        # Creating an image
        image = Image.new("RGBA", scaledSize, background)
        canvas = Canvas(ImageDraw.Draw(image), scaledSize, (0, 0), color, background, scaledWidth)
        # Calling the function
        function(canvas, *scaledSize, scaledWidth, color, background)
        image = image.resize(size, resample=Image.LANCZOS)
        # Getting image file path
        folderpath = f"images/{folder}"
        filepath = f"{folderpath}/{function.__name__}.png"
        if not os.path.exists(folderpath):
            os.makedirs(folderpath)
        # Comparing older image
        if os.path.exists(filepath):
            diff = ImageChops.difference(image, Image.open(filepath))
            if not diff.getbbox():
                return function
        # Saving the image
        image.save(filepath, "PNG")
        print(filepath)
        return function
    return wrapper