#!/usr/bin/env python3

import sqlite3, os, re, sys
from pprint import pprint

db_filename = 'dhcp_snooping.db'
connection = sqlite3.connect(db_filename)
keys = ['mac', 'ip', 'vlan', 'interface', 'switch']


def get_data(connection):	
	try:
		with connection:
			connection.execute(query, (value, )) 
	except sqlite3.IntegrityError as e:
		print ('Error occured while adding data: ', e)
	for row in connection.execute(query, (value, )):
		print(row)
	connection.close()
	

def get_all_data(connection):	
	try:
		with connection:
			connection.execute(query) 
	except sqlite3.IntegrityError as e:
		print ('Error occured while adding data: ', e)
	for row in connection.execute(query):
		print(row)
	connection.close()
	
	
###Entered arguments check:

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
	#print('Whole table selected')
	query = 'select * from dhcp'
	get_all_data(connection)	
if len(sys.argv) > 3:
	print('Entered more than 2 args')
	exit()



