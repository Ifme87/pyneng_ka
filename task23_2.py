#!/usr/bin/env python3

import telnetlib
import time
from textfsm import clitable
from pprint import pprint

class CiscoTelnet:
	def __init__(self, ip, username, password, secret):
		self.ip = ip
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
	def __enter__(self):
		return self
	def __exit__(self, exc_type, exc_values, traceback):
		self.t.close()
	def _write_line(self, line):
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
			
	def _check_errors(self, command):
		out = self.t.read_very_eager().decode("utf-8")
		err = None
		if 'Invalid input detected' in out:
			err = f"Command {command} executed with error 'Invalid input detected' on device {self.ip}"
		elif 'Incomplete command' in out:
			err = f"Command {command} executed with error 'Incomplete command' on device {self.ip}"
		elif 'Ambiguous command' in out:
			err = f"Command {command} executed with error 'Ambiguous command' on device {self.ip}"
		return (out, err)
		
	def _check_errors_strict(self, command):
		out = self.t.read_very_eager().decode("utf-8")
		if 'Invalid input detected' in out:
			raise ValueError(f"Command {command} executed with error 'Invalid input detected' on device {self.ip}")
		elif 'Incomplete command' in out:
			raise ValueError(f"Command {command} executed with error 'Incomplete command' on device {self.ip}")
		elif 'Ambiguous command' in out:
			raise ValueError(f"Command {command} executed with error 'Ambiguous command' on device {self.ip}")
		return out
		
	def send_config_commands(self, commands, strict=True):
		self._write_line('conf terminal')
		time.sleep(0.1)
		if type(commands) == list:
			checked_result = ''
			errors = ''
			for i in commands:
				if strict:
					self._write_line(i)
					time.sleep(0.1)
					out = self._check_errors_strict(i)
					checked_result = checked_result + out
				else:
					self._write_line(i)
					time.sleep(0.1)
					out, err = self._check_errors(i)
					checked_result = checked_result + out
					if err:
						errors = errors + err + '\n'
			if not len(errors) == 0:
				print(errors)
				print('\n')
			print(checked_result)	 
		else:
			if strict:
				self._write_line(commands)
				time.sleep(0.1)
				out = self._check_errors_strict(commands)
			else:
				self._write_line(commands)
				time.sleep(0.1)
				out, err = self._check_errors(commands)
				if err:
					print(err)
					print('\n')
			print(out)
		self._write_line('end')
		time.sleep(0.5)
		output = self.t.read_very_eager().decode("utf-8")
	
		print(output)
		
