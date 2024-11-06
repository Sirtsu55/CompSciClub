from machine import Pin
from time import sleep
from GroveSensors.Digital.UltrasonicSensor import UltrasonicSensor

sensor = UltrasonicSensor(16)

while True:
    # Distance in cm
    print(sensor.GetDistance())
    sleep(0.1)
    
