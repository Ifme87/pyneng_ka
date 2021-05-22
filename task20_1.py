#!/usr/bin/env python3

import yaml
from pprint import pprint
from jinja2 import Environment, FileSystemLoader


def generate_config(template, data_dict):
	template_parse = template.split('/')
	template_dir = '/'.join(template_parse[:(-1)])
	env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True)
	template = env.get_template(template_parse[-1])
	return template.render(data_dict)

if __name__ == "__main__":
    data_file = "data_files/for.yml"
    template_file = "templates/for.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
        print(generate_config(template_file, data))
