from base import read_image
from pathlib import Path

def test_read():
    # Arrange
    img_path = Path().cwd() / "src" / "python" / "sample_data" / "sample_image1.png"
    # Act
    img = read_image(img_path)
    # Assert
    print([x for x in Path().cwd().glob('**/*') if "sample" in str(x)])
    print(img_path)
    print(type(img))
    assert False
