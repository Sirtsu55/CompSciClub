from machine import Pin
import utime
from GroveSensors.Digital.buzzer import Music


# Buzzer is connected to pin 20
buzzer = Music(Pin(20))


# Play a tone
# There are 0-8 tones, 0 is no tone
buzzer.music(1)

# Wait for a second
utime.sleep(0.1)

# Play a tone
buzzer.music(2)

# Wait for a second
utime.sleep(0.1)

# Stop the tone
buzzer.music(0)