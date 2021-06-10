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
	def send_config_set(self, commands, *args, ignore_errors=True, **kwargs):
		if type(commands) == list:
			result = []
			for i in commands:
				out_cfg = CiscoIosSSH.send_config_set(self, i, *args, **kwargs)
				if not ignore_errors:
					self._check_error_in_command(i, out_cfg)
				result.append(out_cfg)
			return result 
		else:
			out_cfg = CiscoIosSSH.send_config_set(self, commands, *args, **kwargs)
			if not ignore_errors:
				self._check_error_in_command(commands, out_cfg)
			return out_cfg 
		
device_params = {
    "device_type": "cisco_ios",
    "ip": "10.0.0.100",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
    }
