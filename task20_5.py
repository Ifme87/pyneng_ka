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
	
	
def create_vpn_config(template1, template2, data_dict):
	'''template1'''
	template_parse1 = template1.split('/')
	template_dir1 = '/'.join(template_parse1[:(-1)])
	env1 = Environment(loader=FileSystemLoader(template_dir1), trim_blocks=True)
	template1 = env1.get_template(template_parse1[-1])
	'''template2'''
	template_parse2 = template2.split('/')
	template_dir2 = '/'.join(template_parse2[:(-1)])
	env2 = Environment(loader=FileSystemLoader(template_dir2), trim_blocks=True)
	template2 = env2.get_template(template_parse2[-1])
	'''rendering'''
	result = (template1.render(data_dict), template2.render(data_dict))
	return result


if __name__ == "__main__":
    template_file1 = "templates/gre_ipsec_vpn_1.txt"
    template_file2 = "templates/gre_ipsec_vpn_2.txt"
    pprint(create_vpn_config(template_file1, template_file2, data))
