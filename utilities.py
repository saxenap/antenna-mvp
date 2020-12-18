import os, sys
import pprint
from tabulate import tabulate 
from IPython.display import display, HTML
import yaml


def save_file(file_path, content):
  os.makedirs(os.path.dirname(file_path), exist_ok=True)
  with open(file_path, "w") as f:
    f.write(content)

def dict_output(data):
    print(yaml.dump(data, allow_unicode=True, default_flow_style=False))

# def output(data):
#     print(pprint.pformat(data))


def output(data):
    display(data)
    

def doutput(data):
    print(tabulate(data, showindex=True, headers='keys', tablefmt='pretty'))