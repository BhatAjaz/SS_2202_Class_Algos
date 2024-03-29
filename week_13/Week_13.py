#PRIMS algorithm
from collections import defaultdict
import heapq


def PrimsMST(graph, starting_vertex):
    mst = defaultdict(set) # tree we require, set because we don't want cycles
    visited = set([starting_vertex])  # list of vertices visited, so far only starting vertex
    total_cost = 0
    # find all edges from starting vertex 
    edges = [ (cost, starting_vertex, to) for to, cost in graph[starting_vertex].items() ]  #list comprehension
    
    heapq.heapify(edges) #and order them into a heap, with smallest at the top
    
    while visited  !=  set(graph.keys()): #edges: # process below while all vertices have not been visited
        cost, frm, to = heapq.heappop(edges) # collect/pop the smallest edge from the heap, which is the one at its top 
        if to not in visited: # if the vertex 'to' connected to this edge is not in the visited list yet
            visited.add(to)   # add this vertex to the visted list 
            mst[frm].add(to)  # add the existing vertex in cloud and this newly added vertex as key,value pair to the MST dictionary
            total_cost += cost #add the cost of the edge to the total cost of the MST
            for to_next, cost in graph[to].items(): # process all the edges of the newly visted vertex 'to'
                if to_next not in visited:    # check if the vertices conncetd to these edges are not in the visited already
                    heapq.heappush(edges, (cost, to, to_next)) # if not in the visited, insert them to the heap of edges
    print('total cost of MST is ', total_cost)
    return mst

example_graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1, 'G': 1},
    'G': {'F': 1},
}

print(PrimsMST(example_graph, 'A'))

# {'A': set(['B']),
#  'B': set(['C', 'D']),
#  'D': set(['E']),
#  'E': set(['F']),
#  'F': set(['G'])}



############################




#Kruskals algorithm
from collections import defaultdict
import heapq
## INCORRECT YET; It finds all partitions but doesn't connect them. Need to connect
def Kruskals_MST(graph):
    mst = defaultdict(set) # tree we require
    visited = set()  # list of vertices visited, so far only starting vertex
    total_cost = 0
    # find all edges from starting vertex 
    edges = []
    for starting_vertex, val in graph.items():
        for to, cost in graph[starting_vertex].items():
            edges.append ((cost, starting_vertex, to))
    #print(edges)
    
    heapq.heapify(edges) #and order them into a heap, with smallest at the top
    
#    while visited  !=  set(graph.keys()): #edges: # 
    while edges:    
        cost, frm, to = heapq.heappop(edges)
        print( cost, frm, to)
        if (frm and to) not in visited:
            visited.add(frm)
            visited.add(to)
            mst[frm].add(to)
            total_cost += cost
        elif to not in visited:
            visited.add(to)
            mst[frm].add(to)
            total_cost += cost
    print('total cost of MST is ', total_cost)
    return mst

example_graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 4, 'D': 5, 'E': 9},
    'C': {'A': 3, 'B': 4, 'F': 5},
    'D': {'B': 5, 'E': 4},
    'E': {'B': 9, 'D': 4, 'F': 2},
    'F': {'C': 5, 'E': 2, 'G': 1},
    'G': {'F': 1},
}

example_graph = {
    'A': {'B': 1, 'C': 7, 'D':10},
    'B': {'A': 1, 'C': 5, 'E': 8},
    'C': {'A': 7, 'B': 5, 'D': 11, 'E':9},
    'D': {'A': 10,'C': 11,'E': 3},
    'E': {'B': 8, 'C': 9, 'D': 3},
    'F': {'G': 4, 'H': 2},
    'G': {'F': 4, 'H': 6},
    'H': {'F': 2, 'G': 6}
}

print(Kruskals_MST(example_graph))




#Kruskals algorithm
from collections import defaultdict
import heapq

def notACycleFormingEdge(frm, to, mst):
    
    mst[frm].add(to)
    vert= frm
    while not all edges explored in mst:
      vert_to = mst[vert]
      if frm in vert_to:
          return False
      else:
          for verts in vert_to:
              
    return True

def Kruskals_MST(graph):
    mst = defaultdict(set) # tree we require
    total_cost = 0
    # find all edges from starting vertex 
    edges = []
    for starting_vertex, val in graph.items():
        for to, cost in graph[starting_vertex].items():
            edges.append ((cost, starting_vertex, to))
    #print(edges)
    
    heapq.heapify(edges) #and order them into a heap, with smallest at the top
    
#    while visited  !=  set(graph.keys()): #edges: # 
    while edges:    
        cost, frm, to = heapq.heappop(edges)
        print( cost, frm, to)
        if notACycleFormingEdge(frm, to, mst):
            mst[frm].add(to)
            total_cost += cost

    print('total cost of MST is ', total_cost)
    return mst