#!/usr/bin/env python3

from netmiko import ConnectHandler
import textfsm
from pprint import pprint
from textfsm import clitable


def parse_command_output(template, command_output):
	with open(template) as template:
		fsm = textfsm.TextFSM(template)
		result = fsm.ParseText(command_output)
		result.insert(0, fsm.header)
	return result

	
attr = {'Command': 'sh ip int br',
		'Vendor': 'cisco_ios'
}
	

def parse_command_dynamic(command_output, attributes_dict, index_file="index", templ_path="templates"):
	cli = clitable.CliTable(index_file, templ_path)
	cli.ParseCmd(command_output, attributes_dict)
	out = []
	header = cli[0]
	for line in cli:
		dictionary = {}
		counter = 0
		for key in header:
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
	result = parse_command_dynamic(output, attr)
	print(result)	
