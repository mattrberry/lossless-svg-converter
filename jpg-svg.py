import sys
import os
from PIL import Image

for png in sys.argv[1:]:
    root, ext = os.path.splitext(png)
    image = Image.open(png)

    width, height = image.size
    pixels = image.load()

    output = "<svg width=\"%d\" height=\"%d\" viewBox=\"0 0 %d %d\" xmlns=\"http://www.w3.org/2000/svg\">" % (width, height, width, height)

    for r in range(height):
        for c in range(width):
            color = "#%02X%02X%02X" % pixels[c, r]
            output += "<rect x=\"%d\" y=\"%d\" width=\"1\" height=\"1\" fill=\"%s\"/>" % (c, r, color)

    output += "</svg>"

    with open(root + ".svg", "w") as f:
        f.write(output)
