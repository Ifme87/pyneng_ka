#!/usr/bin/env python3

import ipaddress
import subprocess

checklist = ['8.8.8.8', '8.8.4.4', '192.168.0.1', '85.26.252.2', '10.1.1.1-10.1.1.2', '192.168.120.1-2']


def convert_ranges_to_ip_list(convert_list_ip):
	final_list = []
	for ip in convert_list_ip:
		if '-' in ip:
			check_1 = ip.split('.')
			if len(check_1) == 4:
				 range_values = check_1[3].split('-')
				 generate_ips = range(int(range_values[0]), (int(range_values[1]) + 1))
				 for i in generate_ips:
					 list_ips = '{}.{}.{}.{}'.format(check_1[0], check_1[1], check_1[2], i)
					 final_list.append(list_ips)	
			if len(check_1) > 4:
				ip_min_max = ip.split('-')
				ip_min = ip_min_max[0].split('.')
				ip_max = ip_min_max[1].split('.')
				generate_ips = range(int(ip_min[3]), (int(ip_max[3]) + 1))
				for i in generate_ips:
					 list_ips = '{}.{}.{}.{}'.format(ip_min[0], ip_min[1], ip_min[2], i)
					 final_list.append(list_ips)
		else:
			final_list.append(ip)
	return final_list
				 
def ping_ip_addresses(ip_list):
	unavailable_ips = ['unavalable:']
	available_ips = ['available:']
	preresult = []
	for ip in ip_list:
		vcheck = subprocess.run(['ping', '-c', '1', '-n', ip])
		if vcheck.returncode == 0:
			available_ips.append(ip)
		else:
			unavailable_ips.append(ip)
	preresult.append(available_ips)
	preresult.append(unavailable_ips)
	result = tuple(preresult)
	return result
	
for_ping_check = convert_ranges_to_ip_list(checklist)
print(ping_ip_addresses(for_ping_check))
			
	
