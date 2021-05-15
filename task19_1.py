#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from itertools import repeat
import logging, yaml, netmiko

ip_set = ['8.8.8.8', '10.12.2.3']

#for 1 ip ping DONE!
def ping_ip(ip, device):
	try:
		with netmiko.ConnectHandler(**device) as ssh:
			ssh.enable()
			result = ssh.send_command_timing(f'ping {ip} repeat 1')
			return result
	except (netmiko.NetmikoAuthenticationException, netmiko.NetmikoTimeoutException) as err:
		return err
	
#for threading
def ping_ip_addresses(ip_list, limit=3):
	with ThreadPoolExecutor(max_workers=limit) as executor:
		future_var = executor.submit(ping_ip, ip, device)
		for f in as_completed([future_var]):
			print(f.result())
			
			
if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
for dev in devices:
	for ip in ip_set:
		print(ping_ip(ip, dev))
	
