# Intent parser for WECE lights

import multiprocessing
import time

# local imports
from weather_lights.wind_speed_lights import wind_speed_lights

# helper to run a given function as a subprocess
# for functions that run forever, (i.e. only stop on ctrl-C)
# allows us to stop based on some time
# target is name of function
# args are the arguments to that function
# t is the amount of time function should be run before terminating
def run_func_sub(target, args, t, pixels):
        # start func as a process
        p = multiprocessing.Process(target = target, args = args)
        p.start() # starting wind_speed_lights function, same as wind_speed_lights(w, pixels) 

        # want to run this function for t seconds
        time.sleep(t)
        p.terminate()
        p.join()
        
        # Shutting the lights off. this is usally taken care of in the except block of the
        # functions, but we don't catch the SIGTERM. There is probably a cleaner way to do
        # this. This will do for now.
        # TODO figure out cleanup
        pixels.fill((0, 0, 0))
        pixels.show()
    
# command is the string command
# w is WeatherLights object
def parse_intent(command, pixels, w):
    command = command.lower()
    print(command)
    
    # TODO actual implementation -- need to correctly map command to function
    # currently only example of how code would work
    if("weather" in command):
        run_func_sub(wind_speed_lights, (w, pixels), 5, pixels)

    
    