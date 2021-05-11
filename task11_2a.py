#!/usr/bin/env python3

from pprint import pprint
import sys

try:
    import graphviz as gv
except ImportError:
    print("Module graphviz needs to be installed")
    print("pip install graphviz")
    sys.exit()
    
styles = {
    "graph": {
        "label": "Network Map",
        "fontsize": "16",
        "fontcolor": "white",
        "bgcolor": "#333333",
        "rankdir": "BT",
    },
    "nodes": {
        "fontname": "Helvetica",
        "shape": "box",
        "fontcolor": "white",
        "color": "#006699",
        "style": "filled",
        "fillcolor": "#006699",
        "margin": "0.4",
    },
    "edges": {
        "style": "dashed",
        "color": "green",
        "arrowhead": "open",
        "fontname": "Courier",
        "fontsize": "14",
        "fontcolor": "white",
    },
}


def apply_styles(graph, styles):
    graph.graph_attr.update(("graph" in styles and styles["graph"]) or {})
    graph.node_attr.update(("nodes" in styles and styles["nodes"]) or {})
    graph.edge_attr.update(("edges" in styles and styles["edges"]) or {})
    return graph
      

def unique_network_map(topology_dict):
	unique_result = dict()
	last_value = []
	for item in topology_dict.items():
		if item[0] in topology_dict.values(): 
			if not item[0] in last_value:
				last_value.append(item[1])
				continue
			else:
				unique_result.update({item})
		else:
			unique_result.update({item})
	return unique_result


def draw_topology(topology_dict, output_filename="img/topology"):
    """
    topology_dict - словарь с описанием топологии
    Этот словарь
        {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
         ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}
    соответствует топологии:
    [ R5 ]-Fa0/1 --- Fa0/1-[ R4 ]-Fa0/2---Fa0/0-[ R6 ]
    Функция генерирует топологию, в формате svg.
    И записывает файл topology.svg в каталог img.
    """
    nodes = set(
        [item[0] for item in list(topology_dict.keys()) + list(topology_dict.values())]
    )

    g1 = gv.Graph(format="svg")

    for node in nodes:
        g1.node(node)

    for key, value in topology_dict.items():
        head, t_label = key
        tail, h_label = value
        g1.edge(head, tail, headlabel=h_label, taillabel=t_label, label=" " * 12)

    g1 = apply_styles(g1, styles)
    filename = g1.render(filename=output_filename)
    print("Graph saved in", filename)


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
	
topology = dict()
	
for f in infiles:
	with open(f) as dict_to_add:
		preresult = create_network_map(dict_to_add.read())
		topology.update(preresult)
	
to_draw = pprint(unique_network_map(topology))
draw_topology(to_draw)
