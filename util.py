# from talon import
import csv
from pathlib import Path
import re
import os

cwd = os.path.expanduser("~") + "/.talon/user/"
dont_capitalize_these_words = ['a', 'an', 'and', 'or', 'the', 'of', 'in']

def csv_to_object(file_name, result: dict[str, str] = {}):
  with open(os.path.expanduser("~/.talon/user/") + file_name, 'r') as file:
    for line in file.readlines():
      content = line.split(',', 1)
      result.update({content[0]: content[1].rstrip()})
  return result
