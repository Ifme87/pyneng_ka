#!/usr/bin/env python3

import ipaddress

class IPAddress:
	def __init__(self, ip):
		ip_add, mask = self._check_ip(ip)
		self.ip = ip_add
		self.mask = mask
	def __str__(self):
		return f"IP address {self.ip}/{self.mask}"
	def __repr__(self):
		return f"IPAddress('{self.ip}/{self.mask}')"
	def _check_ip(self, ip):
		ip_mask = ip.split('/')
		octets = ip_mask[0].split('.')
		if not len(octets) == 4:
			raise ValueError('Incorrect IPv4 address')
		for inx in [0,1,2,3]:
			if not octets[inx].isdigit() or not int(octets[inx]) in range(0, 256): 
				raise ValueError('Incorrect IPv4 address')
		if not ip_mask[1].isdigit() or not int(ip_mask[1]) in range(0, 33):
			raise ValueError('Incorrect mask')
		return ip_mask[0], ip_mask[1] 
		
if __name__ == "__main__":
	ip_test = IPAddress('10.0.0.1/21')
	str(ip_test)
	print(ip_test)
	ip_test
	
	ip_list = []
	ip_list.append(ip_test)
	print(ip_list)
