#!/usr/bin/python
import time
import datetime
from miranda import upnp
from datetime import timedelta

LOGGING_FILE = "/var/log/wemo/switchlog"

conn = upnp()

resp = conn.sendSOAP('192.168.1.8:49153', 'urn:Belkin:service:basicevent:1', 
     'http://192.168.1.8:49153/upnp/control/basicevent1', 
     'SetBinaryState', {'BinaryState': (1, 'Boolean')})


#GENERATE TIMESTAMP
ts = time.time()
current_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%R')

LOGGER = open(LOGGING_FILE, 'a')
LOGGER.write( str(current_time) + " - Piano room turned on." + "\n")
LOGGER.close()
