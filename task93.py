#!/usr/bin/env python3

def get_int_vlan_map(config_filename):
	dict_access = {}
	dict_trunk = {}
	with open(config_filename) as f:
		for line in f:
			if line.startswith('interface'):
				intf = line.split()
			if 'allowed vlan' in line:
				trunk_vlan = line.split()
				list_vlans = [int(i) for i in trunk_vlan[-1].split(',')]
				dict_trunk[intf[1]] = list_vlans
			if 'access vlan' in line:
				access_vlan = line.split()
				dict_access[intf[1]] = int(access_vlan[-1])
	return dict_trunk, dict_access
	
				
