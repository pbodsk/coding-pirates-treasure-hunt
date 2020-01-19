from microbit import *
import radio
radio.on()
radio.config(power=1)
while True:
    incoming = radio.receive()
    if incoming == "Station1":
        display.show("s1")    
    else:
        display.show("NO") 
