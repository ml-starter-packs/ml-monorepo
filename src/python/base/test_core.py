import numpy as np
from base import read_image


def test_read():
    # Arrange
    img_path = "src/python/base/sample_data/sample_image1.png"

    # Act
    img = read_image(img_path)

    # Assert
    assert isinstance(img, np.ndarray)
