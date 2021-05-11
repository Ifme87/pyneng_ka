#!/usr/bin/env python3

f = open('CAM_table.txt')
var = f.readlines()
inx = 6
cicle = False

while not cicle: 
	try: 
		line = var[inx].split() 
		print(f"{line[0]:<20}{line[1]:<20}{line[3]:<20}")	
		inx += 1
	except IndexError:
		cicle = True
		
#	print(f"{'Prefix':<20}{prefix}")
#	print(f"{'AD/Metric':<20}{metric}")
#	print(f"{'Next-Hop':<20}{next_hop}")
#	print(f"{'Last Update':<20}{last_upd}")
#	print(f"{'Outbound Interface':<20}{outbound_int}" + 
