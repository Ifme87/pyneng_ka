#!/usr/bin/env python3

from base_connect_class import BaseSSH

class CiscoSSH(BaseSSH):
	def __init__(self, device_params):
		if not 'username' in device_params.keys():
			username = input('Enter username: ')
			device_params['username'] = username
		if not 'password' in device_params.keys():
			password = input('Enter password: ')
			device_params['password'] = password
		if not 'secret' in device_params.keys():
			secret = input('Enter secret: ')
			device_params['secret'] = secret
		super().__init__(**device_params)
		self.ssh.enable()
		
device_params = {
	"device_type": "cisco_ios",
	"ip": "192.168.100.1",
	#"username": "cisco",
	"password": "cisco",
	"secret": "cisco",
	}
