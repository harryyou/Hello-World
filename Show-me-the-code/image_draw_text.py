#!/usr/bin/env python3
#coding:utf-8

from PIL import Image,ImageDraw,ImageFont

font = ImageFont.truetype("arial.ttf",36)
color = (255,0,0)                   #rgb:red color

def DrawText(img,text):
    im = Image.open(img)            #Image Object
    im_draw = ImageDraw.Draw(im)    #ImageDraw Object
    
    xy = (im.size[0] - 30,0)        #position of the text
    
    im_draw.text(xy,text,font=font,fill=color)
    im.save(img)
    
if __name__ == '__main__':
    img = 'qq.jpg'
    text = "4"
    DrawText(img,text)
    
