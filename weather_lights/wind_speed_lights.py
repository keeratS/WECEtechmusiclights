import board
import neopixel
import time

# local imports 
from WeatherLights import WeatherLights # importing defined class



# weather is a WeatherLights object
def wind_speed_lights(weather, pixels):
    wind_speed = weather.get_wind_speed()

    # let's assume wind speed is between 0 and 50 mph
    # (any faster and you probably already know...)
    max_speed = 50 
    speed_trunc = min(wind_speed, max_speed)
    speed_prop = 1 - speed_trunc/max_speed
    
    # shade of blue proportional to wind speed.
    # lightening by adding green
    green_prop = round(255 * speed_prop)
    color = (0, green_prop, 255)
    
    
    mph_inches = 17.6 # miles per hour to inches per second conversion
    inches_sec = speed_trunc * mph_inches

    dist = 2 # lights sit about 2 inches apart relaxed
    t = 1/inches_sec * dist # time to travel the 2 inches to the next bulb

    try:
        while True:
            # single led lit traveling at defined speed
            for i in range(50):
                pixels[i] = color
                # can acess last pixels like pixels[-1]
                # (this is true in general for lists), so this won't error
                pixels[i-1] = (0, 0, 0)
                pixels.show()
                time.sleep(t)
    except KeyboardInterrupt:
        # shutting off lights
        pixels.fill((0, 0, 0))
        pixels.show()
    
    


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


wind_speed_lights(w, pixels)

