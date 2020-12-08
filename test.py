# Test file for drivers of functions.py resources.

import networkx as nx
from functions import *
from drawing import *
from algorithms import prims_algorithm

graph_data = open('test-graphs/g2.txt', 'r')

G = nx.read_weighted_edgelist(graph_data, nodetype = int)

T = prims_algorithm(G, 1)


draw_subtree(G,T)