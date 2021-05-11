#!/usr/bin/env python3

from pprint import pprint

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
	
if __name__ == "__main__":
    with open("sh_cdp_n_r3.txt") as f:
        pprint(parse_cdp_neighbors(f.read()))
