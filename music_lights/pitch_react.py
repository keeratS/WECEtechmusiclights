#! /usr/bin/env python

#this code is made of additions to the demo_pyaudio 

# Use pyaudio to open the microphone and run aubio.pitch on the stream of
# incoming samples. If a filename is given as the first argument, it will
# record 5 seconds of audio to this location. Otherwise, the script will
# run until Ctrl+C is pressed.

# Examples:
#    $ ./python/demos/demo_pyaudio.py
#    $ ./python/demos/demo_pyaudio.py /tmp/recording.wav

import pyaudio
import sys
import numpy as np
import aubio

#neopixel setup
import time
import board
import neopixel

pixel_pin=board.D18
num_pixels=50
ORDER=neopixel.RGB
pixels=neopixel.NeoPixel( pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

#function to take colors of hsv format and convert it to rgb format
def hsv_to_rgb(h, s, v):
        h=h/360
        if s == 0.0: v*=255; return (v, v, v)
        i = int(h*6.) # XXX assume int() truncates!
        f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
        if i == 0: return (int(v), int(t), int(p))
        if i == 1: return (int(q), int(v), int(p))
        if i == 2: return (int(p), int(v), int(t))
        if i == 3: return (int(p), int(q), int(v))
        if i == 4: return (int(t), int(p), int(v))
        if i == 5: return (int(v), int(p), int(q))

# initialise pyaudio
p = pyaudio.PyAudio()

# open stream
buffer_size = 1024
pyaudio_format = pyaudio.paFloat32
n_channels = 1
samplerate = 44100
stream = p.open(format=pyaudio_format,
                channels=n_channels,
                rate=samplerate,
                input=True,
                frames_per_buffer=buffer_size)

if len(sys.argv) > 1:
    # record 5 seconds
    output_filename = sys.argv[1]
    record_duration = 5 # exit 1
    outputsink = aubio.sink(sys.argv[1], samplerate)
    total_frames = 0
else:
    # run forever
    outputsink = None
    record_duration = None

# setup pitch
tolerance = 0.8
win_s = 4096 # fft size
hop_s = buffer_size # hop size
pitch_o = aubio.pitch("yinfast", win_s, hop_s, samplerate)
pitch_o.set_unit("midi")
pitch_o.set_tolerance(tolerance)

print("*** starting recording")

rgb=(0,0,0)

while True:
    try:
        audiobuffer = stream.read(buffer_size, exception_on_overflow=False)
        signal = np.fromstring(audiobuffer, dtype=np.float32)

        pitch = pitch_o(signal)[0]
        confidence = pitch_o.get_confidence()
        
        #commented out print statements can be useful for debugging
        #print("{} / {}".format(pitch,confidence))
        
        hue=int(pitch*360/100) #based on the pitch from the mic a hue is chosen
    
        if (pitch !=0): #if it didnt hear any noise don't update pitch
            rgb= hsv_to_rgb(hue,1,1) #convert to rgb
        else:
            rgb=(0,0,0)
            #print ("no confidence")

        #rgb= hsv_to_rgb(hue,1,1)
        #print(rgb)
       
       #put the new color on left and cascade the rest
        for i in range (49,0,-1):
            pixels[i]=pixels[i-1]
        pixels[0]=rgb

        #time.sleep(0.05)
        pixels.show()
        #print("updated the lights")
        #print("___")
        
        #back to audio stuff now
        if outputsink:
            outputsink(signal, len(signal))

        if record_duration:
            total_frames += len(signal)
            if record_duration * samplerate < total_frames:
                break
    except KeyboardInterrupt:
        print("*** Ctrl+C pressed, exiting")
        pixels.fill((0,0,0))
        pixels.show()
        break

print("*** done recording")
stream.stop_stream()
stream.close()
p.terminate()
