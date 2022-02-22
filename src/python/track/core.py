from base import Point, read_image


def simple_tracking(path: str) -> Point:
    img = read_image(path)

    return Point(x=int(img.width / 2), y=int(img.height / 2))
