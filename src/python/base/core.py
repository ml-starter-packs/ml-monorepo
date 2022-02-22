from dataclasses import dataclass, field
from pathlib import Path

import cv2
import numpy as np
from cv2.mat_wrapper import Mat


@dataclass
class Image:
    file: Mat = Mat(arr=np.ndarray(shape=(0, 0)))
    width: int = field(default=0, init=False)
    height: int = field(default=0, init=False)

    def __post_init__(self) -> None:
        self.width = self.file.shape[1]
        self.height = self.file.shape[0]


@dataclass
class Point:
    x: int = 0
    y: int = 0

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)


def read_image(path: Path) -> Image:
    return Image(file=cv2.imread(str(path), cv2.IMREAD_UNCHANGED))


def write_image(path: Path, image: Image):
    cv2.imwrite(path, image.file)
