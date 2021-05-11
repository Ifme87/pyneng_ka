#!/usr/bin/env python3

from pprint import pprint

def ignore_command(command, ignore):
	ignore_status = False
	for word in ignore:
		if word in command:
			ignore_status = True
	return ignore_status
			
def convert_config_to_dict(config_filename):
	full_config = dict()
	ignore = ["duplex", "alias", "configuration"]
	with open(config_filename) as f:
		for line in f:
			ignore_next = ignore_command(line, ignore)
			if not '!' in line and ignore_next == False:
				if line.startswith(' '):
					list_of_keys = list(full_config.keys())
					full_config[(list_of_keys[-1]).strip()].append(line.strip())
					del list_of_keys
				else:
					full_config.update({line.strip():[]})			
		return full_config
		
result = convert_config_to_dict('config_sw1.txt')

for v in result.values():
	for i in v:
		"{:<20}".format(i)
		
pprint(result, sort_dicts=False)

	
