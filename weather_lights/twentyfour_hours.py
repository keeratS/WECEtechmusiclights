import board
import neopixel
import time

# local imports
try:
    from weather_lights.WeatherLights import WeatherLights
except:
    from WeatherLights import WeatherLights
    

def get_hourly_temps(w, pixels):
    temps = w.get_24_hour_temp()
    
    try:
        for i in range(24):
            weather = temps[i]
            print(weather)
            
        
            
            while True:
            #need if statements first, then go through each for loop
                if weather in range (0, 21): #white, and then goes to halfway blue
                    red=255
                    sub1 = 21-weather #for loop to then add the darkness of blue, each value back 12.75
                    if not (sub1 == 0):
                        for a in range (0, sub1):
                                red=red-12
                    for a in range (50):
                        pixels[a]= (red, 255, 255)
                        pixels.show()
                        time.sleep(10)
             
                    
                if weather in range (21, 41): #blue to halfway green
                    sub2= 41-weather
                    blue=255
                    if not (sub2 == 0):
                        for i in range (0, sub2):
                            blue=blue-12
                    
                    
                    for b in range (50):
                        pixels[b]=(0, 255, blue)
                        pixels.show()
                        time.sleep(10)
                     
             
                if weather in range (41, 61):# green to halfway yellow
                    sub3 = 61-weather
                    red2=255
                    if not (sub3 == 0):
                        for b in range (0, sub3):
                             red2= red2-12 #changing red gives us yellow with b=0
                    for c in range (50):
                        pixels[c]=(red2, 255, 0)
                        pixels.show()
                        time.sleep(10)
            
                if weather in range (61, 81):#yellow, halfway red (orange should be the result)
                    sub4= 81- weather
                    green=255
                    if not (sub3 ==0):
                     for c in range (0, sub4):
                    #halfway to red in order to get orange
                         green= green-6
                    for d in range (50):
                        pixels[d]=(255, green, 0)
                        pixels.show()
                        time.sleep(10)
            
                if weather in range (81, 101): #orange to red
                    red2=255
                    green2= 127
                    sub5=101-weather
                    if not (sub5 == 0):
                         for d in range (0, sub5):
                            green2=green2-12 #the lowest B value will be 0, giving us total green
                    
                    for e in range (50):
                        pixels[e]=(red2, green2, 0)
                        pixels.show()   
                        time.sleep(10)

               
                #could implement some sort of effect here.
    except KeyboardInterrupt:
        # shutting off lights
            pixels.fill((0, 0, 0))
            pixels.show()
    
    #return the list
    return (temps)


if __name__ == "__main__":
    w = WeatherLights()
    
    ORDER=neopixel.RGB
    pixel_pin =board.D18
    n_leds = 50
    pixels = neopixel.NeoPixel(board.D18, n_leds, auto_write=False, pixel_order= ORDER)
    
    get_hourly_temps(w, pixels)