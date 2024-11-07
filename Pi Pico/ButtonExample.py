from machine import Pin

button = Pin(18, Pin.IN, Pin.PULL_UP)

def InterruptsButton(pin):
    print("Button pressed")

button.irq(lambda pin: InterruptsButton, Pin.IRQ_FALLING)

while True:  
    pass