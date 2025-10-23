# RFPS_ICONS v1.0

![Icon examples](docs/Examples.png)

This repository is a part of the *RFPS* project.
It is used for creating icons and other simple PNG images. Images are constructed using simple shapes, such as lines, circles and curves. Icons produced by this codebase are then used in the *RFPS* repository and diagrams are used in *RFPS_THESIS*.

This project is a wrapper to the python's Pillow library. Each image definition is meant to be stored in a function, which, when decorated, behaves like an instance method. Each function has 5 arguments - bounding box width and height, line width and foreground and background colors. These functions can then be loaded into one another. Images are generated in high resolution and then downscaled to their desired size.

The codebase could be improved by adding features such as image rotation or by ensuring that anything created beyond the bounding box of a single image does not bleed out when imported to another image. SVG output could be added as well.

## How to run

Make sure that you have Python3 on your device (version 3.10 was used in development). Then install all dependencies:

```shell
make install
```

To generate the images, use:

```shell
make run
```

## Usage examples

If you want to make your own images, start by creating a new script. Declare an image function, decorated by the `createImage` decorator imported from the `Files` module. Then call draw methods from within the function, like this:

```py
from src.Files import createImage

@createImage()
def Globe(self, W, H, L, C, B) -> None:
    self.ellipse((0, 0), (W, H), fill=None)
    self.ellipse((W*0.275, 0), (W*0.725, H), fill=None)
    for i in (-1, 1):
        self.line((L, H/2 + i*H*0.15), (W-L, H/2 + i*H*0.15))
```

Run the script. The decorator automatically creates image files that match the name of the function it decorates.