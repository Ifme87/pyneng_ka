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

#exceptions
def send_commands(device, *, show, config):
	if show and config:
		raise ValueError('Only show commands OR config commands available')
	if show:
		return send_show_commands(device, show)
	elif config:
		return send_config_commands(device, config)

#show
def send_show_commands(device, command):
	with ConnectHandler(**device) as ssh:
		ssh.enable()
		hostname = ssh.find_prompt()
		result = []
		for comm in command:
			result.append(ssh.send_command_timing(comm, strip_command=False))
		return result, hostname
		
#config
def send_config_commands(device, command):
	with ConnectHandler(**device) as ssh:
		ssh.enable()
		hostname = ssh.find_prompt()
		result = []
		result.append(ssh.send_config_set(command, strip_command=False))
		return result, hostname

#base def for 
def send_commands_to_devices(devices, filename, *, show_commands=None, config_commands=None, limit=3):
	with ThreadPoolExecutor(max_workers=limit) as executor:
		result = []
		for device in devices:
			result.append(executor.submit(send_commands, device, show=show_commands, config=config_commands))
	with open(filename, 'w') as w:
		for i in result:
			command, hostname = i.result()
			for line in command:
				w.write('\n'*2 + hostname)
				w.write(line)
	print('Done')


if __name__ == "__main__":
	'''commands = {
    "10.0.0.30": ["sh clock", "sh ip arp"],											#sw15
    "10.0.0.100": ["sh ip int br", "show interf status", "sh mac address-table"], #sw5
    "10.0.0.200": ["sh int desc", "sh version | i upt"]							#sw14
}'''
	show = ["sh ip int br", "show interf status", "sh mac address-table"]
	config = ["logging 10.5.5.5", "ip routing", "vlan 222"]
	with open('devices.yaml') as f:
		devs = yaml.safe_load(f)
	send_commands_to_devices(devs, 'res19_4.txt', config_commands=config, limit=3)
	
