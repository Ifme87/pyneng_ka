#!/usr/bin/env python3

entered_vlan = input('Enter VLAN: ')

with open('CAM_table.txt') as f:
	vlans = []
	for line in f:
		splitted_line = line.split()
		if len(splitted_line) == 0:
			continue
		elif splitted_line[0].isdigit() == False:
			continue
		else:
			vlans.append(int(splitted_line[0]))

	vlans.sort()
	
with open('CAM_table.txt') as f:
	for line in f:
		splitted_line = line.split()
		if len(splitted_line) == 0:
			continue
		elif splitted_line[0].isdigit() == False:
			continue
		elif entered_vlan == splitted_line[0]:
			print(f"{splitted_line[0]:<20}{splitted_line[1]:<20}{splitted_line[3]:<20}")
			continue
		
#	print(f"{'Prefix':<20}{prefix}")
#	print(f"{'AD/Metric':<20}{metric}")
#	print(f"{'Next-Hop':<20}{next_hop}")
#	print(f"{'Last Update':<20}{last_upd}")
#	print(f"{'Outbound Interface':<20}{outbound_int}" + 
