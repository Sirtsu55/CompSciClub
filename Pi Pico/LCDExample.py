from machine import Pin, I2C
from time import sleep
from GroveSensors.I2C.lcd1602 import LCD1602

# These are the pins that the Grove LCD is connected to
# The I2C0 is connected to scl=Pin(9), sda=Pin(8)
# The I2C1 is connected to scl=Pin(1), sda=Pin(0)
# The first parameter is the I2C bus number so if you use I2C1 then you need to specify 1 
# or if you use I2C0 then you need to specify 0
# Frequency is 400000 (400kHz), so 
connection = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)

# There is 2 lines and 16 characters in each line
lcd = LCD1602(connection, 2, 16)

# Print a two line message
lcd.print("Hello, Pico!")

# Set the cursor position to column 0, line 1
lcd.setCursor(0, 1)

# Print a message on the second line
lcd.print("Hello, World!")

# Wait for a second
sleep(1)

# Replace the Pico to Buddy
# We can specify specific location
#lcd.setCursor(7, 0)
#lcd.print("Buddy!")

# or we can set it to the first line and print the whole message
lcd.setCursor(0, 0)
lcd.print("Hello, Buddy!")

sleep(1)

# Clear the LCD
lcd.clear()

