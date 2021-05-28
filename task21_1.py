#!/usr/bin/env python3

from netmiko import ConnectHandler
import textfsm
from pprint import pprint

def parse_command_output(template, command_output):
	with open(template) as template:
		fsm = textfsm.TextFSM(template)
		result = fsm.ParseText(command_output)
		result.insert(0, fsm.header)
	return result

if __name__ == "__main__":
'''	r1_params = {
		"device_type": "cisco_ios",
		"host": "10.0.0.100",
		"username": "cisco",
		"password": "cisco",
		"secret": "cisco",
		}
	with ConnectHandler(**r1_params) as r1:
		r1.enable()
		output = r1.send_command("sh ip int br")
		result ='''
	parse_command_output("templates/sh_ip_dhcp_snooping.template", "output/sh_ip_dhcp_snooping.txt")
	pprint(result)	
