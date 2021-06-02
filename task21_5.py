#!/usr/bin/env python3

import yaml
from netmiko import ConnectHandler
import textfsm
from pprint import pprint
from textfsm import clitable
from concurrent.futures import ThreadPoolExecutor, as_completed


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
	

def send_and_parse_command_parallel(devices, command, limit=2):
	with ThreadPoolExecutor(max_workers=limit) as executor:
		result = []
		hosts = []
		out = dict()
		for device in devices:
			result.append(executor.submit(send_and_parse_show_command, device, command))
			hosts.append(device['host'])
		for key, value in zip(hosts, as_completed(result)):
			out[key] = value.result()
	return out

if __name__ == "__main__":
	with open("devices.yaml") as f:
		devices = yaml.safe_load(f)
		result = send_and_parse_command_parallel(devices, "sh ip int bri")
		pprint(result)
