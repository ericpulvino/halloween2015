#!/usr/bin/python

import sys
import time
import signal
import datetime
from miranda import upnp
import xml.etree.ElementTree as ET
from contextlib import contextmanager


#Args
ip_address = sys.argv[1]
wemo_name = sys.argv[2]
timeout_val = 3


class TimeoutException(Exception): pass

@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException, "Timed out!"
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

#print "IP Address: " + ip_address + " WEMO_NAME: " + wemo_name


current_state=""
conn = upnp()
try:
    with time_limit(timeout_val):
        resp = conn.sendSOAP(str(ip_address) +':49153', 'urn:Belkin:service:basicevent:1','http://'+ str(ip_address) + ':49153/upnp/control/basicevent1', 'GetBinaryState', {})
        tree = ET.fromstring(resp)    
        current_state = tree.find('.//BinaryState').text
        if str(current_state) != "1" and str(current_state) != "0": current_state = "2"
except:
    print "ERROR: " + wemo_name + " -- state cannot be determined!"
    current_state = "2"


if current_state == "1":
    print "INFO: " + wemo_name + " --  > on <"
elif current_state == "0":
    print "INFO: " + wemo_name + " --  > off <"
else:
    print "ERROR: " + wemo_name + " -- state cannot be determined!"
