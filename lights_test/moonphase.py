#moon illumination reporting code

import time
import board
import neopixel
import numpy

import random

def gradient(pixels,shift):
  '''This function creates a gradient'''
  #colors to gradient in RGB
  bcolor=np.array(167,158,235) #bright color in RGB
  ncolor=np.array(216,222,255) #neutral color in RGB

  #calculations
  #colorstep = tuple(map(lambda i, j: i - j, bcolor, ncolor)) #subtract tuples from each other
  colorstep= bcolor-ncolor
  colorstep = colorstep/(pixels.n)

  for i in range(pixels):
      i=(i+shift)%pixels.n
    pixels[i]=(bcolor[0]+colorstep[0]*i,bcolor[1]+colorstep[1]*i,bcolor[2]+colorstep[2]*i)


from bs4 import BeautifulSoup
from urllib import request
def moonshine(pixels):
  '''  This function communicates how much of the moon is illuminated at the time by referencing a specific website. '''

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
  darkstart = int(pixels.n*illumination)
  gradient(pixels.n,0)
  pixels.show() #turn on the pixels under the gradient to show the command was received
  time.sleep(4)

  #turn on the lights according to above calculation
  offset = 0;
  while ("wece"=="wece")
    gradient(pixels.n,offset)
    for i in range(darkstart,pixels.n+1):
        pixels[1]=(0,0,0) #turn off all pixels except

    pixels.show()
    offset=(offset+1)%50
