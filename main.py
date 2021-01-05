# Performs hardware set up and then listens for audio.
# Calls intent_parser which calls lights commands when audio is recognized.
# TODO listen continuously

import speech_recognition as sr
import board
import neopixel

import time
import os
import multiprocessing

# local imports
import intent_parser
from weather_lights.WeatherLights import WeatherLights
from lights_test.neopixel_rpi_simpletest import rainbow_cycle

# Lights set-up
# defining information about our lights
pixel_pin = board.D18
num_pixels = 50

# allows us to use RGB ordering
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

pixels.fill((0, 0, 0))
pixels.show()



# lights test on start (runs through quick sequence)
rainbow_cycle(pixels, 0.001)
pixels.fill((0, 0, 0))
pixels.show()


# creating WeatherLights object 
w = WeatherLights()

# listens for one command and calls parser accordingly
# TODO add to loop for continuous listening, including background listenting for stop

# obtain audio from the microphone  
r = sr.Recognizer()  
with sr.Microphone() as source:  
    print("Please wait. Calibrating microphone...")  
    # listen for 5 seconds and create the ambient noise energy level  
    r.adjust_for_ambient_noise(source, duration=5)  
    print("Say something!")
    audio = r.listen(source)
    
language_path = os.path.join(os.getcwd(), "en-WECE")

# recognize speech using Sphinx  
try:  
    command = r.recognize_sphinx(audio, language=language_path)
    
    # will call relevant functions based on command
    intent_parser.parse_intent(command, pixels, w)
    
except sr.UnknownValueError:  
    print("Sphinx could not understand audio")  
except sr.RequestError as e:  
    print("Sphinx error; {0}".format(e))
    
