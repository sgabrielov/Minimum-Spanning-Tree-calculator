UHD MATH2305 Final Project
Sergei Gabrielov

This project uses Prim's Algorithm to calculate the minimum spanning tree (MST) for a given undirected graph.

Changelog:
1.0 
Added main.py - Menu driven primary end user file.
Modified algorithms.py to add cost to subtree edges

0.2
Added drawing.py
Added test-graphs/g4.txt
Modified algorithms.py to add plot drawing and cost calculating functionality

0.1 
Added algorithms.py
Added functions.py


How to use:
Using main.py

Prepare a text file that contains a weighted edgelist for an undirected graph. Included are g#.txt example files in test-graphs/
General format for edgelist:
1 2 3
1 3 1

Each line represents an edge with vertices v1, v2 and cost c
v1 v2 c

Program options:
Plot show - draws graphs while the subtree is constructed. Shows the inital graph, highlights each edge that is added, shows final subtree.
Calculate cost - Calculates the total cost of the final subtree and displays at the end
Select starting vertex - Runs the algorithm with the selected root. Defaults to 1 for any value less than 1.
			 Terminates with error for any value that does not exist as a vertex in the starting graph.

Optionally saves the MST to test-graphs/trees/