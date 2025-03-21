# About RFPS ICONS

![Icon examples](docs/Examples.png)

This repository is used for creating simple icons and other images using Python's Pillow library.

## How to run

1. **Install requirements** : `make install`
2. **Generate images** : `make run`

## Documentation

- **Create documentation** : `make doc`
- **Count lines of code** : `make cloc`

## How to reuse

1. Import the `createImage` decorator from the Image module.
2. Declare an image function, decorated by `createImage`.
3. Call draw methods inside the function, like this:
```py
from Utils.Files import createImage

@createImage()
def Globe(self, W, H, L, C, B) -> None:
    self.ellipse((0, 0), (W, H), fill=None)
    self.ellipse((W*0.275, 0), (W*0.725, H), fill=None)
    for i in (-1, 1):
        self.line((L, H/2 + i*H*0.15), (W-L, H/2 + i*H*0.15))
```
4. Run the script.

## How it works

- The `createImage` decorator renders and writes image data into a file (if it doesn't exist already). It has the following kwarg arguments, all of which are optional:
    - `folder` - output folder path, defaults to `"images/"`,
    - `size` - output image size in pixels, defaults to `(100, 100)`,
    - `sampling` - sampling multiplier (images are generated in high resolution and then downscaled), defaults to `5`,
    - `width` - line width in pixels, defaults to `10`,
    - `background` - background color, defaults to `(0, 0, 0, 0)` (transparent),
    - `color` - foreground color, defaluts to `(255, 255, 255)` (solid white).

- Each image function represents a single image or an icon. It has the following positional arguments (to avoid unnecessarily long `self.*` calls):
    - `W` - sampled image width in pixels,
    - `H` - sampled image height in pixels,
    - `L` - sampled line width in pixels,
    - `C` - foreground color,
    - `B` - background color.

- Inside an image function you can use the following draw methods:
    - `line(*points, fill, width, joint)` - drawing straight lines between the specified points,
    - `ellipse(*points, fill, outline, width)` - drawing an ellipse with two points for the bounding box,
    - `arc(*points, start, end, fill, width)` - drawing a part of an ellipse with start and stop angles,
    - `rectangle(*points, fill, outline, width)` - drawing a rectangle with two points as the bounding box,
    - `roundedRectangle(*points, fill, outline, width, radius, corners)` - drawing a rectangle with rounded corners,
    - `polygon(*points, fill, outline, width)` - drawing a closed polygon between the specified points,
    - `dot(point, fill, outline, width)` - drawing a small circle from the specified center point.

- Each draw method has points (tuples of x-y coordinates in pixels) as *args and some of the following optional kwarg arguments:
    - `width` - line width in pixels, defaults to image line width,
    - `outline` - outline width in pixels, defaults to image foreground color,
    - `fill` - fill color, defaults to image foreground color,
    - `start` - start angle, defaults to `0`,
    - `end` - end angle, defaults to `180`,
    - `joint` - line joint type, defaults to `"curve"`,
    - `radius` - curve radius, defaults to image line width,
    - `corners` - corner curve settings, defaults to `(True, True, True, True)`.

- You can also load another image inside an image function by calling `self.load()` with the following arguments:
    - `function` - name of an already defined image function to load,
    - `size` - size of the loaded image in pixels, defaults to parent image size,
    - `offset` - offset of the loaded image inside self, defaults to `(0, 0)`,
    - `color` - foreground color of the loaded image, defaults to parent foreground color,
    - `background` - background color of the loaded image, defaults to parent background color,
    - `width` - line width, defaults to parent line width.