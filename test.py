# Test file for drivers of functions.py resources.

import networkx as nx
from functions import *


graph_data = open('test-graphs/g1.txt', 'r')

G = nx.read_weighted_edgelist(graph_data, nodetype = int)

print(f'The vertex set of G is V(G) = {V(G)}')
print(f'The edge set of G is E(G) = {E(G)}')

T = prims_initialize(G, 12)

print('')

print(f'The vertex set of T is V(T) = {V(T)}')
print(f'The edge set of T is E(T) = {E(T)}')

print('')
print(f'Is T spanning? {is_spanning(G, T)}')

temp_edges = list(G.edges(V(T)))
print('')
print(f'The edges containing vertex 4 are E(4) = {temp_edges}')
print(f'The cost of edge (4,2) is W(4,2) = {W(G,temp_edges[0])}')
print(f'The cost of edge (4,5) is W(4,5) = {W(G,temp_edges[1])}')

temp_edges.sort(key = lambda e : W(G, e))
print(f'The edges containing vertex 4 are E(4) = {temp_edges}')

#T.add_edge(4,5)
#T.add_edge(2,4)
#T.add_edge(2,3)
#T.add_edge(1,3)

print(f'The edges contained in T are G.edges(V(T)) = {list(G.edges(V(T)))}')
print(f'The possible edges for new V in T are possible_edges(G, T) = {possible_edges(G,T)}')


()
