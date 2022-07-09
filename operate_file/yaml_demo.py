# coding:utf8
# PyYAML
#   https://github.com/yaml/pyyaml
#   pip install pyyaml

from collections import OrderedDict

import yaml


def yml_load(yml_file):
    yaml.add_constructor('tag:yaml.org,2002:map', lambda loader, node: OrderedDict(loader.construct_pairs(node)))
    with open(yml_file, 'r') as fp:
        return yaml.load(fp, Loader=yaml.SafeLoader)


class MyDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)


def yml_dump(data, yml_file):
    yaml.add_representer(OrderedDict, lambda dumper, dict_data: dumper.represent_dict(dict_data.items()))
    with open(yml_file, "w") as fp:
        yaml.dump(data, fp, Dumper=MyDumper, default_flow_style=False)
