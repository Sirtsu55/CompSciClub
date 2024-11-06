from machine import ADC
from time import sleep

motion = ADC(26)

# Maximum value that the wheel reports
MAX_VALUE = 65535

while True:
    val = motion.read_u16()
    
    # Dividing by max gives a value in the range 0-1
    print(val / MAX_VALUE)
        
    sleep(1)