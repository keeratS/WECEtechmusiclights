import board
import neopixel
import random
import time


n_leds = 50
pixels = neopixel.NeoPixel(board.D18, n_leds, auto_write=False)

def fire_animation():
    try:
        while True:
            rgb = (255, 96, 12)
            delay = random.choice(range(50, 150))/1000

        for p in range(n_leds):
            flicker = random.choice(range(40))
            rgb_r = tuple([x - flicker if x-flicker >= 0 else 0 for x in rgb ])
            pixels[p] = rgb_r
        pixels.show()
        time.sleep(delay)

      
    except KeyboardInterrupt:
    #shutting off lights
        pixels.fill((0,0,0))
        pixels.show()
