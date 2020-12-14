# Test file for drivers of functions.py resources.

import networkx as nx
from functions import *
from drawing import *
from algorithms import prims_algorithm

import re

graph_file = 'C:/test/path/to/file.txt'
graph_file = re.search("[ \w-]+?(?=\.)", graph_file).group()
outfile = 'test-graphs/trees/' + graph_file + '.txt'
print("Save output tree to " + outfile)