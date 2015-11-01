#!/bin/bash

cd /home/pi/wemo/

/home/pi/wemo/driveway_on.py &
/home/pi/wemo/frontporch_on.py &
/home/pi/wemo/plug1_on.py &

echo "DONE!"

