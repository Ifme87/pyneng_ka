#!/usr/bin/env python3

import re
from pprint import pprint


def convert_ios_nat_to_asa(nat_ios, nat_asa):
	result = []
	with open(nat_ios) as f:
		with open(nat_asa, 'w') as w:
			for line in f:
				match = re.sub('.*tcp (\w+\.\w+\.\w+\.\w+) (\w+).* (\w+)',
							   'object network LOCAL_\\1\n'
							   ' host \\1\n'
							   ' nat (inside, outside) static interface service tcp'
							   ' \\2 \\3', line)
				if match:
					w.write(match)
		
		
convert_ios_nat_to_asa('cisco_nat_config.txt', 'cisco_asa_config.txt')
			
