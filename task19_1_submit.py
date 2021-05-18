#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from itertools import repeat
import logging, yaml, netmiko
from pprint import pprint

logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)


ip_set = ['8.8.8.8', '10.10.10.10', '4.4.4.4']

#for 1 ip ping DONE!
def ping_ip(ip, device):
	try:
		with netmiko.ConnectHandler(**device) as ssh:
			ssh.enable()
			result = ssh.send_command_timing(f'ping {ip} repeat 1')
			if 'Success rate is 0' in result:
				unpingable_ips.append(ip)
			else:
				pingable_ips.append(ip)
	except (netmiko.NetmikoAuthenticationException, netmiko.NetmikoTimeoutException) as err:
		return err	
	return result
	 
#for threading
def ping_ip_addresses(ip_list, limit=3):
	with ThreadPoolExecutor(max_workers=limit) as executor:
		future_var = []
		for ip in ip_list:
			future_var.append(executor.submit(ping_ip, ip, device))
			
#do result with set, as its takes only unique values
		
if __name__ == "__main__":
	with open("devices.yaml") as f:
		devices = yaml.safe_load(f)
	pingable_ips = []
	unpingable_ips = []	
	for device in devices:
		ping_ip_addresses(ip_set, limit=3)
		print('done for particular device')
		break
	fin = (pingable_ips, unpingable_ips)
	pprint(fin)
		
