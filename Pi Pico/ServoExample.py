from machine import Pin
from GroveSensors.Digital.AnalogServo import SERVO
from time import sleep

servo = SERVO(Pin(20))

# Valid angles are 0-180
# This function "sets the angle", so it's not like "turn 45 to the right from this position"
servo.turn(45)
