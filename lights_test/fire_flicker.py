#print("urmom")

import board
import neopixel
import random
import time


ORDER=neopixel.RGB
pixel_pin =board.D18
n_leds = 50
pixels = neopixel.NeoPixel(board.D18, n_leds, auto_write=False, pixel_order= ORDER)

def fire_animation():
    print("trying fire")
    try:
        while True:
            rgb = (255, 96, 12)
            delay = random.choice(range(50, 150))/1000

            for p in range(n_leds):
                flicker = random.choice(range(40))
                rgb_r = tuple([x - flicker if x-flicker >= 0 else 0 for x in rgb ])
                pixels[p] = rgb_r
                #print("chaning" +str(p) + "to color" + str(tuple))
        
            pixels.show()
                #print("updating")
            time.sleep(delay)
        
    
      
    except KeyboardInterrupt:
    #shutting off lights
        pixels.fill((0,0,0))
        pixels.show()
        
fire_animation() 
        
        
        
        
