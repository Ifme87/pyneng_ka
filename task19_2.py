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
		result = ssh.send_command_timing(command)
	return result, hostname
	
	
def send_show_command_to_devices(devices, command, filename, limit=3):
	with ThreadPoolExecutor(max_workers=limit) as executor:
		result = executor.map(send_show_command, devices, repeat(command))
	with open(filename, 'w') as w:
		for i in result:
			w.write(i[1] + command +'\n' + i[0] + '\n')
	print('Done')


if __name__ == "__main__":
	command = 'sh ip int brie'
	with open('devices.yaml') as f:
		devs = yaml.safe_load(f)
	send_show_command_to_devices(devs, command, 'res19_2.txt', limit=3)
	
