from microbit import *
import radio


radio.on()
radio.config(power=1)
while True:
    radio.send("Station1")
    display.show("OK")
