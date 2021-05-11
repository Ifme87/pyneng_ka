#!/usr/bin/env python3

import csv
import re


def write_dhcp_snooping_to_csv(filenames, output):
	with open(output, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(('switch', 'mac', 'ip', 'vlan', 'interface'))
		with open(filenames) as file_to_parse:
			for prerow in file_to_parse:
				match = re.match('(\w+:)+\w+.*', prerow)
				if match:
					row = prerow.split()
					del row[2]
					del row[2]
					switch_name = re.match('(.*?)_', filenames)
					row.insert(0, switch_name.group(1))
					writer.writerow(row)
		
	
write_dhcp_snooping_to_csv('sw1_dhcp_snooping.txt', 'result_csv.csv')
#write_dhcp_snooping_to_csv('sw2_dhcp_snooping.txt', 'result_csv.csv')
#write_dhcp_snooping_to_csv('sw3_dhcp_snooping.txt', 'result_csv.csv')
