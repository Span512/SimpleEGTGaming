# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 20:57:05 2020

@author: span1024
"""
import numpy as np
import networkx as nx
from copy import deepcopy
import random

def matrixInit(p, n):
    kappa,K1,K2,a1,a2,b1,b2,t1,t2,w1,w2,f1,f2,c1,c2 = p
    res = []
    A1 = (1 + t1) * a1 * K1 * b1 + w1 * a1 * K1 - c1 * a1 * K1 / (n - 1)
    B1 = w1 * a1 * K1 - c1 * a1 * K1 / (n - 1)
    C1 = a1 * K1 * b1
    D1 = 0
    res.append([[A1, A1], [B1, C1], [C1, B1], [D1, D1]])
    A2 = (1 + t1) * a2 * K2 * b1 + w1 * a1 * K1 - c1 * a1 * K1 / (n - 1)
    B2 = w1 * a1 * K1 - c1 * a1 * K1 / (n - 1)
    C2 = a2 * K2 * b1
    D2 = 0
    E1 = (1 + t2) * a1 * K1 * b2 + w2 * a2 * K2 - c2 * a2 * K2 / (n - 1)
    F1 = a1 * K1 * b2
    G1 = w2 * a2 * K2 - c2 * a2 * K2 / (n - 1)
    H1 = 0
    res.append([[A2, E1], [B2, F1], [C2, G1], [D2, H1]])
    A3 = (1 + t1) * a1 * K1 * b1 - c1 * a1 * K1 / (n - 1) - f1 * a1 * K1
    B3 = -1 * c1 * a1 * K1 / (n - 1) - f1 * a1 * K1
    C3 = a1 * K1 * b1
    D3 = 0
    res.append([[A3, A3], [B3, C3], [C3, B3], [D3, D3]])
    A4 = (1 + t1) * a2 * K2 * b1 - c1 * a1 * K1 / (n - 1) - f1 * a1 * K1
    B4 =-1 * c1 * a1 * K1 / (n - 1) - f1 * a1 * K1
    C4 = a2 * K2 * b1
    D4 = 0
    E2 = (1 + t2) * a1 * K1 * b2 - c2 * a2 * K2 / (n - 1) - f2 * a2 * K2
    F2 = a1 * K1 * b2
    G2 = -1 * c2 * a2 * K2 / (n - 1) - f2 * a2 * K2
    H2 = 0
    res.append([[A4, E2], [B4, F2], [C4, G2], [D4, H2]])
    E3 = (1 + t2) * a2 * K2 * b2 + w2 * a2 * K2 - c2 * a2 * K2 / (n - 1)
    F3 = a2 * K2 * b2
    G3 = w2 * a2 * K2 - c2 * a2 * K2 / (n - 1)
    H3 = 0
    res.append([[E3, E3], [G3, F3], [F3, G3], [H3, H3]])
    E4 = (1 + t2) * a2 * K2 * b2 - c2 * a2 * K2 / (n - 1) - f2 * a2 * K2
    F4 = a2 * K2 * b2
    G4 =  -1 * c2 * a2 * K2 / (n - 1) - f2 * a2 * K2
    H4 = 0
    res.append([[E4, E4], [G4, F4], [F4, G4], [H4, H4]])
    for m in res:
        for e in m:
            for i in e:
                round(i, 3)
    return res
    
def actGame(m, c, t1, t2, s1, s2):
    if c == 1:
        if t1 == 'A' and t2 == 'A':
            if s1 == 1 and s2 == 1:
                return m[0][0]
            elif s1 == 1 and s2 == 0:
                return m[0][1]
            elif s1 == 0 and s2 == 1:
                return m[0][2]
            else:
                return m[0][3]
        elif t1 == 'A' and t2 == 'B':
            if s1 == 1 and s2 == 1:
                return m[1][0]
            elif s1 == 1 and s2 == 0:
                return m[1][1]
            elif s1 == 0 and s2 == 1:
                return m[1][2]
            else:
                return m[1][3]
        elif t1 == 'B' and t2 == 'A':
            if s1 == 1 and s2 == 1:
                return m[1][0][::-1]
            elif s1 == 1 and s2 == 0:
                return m[1][2][::-1]
            elif s1 == 0 and s2 == 1:
                return m[1][1][::-1]
            else:
                return m[1][3][::-1]
        else:
            if s1 == 1 and s2 == 1:
                return m[4][0]
            elif s1 == 1 and s2 == 0:
                return m[4][1]
            elif s1 == 0 and s2 == 1:
                return m[4][2]
            else:
                return m[4][3]
    else:
        if t1 == 'A' and t2 == 'A':
            if s1 == 1 and s2 == 1:
                return m[2][0]
            elif s1 == 1 and s2 == 0:
                return m[2][1]
            elif s1 == 0 and s2 == 1:
                return m[2][2]
            else:
                return m[2][3]
        elif t1 == 'A' and t2 == 'B':
            if s1 == 1 and s2 == 1:
                return m[3][0]
            elif s1 == 1 and s2 == 0:
                return m[3][1]
            elif s1 == 0 and s2 == 1:
                return m[3][2]
            else:
                return m[3][3]
        elif t1 == 'B' and t2 == 'A':
            if s1 == 1 and s2 == 1:
                return m[3][0][::-1]
            elif s1 == 1 and s2 == 0:
                return m[3][2][::-1]
            elif s1 == 0 and s2 == 1:
                return m[3][1][::-1]
            else:
                return m[3][3][::-1]
        else:
            if s1 == 1 and s2 == 1:
                return m[5][0]
            elif s1 == 1 and s2 == 0:
                return m[5][1]
            elif s1 == 0 and s2 == 1:
                return m[5][2]
            else:
                return m[5][3]

def strategyChange(G, kappa):
    n = G.number_of_nodes()
    for i in range(n):
        neighborRandom = random.choice(list(G.neighbors(i)))
        u1 = G.node[i]['profit']
        u2 = G.node[neighborRandom]['profit']
        W = 1 / (1 + np.exp((u1 - u2) / kappa))
        #print(i, neighborRandom, u1, u2, W)
        if random.random() <= W:
            G.node[i]['share'] = G.node[neighborRandom]['share']
        
def networkUpdate(G, matrix, kappa):
    '''
    p(parameter used for gaming):
        0.K1
        1.K2
        2.a1
        3.a2
        4.b1
        5.b2
        6.t1
        7.t2
        8.w1
        9.w2
        10.f1
        11.f2
        12.c1
        13.c2
    '''
    tG = deepcopy(G)
    n = G.number_of_nodes()
    for i in range(n):
        tG.node[i]['profit'] = 0
    for i in range(n):
        for j in range(i + 1, n):
            profit = actGame(matrix, j in list(tG.neighbors(i)), tG.node[i]['type'],tG.node[j]['type'] ,tG.node[i]['share'],tG.node[j]['share'])
            #print(j in list(G.neighbors(i)), tG.node[i]['type'],tG.node[j]['type'],tG.node[i]['share'],tG.node[j]['share'], sep = ' ')
            #print(i, j, "[%.3lf, %.3lf]" %(profit[0], profit[1]))
            tG.node[i]['profit'] += profit[0]
            tG.node[j]['profit'] += profit[1]
    strategyChange(tG, kappa)
    return tG
def networkCompare(G1, G2):
    for i in range(G1.number_of_nodes()):
        if G1.node[i]['share'] != G2.node[i]['share']:
            return False
    return True
           
                
        
        
    