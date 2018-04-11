#!/usr/bin/env python
# -*- coding: utf-8 -*-
from optparse import OptionParser
from PIL import Image, ImageDraw, ImageFont
import os

class ImageMaker:
    def __init__(self, count, size, prefix, output, ext):
        self.count = count
        self.size = size
        self.prefix = prefix
        self.output = output
        self.ext = ext
    
    def prepareOutputDir(self):
        if not os.path.exists(self.output):
            os.makedirs(self.output)

    def getFilenameFormat(self):
        prefix = '{}_'.format(self.prefix) if self.prefix else ''
        return '{}/{}{{:03d}}.{}'.format(self.output, prefix, self.ext)

    def make(self):
        self.prepareOutputDir()
        filenameFormat = self.getFilenameFormat()

        width, height = self.size
        font = ImageFont.truetype(
            font = 'RobotoSlab-Bold.ttf',
            size = int(height/3)
        )

        for i in range(1, self.count + 1):
            filename = filenameFormat.format(i)

            print('make {}'.format(filename))
            text = str(i)
            im = Image.new(mode = 'RGB', size = self.size, color=(255,255,255))
            draw = ImageDraw.Draw(im)
            w, h = draw.textsize(text, font)
            draw.text(
                xy = ((width - w) / 2, (height - h) / 2),
                text = text,
                fill = (0,0,0),
                font = font
            )
            im.save(filename)    


def main():
    usage = 'usage: %prog [options] count'
    parser = OptionParser(usage)
    parser.add_option('--prefix', type='string', help='filename prefix')
    parser.add_option('--ext', type='string', default='png', help='file ext (\'png\', \'jpg\', \'gif\')')
    parser.add_option('--output', type='string', default='output', help='output dir')
    parser.add_option('--width', type='int', default=600, help='image width')
    parser.add_option('--height', type='int', default=600, help='image height')

    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error('no count')

    imageMaker = ImageMaker(
        count = int(args[0]),
        size = (options.width, options.height),
        prefix = options.prefix,
        output = options.output,
        ext = options.ext
    )
    imageMaker.make()


if __name__ == '__main__':
    main()
