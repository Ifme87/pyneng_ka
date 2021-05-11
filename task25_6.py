#!/usr/bin/env python3

import sqlite3, os, re, glob
from datetime import timedelta, datetime


def create_db(db_name, db_schema):
	db_exists = os.path.exists(db_name) 
	if not db_exists:
		connection = sqlite3.connect(db_name)
		print('Creating schema...')
		with open(db_schema) as f:
			schema = f.read()
			connection.executescript(schema)
		print('Done')
		connection.close()
	else:
		print('Database exists')
				
				
def add_data_switches(db_file, filename):
	for fn in filename:
		regex_switches = re.compile(' +(\S+): (.*)')
		result_switches = []
		with open(fn) as f:
			for line in f:
				match = regex_switches.match(line)
				if match:
					result_switches.append(match.groups())
		print('Inserting switches data...')
		connection = sqlite3.connect(db_file)
		with connection:
			for row in result_switches:
				try:
					query = '''insert into switches (hostname, location) values (?, ?)'''
					connection.execute(query, row)
				except sqlite3.IntegrityError as error:
					print('Error while adding: {}'.format(row), error)
		#connection.commit()
		connection.close()		


def del_old_inactive(connection):
	now = datetime.today().replace(microsecond=0)
	week_ago = now - timedelta(days=7)
	del_old = "DELETE from dhcp WHERE last_active < '{}'".format(week_ago)
	connection.execute(del_old)
	print('Older that week old data deleted!')

			
def add_data(db_file, filename):
	for fn in filename:
		regex_dhcp = re.compile('((?:\w+:)+(?:\w+)) +(\S+) .*(\S+) +(.*)\n')
		regex_dhcp_switchname = re.compile('(?:.*?\/)*(\S+?)_.*')
		result_dhcp = []
		hostname = regex_dhcp_switchname.match(fn)
		with open(fn) as f:
			for line in f:
				match = regex_dhcp.match(line)
				if match:
					result_dhcp.append(match.groups() + hostname.groups())
		print('Inserting DHCP Snooping data...')
		connection = sqlite3.connect(db_file)
		with connection:
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
		del_old_inactive(connection)
		connection.commit()
		connection.close()
	

def get_data(db_filename, key, value):
	query = 'select * from dhcp where {} = ?'.format(key)
	connection = sqlite3.connect(db_filename)
	try:
		with connection:
			connection.execute(query, (value, )) 
	except sqlite3.IntegrityError as e:
		print ('Error occured while adding data: ', e)
	for row in connection.execute(query, (value, )):
		print(row)
	connection.close()
	
	
def get_all_data(db_filename):
	query_active = "select * from dhcp where active = '1'"
	query_inactive = "select * from dhcp where active = '0'"	
	connection = sqlite3.connect(db_filename)
	with connection:	
		#show active mac
		try:
			connection.execute(query_active)
		except sqlite3.IntegrityError as e:
			print ('Error occured while adding data: ', e)
		print('Active mac: ')
		print('-' * 80)
		for row in connection.execute(query_active):
			print(row)
		#show inactive mac
		try:	
			connection.execute(query_inactive)
		except sqlite3.IntegrityError as e:
			print ('Error occured while adding data: ', e)
		#check if there no inactive and don\t show 'inactive mac' header
		check_if_no_inactives = []
		for row in connection.execute(query_inactive):
			check_if_no_inactives.append(row)
		if len(check_if_no_inactives) > 0:
			print('\n' + 'Inactive mac: ')
			print('-' * 80)
			for row in connection.execute(query_inactive):
				print(row)
	connection.close()
