#!/usr/bin/env python3

f = open('task722.txt')
var = f.readlines()
ignore = ["duplex", "alias", "configuration"]

for line in var:
	if line[0] != '!':
		if line.find(ignore[0]) == -1:
			if line.find(ignore[1]) == -1:
				if line.find(ignore[2]) == -1: 
					print(line.rstrip())
	else:
		continue
		


#for inx in [0,1,2,3,4,5]:
#	line = var[inx].split()
#	prefix = line[1] 
#	metric = (line[2])[:-1][1:]
#	next_hop = (line[4])[:-1]
#	last_upd = (line[5])[:-1]
#	outbound_int = line[6]
#	print(f"{'Prefix':<20}{prefix}")
#	print(f"{'AD/Metric':<20}{metric}")
#	print(f"{'Next-Hop':<20}{next_hop}")
#	print(f"{'Last Update':<20}{last_upd}")
#	print(f"{'Outbound Interface':<20}{outbound_int}" + '\n')
