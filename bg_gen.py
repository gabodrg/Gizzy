# background generator for this thing

# convert image series to gif
# ffmpeg -f image2 -framerate 9 -i %1d.png -vf scale=320x480 out.gif

from PIL import Image, ImageDraw

w = 320
h = 480
circlew=8
image = Image.new('RGBA', (w, h))
imd = ImageDraw.Draw(image)
colors = [(97,53,254),(71,42,210),(65,22,186),(50,17,142),(51,171,234)]

def circlecc(x,y,r):
    return (x-r*2,y-r*2, x+r*2, y+r*2)

for imgindex in range(len(colors)):
    for x in reversed(range(180)):   
        if x < 1:
            break
        cc= circlecc(w/2,h/2,x*circlew)
        imd.ellipse(cc, fill=colors[(x+imgindex)%len(colors)], outline=None, width=1)
    image.save("{0}.png".format(imgindex))
