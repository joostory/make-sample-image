#!/usr/bin/env python
# -*- coding: utf-8 -*-
from optparse import OptionParser
from PIL import Image, ImageDraw, ImageFont
import os

def makeImage(count, size, name):
    print "make %d image (%dx%d)" % (count, size[0], size[1])

    font = ImageFont.truetype(
        font='RobotoSlab-Bold.ttf',
        size=int(size[1]/3)
    )

    outputDir = 'output'

    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    for i in range(1, count + 1):
        filename = '{}/{}_{:03d}.jpg'.format(outputDir, name, i)
        
        print "make %s" % (filename)
        text = str(i)
        im = Image.new(mode = 'RGB', size = size, color=(255,255,255))
        draw = ImageDraw.Draw(im)
        w, h = draw.textsize(text, font)
        draw.text(
            xy=((size[0] - w) / 2, (size[1] - h) / 2),
            text=text,
            fill=(0,0,0),
            font=font
        )
        im.save(filename)


def main():
    usage = "usage: %prog [options] count"
    parser = OptionParser(usage)
    parser.add_option("--name", type="string", default="image")
    parser.add_option("--width", type="int", default=800)
    parser.add_option("--height", type="int", default=600)

    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("no count")


    makeImage(
        count=int(args[0]),
        size = (options.width, options.height),
        name=options.name
    )


if __name__ == '__main__':
    main()
