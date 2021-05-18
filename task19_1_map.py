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
			return result
	except (netmiko.NetmikoAuthenticationException, netmiko.NetmikoTimeoutException) as err:
		return err
	
#for threading
def ping_ip_addresses(ip_list, limit=3):
	with ThreadPoolExecutor(max_workers=3) as executor:
		result = executor.map(ping_ip, ip_list, repeat(device))
		for i in result:
			print('\n' + device['host'] + '\n===>\n' + i)
			
			
if __name__ == "__main__":
	with open("devices.yaml") as f:
		devices = yaml.safe_load(f)
	for device in devices:
		ping_ip_addresses(ip_set, limit=3)
			
