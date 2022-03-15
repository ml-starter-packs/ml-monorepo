from pathlib import Path

import pytest  # type: ignore
from base import read_image
from resize import rescale, resize


@pytest.fixture
def mock_img():
    path = (
        Path.cwd() / "src" / "python" / "resize" / "sample_data" / "sample_image1.png"
    )
    return read_image(path)


def test_rescale(mock_img):
    # Arrange
    # Act
    output = rescale(im=mock_img, scale=0.5)

    # Assert
    assert output.width == mock_img.width // 2
    assert output.height == mock_img.height // 2


def test_resize(mock_img):
    # Arrange

    # Act
    output = resize(mock_img, size=(150, 175))

    # Assert
    assert output.width == 150
    assert output.height == 175
