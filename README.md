# ADM_HW4
## Homework 4 Group 15

modules.py - contains all functions

main.py - running file

## ___Part1___
The first part of homework required to parse json files and building a graph object.Given file contains dictionaries with authors, their pubblications and conferences in which they partecipated.

By parsing json documents, we created one dictionary with all author_id's like a KEY and their list of pubblications like VALUE and another with id's and conferences, which we used in one of the exercises later.

Creation of dictionaries is performed by two function which takes in input only a full path of the json file:

    a)  process_data

    b)  conference_dict

Subsequenly we created a graph object by adding nodes and weighted edges only for authors who has at least one pubblication in common. We used two functions, one for calculate jaccard distances beetwen sets of pubblications and other for building a graph:

     c)  jaccard  (takes in input two author's ids)

     d)  buildGraph   (takes in input a dictionary created by a function load_data on the previous step)

## ___Part2___
The second part required to create some subgraphs:

   - Given in input a conference we should return a subgraph induced by the set of authors who published at the input conference at least once. Creation of this subgraph is performed by:

         e) conference_subgraph  (takes in input only graph object)

The same function make a plot for the subgraph and computes 3 types of centralities measures for it(degree, betweenness, closeness centrality ). 

It also make a plot for every type of measure using a color intensities for highlight different levels of centrality measures for nodes, which performed by function:

     f)  draw  (takes in input graph object, positions of nodes, measure, name of measure)

   - Given in input an author and an integer d, we made a subgraph induced by the nodes that have the number of edges at most equal to d with the input author. We implemented Breath-First Search algoritm adding the condition on the length of path(d).Then we made a plot for our subgraph. This procedure was performed by functions:

         g) author_subgraph  (takes in input graph object,start node,integer number which indicates the length)

         h) bfs_components  (algoritm which performes distances of length $d$). 


## ___Part3___

In the third part we created a python software which performed two types of queries:

   - takes in input an author (id) and returns the weight of the shortest path that connects the input author with Aris. It's done by functions:

         i)  ariss  (search for id which corresponds to name Aris in the file)

         j)  dijkstra  (using Dijkstra's algorithm find shortest path beetwen Aris and input node, takes in input graph object and two nodes)

    - takes in input a subset of nodes (>21) and returns, for each node of the graph, its GroupNumber. We implemented a function which
        
          k)  buildGroupNumber (builds a dictionary to store distances from every node of the graph to input nodes)
          m)  groupNumber (get the minimum from a dictionary for every node in the input)

