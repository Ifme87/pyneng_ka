#!/usr/bin/env python3

import csv
import re
import glob

sh_version_files = glob.glob("sh_vers*")
headers = ["hostname", "ios", "image", "uptime"]

def parse_sh_version(sh_version):
	regex = re.compile('.*? Version (.*?),'
					   '.*?uptime is (.*?)\n'
					   '.*?image file is "(.*?)".*', re.DOTALL)
	with open(sh_version) as f:
		line = f.read()
		match = re.match(regex, line)
		result = match.group(1,3,2)
	return result
	
	
def write_inventory_to_csv(data_filenames, csv_filename):
	regex = re.compile('sh_version_(.+?).txt')
	with open(csv_filename, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(headers)
		for i in data_filenames:
			data = parse_sh_version(i)
			host_name = re.match(regex, i)
			result = list(host_name.groups())
			result.extend(data)
			writer.writerow(result)
		

write_inventory_to_csv(sorted(sh_version_files), 'task17_2_result.csv')
