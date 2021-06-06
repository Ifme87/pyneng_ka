#!/usr/bin/env python3

import telnetlib
import time
from textfsm import clitable
from pprint import pprint

class CiscoTelnet:
	def __init__(self, ip, username, password, secret):
		self.t = telnetlib.Telnet(ip)
		
		self.t.read_until(b"Username: ")
		self._write_line(username)
		
		self.t.read_until(b"Password: ")
		self._write_line(password)
		
		enable_status, m, output =self. t.expect([b'>', b'#'])
		if enable_status == 0:
			self._write_line('enable')
			self.t.read_until(b'Password')
			self._write_line(secret)
			self.t.read_until(b'#')
			
		self._write_line('terminal length 0')
		self.t.read_until(b'#')
	def _write_line(self, line):
		if type(line) == list:
			for command in line:
				self.t.write(command.encode() + b'\n')
				time.sleep(0.1)
		else:
			self.t.write(line.encode() + b'\n')
	def send_show_command(self, command, parse=True, templates='templates', index='index'):
		self._write_line(command)
		time.sleep(0.1)
		output = self.t.read_very_eager().decode("utf-8")
		if parse:
			cli = clitable.CliTable(index, templates)
			attr = {'Command': command,
					'Vendor': 'cisco_ios',
					}
			cli.ParseCmd(output, attr)
			out = []
			header = cli[0]
			for line in cli:
				dictionary = {}
				counter = 0
				for key in header:
					dictionary[key] = line[counter]
					counter += 1		
				out.append(dictionary)
			pprint(out)
		else:
			print(output)
			
	def send_config_commands(self, command):
		self._write_line('conf terminal')
		time.sleep(0.1)
		self._write_line(command)
		time.sleep(0.1)
		self._write_line('end')
		time.sleep(0.5)
		output = self.t.read_very_eager().decode("utf-8")
		return output
		
if __name__ == "__main__":
	r1_params = {
	    'ip': '10.0.0.100',
		'username': 'cisco',
	    'password': 'cisco',
	    'secret': 'cisco'}
