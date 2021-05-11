#!/usr/bin/env python3

def get_int_vlan_map(config_filename):
	dict_access = {}
	dict_trunk = {}
	native_vlan = False
	with open(config_filename) as f:
		for line in f:
			if line.startswith('interface'):
				if 'Vlan' in line:
					continue
				intf = line.split()
			if 'access vlan' in line:
				native_vlan = False		
				access_vlan = line.split()
				dict_access[intf[1]] = int(access_vlan[-1])
			if native_vlan:
				dict_access[intf[1]] = 1
			if 'allowed vlan' in line:
				trunk_vlan = line.split()
				list_vlans = [int(i) for i in trunk_vlan[-1].split(',')]
				dict_trunk[intf[1]] = list_vlans
			if 'mode access' in line:
				native_vlan = True	
	return dict_trunk, dict_access
	
				
