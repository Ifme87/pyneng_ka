#!/usr/bin/env python3

trunk_template = [
"switchport trunk encapsulation dot1q",
"switchport mode trunk",
"switchport trunk allowed vlan",
]

trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

for intf in trunk.keys():
	print("interface FastEthernet" + intf)
	var1 = trunk[intf]
	for command in trunk_template:
		if command.endswith("allowed vlan"):
			vlan = (',').join(var1[1::])
			if var1[0] == "add":
				print(f" {command} add {vlan}")
			if var1[0] == "only":
				print(f" {command} {vlan}")
			if var1[0] == "del":
				print(f" {command} remove {vlan}")
			else:
				continue
		else:
			print(f" {command}")
