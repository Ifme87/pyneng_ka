#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from itertools import repeat
import logging, yaml
from pprint import pprint
from netmiko import ( 
	ConnectHandler,
	NetmikoTimeoutException,
	NetmikoAuthenticationException,
)
import re


def send_show_command(device, command):
	with ConnectHandler(**device) as ssh:
		ssh.enable()
		hostname = ssh.find_prompt()
		result = ssh.send_command_timing(command, strip_command=False)
	return result, hostname
	
	
def send_show_command_to_devices(devices, commands_dict, filename, limit=3):
	with ThreadPoolExecutor(max_workers=limit) as executor:
		result = []
		for device in devices:
			command = commands[device['host']]
			result.append(executor.submit(send_show_command, device, command))
	with open(filename, 'w') as w:
		for i in result:
			hn_command = i.result()
			w.write(hn_command[1] + hn_command[0] + '\n')
	print('Done')


if __name__ == "__main__":
	commands = {
    "10.0.0.30": "sh clock",
    "10.0.0.100": "sh ip int br",
    "10.0.0.200": "sh int desc",
}
	with open('devices.yaml') as f:
		devs = yaml.safe_load(f)
	send_show_command_to_devices(devs, commands, 'res19_3.txt', limit=3)
	
