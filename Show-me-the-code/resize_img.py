#!/usr/bin/env python3
#coding:utf-8

import os
from PIL import Image
#from datetime import datetime

#time = datetime.now().strftime('%Y%m%d')
#dest_dir = 'tmp_' + time

def CompareSize(size):

    x,y = size

    if x > 1136:
        x = 1136

    if y > 640:
        y = 640

    return (x,y)


def ResizeImg(path,dest):

    for dir in os.walk(path):
        if dir[2]:
            for i in dir[2]:
                try:
                    img = Image.open(os.path.join(dir[0],i))
                    size = CompareSize(img.size)
                    img_new = img.resize(size)
                    img_new.save(os.path.join(dest,i))
                    print (os.path.join(dest,i) + " convert over!")
                    img_new.close()
                    img.close()

                except OSError:
                    print (os.path.join(dir[0],i) + " is not a image file!")
                    

if __name__ == '__main__':
    source = r"F:\source"
    dest = r"F:\tmp"
    ResizeImg(source,dest)

