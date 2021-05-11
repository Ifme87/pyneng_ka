#!/usr/bin/env python3

from pprint import pprint


def create_network_map(filenames):
	result = dict()
	interface_abbr = ['Fa ', 'Gi ', 'Te ', 'Po ', 'Eth ']
	lines_list = filenames.split('\n')
	for line in lines_list:			
#		insert HOSTNAME		
		if '>' in line:
			inxs = line.split('>')
			hostname = inxs[0]
			continue
		if '#' in line:
			inxs = line.split('#')
			hostname = inxs[0]
			continue
#		insert parameters
		for i in interface_abbr:
			if i in line:
				args = line.split()
				loc_intfs = args[1] + args[2]
				remote_intfs = args[-2] + args[-1]
				result.update({(hostname, loc_intfs): (args[0], remote_intfs)})
				break
	return result

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]


def parse_cdp_neighbors(command_output):
	result = dict()
	interface_abbr = ['Fa ', 'Gi ', 'Te ', 'Po ', 'Eth ']
	lines_list = command_output.split('\n')
	for line in lines_list:			
#		insert HOSTNAME		
		if '>' in line:
			inxs = line.split('>')
			hostname = inxs[0]
			continue
		if '#' in line:
			inxs = line.split('#')
			hostname = inxs[0]
			continue
#		insert parameters
		for i in interface_abbr:
			if i in line:
				args = line.split()
				loc_intfs = args[1] + args[2]
				remote_intfs = args[-2] + args[-1]
				result.update({(hostname, loc_intfs): (args[0], remote_intfs)})
				break
	return result
	
xxx = dict()
	
for f in infiles:
	with open(f) as dict_to_add:
		preresult = create_network_map(dict_to_add.read())
		xxx.update(preresult)
	
pprint(xxx)
