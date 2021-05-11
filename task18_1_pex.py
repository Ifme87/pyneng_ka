#!/usr/bin/env python3

import pexpect
import yaml
import re, time
from pprint import pprint


def send_show_command(device, command):
	with pexpect.spawn(f"ssh cisco@{device}", timeout=10, encoding="utf-8") as ssh:
		
		ssh.expect('[Pp]assword')
		ssh.sendline('cisco')
		#ssh.before
	
		enable_status = ssh.expect(['>', '#'])
		if enable_status == 0:
			ssh.sendline('enable')
			ssh.expect('[Pp]assword')
			ssh.sendline('cisco')
			ssh.expect('#')
			#ssh.before
			
		ssh.sendline("terminal length 0")
		ssh.expect('#')
		#ssh.before	
			
		result = ''	
		ssh.sendline('sh clock')
		ssh.expect('#')
		result += ssh.before
		
		ssh.sendline(command)
		ssh.expect('#')
		result += ssh.before
		
		print(result)
		ssh.close()

device = '10.0.0.254'
command = 'show ip inter bri'
send_show_command(device, command)


'''if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_show_command(dev, command))
'''
