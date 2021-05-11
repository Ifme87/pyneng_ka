#!/usr/bin/env python3

import pexpect, telnetlib, paramiko
import yaml
import re, time, logging
from pprint import pprint
from datetime import datetime
from netmiko import ( 
	ConnectHandler,
	NetmikoTimeoutException,
	NetmikoAuthenticationException,
)





def send_config_commands(device, config_commands, log=True):
	failed_commands = {}
	executed_commands = {}		
	try:
		with ConnectHandler(**device) as ssh:
			ip = device['host']
			if log:
				print('\n' + 'Connecting to {}...'.format(ip))
			ssh.enable()
			for command in config_commands:
				line = ssh.send_config_set(command)
				if 'Invalid input detected' in line:
					print(f"Command {command} executed with error 'Invalid input detected' on device {ip}")
					failed_commands.update({command: line})
					continue
				if 'Incomplete command' in line:
					print(f"Command {command} executed with error 'Incomplete command' on device {ip}")
					failed_commands.update({command: line})
					continue
				if 'Ambiguous command' in line:
					print(f"Command {command} executed with error 'Ambiguous command' on device {ip}")
					failed_commands.update({command: line})
					continue
				executed_commands.update({command: line})
		t = ()
		t += (executed_commands,)
		t += (failed_commands,) 
		return t
	except (NetmikoAuthenticationException, NetmikoTimeoutException) as err:
		return err
	
	
comms = ['logging 0255.255.1', 'logging', 'a', 'logging buffered 20010', 'ip http server']

	
if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        
    #print(devices)

    for dev in devices:
        pprint(send_config_commands(dev, comms))
