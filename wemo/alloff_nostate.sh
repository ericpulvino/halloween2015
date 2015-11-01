#!/bin/bash

cd /home/pi/wemo/

/home/pi/wemo/driveway_off.py &
/home/pi/wemo/frontporch_off.py &
/home/pi/wemo/plug1_off.py &


echo "DONE!"

