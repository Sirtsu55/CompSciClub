from machine import Pin
import utime
from GroveSensors.Digital.UltrasonicSensor import UltrasonicSensor

sensor = UltrasonicSensor(16)

while True:
    # Distance in cm
    print(sensor.GetDistance())
    utime.sleep(0.1)
    
