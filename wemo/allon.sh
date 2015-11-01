#!/bin/bash

cd /home/pi/scripts/halloween2015/wemo

./wemo_on.py 192.168.1.31 & #driveway
./wemo_on.py 192.168.1.32 & #porch
./wemo_on.py 192.168.1.33 & #plug1

./get_state.py 192.168.1.31 Driveway
./get_state.py 192.168.1.32 Front_Porch
./get_state.py 192.168.1.33 Plug_1


