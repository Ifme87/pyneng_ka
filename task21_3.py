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
	with open("output/sh_ip_dhcp_snooping.txt") as f:
		output = f.read()
	result = parse_command_output("templates/sh_ip_dhcp_snooping.template", output)
	pprint(result)	
