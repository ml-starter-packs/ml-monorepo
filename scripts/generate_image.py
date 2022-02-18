import numpy
from PIL import Image

imarray = numpy.random.rand(200, 200, 3) * 255
im = Image.fromarray(imarray.astype("uint8")).convert("RGBA")
im.save("sample_data/sample_image1.png")