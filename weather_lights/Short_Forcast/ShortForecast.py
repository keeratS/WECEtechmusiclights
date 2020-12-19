# From https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/master/examples/neopixel_rpi_simpletest.py

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import random

from Class_Weather_Lights import Class_Weather_Lights
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
lat = 38.9072
long = -77.0369

w = Class_Weather_Lights(lat, long)

pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 50

# Our lights are GRB lights.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)



def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def cloudy():
    for i in range (50):
        pixels[i] = (250,250,250)
        pixels.show()
        time.sleep(0.025)
    for j in range (50):
        pixels[j] = (0,0,0)
        pixels.show()
        time.sleep(0.025)
def snow():
    for i in range (50):
        pixels[i] = (255,255,255)
        pixels.show()
        time.sleep(0.075)
    for j in range (50):
        pixels[j] = (0,0,0)
        pixels.show()
        time.sleep(0.025)
        
def rain(wait):
    for k in range (50):
        pixels[k] = (0,0,0)
        pixels.show
    for j in range (50):
        if (j % 3 != 0):
            pixels[j] = (250,250,250)
        if (j % 3 == 0):
            pixels[j] = (100,50,255)
        pixels.show()
        time.sleep(wait)
  #  for k in range (50):
       # pixels[k] = (0,0,0)
      #  pixels.show()
   # for i in range (50):
       # if (i%3 != 0):
         #   pixels[i] = (250,250,250)
       # if (i % 3 == 0):
          #  pixels[i] = (220,54,255)
       # pixels.show()
       # time.sleep(wait)
    #for j in range (50):
        #pixels[j] = (0,0,0)
       # pixels.show()
       # time.sleep(wait)
    
def sunny(wait):
    for i in range (50):
        pixels[i] = (150,200,0)
        pixels.show()
        time.sleep(wait)
    for j in range (50):
        pixels[j] = (0,0,0)
        pixels.show()
        time.sleep(wait)
        
def sunny_w_clouds(wait):
    for i in range (50):
        pixels[i] = (150,200,0)
        pixels.show()
        time.sleep(wait)
    for k in range (5):
        pixels[k] = (250,250,250)
        pixels.show()
        time.sleep(wait)

    for m in range (50):
        pixels[m] = (0,0,0)
        pixels.show()
        time.sleep(wait)
def short_forecast(weather, pixels):
    short_forecast = weather.get_short_forecast()
    sunnyF = short_forecast.find('Sunny')
    sunny_w_cloudsF = short_forecast.find
    cloudyF = short_forecast.find('Cloudy')
    rainF = short_forecast.find('Rain')
    snowF = short_forecast.find('Snow')
    
    
    

    print("Press Ctrl-C to turn off lights")
    try: 
        while True:
            if sunnyF != -1:
                sunny(0.05)
            if snowF != -1:
                snow()
            elif cloudyF != -1:
                cloudy()
            elif rainF != -1:
                rain(0.05)
            elif sunny_w_cloudsF != -1:
                sunny_w_clouds(0.05)
            else:
                rainbow_cycle(0.05)
                
                
        #cloudy(0.05) #white
        #cloudy_w_rain(0.05)
        
        
    except KeyboardInterrupt:
    # shutting off lights
        pixels.fill((0, 0, 0))
        pixels.show()
    
short_forecast(w, pixels)

