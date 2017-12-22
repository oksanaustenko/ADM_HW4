print('Importing libraries....')
import json
import networkx as nx
import itertools
import matplotlib.colors as mcolors 
import matplotlib.pyplot as plt
import collections
import random
import heapq
import modules as m
data_file=input('Give me a full path of json file: \n')
print('Building a graph..... \n')
a_graph=m.buildGraph(m.process_data(data_file)[0],data_file)
conferences=m.conference_dict(data_file)
aris=m.ariss(data_file)
print(' Data processed successfully \n' )

ans=True
while ans:
    print("""
          1  Compute some statistics and visualizations for a graph:
              1a Subgraph based on conference
              1b Subgraph based on distances with a specific author
          2  Find distances for Aris 
          3  Compute GroupNumbers
          4  Exit
          """)
    ans=input("What would you like to do? \n")
    if ans=="1a":
        try: 
            print(m.conference_subgraph(a_graph, data_file))
        except ValueError:
            print('Wrong input, please try again \n ')
    if ans=="1b":
        try:
            print(m.author_subgraph(a_graph))
        except ValueError:
            print('Wrong input, please try again \n ')
    if ans=="2":
        try:
            end=int(input('Give me an id from which you want to start: \n'))
            print(m.dijkstra(a_graph,aris,end))
        except ValueError:
            print('Wrong input, please try again \n ')
    if ans=="3":
        v=list(map(int,input('Insert ids separeted by spaces: \n').split()))
        try:
            groups = m.buildGroupNumber(a_graph,v)
            for i in v:
                print(m.groupNumber(i,groups))
        except ValueError:
            print('Wrong input, please try again \n ')
    if ans =='':
        print('Please give me a valid input \n')
    if ans=="4":
        print ('\n Goodbye')
        break
