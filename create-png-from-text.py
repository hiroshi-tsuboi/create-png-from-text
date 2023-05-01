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
if scale <= 0:
    sys.exit()

if 0 < len(lines):
    height = len(lines)
    width = 0
    for line in lines:
        width = max(width, len(line))

    print("original-width=%d original-height=%d" % (width, height))

    image = Image.new("RGB",(width * scale, height * scale))

    for y in range(height):
        line = lines[y]
        for x in range(width):
            if len(line) <= x:
                break
            try:
                c = line[x]
                v = int(c, 16)
                color = [0,0,0]
                for j in range(3):
                    if v & (1 << j):
                        color[j] = 255
                if v == 8:
                    color = [0xc0, 0xc0, 0xc0]
                elif 8 <= v:
                    for i in range(3):
                        color[i] = int((color[i] + 1) / 2)
                # fill block
                for yy in range(scale):
                    yyy = y * scale + yy
                    for xx in range(scale):
                        xxx = x * scale + xx
                        image.putpixel((xxx,yyy), (color[0], color[1], color[2]))
            except:
                pass
    try:
        image.save("a.png")
    except:
        print("failed to save a.png")
        sys.exit()
