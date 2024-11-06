from machine import Pin
from time import sleep

motion = Pin(20, Pin.IN)

while True:
    # If value is 1, then it detects motion, if 0, then no motion
    # It resets after a few seconds, so it will keep "detecting" motion for few seconds even though the motion has stopped
    val = motion.value()
    print(val)

    if val:
        print("Motion")
        
    sleep(1)