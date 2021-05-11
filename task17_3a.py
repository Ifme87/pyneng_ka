#!/usr/bin/env python3

import re
from pprint import pprint
import glob
import yaml

sh_cdp_nei_files = glob.glob("sh_cdp*")


def generate_topology_from_cdp(list_of_files, save_to_filename=None):
	result = {}
	for ffile in list_of_files: 
		with open(ffile) as f:
			sh_cdp_nei = f.read()
			regex = re.compile('(\S+)(?:\>|\#).*|'
							   '(\S+) +(\S+ \w+\/\w+).*?(\S+ \w+\/\w+)$')
			list_iterator = sh_cdp_nei.split('\n')
			for i in list_iterator:
				match = re.match(regex, i)
				if match:
					if match.group(1):
						hostname = match.group(1)
						result[hostname] = {}
					else:
						result[hostname][match.group(3)] = {}
						result[hostname][match.group(3)][match.group(2)] = match.group(4)
	if save_to_filename:
		with open(save_to_filename, 'w') as f:
			yaml.dump(result, f)
	return result

pprint(generate_topology_from_cdp(sh_cdp_nei_files, 'topology.yaml'))
