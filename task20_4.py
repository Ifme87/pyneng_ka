#!/usr/bin/env python3

import yaml
from pprint import pprint
from jinja2 import Environment, FileSystemLoader
from task20_1 import generate_config


if __name__ == "__main__":
    data_file = "data_files/add_vlan_to_switch.yaml"
    template_file = "templates/add_vlan_to_switch.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
        print(generate_config(template_file, data))
