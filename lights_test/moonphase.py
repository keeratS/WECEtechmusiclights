#moon illumination reporting code

import time
import board
import neopixel
import numpy as np

import random

pixelnumber=50

def gradient(pixels,shift):
  '''This function creates a gradient'''
  #colors to gradient in RGB
  bcolor=np.array([167,60,235]) #bright color in RGB
  ncolor=np.array([216,222,255]) #neutral color in RGB

  #calculations
  #colorstep = tuple(map(lambda i, j: i - j, bcolor, ncolor)) #subtract tuples from each other
  colorstep= ncolor-bcolor
#   print(colorstep)
  colorstep = (colorstep/pixelnumber)
#   print(colorstep)

  for i in range(pixelnumber):
    j=(i+shift)%pixelnumber
    newcolor=bcolor+colorstep*j
    pixels[i]=(int(newcolor[0]),int(newcolor[1]),int(newcolor[2]))

from bs4 import BeautifulSoup
from urllib import request
def moonshine(pixels):
    '''  This function communicates how much of the moon is illuminated at the time by referencing a specific website. '''

    try:
        url = "https://www.moongiant.com/phase/today/" #this website tells moon info

        #extraction of relevant information using beautifulsoup to parse html of website
        html = request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        small_soup = soup.select("#moonDetails")[0] #go to the moonDetails id
        croutons = small_soup.find_all('span') #get a list of all the span items

        illumination = croutons[1].get_text() #illumination is second in the list of span items
        illumination = int(illumination[:-2])/100 #turn it into a number for calculation
        print ("this much of the moon is illuminated:")
        print(illumination)

        #find how much of the string lights should be dark
        darkstart = int((pixelnumber-1)*illumination)+1
        print("This many of your lights should be illuminated")
        print(darkstart)
        gradient(pixels,0)
        pixels.show() #turn on the pixels under the gradient to show the command was received
        time.sleep(.1)

            #turn on the lights according to above calculation
        offset = 0;
        while ("wece"=="wece"):
            gradient(pixels,offset)
            for i in range(darkstart,pixels.n):
                pixels[i]=(0,0,0) #turn off all pixels except

            pixels.show()
            offset=(offset+1)%50
            time.sleep(.05)
    except KeyboardInterrupt:
        #shutting off lights
        pixels.fill((0,0,0))
        pixels.show()



if __name__ == "__main__":
    pixel_pin=board.D18
    num_pixels=50
    ORDER=neopixel.RGB
    pixels=neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
    )

#     gradient(pixels, 0)
#     pixels.show()
#     time.sleep(1)
#     print("switch")
#     gradient(pixels,25)
#     pixels.show()
#     time.sleep(1)

    moonshine(pixels)
