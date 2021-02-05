import time
import board
import neopixel
import random
#import re

#from WeatherLights import get_lat_long
try:
    from weather_lights.WeatherLights import WeatherLights
except:
    from WeatherLights import WeatherLights
# # Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# # NeoPixels must be connected to D10, D12, D18 or D21 to work.
# lat = 38.9072
# long = -77.0369
# 
# w = WeatherLights(lat, long)
# 
# pixel_pin = board.D18
# 
# # The number of NeoPixels
# num_pixels = 50
# 
# # Our lights are GRB lights.
# ORDER = neopixel.GRB
# 
# pixels = neopixel.NeoPixel(
#     pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
# )
def precipitation(weather, pixels):
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


    def rainbow_cycle():
        for j in range(255):
            for i in range(num_pixels):
                pixel_index = (i * 256 // num_pixels) + j
                pixels[i] = wheel(pixel_index & 255)
                pixels.show()
                time.sleep(0.05)
            for j in range (50):
                pixels[j] = (0,0,0)
                pixels.show()
                time.sleep(0.05)
                
        #probab is argument, is the chance of preciptation        
    def snow_fall(probab): #will set color, percentage based animation + intensity to follow
        if(probab == 0): 
            for k in range(50):
                if(k <11):
                    pixels[k] = (120,170,250)
                else:
                    pixels[k] = (255, 117, 31)
            
                pixels.show()
        
        litenum = probab * 0.01 * num_pixels #will fill the percentage of lights that it will preciptate.
        litenum = round(litenum)
        
        for i in range (litenum):
            pixels[i] = (0,0,0)
        pixels.show()
        for j in range (litenum):
            if (j % 3 == 0):
                pixels[j] = (255,255,255)
                pixels.show()
                time.sleep(0.35)
                pixels[j] = (0,0,0)
                time.sleep(0.2)
            
    def rain_fall(probab): #will set color, percent based animation + intensity to follow
        if(probab == 0): 
            for k in range(50):
                if(k <11):
                    pixels[k] = (120,170,250)
                else:
                    pixels[k] = (255, 117, 31)
            
                pixels.show()
            
        litenum = probab * 0.01 * num_pixels #will fill the percentage of lights that it will preciptate.
        litenum = round(litenum)
        
        for i in range (litenum):
            pixels[i] = (250,250,250)
        pixels.show()
        for m in range (litenum):
            if (m % 3 == 0):
                pixels[m] = (50,100,255)
                pixels.show()
                time.sleep(0.07)
                
    def rain_n_snow(probab):
        if(probab == 0): 
            for k in range(50):
                if(k <11):
                    pixels[k] = (120,170,250)
                else:
                    pixels[k] = (255, 117, 31)
            
                pixels.show()
        
        litenum = probab * 0.01 * num_pixels #will fill the percentage of lights that it will preciptate.
        litenum = round(litenum)
        
        for i in range (litenum):
            pixels[i] = (250,250,250)
        pixels.show()
        for m in range (litenum):
            #could do a case statement here; note to jyo
            if (m % 3 == 0):
                pixels[m] = (255,255,255)
                pixels.show()
                time.sleep(0.07)
            if (m%3 == 1):
                pixels[m] = (91,12,194)
                pixels.show()
                time.sleep(0.07)
            if (m%3 == 2):
                pixels[m] = (18,243,255)
                pixels.show()
                time.sleep(0.07)
                
    
    #this bit of code checks if there is any report of precipitation in the detailed forecast.
    #if there is, it retrieves the percent probability of precipitation
    det_forecast = weather.get_detailed_forecast()
    print(det_forecast)
    precipchance = det_forecast.find('precipitation')
    preciprob = 0 #probability set to 0 if no mention of "chance of preciptation" (means that the chance for rain/ instensity of rain is almost 0)
    
    print("There's no precip yet")
    
    if (precipchance != -1):
        keyword = 'precipitation'
        before_keyword,keyword,after_keyword = det_forecast.partition(keyword)
        precistr = after_keyword[4] + after_keyword[5]
        preciprob = int(precistr)
    
    rain_state = 0
    snow_state = 0
    if((det_forecast.find('rain') != -1) or (det_forecast.find('Rain') != -1)):
        rain_state = 1
        print("there's rain")
        
    if((det_forecast.find('snow') != -1) or (det_forecast.find('Snow') != -1)):
        snow_state = 1
        print("there's snow")
        
    print("Press Ctrl-C to turn off lights")
    try: 
        while True:
            #If the key words are recognized the .find will output not -1, if it didnt find the key word outputs -1.
            #Based of this, we can run each function using an if else statement prioritizing certain functions.
            if(rain_state == 1 and snow_state == 0):
                #only rain
                rain_fall(preciprob)
                
            elif(rain_state == 0 and snow_state == 1):
                #only snow
                snow_fall(preciprob)
                
            elif(rain_state == 1 and snow_state == 1):
                #rain and snow
                rain_n_snow(preciprob)
            
            #if no key words were detected, then display the rainbow_cycle
            else:
                rainbow_cycle()
        
    except KeyboardInterrupt:
    # shutting off lights
        pixels.fill((0, 0, 0))
        pixels.show()
        

    
    
                
if __name__ == "__main__":
    # creating WeatherLights object with pre-defined latitude and longitude
    lat = 40.1125
    long = -88.2075
        #try to use automatic location detection / using IP address : note to jyo
    w = WeatherLights(lat, long)


    # defining information about our lights.
    # This part will eventually be done centrally instead of redefined in every file
    pixel_pin = board.D18
    num_pixels = 50

    # allows us to use RGB ordering
    ORDER = neopixel.RGB
    pixels = neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
    )
    
    precipitation(w, pixels)