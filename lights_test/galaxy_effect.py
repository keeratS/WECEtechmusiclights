# making something inspired by the night sky

import time
import board
import neopixel

import random

pixel_pin=board.D18
num_pixels=50
ORDER=neopixel.GRB
pixels=neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

def grb(r,g,b):
    '''This function changes an rgb input to a grb input for the readability of rgb with the functionality of grb'''
    return (g,r,b)

def starTwinkle(shift):
    '''This function changes the pixels to light in a repeating pattern of 4 colors in a sequence of 7, shifted by a given offset'''

    #colors we will use in a rgb format
    ultramarine=grb(54,87,255)
    mayablue=grb(80,140,255)
    aqua=grb(54,220,255)
    han=grb(80,50,255)

    #set the pixel array colors as described above
    for i in range(num_pixels):
        if i%7 ==(0+shift)%7:
            pixels[i]=aqua
        if i%7 ==(1+shift)%7 or i%7 ==(7+shift)%7:
            pixels[i]=mayablue
        if i%7 ==(2+shift)%7 or i%7 == (3+shift)%7 or i%7 == (5+shift)%7 or i%7 == (6+shift)%7:
            pixels[i]=ultramarine
        if i%7 ==(4+shift)%7:
            pixels[i]=han
    
    #light up according to the updated array    
    pixels.show()

#now we manipulate the offset to create a twinkling effect
#initially I was experimenting with motion but I think you
#need a fading effect for that to be effective
shiftvalue=0; #offset value
shiftdir=1; #moving forward or backward

try:
    while True:
        if (shiftdir==1):
            shiftvalue=shiftvalue+1
        if (shiftdir==0):
            shiftvalue=shiftvalue-1
    
        if (random.random()<0.1): #have a 1/10 chance of changing direction of shift
            shiftdir= not shiftdir
    
        starTwinkle(shiftvalue) #light up with the updated offset
        waittime=0.1 #you can increase this for a slower twinkling effect
        time.sleep(waittime)
    
        # when commenting out code, if you don't want to remove it
        # ie it serves a useful debugging function
        # do not leave a space between the # and the beginning of the code

        #print(str(waittime)+" "+str(shiftvalue)+" "+str(shiftdir))
except KeyboardInterrupt:
    #shutting off lights
    pixels.fill((0,0,0))
    pixels.show()
