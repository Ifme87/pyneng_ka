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
from task18_2c import send_config_commands
from task18_1b import send_show_command


def send_commands(device, *, show=None, config=None):
	if show and config:
		raise ValueError('Only show commands OR config commands available')
	if show:
		return send_show_command(device, show)
	elif config:
		return send_config_commands(device, config)
	
		
if __name__ == "__main__":
	commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
	command = "sh ip int br"
	with open("devices.yaml") as f:
		devices = yaml.safe_load(f)
		#print(devices)
	for dev in devices:
		pprint(send_commands(dev, show='show clock', config=commands), width=120)
