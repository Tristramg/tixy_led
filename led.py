import datetime
import math
import time

import board
import neopixel

width = 16
height = 4
clamp = 20
max_led = width * height

pixels = neopixel.NeoPixel(board.D18, max_led, auto_write=False)

# Given the coordinates return the index of the led
def led_index(x, y):
    if y % 2 == 0:
        return y * width + x
    else:
        return (y+1) * width - x - 1

def fun(t, i, x, y):
    return math.sin(x/8 + y/2 + t)

start = datetime.datetime.now()
while True:
    t = (datetime.datetime.now() - start).total_seconds()
    print(t)
    for x in range(width):
        for y in range(height):
            i = y * width + height
            idx = led_index(x, y)
            val = fun(t, i, x, y)
            #print(f"Index: ({x}, {y}) -> {idx} -> {val}")
            if val >= 0:
                clamped = min(val, 1) * clamp
                pixels[idx] = (clamped, clamped, clamped)
            if val < 0:
                clamped = max(val, -1) * -clamp * 3
                pixels[idx] = (clamped, 0, 0)
    time.sleep(0.01)
    pixels.show()

