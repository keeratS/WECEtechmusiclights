#!/usr/bin/python3
#fireworks

import time
import board
import neopixel

import random

pixel_pin=board.D18
num_pixels=50
ORDER=neopixel.RGB

pixels=neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

print ("initialized light setup")

def dim (color, amount):
    #color should be a 3-tuple to represent color
    result= (int(color[0]*amount), int(color[1]*amount), int(color[2]*amount))
    #print(result)
    return result

def flash(num):
    # input cleanup
    if num>50:
        num=num%50
    num=int(num)
    
    #randomly pick color
    choice=random.random()
    if choice<0.25:
        color=(0,0,225)
    elif choice <0.5:
        color=(0,225,0)
    elif choice <0.75:
        color=(225,0,0)
    else:
        color=(255,255,255)

    #light up center
    pixels[num] =color
    pixels.show()
    #print("the num is "+str(num))
    time.sleep(0.2)

    #stage1, center-1 dim
    if (num>0):
        pixels[num-1]=dim(color,0.4)
    if (num<49):
        pixels[num+1]=dim(color,0.4)
    pixels.show()
    time.sleep(0.4)

    #stage2, center-2 more dim
    pixels[num]=dim(color,0.4)
    if (num>1):
        pixels[num-2]=dim(color,0.1)
    if (num<48):
        pixels[num+2]=dim(color,0.1)
    pixels.show()
    time.sleep(0.2)

    #stage3, all more dim
    pixels[num]=dim(color,0.1)
    if(num>0):
        pixels[num-1]=dim(color,0.1)
    if(num<49):
        pixels[num+1]=dim(color,0.1)
    pixels.show()
    time.sleep(0.2)

    #stage4, turn off
    pixels[num]=(0,0,0)
    if(num>0):
        pixels[num-1]=(0,0,0)
    if(num<49):
        pixels[num+1]=(0,0,0)
    if(num>1):
        pixels[num-2]=(0,0,0)
    if(num<48):
        pixels[num+2]=(0,0,0)

try:
    print ("beginning lights effect")
    while(1==1):
        flash(random.random()*50)
        time.sleep(0.2)

except KeyboardInterrupt:
    #shutting off lights
    pixels.fill((0,0,0))
    pixels.show()
