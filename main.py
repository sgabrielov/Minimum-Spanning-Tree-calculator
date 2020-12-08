# -*- coding: utf-8 -*-

# Version 0.2
# Sergei Gabrielov
# 12/5/2020

import networkx as nx
from algorithms import prims_algorithm

# TODO
# Ask the user for input, which graph do they want to run, do they want to
# show plot or show cost

graph_data = open('test-graphs/g4.txt', 'r')
G = nx.read_weighted_edgelist(graph_data, nodetype = int)
T = prims_algorithm(G, 3, show_graph = True, show_cost = True)