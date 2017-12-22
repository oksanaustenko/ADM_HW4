import json
import networkx as nx
import itertools
import matplotlib.colors as mcolors 
import matplotlib.pyplot as plt
import collections
import random
import heapq
def process_data(pathname):
    parsed_auths = json.loads(open(pathname,'r').read())
    author_list = {}
    author_pub = collections.defaultdict(set)
    for elmt in parsed_auths:
        authors = elmt['authors']
        pub_id = elmt['id_publication_int']
        for x in authors:
            # create all the authors dictionary with author name  as key
            # and author id as value
            author_list[x['author_id']] = x['author']

            # create all authors publication set as a dictionary
            # with author id as key
            # and set as value
            author_pub[x['author_id']].add(pub_id)
            
    return author_pub,author_list


def buildGraph(pub_dict,pathname):
    parsed_auths = json.loads(open(pathname,'r').read())
    authors_graph = nx.Graph()
    for node in pub_dict.keys():
        authors_graph.add_node(int(node))

    for elmt in parsed_auths:
        # iterations on couple of authors for every publication
        for pair in itertools.combinations(elmt['authors'], 2):
            j = 1 - jaccard(pub_dict[pair[0]['author_id']],pub_dict[pair[1]['author_id']])
            authors_graph.add_edge(int(pair[0]['author_id']), int(pair[1]['author_id']),weight=j)

    return(authors_graph)

def jaccard(ks1,ks2) :
    inter = len(set(ks1) & set(ks2))
    union = len(set(ks1) | set(ks2))
    if union == 0:
        return 0
    return (1 - (inter / float(union)))

def ariss(data_file):    
    init_data=json.load(open(data_file, 'r'))
    all_authors={}
    for a in init_data:
        for aut in a['authors']:
            author_id=aut['author_id']
            all_authors[author_id]=aut['author']
    Aris=[key for key, value in all_authors.items() if value == 'aris anagnostopoulos'][0]
    return Aris

def conference_dict(data_file):    
    init_data=json.load(open(data_file))
    all_authors={}
    result = {}
    for i in range(len(init_data)):
        for author in init_data[i]['authors']:
            for j in range(len(init_data[i]['authors'])):
                author_id=init_data[i]['authors'][j]['author_id']
                if author_id in all_authors.keys():
                    all_authors[author_id].append(init_data[i]['id_conference_int'])
                else:
                    all_authors[author_id]=[init_data[i]['id_conference_int']]   
    for key,value in all_authors.items():
            result[key] = list(set(value))
    return result

def draw(G, pos, measures, measure_name):
    
    nodes = nx.draw_networkx_nodes(G, pos, node_size=25, cmap=plt.cm.plasma, 
                                   node_color=list(measures.values()),
                                   nodelist=list(measures.keys()))
    nodes.set_norm(mcolors.SymLogNorm(linthresh=0.01, linscale=1))
    
    # labels = nx.draw_networkx_labels(G, pos)
    edges = nx.draw_networkx_edges(G, pos)

    plt.title(measure_name)
    plt.colorbar(nodes)
    plt.axis('off')
    plt.show() 

def conference_subgraph(our_graph, data_file):
    conferenceid=input('Enter an id of the conference: \n')
    authors_list=set()
    conferences=conference_dict(data_file)
    for a_id,conf in conferences.items():
        for i in conf:
            if i==int(conferenceid):
                authors_list.add(a_id)
    sub=our_graph.subgraph(list(authors_list))
    pos=nx.spring_layout(sub)
    plt.figure(1)
    nx.draw_networkx(sub, with_labels=False, node_size=20, node_color='r')
    plt.figure(2)
    draw(sub,pos,nx.degree_centrality(sub), 'Degree centrality')
    plt.figure(3)
    draw(sub,pos,nx.betweenness_centrality(sub), 'Betweenness Centrality')
    plt.figure(4)
    draw(sub,pos,nx.closeness_centrality(sub), 'Closeness Centrality')   
    plt.show()
    
def bfs_components(graph, start, d):
    degree = {}    
    degree[start] = 0
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start] 
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        print(node)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
 
            # add neighbours of node to queue
            for neighbour in neighbours:
                degree[neighbour] = degree[node]+1
                if degree[neighbour]<= d :
                    queue.append(neighbour)
                else :
                    explored.append(node)
           
    return set(explored)

def author_subgraph(our_graph,authorid=None,d=None):
    if authorid is None:
        authorid=int(input('Enter an id of author for which I should search about: ' +'\n'))
    if d is None:
        d=int(input('Enter the number of edges you would use: ' +'\n')) 
    neighbors=bfs_components(our_graph,authorid, d)
    sub=our_graph.subgraph(list(neighbors))
    nx.draw_networkx(sub, with_labels=True, node_size=20, node_color=('b', 'r', 'g'), edge_color=('y'))
    return plt.show()

def dijkstra(graph,start,end):
    weights = {} # to save distance of node from start node
    prev = {}  # to save previous node on shortest path
    to_explore = []
    heapq.heappush(to_explore,(start,0))

    nodes = graph.nodes()

    for node in nodes :
        weights[node]= float('inf') # all distance set to infinite
        prev[node]= None # set all previous node to none

    weights[start] = 0 # distance from start to start = 0

    while to_explore :
        # get and remove nearest element to start node  from exploring list
        current_node = heapq.heappop(to_explore)[0]

        # iterate on currentnode neighbor
        # for each neighbor update disance from start node
        for neighbor in nx.all_neighbors(graph,current_node):

            # get distance from current node to neighbor
            ne_weight = float(graph.get_edge_data(current_node,neighbor)['weight'])

            # then add it to current node distance from start node
            # to obtain distance between start node and neighbor
            d = weights[current_node] + ne_weight
            if d < weights[neighbor]:
                weights[neighbor] = d  # update neighbor distance from start node  if new distance is shorter
                prev[neighbor] = current_node # set current node as neighbor previous node in shortest path
                heapq.heappush(to_explore, (neighbor, d)) # add neighbor to exploring list

    # build the path starting from end
    # and taking previous node in shortest path
    # until we reach the start node
    path = []
    x = end
    while x != None:
        path.insert(0,x)
        x = prev[x]

    # if path only contains end node
    # then there is no path
    if len(path)==1:
        path = 'No Path'

    return path,weights



# first we build a dictionaty to store distance
# from every node of the graph to input nodes
def buildGroupNumber(graph,inp):
    nodes = graph.nodes()
    tabs = collections.defaultdict(set)
    # for each element x in the input we run djikstra
    # to get shortest distances from all graph node to x
    for x in inp:
        # we get the distances in a dictionary
        dists = dijkstra(graph, x, None)[1]
        for node in nodes:
            # if node is in the dictionary we get it
            # otherwise it means the distance is infinite
            # for each node we store the disatnces from the input elements
            # in a list

            tabs[node].add(dists.get(node, float('inf')))
    return tabs


# then we just get the minimum for a particular node v
def groupNumber(v,groups):
    if v in groups.keys():
        return [min(groups[v])]
    return None