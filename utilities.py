import os, sys
import pprint
from tabulate import tabulate 

def save_file(file_path, content):
  os.makedirs(os.path.dirname(file_path), exist_ok=True)
  with open(file_path, "w") as f:
    f.write(content)

def foutput(data):
  return pprint.pformat(data)

def output(data):
    print(pprint.pformat(data))

def doutput(data):
    print(tabulate(data, showindex=True, headers='keys', tablefmt='pretty'))