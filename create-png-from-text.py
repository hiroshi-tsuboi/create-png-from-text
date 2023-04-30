import sys

from PIL import Image

# load text

if len(sys.argv) < 2:
    sys.exit()

scale = 1

filename = sys.argv[1]
lines = []
try:
    with open(filename, "rt") as f:
        for line in f:
            if 'scale' in line:
                items = line.split()
                scale = int(items[1])
            else:
                lines.append(line.rstrip())
except:
    print("failed to open %s" % filename)
    sys.exit()

print("scale=%d" % scale)

if 0 < len(lines):
    height = len(lines)
    width = 0
    for line in lines:
        width = max(width, len(line))

    print("width=%d height=%d" % (width, height))

    image = Image.new("RGB",(width, height))

    for y in range(height):
        line = lines[y]
        for x in range(width):
            if x < len(line):
                c = line[x]
                v = int(c)
                color = [0,0,0]
                for j in range(3):
                    if v & (1 << j):
                        color[j] = 255
                image.putpixel((x,y), (color[0], color[1], color[2]))
    try:
        image.save("a.png")
    except:
        print("failed to save a.png")
        sys.exit()




