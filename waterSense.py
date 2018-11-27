from microbit import *
import radio
display.scroll('ON')

#Unique addressing for microprocessor radios
radio.config(channel=32,address=00000001,group=2)

"""Use above settings on other radios:
    -Channel always 32
    -Address reflective of role
        -Last bit addresses indicate slaves
        -[:-2] bit address indicate feedback
        -[:-3] bit address indicates master unit
    -grouping
        -group 2 for slaves
        -group 0 for controller
        -group 1 for actors/feedback controllers

"""

#Turn radio on
radio.on()

#Var x used for water limit, out of possible 1024
x = 450
#Var y used for light levels, out of possible 1024
y = 100
yList = []

#Use async to make this a seperate thread in future
while True:
    #listen for reset command
    ans = radio.receive()
    #Water probe is on pin 1
    water = pin1.read_analog()
    light = pin0.read_analog()
    
    #If water level below x, do:
    if water < x:
        radio.send(water)
    elif water >= x:
        display.scroll("Water me!")
        radio.send(water)
    
    """
    #Lines 46 - 56 need to become thread independent and safe
    if light < y:
        ylist.append(y)
        wait(60000)
        radio.send("y: ",y)
    elif light == 0:
        wait(60000)
        radio.send("ERROR, LIGHT")
    else:
        ylist.append(y)
        wait(60000)
        radio.send("ERROR, LOW LIGHT")
        """
    
    #Needs boolean to detect water existance (if water == True)
    if ans == 'reset':
        display.scroll("CYCLING")
        reset()