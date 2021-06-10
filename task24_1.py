#!/usr/bin/env python3

from base_connect_class import BaseSSH

class CiscoSSH(BaseSSH):
	def __init__(self, **device_params):
		super().__init__(**device_params)
		self.ssh.enable()
		
device_params = {
	"device_type": "cisco_ios",
	"ip": "192.168.100.1",
	"username": "cisco",
	"password": "cisco",
	"secret": "cisco",
	}
