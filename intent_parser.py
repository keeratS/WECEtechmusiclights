# Intent parser for WECE lights

import multiprocessing
import time

# local imports
from weather_lights.wind_speed_lights import wind_speed_lights

# command is the string command
# w is WeatherLights object
def parse_intent(command, pixels, w):
    command = command.lower()
    print(command)
    
    # TODO actual implementation -- need to correctly map command to function
    # currently only example of how code would work
    if("weather" in command):
        # start wind_speed_lights as a process
        p = multiprocessing.Process(target = wind_speed_lights, args = (w, pixels))
        p.start() # starting wind_speed_lights function, same as wind_speed_lights(w, pixels) 
        
        # want to run this function for 10 seconds
        time.sleep(5)
        p.terminate()
        p.join()
        
        # Shutting the lights off. this is usally taken care of in the except block of the
        # functions, but we don't catch the SIGTERM. There is probably a cleaner way to do
        # this. This will do for now.
        # TODO figure out cleanup
        pixels.fill((0, 0, 0))
        pixels.show()
    
    