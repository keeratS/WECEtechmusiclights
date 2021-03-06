# adapted from https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/master/examples/neopixel_rpi_simpletest.py

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

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
    return (r, g, b)


def rainbow_cycle(pixels, wait):
    for j in range(255):
        for i in range(pixels.n):
            pixel_index = (i * 256 // pixels.n) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)
        
# continuous cycle
def rainbow_lights(pixels):
    try:
        while True:
            rainbow_cycle(pixels, 0.001)  # rainbow cycle with 1ms delay per step
            
    except KeyboardInterrupt:
        # shutting off lights
        pixels.fill((0, 0, 0))
        pixels.show()
    
def simple_lights_test(pixels):
    try: 
        while True:
            pixels.fill((255, 0, 0))
            pixels.show()
            time.sleep(1)

            pixels.fill((0, 255, 0))
            pixels.show()
            time.sleep(1)

            pixels.fill((0, 0, 255))
            pixels.show()
            time.sleep(1)
            
            rainbow_cycle(pixels, 0.001)  # rainbow cycle with 1ms delay per step
    except KeyboardInterrupt:
        # shutting off lights
        pixels.fill((0, 0, 0))
        pixels.show()
    

if __name__ == "__main__":
    # Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
    # NeoPixels must be connected to D10, D12, D18 or D21 to work.
    pixel_pin = board.D18

    # The number of NeoPixels
    num_pixels = 50

    ORDER = neopixel.RGB

    pixels = neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
    )
    
    simple_lights_test(pixels)
