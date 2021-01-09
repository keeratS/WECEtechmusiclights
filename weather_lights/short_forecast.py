#Essentially this code displays the current weather
#It utalizes the short forecast to determine what the weather is (snow, cloudy, runny, etc)
#then it runs the designated function for each type of weather reporting.

import time
import board
import neopixel
import random

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
def short_forecast(weather, pixels):
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

    def cloudy():
        for i in range (50):
            pixels[i] = (250,250,250)
            pixels.show()
            time.sleep(0.07)
        for j in range (50):
            pixels[j] = (0,0,0)
            pixels.show()
            time.sleep(0.07)

    def fog():
        for i in range (50):
            pixels[i] = (75,75,75)
            pixels.show()
            time.sleep(0.07)
        for j in range (50):
            pixels[j] = (0,0,0)
            pixels.show()
            time.sleep(0.07)
            
    def snow():
        for i in range (50):
            pixels[i] = (0,0,0)
        pixels.show()
        for j in range (50):
            if (j % 3 == 0):
                pixels[j] = (255,255,255)
                pixels.show()
                time.sleep(0.35)
                pixels[j] = (0,0,0)
                time.sleep(0.2)
            
    def rain():
        for i in range (50):
            pixels[i] = (250,250,250)
        pixels.show()
        for m in range (50):
            if (m % 3 == 0):
                pixels[m] = (50,100,255)
                pixels.show()
                time.sleep(0.07)
        
    def sunny():
        for i in range (50):
            pixels[i] = (200,150,0)
            pixels.show()
            time.sleep(0.05)
        for j in range (50):
            pixels[j] = (0,0,0)
            pixels.show()
            time.sleep(0.05)
            
    def sunny_w_clouds():
        for m in range (50):
            pixels[m] = (250,150,0)
        pixels.show()
        for i in range (50):
            pixels[i] = (250,250,250)
            pixels.show()
            time.sleep(0.07)
        for j in range (50):
            pixels[j] = (250,150,0)
            pixels.show()
            time.sleep(0.07)
            
    #search for key words in the short forecast to determine what the current weather is.
    short_forecast = weather.get_short_forecast()
    sunnyF = short_forecast.find('Sunny')
    cloudyF = short_forecast.find('Cloudy')
    rainF = short_forecast.find('Rain')
    snowF = short_forecast.find('Snow')
    fogF = short_forecast.find('Fog')
    
#     if (cloudyF != -1):
#         if (sunnyF != -1):
#             sunny_w_cloudsF = 1
#     else:
#         sunny_w_cloudsF = -1
        
        
        

    print("Press Ctrl-C to turn off lights")
    try: 
        while True:
            #If the key words are recognized the .find will output not -1, if it didnt find the key word outputs -1.
            #Based of this, we can run each function using an if else statement prioritizing certain functions.
#             if sunny_w_cloudsF != -1:
#                 sunny_w_clouds()
            if sunnyF != -1:
                sunny()
            elif rainF != -1:
                rain()
            elif snowF != -1:
                snow()
            elif cloudyF != -1:
                cloudy()
            elif fogF != -1:
                fog()
            #if no key words were detected, then display the rainbow_cycle
            else:
                rainbow_cycle()
        
    except KeyboardInterrupt:
    # shutting off lights
        pixels.fill((0, 0, 0))
        pixels.show()


if __name__ == "__main__":
    # creating WeatherLights object with pre-defined latitude and longitude
    lat = 38.9072
    long = -77.0369

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
    
    short_forecast(w, pixels)