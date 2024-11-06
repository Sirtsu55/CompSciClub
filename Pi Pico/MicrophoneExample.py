from machine import ADC
from time import sleep

# ADC stands for Analog to Digital Converter
# The microphone is analog, so we need to convert it to digital
# Microphone is connected to pin 26
mic = ADC(26)


while True:
    val = mic.read_u16()
    
    if(val > 50000):
        print("Speech Detected")
        sleep(1)
    else:
        print(val)
    # Wait for a second
    sleep(0.1)
    
    


