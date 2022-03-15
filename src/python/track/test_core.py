from pathlib import Path

import pytest  # type: ignore
from base import Point, read_image
from track import simple_tracking


@pytest.fixture
def mock_img_paths():
    path = Path.cwd() / "src" / "python" / "track" / "sample_data"
    return [x for x in path.glob("**/*") if x.is_file()]


def test_simple_tracking(mock_img_paths):
    # Arrange
    originals = [read_image(x) for x in mock_img_paths]
    expected = [Point(x=int(img.width / 2), y=int(img.height / 2)) for img in originals]

    # Act
    generated = [simple_tracking(x) for x in mock_img_paths]

    # Assert
    assert all([e == g for e, g in zip(expected, generated)])
