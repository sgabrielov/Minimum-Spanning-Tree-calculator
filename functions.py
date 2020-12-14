# -*- coding: utf-8 -*-

# Version 0.3
# Sergei Gabrielov
# 12/5/2020

import networkx as nx

def V(graph):
    """Returns a set of all vertices present in the inputted graph.
    
    Parameters
    ----------
    graph : networkx.classes.graph.Graph type
        An undirected graph
        
    Returns
    -------
    set
        A set of vertices in graph
    
    """
    
    return set(graph.nodes())


def E(graph):
    """Returns a list of all edges present in the inputted graph.
    
    Parameters
    ----------
    graph : networkx.classes.graph.Graph type
        An undirected graph
        
    Returns
    -------
    list
        A set of edges in graph
        
    """
    
    return list(graph.edges())

def W(graph, e):
    """Returns the weight or cost of edge e in the inputted graph.
    
     Parameters
    ----------
    graph : networkx.classes.graph.Graph type
        An undirected graph
    e : tuple
        An edge in graph
        
    Returns
    -------
    float
        The weight of edge e in graph
        
    """
    
    return graph[e[0]][e[1]]['weight']

def prims_initialize(graph, v):
    """Initializes Prim's algorithm for the inputted graph using initial vertex v.
    
    Parameters
    ----------
    graph : networkx.classes.graph.Graph type
        An undirected graph
    v : int
        A vertex in graph
        
    Raises
    ------
    ValueError
        If the initial vertex is not found in graph.    
        
    Returns
    -------
    networkx.classes.graph.Graph type
        A graph containing one vertex v and no edges 
    
    """
    
    if v not in V(graph):
        raise ValueError("{0} is not a vertex in the graph with vertices {1}".format(v, V(graph)))
    else:
        T = nx.Graph()
        T.add_node(v)
        return T
    
def is_spanning(graph, subgraph):
    """Checks if the subgraph is a spanning graph of the inputted graph.
    
    Parameters
    ----------
    graph : networkx.classes.graph.Graph type
        The original graph for which Perm's algorithm will determine the minimum spanning tree.'
    subgraph : networkx.classes.graph.Graph type
        The currently in progress tree that Perm's algorithm is building.
        
    Returns
    -------
    boolean
        Returns true if subgraph is a spanning graph of graph, false otherwise. 
    
    If the set of vertices in the subgraph matches the set of vertices in the graph,
    the subgraph is considered a spanning graph of graph and this function will return true.
    
    The purpose of this function is to determine when Prim's algorithm has added all of the vertices in graph,
    and has therefore completed calculating the minimum spanning tree of graph.'
    """
    
    # V returns a set of vertices.
    return V(graph) == V(subgraph)

def possible_edges(graph, subgraph):
    """Returns a list of possible new edges in graph that can be added to subgraph.
    
    Parameters
    ----------
    graph : networkx.classes.graph.Graph type
        The original graph for which Perm's algorithm will determine the minimum spanning tree.'
    subgraph : networkx.classes.graph.Graph type
        The currently in progress tree that Perm's algorithm is building.
        
    Returns
    -------
    list
         A list containing all edges in graph that can be added to subgraph while
         maintaining a connected tree structure.
    
    By Prim's algorithm, the only edges that can be added to the subgraph are ones in which there is exactly one
    vertex in common. If one of the edges yet to be added contains two vertices that are both in subgraph, 
    it will create a cycle in subgraph and therefore will no longer be a connected tree. If the neither of the vertices
    of the edge to be added are in subgraph, then when added it will not be connected to any of the vertices already in subgraph,
    and therefore it will not be a connected tree.'
    """
    
    # Start with e, the list of all edges in subgraph,
    # then add e to the return list if the vertex at index 0 of e is not in the subgraph,
    # or if the vertex at index 1 is not in the subgraph.
    
    return [e for e in list(graph.edges(V(subgraph))) if e[0] not in V(subgraph) or e[1] not in V(subgraph)]

def min_prims_edge(graph, subgraph):
    """Returns the lowest weight or cost edge in graph that can be added to the subgraph.
    
    Parameters
    ----------
    graph : networkx.classes.graph.Graph type
        The original graph for which Perm's algorithm will determine the minimum spanning tree.'
    subgraph : networkx.classes.graph.Graph type
        The currently in progress tree that Perm's algorithm is building.
        
    Returns
    -------
    tuple
        A tuple representing the edge with minimum weight that can be added to subgraph
        while maintaining a connected tree structure.
    
    By Prim's algorithm, once a list of eligible edges is determined from the input graph, 
    the one that should be added to the subgraph in progress is the one with lowest weight/cost.
    This function returns one edge that is appropriate to add next to the subgraph based on this criterion.
    """
    
    # Get a list of eligible edges from graph that can be added to subgraph.
    possible_edges_list = possible_edges(graph, subgraph)
    
    # Sort the list of edges by their weight/cost.
    possible_edges_list.sort(key = lambda e: W(graph, e))
    
    # Return the first value in the sorted list. This will be the edge with the lowest weight/cost in the list.
    return possible_edges_list[0]
    