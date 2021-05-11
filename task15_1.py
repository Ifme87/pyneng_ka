#!/usr/bin/env python3

import re


def get_ip_from_cfg(config):
	regex = re.compile(' ip address (?P<ip>\S+) (?P<mask>\S+)')
	with open(config) as f:
		match = regex.findall(f.read())
	return match
	

print(get_ip_from_cfg('config_r1.txt'))
		
		
		
