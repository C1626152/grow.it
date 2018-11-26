from microbit import *
import radio
display.scroll('ON')

radio.on()
ans = radio.receive()

#Use async to make this a seperate thread
while True:
    water = pin1.read_analog()
    if water < 500:
        display.scroll(water)
    elif water >= 500:
        display.scroll("Water me!")
        
    #Needs boolean to detect water existance (if water == True)
    if ans == 'reset':
        display.scroll("BYE")
        reset()