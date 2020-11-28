import board
import neopixel
import time

# local imports 
from TodayLights import TodayLights # importing defined class

def grb(r,g,b):
    return (g,r,b)


# weather is a WeatherLights object
def today_temp_lights(weather, pixels):
    today_temp = weather.get_today_temp() #today_temp = weather.get_today_temp(), tbh idk what's happening right here
    #create an array w/ temp color
        #each array w/ color code, and then calling them in the for loop for the color
    
#         colorList = [[255, 255, 255], [0, 0, 255], [0, 255, 0], [255, 255, 0], [255, 0, 0]] white, blue, green, yellow, red

#for i in colorList:
 #   red = i[0] (111)
  #  green = i[1] (222)
   # blue = i[2] (254)
    try:
        #need a pixel statement with this as well
        while True:
            #need if statements firs, then go through each for loop
            if today_temp in range (0, 21): #white, and then goes to halfway blue
                #for loop to then add the darkness of blue, each value back 6.375
                halfway= today_temp % 10 #modulus isn't going to work, if it's 10 F, it'll just show up as white
                    #what if I did division instead?? /10, if the result was greater than 1, it would already be halfway down, and then
                    #decrease red again with the modulus
                
                for x in depth: #need to decrease R, can decrease 6.375 by the modulus
                    
                    blue= blue
                    
                    #lights=grb(
                    #calling the array, adding the value of blue
                
            if today_temp in range (21, 41): #blue to halfway green
                
               #pixels[i] = color
                #pixels[i-1] = (0, 0, 0)
            if today_temp in range (41, 61):# green to halfway yellow
            
            if today_temp in range (61, 81):#yellow, halfway red (orange should be the result)
                
            
            if today_temp in range (81, 101): #orange to red
                
            
            
                
                pixels.show()
                #could implement some sort of effect here.
    except KeyboardInterrupt:
        # shutting off lights
        pixels.fill((0, 0, 0))
        pixels.show()
    
    


# creating WeatherLights object with pre-defined latitude and longitude
lat = 38.9072
long = -77.0369

w = TodayLights(lat, long)


# defining information about our lights.
# This part will eventually be done centrally instead of redefined in every file
pixel_pin = board.D18
num_pixels = 50

# allows us to use RGB ordering
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


today_temp(w, pixels)