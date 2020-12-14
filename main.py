# -*- coding: utf-8 -*-

# Version 1.0
# Sergei Gabrielov
# 12/13/2020

import networkx as nx
from algorithms import prims_algorithm
from functions import W, E

# os directory operations. Find filenames
from os import listdir, path
from os.path import isfile, join

import warnings

# Program generates a Numpy warning:
#
# FutureWarning: arrays to stack must be passed as a "sequence" type such as list or tuple. Support for non-sequence iterables such as generators is deprecated as of NumPy 1.16 and will raise an error in the future.
# pos = np.row_stack((pos[x] for x in node_list))
# 
# Can show warnings again once an update to networkx addresses this.

warnings.simplefilter(action='ignore', category=FutureWarning)

# regex
import re

# TODO
# Ask the user for input, which graph do they want to run, do they want to
# show plot or show 

def main():
    # Declare sentinel values
    choice = -1
    graph_file = 'test-graphs/filename'
    
    # Declare default option values
    opt_plot = True
    opt_cost = True
    vertex = 1
    
    found_file = False
    
    # Loop only on option/file choices and input error. Terminate on run and quit.
    while not choice == 6 and not choice == 7:
        
        if found_file:
            print()
            print("Currently selected graph file: ")
            print(graph_file)
            print()
        
        show_menu(opt_plot,opt_cost,vertex, graph_file)
        choice = try_menu_input("Input 1 through 7: ")
        
        # Select file from list
        if choice == 1:
            
            filechoice = -1 
            print("Choose a file: ")
            filelist = get_files_in_test_path()
            show_filelist(filelist)
            
            # Loop only when input is invalid        
            while filechoice < 1 or filechoice > len(filelist):
                filechoice = try_menu_input("Input 1 through " + str(len(filelist)) + ": ")
                
                # If invalid input
                if filechoice < 1 or filechoice > len(filelist):
                    print("Choice must be between 1 through " + str(len(filelist)) + ". Please try again. ")
                    print()
                    show_filelist(filelist)
        
            graph_file = 'test-graphs/' + filelist[filechoice-1]
            found_file = True
        
        # Request a full file path input
        if choice == 2:
            graph_file = input("Input full C:/path/to/file\n")
            found_file = path.exists(graph_file)
            if not found_file:
                print("Error, file not found.")
                print()
                
        # Toggle show plot
        if choice == 3:
            opt_plot = not opt_plot
        
        # Toggle show cost
        if choice == 4:
            opt_cost = not opt_cost
        
        # Update starting vertex
        if choice == 5:
            vertex = try_menu_input("Input starting vertex: ")
            
            # The try_menu_input function defaults to -1 for an invalid input.
            # Instead, set vertex back to the default.
            if vertex == -1:
                vertex = 1
                
        # Invalid input
        if choice < 0 or choice > 7:
            print("Input must be 1 through 7. ")
    
    # If not exiting the program
    if not choice == 7:
        
        # Open input file
        graph_data = open(graph_file, 'r')
        
        # Read graph data
        G = nx.read_weighted_edgelist(graph_data, nodetype = int)
        
        # Close input file
        graph_data.close()
        
        # Perform Prim's on graph with selected options
        T = prims_algorithm(G, vertex, show_graph = opt_plot, show_cost = opt_cost)
        
        
        # Uses regex to find just the filename without extension of the input file.
        graph_file = re.search("[ \w-]+?(?=\.)", graph_file).group()
        
        # Generate string for outfile path
        outfilename = 'test-graphs/trees/' + graph_file + 'tree.txt'
        
        print("Save output tree to " + outfilename)
        
        if path.exists(outfilename):
            print("WARNING: output file exsists and will be overwritten.")
        choice = input("Input yes/no : ")
        if choice[0].lower() == 'y' or choice[0] == '1':
                outfile = open(outfilename, 'w')
                outdata = generate_output_tree(T)
                outfile.write(outdata)
                outfile.close()
            

def show_menu(opt_plot, opt_cost, v, filename):
    print("1. Select a graph file from /test-graphs/")
    print("2. Input a full path to a graph file")
    print("3. Toggle plot show. Disable for non-planar graphs. Currently ", end="")
    if opt_plot:
        print("ON")
    else:
        print("OFF")
    print("4. Toggle calculate cost. Currently ", end="")
    if opt_cost:
        print("ON")
    else:
        print("OFF")
    print("5. Select starting vertex. Currently",v)
    print("6. Start Prim's with selected graph file and options.")
    print("7. Quit")
        
def show_filelist(filelist):
    count = 0
    for f in filelist:
        count = count + 1
        print(str(count) + ". " + f)
    
def get_files_in_test_path():
    
    # Get all .txt filenames in test dir
    filelist = [f for f in listdir("test-graphs/") if isfile(join("test-graphs/", f)) and ".txt" in f]
    return filelist

def try_menu_input(prompt_str):
    
    # Forces int input from user
    try:
        choice = int(input(prompt_str))
        return choice
    
    # If non integer input, return invalid input sentinal int
    except ValueError:
        return -1
    
def generate_output_tree(graph):
    
    # Generate the string that will be outputted to file
    out_data = ""
    edges = E(graph)
    for e in edges:
        out_data = out_data + str(e[0]) + " " + str(e[1]) + " " + str(W(graph, e)) + "\n"
    return out_data

main()
