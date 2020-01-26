from microbit import *
import radio
radio.on()
radio.config(power=1)
while True:
    incoming = str(radio.receive())
    if incoming == "None":
        incoming = "-"
    display.show(incoming) 
