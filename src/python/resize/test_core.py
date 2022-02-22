from pathlib import Path

import pytest
from resize import resize


@pytest.fixture
def mock_img_path():
    return (
        Path.cwd() / "src" / "python" / "resize" / "sample_data" / "sample_image1.png"
    )


def test_resize_percentage(mock_img_path):
    # Arrange
    im = read_image(mock_img_path)

    # Act
    img = resize(
        path=mock_img_path,
        percentage=0.5,
    )

    # Assert
    assert img.width == original.width // 2
    assert img.height == original.height // 2


def test_resize_tuple(mock_img_path):
    # Arrange

    # Act
    img = resize(path=mock_img_path, width_height=(150, 175))

    # Assert
    assert img.width == 150
    assert img.height == 175
