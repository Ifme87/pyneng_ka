#!/usr/bin/env python3

import re
from pprint import pprint


def get_ip_from_cfg(config):
	regex = re.compile(r'interface (?P<intf>\S+)'
					   r'(?:\n .*)*ip address (?P<ip>\S+) (?P<mask>\S+)')
	result = {}
	with open(config) as f:
		match = regex.findall(f.read())
		for i in match:
			result[i[0]] = i[1], i[2]
	return result
	

pprint(get_ip_from_cfg('config_r1.txt'))
