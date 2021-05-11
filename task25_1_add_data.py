#!/usr/bin/env python3

import sqlite3
import os
import re

connection = sqlite3.connect('dhcp_snooping.db')


def insert_data_into_switches(data_file): #'switches.yml'
	regex_switches = re.compile(' +(\S+): (.*)')
	result_switches = []

	with open(data_file) as f:
		for line in f:
			match = regex_switches.match(line)
			if match:
				result_switches.append(match.groups())
		
	print('Inserting switches data...')
	for row in result_switches:
		try:
			with connection:
				query = '''insert into switches (hostname, location) values (?, ?)'''
				connection.execute(query, row)
		except sqlite3.IntegrityError as error:
			print('While adding: {} Error occupied: '.format(row), error)
			
	
def insert_dhcp_snooping_data(file_to_parse): #sw1_dhcp_snooping.txt F.E.
	regex_dhcp = re.compile('((?:\w+:)+(?:\w+)) +(\S+) .*(\S+) +(.*)\n')
	regex_dhcp_switchname = re.compile('(\S+?)_')
	result_dhcp = []
	hostname = regex_dhcp_switchname.match(file_to_parse) 
	with open(file_to_parse) as f:
		for line in f:
			match = regex_dhcp.match(line)
			if match:
				result_dhcp.append(match.groups() + hostname.groups())
	print('Inserting DHCP Snooping data...')
	for row in result_dhcp:
		try:
			with connection:
				query = '''insert into dhcp (mac, ip, vlan, interface, switch) values (?, ?, ?, ?, ?)'''
				connection.execute(query, row)
		except sqlite3.IntegrityError as error:
			print('While adding: {} Error occupied: '.format(row), error)
	


if __name__ == "__main__":
	insert_data_into_switches('switches.yml')
	dhcp_files = ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
	for i in dhcp_files:
		insert_dhcp_snooping_data(i)


