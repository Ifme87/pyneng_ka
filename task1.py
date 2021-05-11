#!/usr/bin/env python3

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}


var1 = input('Zhelezka:')
var2 = sorted(london_co[var1])
var3 = input("Parameter {0} :".format(var2))
var4 = var3.lower()

if var4 in var2:
	print(london_co[var1][var4])
else:
	print("Net takogo")

