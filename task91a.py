#!/usr/bin/env python3

access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]

def generate_access_config(intf_vlan_mapping, access_template, psecurity=False):
	lines = []
	for intf, vlan in intf_vlan_mapping.items():
		lines.append(f'interface {intf}')
		for i in access_template:
			if i.endswith('vlan'):
				i = f"{i} {vlan}"
			lines.append(i)
		if psecurity:
			for portsec_lines in port_security_template:
				lines.append(portsec_lines)
	return lines
	
print(generate_access_config(access_config, access_mode_template))
		
