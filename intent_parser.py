# Intent parser for WECE lights

import multiprocessing
import time
import time
import speech_recognition as sr
import datetime

# local imports
from weather_lights.wind_speed_lights import wind_speed_lights
from weather_lights.short_forecast import short_forecast
from lights_test.galaxy_effect import galaxy_lights
from lights_test.rainbow_shift import rainbow_shift
from lights_test.neopixel_rpi_simpletest import simple_lights_test

# returns elapsed seconds since start time
def time_delta(start_time):
    current_time = datetime.datetime.now()
    difference = current_time - start_time
    return difference.total_seconds()   


# helper to run a given function as a subprocess
# for functions that run forever, (i.e. only stop on ctrl-C)
# allows us to stop based on some time or wait for external stop command
# target is name of function
# args are the arguments to that function
# t is the amount of time function should be run before terminating
def run_func_sub(target, args, t, pixels, r):
        # start func as a process
        p = multiprocessing.Process(target = target, args = args)
        p.start() # starting wind_speed_lights function, same as wind_speed_lights(w, pixels)
    
        def kill_process():
            if p.is_alive():
                p.terminate()
                p.join()
                
        # function for background listening for stop function
        # listens for "stop lights" to immediately terminate anything currently going on
        def callback(recognizer, audio):
            language_path = "/home/pi/Documents/wece_lights/WECEtechmusiclights/en-WECE"
            try:  
                command = r.recognize_sphinx(audio, language=language_path)
                print("Sphinx thinks you said", command)
                command = command.lower()
                
                if "stop" in command and "light" in command:
                    print("Stopping lights")
                    # would ideally do this with a stop flag, but doesn't work here.
                    # Slightly reduntant, but works
                    kill_process()
                    
            except sr.UnknownValueError:  
                print("Sphinx could not understand audio")  
            except sr.RequestError as e:  
                print("Sphinx error; {0}".format(e))


        # start listening in the background (note that we don't have to do this inside a `with` statement)
        print("Say 'stop lights' to end command")
        stop_listening = r.listen_in_background(sr.Microphone(), callback)
        # `stop_listening` is now a function that, when called, stops background listening
        

        # allow function to run for duration of time
        start_time = datetime.datetime.now()
        while(time_delta(start_time) < t and p.is_alive()):
            time.sleep(0.1)
        
        stop_listening(wait_for_stop=False)
        
        # in case of timeout
        kill_process()
        
        # Shutting the lights off. this is usally taken care of in the except block of the
        # functions, but we don't catch the SIGTERM. There is probably a cleaner way to do
        # this. This will do for now.
        # TODO figure out cleanup
        pixels.fill((0, 0, 0))
        pixels.show()
    
# command is the string command
# w is WeatherLights object
def parse_intent(command, pixels, w, recognizer):
    command = command.lower()
    print(command)
    
    # TODO actual implementation -- need to correctly map command to function
    # currently only example of how code would work
    if("wind speed" in command): #works
        run_func_sub(wind_speed_lights, (w, pixels), 5, pixels, recognizer)
    #not reformatted yet
    #if("temperature" in command):
        #run_func_sub(today_temp, (w, pixels), 5, pixels)
    if("weather" in command):
        run_func_sub(short_forecast, (w, pixels), 5, pixels, recognizer)
        
    if("fireworks" in command):
        run_func_sub(firework_lights, (pixels,), 5, pixels, recognizer)
    if("galaxy" in command):
        run_func_sub(galaxy_lights, (pixels,), 5, pixels, recognizer)
    if("lights" in command):
        run_func_sub(simple_lights_test, (pixels,), 5, pixels, recognizer)
    if("rainbow" in command): #works
        run_func_sub(rainbow_shift, (pixels,), 5, pixels, recognizer)
    
    
    
        
    