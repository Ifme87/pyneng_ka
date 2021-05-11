#!/usr/bin/env python3

trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

trunk_config_2 = {
    "FastEthernet0/11": [120, 131],
    "FastEthernet0/15": [111, 130],
    "FastEthernet0/14": [117],
}

def generate_trunk_config(intf_vlan_mapping, trunk_template):
	lines = {}
	commands = []
	for intf, vlan in intf_vlan_mapping.items():
		lines[intf] = commands
		for command in trunk_template:
			if command.endswith('allowed vlan'):
				vlan_nums = [str(i) for i in vlan]
				commands.append(f"{command} {', '.join(vlan_nums)}") 
			commands.append(command)
	return lines
	
print(generate_access_config(access_config, access_mode_template))
		
