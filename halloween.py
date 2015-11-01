#!/usr/bin/python

import sys
import time
import random
import subprocess
import RPi.GPIO as GPIO
start_time=time.time()


#Hardcoded Pins
pir_pin = 7
smoke_pin=23

#behavior vars
trip_delay=0.01 #delay in between motion sensing and tripping the lights
smoke_period=25 #amount of time to dispatch smoke
next_fire_delay=5 #amount of time in between the end of last routine and restarting motion detection
alarm_interval_threshold = 20 #number of detection intervals required to be positive before starting routine
lights_off_period=1 #amount of time lights should be off for
evil_sound_delay=0.1 #amount of time between killing the lights and playing the scary sound
dry_run=False #disables the killing of the lights and pumping of smoke

#working directory
working_dir="/home/pi/scripts/halloween2015"

#setup
print "SETTING UP GPIO PINS (PIR Pin: %s Smoke Pin: %s)" % (pir_pin, smoke_pin) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir_pin,GPIO.IN) #activate input
GPIO.setup(smoke_pin,GPIO.OUT)

print "SETTING STARTING POSITIONS..."
#Start position
GPIO.output(smoke_pin,True)
output=subprocess.check_output(working_dir+"/wemo/allon.sh", shell=True)
print "   >READY<"

print "### SCANNING FOR MOTION ###"

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
                output=subprocess.check_output(working_dir+".wemo/alloff.sh", shell=True)
                print output
            print "    waiting %s seconds to play evil sound..." % evil_sound_delay
            time.sleep(evil_sound_delay)
            print "       playing evil sound!"
            proc = subprocess.Popen("/usr/bin/aplay "+working_dir+"/sounds/%s.wav" % (random.randint(1, 10)), shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)
            time.sleep(lights_off_period-evil_sound_delay)
            print "       Bringing Lights Back!"
            if not dry_run:
                output=subprocess.check_output(working_dir+"/wemo/allon.sh", shell=True)
                print output
            remaining_sleep = smoke_period-evil_sound_delay-lights_off_period-trip_delay
            print "    continuing to smoke for %s seconds..." % remaining_sleep
            time.sleep(remaining_sleep)
            GPIO.output(smoke_pin,True)       
            print "    delaying %s seconds for next run of scare routine" % next_fire_delay
            time.sleep(next_fire_delay)
            print "### SCANNING FOR MOTION ###"

    elif not GPIO.input(pir_pin):
        running_count=0 #reset the consecutive positive interval count to 0
    time.sleep(0.01)
