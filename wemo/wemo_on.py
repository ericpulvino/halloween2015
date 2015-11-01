#!/usr/bin/python
import sys
from miranda import upnp

ip_address = sys.argv[1]

conn = upnp()

resp = conn.sendSOAP(ip_address+':49153', 'urn:Belkin:service:basicevent:1', 
     'http://'+ip_address+':49153/upnp/control/basicevent1', 
     'SetBinaryState', {'BinaryState': (1, 'Boolean')})

