#!/usr/bin/env python3

var1 = input('Enter IP for analisys (x.x.x.x): ')
var2 = var1.split('.')

if int(var2[0]) >= 1 and int(var2[0]) <= 223:
	print('unicast')
elif int(var2[0]) >= 224 and int(var2[0]) <= 239:
	print('multicast')
elif var2 == ['255', '255', '255', '255']:
	print("local broadcast")
elif var2 == ['0','0','0','0']:
	print("unassigned")
else:
	print("unused")
		
