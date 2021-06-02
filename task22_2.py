#!/usr/bin/env python3

import telnetlib
import time

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
		self.t.write(line.encode() + b'\n')
	def send_show_command(self, command):
		self._write_line(command)
		time.sleep(0.1)
		result = self.t.read_very_eager().decode("utf-8")
		print(result)
		
if __name__ == "__main__":
	r1_params = {
	    'ip': '192.168.100.1',
		'username': 'cisco',
	    'password': 'cisco',
	    'secret': 'cisco'}
