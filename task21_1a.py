#!/usr/bin/env python3

from netmiko import ConnectHandler
import textfsm
from pprint import pprint

def parse_output_to_dict(template, command_output):
	with open(template) as template:
		fsm = textfsm.TextFSM(template)
		result = fsm.ParseText(command_output)
		out = []
		for line in result:
			dictionary = {}
			counter = 0
			for key in fsm.header:
				dictionary[key] = line[counter]
				counter += 1
			out.append(dictionary)
	return out

if __name__ == "__main__":
	r1_params = {
		"device_type": "cisco_ios",
		"host": "10.0.0.100",
		"username": "cisco",
		"password": "cisco",
		"secret": "cisco",
		}
	with ConnectHandler(**r1_params) as r1:
		r1.enable()
		output = r1.send_command("sh ip int br")
		result = parse_output_to_dict("templates/sh_ip_int_br.template", output)
		print(result)	
