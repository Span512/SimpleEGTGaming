# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 18:18:29 2020

@author: Span1024
"""
import networkx as nx
import matplotlib.pyplot as plt
import time

def GraphPainter(G, mode = 'ABshare'):
    color = []
    if mode == 'ABshare':
        for idx in range(len(G.node)):
            if(G.node[idx]['type'] == 'A' and G.node[idx]['share'] == 1):
                color.append('red')
            elif(G.node[idx]['type'] == 'B' and G.node[idx]['share'] == 1):
                color.append('yellow')
            elif(G.node[idx]['type'] == 'A' and G.node[idx]['share'] == 0):
                color.append('blue')
            else:
                color.append('black')
    elif mode == 'AB':
        for idx in range(len(G.node)):
            if(G.node[idx]['type'] == 'A'):
                color.append('red')
            else:
                color.append('black')
    elif mode == 'share':
        for idx in range(len(G.node)):
            if(G.node[idx]['share'] == 1):
                color.append('red')
            else:
                color.append('black')
    else:
        color = ['black'] * len(G.node)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_label = False, node_color = color, node_size = 150)
    plt.show()

def lineChartPainter(res, save_file = True):
    marker = ['*', 'o', '>', '<', '^', 'v', '1', '2','3','4','8','s','p','h','+', 'x','d']
    x = range(len(res[0]))
    for i in range(len(res)):
        label = "P" + str(i + 1)
        if save_file:
            plt.plot(x, res[i], label = label, marker = marker[int(i % len(marker))],markevery = list(range(0,len(res[0]), 5)))
        else:
            plt.plot(x, res[i])
    plt.title("Result")
    plt.xlabel("Time")
    plt.ylabel("The proportion of nodes choose to share")
    plt.legend()
    name = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))  + r".jpg"
    #name = "result.jpg"
    if save_file:
        plt.savefig(name, dpi = 1800)
    else:
        plt.show()
        