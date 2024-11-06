from machine import I2C, Pin
from GroveSensors.I2C.dht20 import DHT20
from GroveSensors.I2C.lcd1602 import LCD1602

# These are the pins that the Grove LCD is connected to
# The I2C0 is connected to scl=Pin(9), sda=Pin(8)
# The I2C1 is connected to scl=Pin(1), sda=Pin(0)
# The first parameter is the I2C bus number so if you use I2C1 then you need to specify 1 
# or if you use I2C0 then you need to specify 0
# Frequency is 400000 (400kHz), so 
lcd_i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
dht_i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

# There is 2 lines and 16 characters in each line
lcd = LCD1602(lcd_i2c, 2, 16)
dht20 = DHT20(dht_i2c)

temper = dht20.dht20_temperature()
humidity = dht20.dht20_humidity()


lcd.setCursor(0, 0)
lcd.print(f"Temp: {temper}") 
