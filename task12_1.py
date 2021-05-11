#!/usr/bin/env python3

import ipaddress
import subprocess

checklist = ['8.8.8.8', '8.8.4.4', '192.168.0.1', '85.26.252.2']

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
	
print(ping_ip_addresses(checklist))
			
	
