#!/usr/bin/env python3

import sqlite3
import os

db_exists = os.path.exists('dhcp_snooping.db') 

if not db_exists:
	connection = sqlite3.connect('dhcp_snooping.db')
	print('Creating schema...')
	with open('dhcp_snooping_schema.sql') as f:
		schema = f.read()
		connection.executescript(schema)
	print('Done')
	connection.close()
else:
	print('Database exists')
	
