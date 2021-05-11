#!/usr/bin/env python3

import pexpect, telnetlib, paramiko
import yaml
import re, time
from pprint import pprint
from netmiko import ( 
	ConnectHandler,
	NetmikoTimeoutException,
	NetmikoAuthenticationException,
)


def send_show_command(device, command):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname=device['host'], username='cisco', password='cisco', look_for_keys=False,
				   allow_agent=False)
		
	with client.invoke_shell() as ssh:
		time.sleep(0.5)
		ssh.send('enable\n')
		time.sleep(0.5)
		ssh.send('cisco\n')
		time.sleep(0.5)
		ssh.send('terminal length 0\n')
		time.sleep(0.5)
		ssh.recv(300)
		time.sleep(0.5)
		ssh.send(command + '\n')
		time.sleep(1)
		result = ssh.recv(2000).decode('ascii')
		return result
		

	
	
if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        
    #print(devices)

    for dev in devices:
        print(send_show_command(dev, command))

	
	
	
	
	
	
	
	
	
	
	
	
	
'''	with telnetlib.Telnet(device) as t:
		t.read_until(b"Username: ")
		t.write(b'cisco\n')
		
		t.read_until(b"Password: ")
		t.write(b'cisco\n')
			
		enable_status, m, output = t.expect([b'>', b'#'])
		if enable_status == 0:
			t.write(b'enable\n')
			t.read_until(b'Password')
			t.write(b'cisco\n')
			t.read_until(b'#')
			
		t.write(b'terminal length 0\n')
		t.read_until(b'#')
		
		t.write(b'sh clock\n')
		time.sleep(0.1)
		t.write(command + b'\n')
		time.sleep(0.1)
		result = t.read_very_eager().decode("utf-8")
		
		print(result)

device = '10.0.0.254'
command = b'show ip inter bri'
send_show_command(device, command)

'''
