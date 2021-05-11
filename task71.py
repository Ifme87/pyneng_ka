#!/usr/bin/env python3

f = open('task711.txt')
var = f.readlines()

for inx in [0,1,2,3,4,5]:
	line = var[inx].split()
	prefix = line[1] 
	metric = (line[2])[:-1][1:]
	next_hop = (line[4])[:-1]
	last_upd = (line[5])[:-1]
	outbound_int = line[6]
	print(f"{'Prefix':<20}{prefix}")
	print(f"{'AD/Metric':<20}{metric}")
	print(f"{'Next-Hop':<20}{next_hop}")
	print(f"{'Last Update':<20}{last_upd}")
	print(f"{'Outbound Interface':<20}{outbound_int}" + '\n')
