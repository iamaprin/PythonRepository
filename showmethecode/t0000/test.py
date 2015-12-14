import sys
from PIL import ImageFont, ImageDraw, Image

image = Image.open("E:\\pic\\06.jpg")
print(image.format, image.size, image.mode)
image.rotate(45).show()
