#!/usr/bin/env python3

from task24_2d import MyNetmiko
from pprint import pprint

device_params = {
    "device_type": "cisco_ios",
    "ip": "10.0.0.100",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
    }

r1 = MyNetmiko(**device_params)

#commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console", "lo"]

#print(r1.send_config_set('lo'))
#print('\n'*3)
#print(r1.send_config_set('lo', ignore_errors=True))
#print('\n'*3)
print(r1.send_config_set('lo', ignore_errors=False))
