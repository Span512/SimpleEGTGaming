# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:16:46 2020

@author: Span1024
"""
import painter
import simulation
import time
import os

def main():
    
    
    parameters = [[[10, 5, 'ws', 0.1], [1, 1.0, 0.5, 0.5],[0.001 ,5, 1, 0.5, 0.5, 0.8, 0.8, 0.8, 0.8, 0.4, 0.4, 0.3, 0.3, 0.5, 0.5]],
                  [[10, 5, 'ws', 0.1], [1, 0.5, 0.5, 0.5],[0.001 ,5, 1, 0.5, 0.5, 0.8, 0.8, 0.8, 0.8, 0.4, 0.4, 0.3, 0.3, 0.5, 0.5]],
                  [[10, 5, 'ws', 0.1], [1, 0.0, 0.5, 0.5],[0.001 ,5, 1, 0.5, 0.5, 0.8, 0.8, 0.8, 0.8, 0.4, 0.4, 0.3, 0.3, 0.5, 0.5]]]
    '''
    parameters = [[[10, 6, 'ws', 0.5], [0, 0.5, 0.5, 0.5],[0.1 ,1, 1, 1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]]]
    '''
    start = time.clock()
    res = simulation.doSimulation(parameters, 10)
    #res = simulation.doSimulation(parameters, 100， max_time = 50)
    finish = time.clock()
    print(res)
    print(str(finish - start))
    painter.lineChartPainter(res)
    '''
    parameters = [[[10, 4, 'ba', 0.5], [1, 0.2, 0.5, 0.5],[0.1 ,1, 1, 1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]],
                  [[10, 4, 'ba', 0.5], [1, 0.4, 0.5, 0.5],[0.1 ,1, 1, 1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]]]
    res = simulation.doSimulation(parameters, 10, max_time = 20)
    '''
if __name__ == '__main__':
    main()
    #os.system('pause')

