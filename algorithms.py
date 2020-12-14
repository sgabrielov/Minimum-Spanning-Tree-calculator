# -*- coding: utf-8 -*-

# Version 0.3
# Sergei Gabrielov
# 12/5/2020

from functions import min_prims_edge, prims_initialize, is_spanning, W, E
from drawing import show_weighted_graph, draw_subtree

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

def prims_algorithm(graph, starting_vertex, show_graph = False, show_cost = False):
    """Uses Prim's algorithm to find the minimum spanning tree for a given undirected graph.
    
    Parameters
    ----------
    G : networkx.classes.graph.Graph type
        An undirected graph
    starting_vertex : int
        A vertex in G
    show_graph 
        If true, display a visual plot showing the minimum spanning tree as edges are added
        and upon completion
    show_cost
        If true, display the total cost of the minimum spanning tree
        
    Raises
    ------
    ValueError
        If starting_vertex is not found in G.    
        
    Returns
    -------
    networkx.classes.graph.Graph type
        The minimum spanning tree of graph.
    
    """

    if show_graph:
        # Show the initial graph
        show_weighted_graph(graph)
        
    # Create a subtree with one vertex.
    T = prims_initialize(graph, starting_vertex)
    
    if show_graph:
        # Draw the initial subtree showing the first vertex
        draw_subtree(graph,T)
        
    # While T is not a spanning tree of G
    # While there are still vertices in G to be added to T
    while not is_spanning(graph, T):
        
        # Add the minimum cost edge from G to T
        e = min_prims_edge(graph,T)
        T.add_edge(e[0], e[1], weight=W(graph, e))
        
        if show_graph:
            
            # Highlight the edge that was just added.
            draw_subtree(graph,T)
    
    if show_cost:
        
        # Calculate the total cost of the minimum spanning tree.
        c = sum([W(graph, e) for e in E(T)])
        print(f'The cost of this spanning tree is {c}')
        
    return T