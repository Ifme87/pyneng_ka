#!/usr/bin/env python3

import sqlite3, os, re, glob
from datetime import timedelta, datetime 

now = datetime.today().replace(microsecond=0)
week_ago = now - timedelta(days=5)


###FUNCTIONS
	
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
	try:
		query = "update dhcp set active = '0' where switch = '{}'".format(hostname.group(1))
		connection.execute(query)
	except sqlite3.OperationalError as err:
		print('Error when inserting term', err)
	for row in result_dhcp:
		query = '''insert or replace into dhcp (mac, ip, vlan, interface, switch, active, last_active) 
				   values (?, ?, ?, ?, ?, '1', datetime('now'))'''
		connection.execute(query, row)
	print('All lines successfully added!')
		
#3
def del_old_inactive(connection):
	now = datetime.today().replace(microsecond=0)
	week_ago = now - timedelta(days=7)
	del_old = "DELETE from dhcp WHERE last_active < '{}'".format(week_ago)
	connection.execute(del_old)
	print('Older that week old data deleted!')
	
###################################################################
		
if __name__ == "__main__":
	connection = sqlite3.connect('dhcp_snooping.db')
	dhcp_files = glob.glob('new_data/sw*_dhcp_snooping.txt')
#1
	insert_data_into_switches('switches.yml')
#2	
	for i in dhcp_files:
		insert_dhcp_snooping_data(i)
#3	
	del_old_inactive(connection)
	
	connection.commit()
	connection.close()



