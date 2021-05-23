#!/usr/bin/env python3

import yaml
from pprint import pprint
from jinja2 import Environment, FileSystemLoader
from task20_1 import generate_config


data = {
    "tun_num": 10,
    "wan_ip_1": "192.168.100.1",
    "wan_ip_2": "192.168.100.2",
    "tun_ip_1": "10.0.1.1 255.255.255.252",
    "tun_ip_2": "10.0.1.2 255.255.255.252",
}
	
	
def parse_command(template_file, data):
	template_parse = template_file.split('/')
	template_dir = '/'.join(template_parse[:(-1)])
	env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True)
	template = env.get_template(template_parse[-1])
	command = template.render(data)
	return command
	
	
def create_vpn_config(template1, template2, data_dict):
	out_1 = parse_command(template1, data_dict)
	out_2 = parse_command(template2, data_dict)
	result = (out_1, out_2)
	return result


if __name__ == "__main__":
    template_file1 = "templates/gre_ipsec_vpn_1.txt"
    template_file2 = "templates/gre_ipsec_vpn_2.txt"
    pprint(create_vpn_config(template_file1, template_file2, data))
