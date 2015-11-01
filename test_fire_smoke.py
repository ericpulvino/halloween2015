#!/usr/bin/python

import time
import RPi.GPIO as GPIO

smoke_pin=23

GPIO.setmode(GPIO.BOARD)
GPIO.setup(smoke_pin,GPIO.OUT)

while True:
    GPIO.output(smoke_pin,False)
    time.sleep(20)
    GPIO.output(smoke_pin,True)
    time.sleep(60)
