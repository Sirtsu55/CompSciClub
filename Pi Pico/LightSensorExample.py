from machine import ADC
from time import sleep

light = ADC(27)

while True:
    brightness = light.read_u16()
    print(brightness)
    sleep(1)