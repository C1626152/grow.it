from microbit import *
import radio, thread, time

# Var x used for water limit, out of possible 1024
x = 450
# Var y used for light levels, out of possible 1024
y = 100
yList = []

display.scroll('ON')

# Unique addressing for microprocessor radios
radio.config(channel=32, address=0x00000001, group=2)
"""
Use above settings on other radios:
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

# timer object to reset the microprocessor after every hour of running
t = time.Timer(3600.0, reset)

def detectLight():
    if light < y:
        yList.append(y) 
        sleep(6000)
    elif light == 0:
        radio.send("ERROR, LIGHT")
        sleep(6000)
    else:
        yList.append(y)
        radio.send("ERROR, LOW LIGHT")
        sleep(6000)

def reportLight(ylist):
    if len(ylist) == 60:
        radio.send(yList)
        ylist = []

def detectWater():
    # Water probe is on pin 1
    water = pin1.read_analog()
    """ If water level below x, do:
    Probe is mesuring the resistance caused by the soil
    hence the backwards operands '</>' """
    if water < 0:
        if water < x:
            radio.send(water)
        elif water >= x:
            radio.send(water)
            display.scroll("Water me!")
    

# Turn radio on
radio.on()

while True:
    t.start()
    """ Two threads here for detecting and reporting light levels
    this may be superfluous and cause thread lock"""
    thread.start_new_thread(detectLight())
    thread.start_new_thread(reportLight())
    detectWater()
    # listen for reset command
    ans = radio.receive()
    light = pin0.read_analog()
    
    if ans == 'reset':
        display.scroll("CYCLING")
        reset()