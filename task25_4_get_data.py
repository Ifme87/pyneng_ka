#!/usr/bin/env python3

import sqlite3, os, re, sys
from pprint import pprint


db_filename = 'dhcp_snooping.db'
connection = sqlite3.connect(db_filename)
keys = ['mac', 'ip', 'vlan', 'interface', 'switch', 'active']


#if 2 args
def get_data(connection):	
	try:
		with connection:
			connection.execute(query, (value, )) 
	except sqlite3.IntegrityError as e:
		print ('Error occured while adding data: ', e)
	for row in connection.execute(query, (value, )):
		print(row)
	connection.close()
	

#if no args
def get_all_data(connection):
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
	
###Check block for entered arguments and run functions:

try:
	key = sys.argv[1]
	if not key in keys:
		print('No such key. Possible values: mac, ip, vlan, interface, switch')
		exit()
	try:
		value = sys.argv[2]
		query = 'select * from dhcp where {} = ?'.format(key)
		get_data(connection)
	except IndexError:
		print('Enter 0 or 2 args')
		exit()
except IndexError:
	query_active = "select * from dhcp where active = '1'"
	query_inactive = "select * from dhcp where active = '0'"
	get_all_data(connection)	
if len(sys.argv) > 3:
	print('Entered more than 2 args')
	exit()

