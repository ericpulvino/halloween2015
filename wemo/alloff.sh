#!/bin/bash

cd /home/pi/wemo/

/home/pi/wemo/driveway_off.py &
/home/pi/wemo/frontporch_off.py &
/home/pi/wemo/plug1_off.py &

/home/pi/wemo/get_state.py 192.168.1.6 Driveway
/home/pi/wemo/get_state.py 192.168.1.9 Front_Porch
/home/pi/wemo/get_state.py 192.168.1.11 Plug_1


echo "DONE!"

