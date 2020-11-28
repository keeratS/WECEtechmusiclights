import board
import neopixel
import time

# local imports 
from TodayLights import TodayLights # importing defined class

def grb(r,g,b):
    return (g,r,b)


# weather is a WeatherLights object
def today_temp_lights(weather, pixels):
     #today_temp = weather.get_today_temp(), tbh idk what's happening right here
    #all the values need to be scaled for the range, couldn't I just do a for loop to decrease red by a specific amount?
    try:
        #need a pixel statement with this as well
        while True:
            #need if statements firs, then go through each for loop
            if weather in range (0, 21): #white, and then goes to halfway blue
                red=255#for loop to then add the darkness of blue, each value back 12.75
                for x in range (weather):
                    red= red-12
                
                
             pixels.fill((red, 255, 255))
             pixels.show()
                
            if today_temp in range (21, 41): #blue to halfway green
                blue=255
                 for x in range (weather):
                    blue= blue-12 #the lowest B value will be 0, giving us total green
             pixels.fill((0, 255, blue))
             pixels.show()
                 
             
            if today_temp in range (41, 61):# green to halfway yellow
                red=255
                 for x in range (weather):
                    red= red-12 #changing red gives us yellow with b=0
             pixels.fill((red, 255, 0))
             pixels.show()
            
            if today_temp in range (61, 81):#yellow, halfway red (orange should be the result)
                green=255
                 for x in range (weather)
                    #halfway to red in order to get orange
                     green= 255-6
             pixels.fill((255, green, 0))
             pixels.show()
            
            if today_temp in range (81, 101): #orange to red
                green= 127
                 for today_temp in range (21):
                    green=green-12 #the lowest B value will be 0, giving us total green
             pixels.fill((red, green, 0))
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