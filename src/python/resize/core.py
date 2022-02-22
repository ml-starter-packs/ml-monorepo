from copy import copy
from pathlib import Path
from typing import Optional, Tuple

import cv2
from base import Image, read_image


def resize(
    im: Image,
    size: Tuple[int, int],
    interpolation=cv2.INTER_AREA,
    **kwargs,
) -> Image:
    """Resizes a given image to dimensions specified by `size=(width, height)`.
    Convenience wrapper around `cv2.resize`.
    """
    if max(size) <= 0:
        raise ValueError("`size` must only contain positive dimensions")
    return Image(file=cv2.resize(im.file, size, interpolation=interpolation, **kwargs))


def rescale(im: Image, scale: float = 1.0, **kwargs) -> Image:
    """Rescales an image by some fixed proportion for both width and height.
    """
    if scale <= 0:
        raise ValueError("`scale` must be positive")
    size = (int(im.width * scale), int(im.height * scale))
    return resize(im, size, **kwargs)
