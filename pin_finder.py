#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

target_pin=int(sys.argv[1])

print "Operating on Pin %s" % target_pin 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(target_pin,GPIO.OUT)

while True:
    GPIO.output(target_pin,False)
    time.sleep(1)
    GPIO.output(target_pin,True)
    time.sleep(1)
