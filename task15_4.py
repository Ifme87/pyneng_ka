#!/usr/bin/env python3

import re
from pprint import pprint


def get_ints_without_description(config):
	result = []
	with open(config) as f:
		with_descr = re.findall(r'(interface \S+?)\n des', f.read())
	with open(config) as f:
		for line in f:
			match = re.search(r'(^interface \S+?)\n', line)
			if match:
				if match.groups()[0] in with_descr:
					continue
				else:
					result.append(match.groups()[0])
	return result
			
		
pprint(get_ints_without_description('config_r1.txt'))
			
