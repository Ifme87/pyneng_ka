#!/usr/bin/env python3

import re
from pprint import pprint
import glob

sh_cdp_nei_files = glob.glob("sh_cdp*")


def parse_show_cdp_neighbors(files_to_parse):
	result = {}
	for ffile in files_to_parse: 
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
	return result


pprint(parse_show_cdp_neighbors(sh_cdp_nei_files))
