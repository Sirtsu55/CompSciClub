# Read ultrasensor Grove Ultrasonic Ranger

from machine import Pin
import utime
from GroveSensors.Digital.UltrasonicSensor import UltrasonicSensor

# Pins are same for receiving and sending

sensor = UltrasonicSensor(Pin(16))

while True:
    print(sensor.GetDistance())
    utime.sleep(1)
    
