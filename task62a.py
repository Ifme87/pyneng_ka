#!/usr/bin/env python3

#import sys

### Variables here

ip = input('Enter IP for analisys (x.x.x.x): ')
octets = ip.split('.')

### Check ip 

ip_correct = False

while not ip_correct:
	for inx in [0, 1, 2, 3]:
		if not len(octets) == 4:
			print('Incorrect IP format, correct is X.X.X.X')
			ip = input('Enter IP with 4 octets (x.x.x.x): ')
			octets = ip.split('.')
			break
		elif not octets[inx].isdigit():
			print('Octets should include digits only!')
			ip = input('Enter IP with digits and dots (x.x.x.x): ')
			octets = ip.split('.')
			break
		elif not int(octets[inx]) in range(0, 256): 
			print('Octets should be in range from 0 to 255!')
			ip = input('Enter IP with octets in correct range (x.x.x.x): ')
			octets = ip.split('.')
			break
	else:
		ip_correct = True
		
### Classification
		
if int(octets[0]) >= 1 and int(octets[0]) <= 223:
	print('\n' + 'unicast' + '\n')
elif int(octets[0]) >= 224 and int(octets[0]) <= 239:
	print('\n' + 'multicast' + '\n')
elif octets == ['255', '255', '255', '255']:
	print('\n' + "local broadcast" + '\n')
elif octets == ['0','0','0','0']:
	print('\n' + "unassigned" + '\n')
else:
	print('\n' + "unused" + '\n')
		
