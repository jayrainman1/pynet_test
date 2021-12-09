#!/usr/bin/env python
import yaml 
from rich import print


def read_yaml(filename):
    with open(filename) as f:
        return yaml.safe_load(f)


if __name__ =="__main":
    filename ="yaml.ex2.yaml"
    print(read_yaml(filename))

