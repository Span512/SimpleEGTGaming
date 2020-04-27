# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:53:02 2020

@author: Span1024
"""
import numpy as np
import random 
import networkx as nx
import matplotlib.pyplot as plt
import graph
import gaming
import painter
from copy import deepcopy

def doSimulation(parameters, times, max_time = 100):
    res = []
    #print(parameters)
    for i in range(len(parameters)):
        network = parameters[i][0]
        division = parameters[i][1]
        game = parameters[i][2]
        m = gaming.matrixInit(game, network[0])
        
        tmp = []
        res.append([])
        for j in range(times):
            G = graph.networkCreate(network[0], network[1], network[2], network[3], division)
            tmp.append([])
            for k in range(max_time):
                if k > 0 and (tmp[j][k - 1] == 0 or tmp[j][k - 1] == 1):
                    tmp[j].append(tmp[j][k - 1])
                else:
                    tmp[j].append(graph.proportionOfShare(G))
                    G = gaming.networkUpdate(G, m, game[0])
                if k == max_time - 1:
                    painter.GraphPainter(G)
            print("%.3f%%" %((i*times + j + 1)/(len(parameters) * times) * 100))
        for j in range(max_time):
            res[i].append(round(np.mean([tmp[k][j] for k in range(times)]), 3))
    return res
        
        
        
    