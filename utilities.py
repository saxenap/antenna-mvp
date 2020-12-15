import os, sys
import pprint
from tabulate import tabulate 

def save_file(file_path, content):
  os.makedirs(os.path.dirname(file_path), exist_ok=True)
  with open(file_path, "w") as f:
    f.write(content)

def fileprint(data):
  return pprint.pformat(data)

def output(data):
    print(fileprint(data))

def tprint(data):
    print(tabulate(data, showindex=True, headers='keys', tablefmt='pretty'))