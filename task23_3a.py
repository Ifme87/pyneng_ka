#!/usr/bin/env python3

from task17_3b import unique_network_map
from pprint import pprint

class Topology:
	def __init__(self, dic):
		self.topology = self._normalize(dic)
	def __add__(self, otherself):
		self.summ = {}
		self.summ.update(self.topology)
		self.summ.update(otherself.topology)
		return Topology(self.summ)
	def __iter__(self):
		#i = iter(self.topology.items())
		self._index = -1
		return self
	def __next__(self):
		self._index += 1
		try:
			i = list(self.topology.items())
			return i[self._index]
		except IndexError:
			raise StopIteration
	def _normalize(self, dic):
		return unique_network_map(dic)
	def delete_link(self, link1, link2):
		if link1 in self.topology.keys():
			if self.topology[link1] == link2:
				del self.topology[link1]
		elif link2 in self.topology.keys():
			if self.topology[link1] == link2:
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
	def add_link(self, link1, link2):
		if link1 in self.topology.keys() or link1 in self.topology.values():
			if self.topology.get(link1) == link2:
				print('Connection exists')
			else:
				print('Connection with one of the ports exists')
		elif link2 in self.topology.keys() or link2 in self.topology.values():
			if self.topology.get(link2) == link1:
				print('Connection exists')
			else:
				print('Connection with one of the ports exists')				
		else:
			self.topology[link1] = link2
			
	
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

topology_example2 = {('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
                     ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}


t1 = Topology(topology_example)
t2 = Topology(topology_example2)
t3 = t1+t2
for i in t2:
	print(i)
