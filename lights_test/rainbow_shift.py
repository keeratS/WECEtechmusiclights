# From https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/master/examples/neopixel_rpi_simpletest.py

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
# pixel_pin = board.D18
# 
# # The number of NeoPixels
# num_pixels = 50
# 
# # Our lights are GRB lights.
# ORDER = neopixel.GRB
# 
# pixels = neopixel.NeoPixel(
#     pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
# )
def rainbow_shift(pixels):

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
        return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


    def rainbow_cycle(wait):
        for j in range(255):
            for i in range(num_pixels):
                pixel_index = (i * 256 // num_pixels) + j
                pixels[i] = wheel(pixel_index & 255)
            pixels.show()
            time.sleep(wait)

    def count_cycle(wait, x, y, z):
        for i in range (50):
            pixels[i] = (x,y,z)
            pixels.show()
            time.sleep(wait)
        for j in range (50):
            pixels[j] = (0,0,0)
            pixels.show()
            time.sleep(wait)
            
            
    print("Press Ctrl-C to turn off lights")
    try: 
        while True:

            count_cycle(0.05, 255, 0, 0)     #red
            count_cycle(0.05, 255, 100, 0)   #orange
            count_cycle(0.05, 255, 200, 0)   #yellow
            count_cycle(0.05, 0, 255, 0)     #green
            count_cycle(0.05, 0, 0, 255)     #blue
            count_cycle(0.05, 128, 0, 128)   #purple
            count_cycle(0.05, 255, 255, 255) #white
            
    except KeyboardInterrupt:
        # shutting off lights
        pixels.fill((0, 0, 0))
        pixels.show()
    
if __name__ == "__main__":   
    ORDER=neopixel.RGB
    pixel_pin =board.D18
    n_leds = 50
    pixels = neopixel.NeoPixel(board.D18, n_leds, auto_write=False, pixel_order= ORDER)

    rainbow_shift(pixels) 
