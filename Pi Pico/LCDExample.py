from machine import Pin, I2C
import utime
from GroveSensors.I2C.lcd1602 import LCD1602

# These are the pins that the Grove LCD is connected to
connection = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)

# There is 2 lines and 16 characters in each line
lcd = LCD1602(connection, 2, 16)

# Print a two line message
lcd.print("Hello, Pico!")

# Set the cursor position to column 0, line 1
lcd.setCursor(0, 1)

# Print a message on the second line
lcd.print("Hello, World!")

# Wait for a second
utime.sleep(1)

# Replace the Pico to Buddy
# We can specify specific location
#lcd.setCursor(7, 0)
#lcd.print("Buddy!")

# or we can set it to the first line and print the whole message
lcd.setCursor(0, 0)
lcd.print("Hello, Buddy!")


utime.sleep(1)

# Clear the LCD
lcd.clear()

