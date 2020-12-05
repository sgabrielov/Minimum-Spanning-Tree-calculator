# -*- coding: utf-8 -*-

# Version 0.1
# Sergei Gabrielov
# 12/5/2020

import networkx as nx
from functions import min_prims_edge, prims_initialize, is_spanning

# Prim's algorithm for finding an MST - 
#
# Input: An undirected, connected, weighted graph G.
# Output: T, a minimum spanning tree for G.
#
# T := ∅.
# Pick any vertex in G and add it to T.
#
# For j = 1 to n-1
#       Let C be the set of edges with one endpoint inside T and one endpoint outside T.
#       Let e be a minimum weight edge in C.
#       Add e to T.
#       Add the endpoint of e not already in T to T.
# End-for

# Input Files : test-graphs\g#.txt

def prims_algorithm(G, starting_vertex):
    T = prims_initialize(G, starting_vertex)
    
    while not is_spanning(G, T):
        T.add_edge(*min_prims_edge(G,T))
    
    return T