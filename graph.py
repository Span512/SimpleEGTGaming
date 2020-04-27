# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 18:15:27 2020

@author: span1024
"""
import random 
import networkx as nx
import numpy as np

def networkCreate(total_node, average_degree, network_type, k, division_parameter):
    '''
    division_parameter:
        0:
            0 for divide by degree
            1 for divide randomly
        1:
            the proportion of node A in division
        2:
            the probability type-A nodes choose to share
        3:
            the probability type-B nodes choose to share
    '''
    if len(division_parameter) != 4 :
        print("parameter numbers error!")
    else:
        if network_type == "ws":
            G = nx.random_graphs.watts_strogatz_graph(total_node, average_degree, k)
        else:
            G = nx.random_graphs.barabasi_albert_graph(total_node, int(average_degree/2))
        degree = [i[1] for i in nx.degree(G)]
        division_arr = list(range(total_node))
        if division_parameter[0]:
            random.shuffle(division_arr)
        else:
            division_arr.sort(key = lambda d:degree[d])
        typeB = division_arr[:int(total_node * (1 - division_parameter[1]))]
        typeA = division_arr[int(total_node * (1 - division_parameter[1])):]
        random.shuffle(typeA)
        random.shuffle(typeB)
        share = typeA[:int(len(typeA) * division_parameter[2])] + typeB[:int(len(typeB) * division_parameter[3])]
        for idx in range(len(G.node)):
            if idx in typeA:
                G.node[idx]['type'] = 'A'
            else:
                G.node[idx]['type'] = 'B'
            if idx not in share:
                G.node[idx]['share'] = 0
            else:
                G.node[idx]['share'] = 1
        return G
def networkInfo(G):
    num_of_nodes = len(G.node)
    num_of_share_A = 0
    num_of_share_B = 0
    num_of_A = 0
    num_of_B = 0
    for idx in range(len(G.node)):
        if G.node[idx]['type'] == 'A':
            num_of_A += 1
            if(G.node[idx]['share']):
                num_of_share_A += 1
        else:
            num_of_B += 1
            if(G.node[idx]['share']):
                num_of_share_B +=1
    average_degree = np.mean([i[1] for i in G.degree()])
    print("The number of nodes is %d" %num_of_nodes)
    print("There are %d A nodes and %d B nodes" %(num_of_A,num_of_B))
    print("And %d A nodes and %d B nodes choose to share" %(num_of_share_A,num_of_share_B))
    print("The average degree is %lf" %average_degree)
def proportionOfShare(G):
    num_of_share = 0
    for idx in range(len(G.node)):
        if G.node[idx]['share']:
            num_of_share += 1
    return num_of_share / len(G.node)
            
    
    