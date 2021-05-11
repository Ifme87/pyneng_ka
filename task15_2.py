#!/usr/bin/env python3

import re
from pprint import pprint

def parse_sh_ip_int_br(sh_ip_int_br):
	regex = re.compile(r'((?:Fa|Eth|Gi|Ten|Lo)\S+) +(\S+).*?(up|(?:adm.*?down)|down) +(up|down)')
	result = []
	with open(sh_ip_int_br) as f:
		for line in f:
			match = re.search(regex, line)
			if match:
				preresult = tuple(match.groups())
				result.append(preresult)
	return result

pprint(parse_sh_ip_int_br('sh_ip_int_br.txt'))
			
