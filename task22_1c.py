#!/usr/bin/env python3

from task17_3b import unique_network_map

class Topology:
	def __init__(self, dic):
		self.topology = self._normalize(dic)
	def _normalize(self, dic)
		return unique_network_map(dic)
	def delete_link(self, link1, link2)
		if link1 in self.topology.keys():
			if self.topology[link1] = link2
				del self.topology[link1]
		elif link2 in self.topology.keys():
			if self.topology[link1] = link2
				del self.topology[link2]
		else:
			print('No such link') 
	def delete_node(self, node):
		items_to_delete = []
		for item in self.topology.items():
			if node in item[0] or node in item[1]:
				items_to_delete.append(item[0])
		if len(items_to_delete) == 0:
			print('No such device')
		else:
			for key in items_to_delete:
				del self.topology[key]
					
		
	
topology_example = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
}
