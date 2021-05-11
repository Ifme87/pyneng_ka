#!/usr/bin/env python3

import re
from pprint import pprint


def get_ip_from_cfg(config):
	regex = re.compile('interface ((?:Lo|Eth).*)(?:\n )*'
					   '(?:\n .*)*?'
					   'ip address (\S+) (\S+).*'
					   '(?:\n ip address (\S+) (\S+).*)*')
	with open(config) as f:
		match = regex.findall(f.read())
		result = {}
		for i in match:
			if not '' in i:
				result[i[0]] = [(i[1], i[2]), (i[3], i[4])]
			else:
				result[i[0]] = [(i[1], i[2])]
	return match
	

pprint(get_ip_from_cfg('config_r2.txt'))
