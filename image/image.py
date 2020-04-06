#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
from PIL import Image, ImageDraw
import os


def create_image(width, height):
    im = Image.new("RGB", (width, height), "lightblue")
    draw = ImageDraw.Draw(im)
    msg = "{}*{}".format(width, height)
    w, h = draw.textsize(msg)
    draw.text(((width - w) // 2, (height - h) // 2), msg)
    im.save(os.path.join("out", msg + ".png"))


if __name__ == '__main__':
    create_image(int(sys.argv[1]), int(sys.argv[2]))
