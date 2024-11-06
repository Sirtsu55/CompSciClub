from GroveSensors.Digital.ws2812 import WS2812
from time import sleep


# WS2812(pin_num,led_count), this one only has 1 LED
# This was made for a device that had multiple LEDs in an array
led = WS2812(18,1)

# 0 indexes to the first LED
# RGB color
led.pixels_set(0, (255, 0, 0))
led.pixels_show()
sleep(1)

led.pixels_set(0, (0, 255, 0))
led.pixels_show()
sleep(1)

led.pixels_set(0, (0, 0, 255))
led.pixels_show()
sleep(1)

# Off
led.pixels_set(0, (0, 0, 0))
led.pixels_show()
sleep(1)

# This cycles through all the colors with the interval 0.01s
led.rainbow_cycle(0.01)

# Off
led.pixels_set(0, (0, 0, 0))
led.pixels_show()