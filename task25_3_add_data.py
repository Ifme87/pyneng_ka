#!/usr/bin/env python3

import sqlite3
import os
import re
import glob 

connection = sqlite3.connect('dhcp_snooping.db')

#1
def insert_data_into_switches(data_file):
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
			print('Error while adding: {}'.format(row), error)
			
#2	
def insert_dhcp_snooping_data(file_to_parse): 
	regex_dhcp = re.compile('((?:\w+:)+(?:\w+)) +(\S+) .*(\S+) +(.*)\n')
	regex_dhcp_switchname = re.compile('(?:.*?\/)*(\S+?)_.*')
	result_dhcp = []
	hostname = regex_dhcp_switchname.match(file_to_parse)
	with open(file_to_parse) as f:
		for line in f:
			match = regex_dhcp.match(line)
			if match:
				result_dhcp.append(match.groups() + hostname.groups())
	print('Inserting DHCP Snooping data...')
	with connection:
		try:
			query = "update dhcp set active = '0' where switch = '{}'".format(hostname.group(1))
			connection.execute(query)
		except sqlite3.OperationalError as err:
			print('Error when choosing term', err)
	for row in result_dhcp:
		print('Successfully added! ', row)
		query = "insert or replace into dhcp (mac, ip, vlan, interface, switch, active) values (?, ?, ?, ?, ?, '1')"
		connection.execute(query, row)
	connection.commit()
		
					
#1
insert_data_into_switches('switches.yml')
dhcp_files = glob.glob('new_data/sw*_dhcp_snooping.txt')
for i in dhcp_files:
	#2
	insert_dhcp_snooping_data(i)


