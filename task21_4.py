#!/usr/bin/env python3

import yaml
from netmiko import ConnectHandler
import textfsm
from pprint import pprint
from textfsm import clitable


'''
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

'''

def send_and_parse_show_command(device_dict, command):
	with ConnectHandler(**device_dict) as r1:
		r1.enable()
		command_output = r1.send_command(command, use_textfsm=True)
	return command_output


if __name__ == "__main__":
	with open("devices.yaml") as f:
		devices = yaml.safe_load(f)
	for dev in devices:
		result = send_and_parse_show_command(dev, "sh ip int bri")
		pprint(result)
