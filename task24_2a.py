#!/usr/bin/env python3

from netmiko.cisco.cisco_ios import CiscoIosSSH

class ErrorInCommand(Exception):
	pass

class MyNetmiko(CiscoIosSSH):
	def __init__(self, **device_params):
		CiscoIosSSH.__init__(self, **device_params)
		self.enable()
		self.ip = device_params['ip']
	def _check_error_in_command(self, command, output):
		if 'Invalid input detected' in output:
			raise ErrorInCommand(f"Command \"{command}\" executed with error 'Invalid input detected' on device {self.ip}")
		elif 'Incomplete command' in output:
			raise ErrorInCommand(f"Command \"{command}\" executed with error 'Incomplete command' on device {self.ip}")
		elif 'Ambiguous command' in output:
			raise ErrorInCommand(f"Command \"{command}\" executed with error 'Ambiguous command' on device {self.ip}")		
	def send_command(self, command, *args, **kwargs):
		out = CiscoIosSSH.send_command(self, command, *args, **kwargs)
		self._check_error_in_command(command, out)
		print(out)
	
		
		
device_params = {
    "device_type": "cisco_ios",
    "ip": "10.0.0.100",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
    }
