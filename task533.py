#!/usr/bin/env python3

switchport = {
	"access": '''switchport mode access
switchport access vlan {}
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
		''',	
	"trunk": '''switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan {}
	''',
}

mode = {
	"access": 'Enter VLAN tag: ',	
	"trunk": 'Enter allowed VLAN(s): ',
}

var1 = input('Enter switchport mode (access/trunk): ')
var2 = input('Enter interface number: ')
var3 = input(mode[var1.lower()])
var4 = str(switchport[var1.lower()]).format(var3)

print('\n' + 'interface {}'.format(var2.lower()))
print(var4)
