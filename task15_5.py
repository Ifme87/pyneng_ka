#!/usr/bin/env python3

import re
from pprint import pprint


def generate_description_from_cdp(show_cdp):
	regex = re.compile(r'^(\S+) +(\S+ \w+\/\w+).+ (\S+ \w+\/\w+)')
	result = {}
	with open(show_cdp) as f:
		for line in f:
			match = re.search(regex, line)
			if match:
				descript = 'description Connected to {} port {}'.format(match.group(1), match.group(3))
				result[match.group(2)] = descript
	return result
	
	
pprint(generate_description_from_cdp('sh_cdp_n_sw1.txt'))
			
