#!/usr/bin/python

import sys
import time
import random
import subprocess
import RPi.GPIO as GPIO
start_time=time.time()



#pir_pin=int(sys.argv[1])
pir_pin = 7
smoke_pin=23

#behavior vars
trip_delay=0.01
smoke_period=25
next_fire_delay=5
alarm_interval_threshold = 20
lights_off_period=1
evil_sound_delay=0.1
dry_run=False


#setup
print "Starting with PIR Pin %s and Smoke Pin %s" % (pir_pin, smoke_pin) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir_pin,GPIO.IN) #activate input
GPIO.setup(smoke_pin,GPIO.OUT)

#Start position
GPIO.output(smoke_pin,True)
output=subprocess.check_output("/home/pi/wemo/allon.sh", shell=True)

running_count=0
while True:
    if GPIO.input(pir_pin):
        running_count +=1
        if running_count >= alarm_interval_threshold:
            print "TIME: %ssec Motion Detected!" % (time.time()-start_time)
            print "### Smoking for %s seconds" % smoke_period
            if not dry_run:
                GPIO.output(smoke_pin,False)
            print "    waiting %s seconds to trip lights..." % trip_delay
            time.sleep(trip_delay)
            print "       killing lights!"
            if not dry_run:
                output=subprocess.check_output("/home/pi/wemo/alloff.sh", shell=True)
                print output
            print "    waiting %s seconds to play evil sound..." % evil_sound_delay
            time.sleep(evil_sound_delay)
            print "       playing evil sound!"
            proc = subprocess.Popen("/usr/bin/aplay /home/pi/sounds/%s.wav" % (random.randint(1, 10)), shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)
            #output=subprocess.check_output("/usr/bin/aplay /home/pi/sounds/%s.wav" % (random.randint(1, 11)), shell=True)
            time.sleep(lights_off_period-evil_sound_delay)
            print "       Bringing Lights Back!"
            if not dry_run:
                output=subprocess.check_output("/home/pi/wemo/allon.sh", shell=True)
                print output
            remaining_sleep = smoke_period-evil_sound_delay-lights_off_period-trip_delay
            print "    continuing to smoke for %s seconds..." % remaining_sleep
            time.sleep(remaining_sleep)
            GPIO.output(smoke_pin,True)       
            print "    delaying %s seconds for next run of scare routine" % next_fire_delay
            time.sleep(next_fire_delay)
            print "### SEARCHING FOR MOTION ###"

    elif not GPIO.input(pir_pin):
        running_count=0
#        print "    All Clear"
    time.sleep(0.01)
