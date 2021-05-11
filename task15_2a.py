#!/usr/bin/env python3

import re
from pprint import pprint

headers_list = ["hostname", "ios", "platform"]

data_list = [
	("R1", "12.4(24)T1", "Cisco 3825"),
	("R2", "15.2(2)T1", "Cisco 2911"),
	("SW1", "12.2(55)SE9", "Cisco WS-C2960-8TC-L"),
]


def convert_to_dict(headers, data):
	result = []	
	for router in data:
		dictionary = dict.fromkeys(headers)
		i = 0
		for key in dictionary:
			dictionary[key] = router[i]
			i += 1
		result.append(dictionary)
	return result 
	 
	
pprint(convert_to_dict(headers_list, data_list))
			
