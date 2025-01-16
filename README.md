# About RFPS Icons

This repository is used for creating simple icons and other images using Python's *Pillow* library. 

All icons are generated as white-on-transparent PNG images.

Images are generated in high resolution and then downscaled to 100x100 pixels.

## How to run
1. **Install requirements** : `make install`
2. **Generate images** : `make run`

## Documentation
- **Create documentation** : `make doc`
- **Count lines of code** : `make cloc`

Run Doxygen after image generation to see them in HTML documentation.

## How to reuse

- Import the `createImage` decorator from the Image module. Adding the decorator to a function automatically draws and saves the image into `images/FunctionNameHere.png`
- The decorator controls image parameters, such as size, foreground and background colors etc. They can be modified by using specific kwargs. Just don't forget to add brackets at the end of the decorator call.
- Each function has parameters for calculating proportional positions and color to avoid using absolute values. The variables are:
    - **W** as image width,
    - **H** as image height,
    - **L** as line width,
    - **C** as foreground color and
    - **B** as background color.
- The purspose of that is make the variable names as short as possible and avoid using any unnecessarily long `self.*` calls.
- Each Canvas method used for drawing accepts the same kwargs as its Pillow variant but with custom default values defined in the `defaultSettings` decorator.

The following is a code sample of one of the draw functions. Running this code will create and save the image (if it doesn't exist already).

```py
from Image import createImage

@createImage() # The image will be saved to "images/Globe.png"
def Globe(self, W, H, L, C, B) -> None:
    self.ellipse((0, 0), (W, H), fill=None)
    self.ellipse((W*0.275, 0), (W*0.725, H), fill=None)
    for i in (-1, 1):
        self.line((L, H/2 + i*H*0.15), (W-L, H/2 + i*H*0.15))
```