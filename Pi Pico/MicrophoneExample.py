from machine import ADC
import utime

# ADC stands for Analog to Digital Converter
# The microphone is analog, so we need to convert it to digital
# Microphone is connected to pin 26
mic = ADC(26)


while True:
    val = mic.read_u16()
    
    
    if(val > 50000):
        print("Speech Detected")
        utime.sleep(1)
    else:
        print(val)
    # Wait for a second
    utime.sleep(0.1)
    
    


