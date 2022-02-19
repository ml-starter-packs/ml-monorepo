from copy import copy
from pathlib import Path
from typing import Optional, Tuple

import cv2
from base import Image, read_image


class IncorrectParameters(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def resize(
    path: Path,
    percentage: Optional[float] = None,
    width_height: Optional[Tuple[int, int]] = None,
) -> Image:
    """Resizes a given image, `percentage` parameter preserves aspect ratio,
    `width_height` does not.
    """
    if percentage and width_height:
        raise IncorrectParameters("Don't provide both at the same time!")

    img = read_image(path)

    if percentage:
        dimentions = (int(img.width * percentage), int(img.height * percentage))
    else:
        dimentions = copy(width_height)

    return Image(file=cv2.resize(img.file, dimentions, interpolation=cv2.INTER_AREA))
