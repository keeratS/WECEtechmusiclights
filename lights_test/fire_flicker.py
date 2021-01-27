#print("urmom")

import board
import neopixel
import random
import time

def fire_animation(pixels):
    print("trying fire")
    try:
        while True:
            rgb = (255, 96, 12)
            delay = random.choice(range(50, 150))/1000

            for p in range(50):
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
        
if __name__ == "__main__":
    pixel_pin=board.D18
    num_pixels=50
    ORDER=neopixel.RGB
    pixels=neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
    )
    fire_animation(pixels)
