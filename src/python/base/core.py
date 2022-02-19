from pathlib import Path

import cv2
from cv2.mat_wrapper import Mat


def read_image(path: Path) -> Mat:
    return cv2.imread(str(path))


def write_image(path: Path, image: Mat):
    cv2.imwrite(path, image)
