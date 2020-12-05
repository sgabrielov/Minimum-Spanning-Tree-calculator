# -*- coding: utf-8 -*-

# Version 0.1
# Sergei Gabrielov
# 12/5/2020

import networkx as nx
from algorithms import prims_algorithm
from functions import V, E

graph_data = open('test-graphs/g3.txt', 'r')
G = nx.read_weighted_edgelist(graph_data, nodetype = int)
T = prims_algorithm(G, 11)

print(f'The vertex set of G is V(G) = {V(G)}')
print(f'The edge set of G is E(G) = {E(G)}')

print('')

print(f'The vertex set of T is V(T) = {V(T)}')
print(f'The edge set of T is E(T) = {E(T)}')