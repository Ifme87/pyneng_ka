#!/usr/bin/env python3


import yaml
from pprint import pprint
from jinja2 import Environment, FileSystemLoader
from task20_1 import generate_config
from task20_5 import parse_command
from task18_1_netmiko import send_show_command
import netmiko
import re


def send_config_commands(device, config_commands, log=True):	
	try:
		with netmiko.ConnectHandler(**device) as ssh:
			ip = device['host']
			if log:
				print('\n' + 'Connecting to {}...'.format(ip))
			ssh.enable()
			line = ssh.send_config_set(config_commands, exit_config_mode=False)
			return line
	except (netmiko.NetmikoAuthenticationException, netmiko.NetmikoTimeoutException) as err:
		return err
	
	
def create_vpn(src_device_params, dst_device_params, src_template, dst_template, vpn_data_dict):
	'''parse commands '''
	command_src = parse_command(src_template, vpn_data_dict)
	command_dst = parse_command(dst_template, vpn_data_dict)
	command_src = command_src.split('\n')
	command_dst = command_dst.split('\n')
	'''send commands '''
	result_scr = send_config_commands(src_device_params, command_src)
	result_dst = send_config_commands(dst_device_params, command_dst)
	'''print '''
	output = (result_scr, result_dst)
	return output
		

def generate_free_tun_num(devices, command):
	'''grab all tun nums '''
	tun_numbers = []
	for device in devices:
		result = send_show_command(device, command)
		regex = re.compile('Tu(\w+)')
		result = result.split('\n')
		for i in result:
			match = re.match(regex, i)
			if match:
				tun_numbers.append(int(match.group(1)))
	'''looking for free tun num '''
	tun_num = 0
	counter = True
	while counter == True:
		if tun_num in tun_numbers:
			tun_num += 1 
		elif tun_num == 30:
			print('stopped - more that 30 tunnels')
		else:
			counter = False
	return tun_num
	
	
	
data = {
    "tun_num": None,
    "wan_ip_1": "10.0.0.100",
    "wan_ip_2": "10.0.0.200",
    "tun_ip_1": "10.0.1.1 255.255.255.252",
    "tun_ip_2": "10.0.1.2 255.255.255.252",
}
	

if __name__ == "__main__":
	template_file1 = "templates/gre_ipsec_vpn_1.txt"
	template_file2 = "templates/gre_ipsec_vpn_2.txt"
	with open('devices.yaml') as f:
		device_data = yaml.safe_load(f)
	data['tun_num'] = generate_free_tun_num(device_data, 'sho int descr | i Tu')
	pprint(create_vpn(device_data[0], device_data[1], template_file1, template_file2, data))
	
