#!/usr/bin/env python3

from netmiko.cisco.cisco_ios import CiscoIosSSH

class MyNetmiko(CiscoIosSSH):
	def __init__(self, **device_params):
		CiscoIosSSH.__init__(self, **device_params)
		self.enable()
		
device_params = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
    }
