# ADM_HW4
## Homework 4 Group 15

## ___Part1___
The first part of homework required to parse json files and building a graph object.Given file contains dictionaries with authors, their pubblications and conferences in which they partecipated.

By parsing json documents, we created one dictionary with all author_id's like a KEY and their list of pubblications like VALUE and another with id's and conferences, which we used in one of the exercises later.

Creation of dictionaries is performed by two function which takes in input only a full path of the json file:

    a)  load_data

    b)  conference_dict

Subsequenly we created a graph object by adding nodes and weighted edges only for authors who has at least one pubblication in common. We used two functions, one for calculate jaccard distances beetwen sets of pubblications and other for building a graph:

     c)  jaccard_weights  (takes in input two author's ids)

     d)  build_graph   (takes in input a dictionary created by a function load_data on the previous step)

## ___Part2___
The second part required to create some subgraphs:

   - Given in input a conference we should return a subgraph induced by the set of authors who published at the input conference at least once. Creation of this subgraph performed by:
   
