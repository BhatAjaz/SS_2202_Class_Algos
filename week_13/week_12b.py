class Stack:
    def __init__ (self):
        ## create an empty stack
        self.s = []
        
    def push (self, value):
        # add an element onto the stack 
        self.s.append(value)
        
    def pop (self):
        #collect the topmost element
        return self.s.pop()
        
    def size (self):
        return len(self.s)
    
    def peek (self):
        #just see the topmost element, don't collect it
        return self.s[-1]
    
    def is_empty(self):
        return (len(self.s) == 0) 
    
  
class Queue:
    DEFAULT_CAPACITY = 10 #N
    
    def __init__(self):
        self.data = [None] * Queue.DEFAULT_CAPACITY #N
        self.size = 0  #elements inside the queue
        self.front = 0

    def Size(self):
        """ Returns the number of elements in the queue"""
        return self.size

    def is_empty(self):
        """ Returns True if the queue is empty"""
        return self.size == 0
    
    def enqueue(self,value):
        """Add an element (value) to the rear of the queue"""
        if self.size == Queue.DEFAULT_CAPACITY:
            raise Exception ('Queue is Full')

        rear = (self.front + self.size)%Queue.DEFAULT_CAPACITY
        self.data[rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception ('Queue is Empty')

        # below code returns  data[front], moves front ahead 
        front_element = self.data[self.front] # collects the data[front]
        self.data[self.front] = None ## clears the location, garbage collection
        self.front = ( self.front + 1 ) % Queue.DEFAULT_CAPACITY # moves front ahead
        self.size -= 1 # updates the current size of the queue
        return front_element # returns the collected element
    
    

graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

graph = {'1': ['2', '3', '4'],
         '2': ['1', '3'],
         '3': ['1', '2', '4', '5'],
         '4': ['1', '3', '5'],
         '5': ['4', '3', '6', '7'],
         '6': ['5'],
         '7': ['5']}

def bfs(graph, start): 
    visited = []           # the list of all vertices visited over bfs
    vert_Q = Queue()       # a queue that holds vertices temporarily as we go bfs
    vert_Q.enqueue(start)  # add the starting vertex to the rear of queue

    while not vert_Q.is_empty():   # keep exploring till no vertex remains unvisited
        vertex = vert_Q.dequeue()  # get the first vertex at the head of the queue
        if vertex not in visited:  # if this vertex has not been visited before, (i.e. not in visisted list yet)
            visited.append(vertex) # visit it, i.e. add it to the visited list
            for v in graph[vertex]: # for all its adjacent vertices
                if v not in visited: # in case any of these has not been visited before
                    vert_Q.enqueue(v) # add it to the rear of the queue
    return visited                    # when the queue is emptied, return the visited sequence   

bfs(graph, '6') # {'B', 'C', 'A', 'F', 'D', 'E'}


graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

def dfs(graph, start, visited=[]):    # visited is the list of all vertices visited over dfs
    vert_stack = Stack()              # a stack that holds vertices temporarily as we go dfs
    vert_stack.push(start)            # push the starting vertex onto the top of stack
    
    while not vert_stack.is_empty():   # keep exploring till no vertex remains unvisited
        vertex = vert_stack.pop()      # get the first vertex at the top of the stack
        #print(vertex)
        if vertex not in visited:      # if this vertex has not been visited before, (i.e. not in visisted list yet)
            visited.append(vertex)     # visit it, i.e. add it to the visited list
            for v in graph[vertex]:    # for each of its adjacent vertices, v
                if v not in visited:   # in case the vertex v has not been visited before
                    dfs(graph, v, visited)  # depth first search the vertex v
    return visited                      # when the stack is emptied, return the visited sequence 

dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}




graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

def dfs(graph, start, visited=[]):    # visited is the list of all vertices visited over dfs
    vert_stack = Stack()              # a stack that holds vertices temporarily as we go dfs
    vert_stack.push(start)            # push the starting vertex onto the top of stack
    
    while not vert_stack.is_empty():   # keep exploring till no vertex remains unvisited
        vertex = vert_stack.pop()      # get the first vertex at the top of the stack
        #print(vertex)
        if vertex not in visited:      # if this vertex has not been visited before, (i.e. not in visisted list yet)
            visited.append(vertex)     # visit it, i.e. add it to the visited list
            for v in graph[vertex]:    # for each of its adjacent vertices, v
                if v not in visited:   # in case the vertex v has not been visited before
                    vert_stack.push(v)   # depth first search the vertex v
    return visited                      # when the stack is emptied, return the visited sequence 

dfs(graph, 'D') # {'E', 'D', 'F', 'A', 'C', 'B'}


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dict:", self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:#bSB
            return [path]

        if start not in self.graph_dict: #Toronto
            return []

        paths = []
        for node in self.graph_dict[start]:#each 
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortestPath = None
        for intermediate in self.graph_dict[start]:
            if intermediate not in path:
                sp = self.get_shortest_path(intermediate, end, path)
                if sp:
                    if shortestPath is None or len(sp) < len(shortestPath):
                        shortestPath = sp

        return shortestPath

if __name__ == '__main__':

    routes = [
        ("BSB","Manila"),
        ("BSB", "Kualalumpur"),
        ("Kualalumpur", "Bilkent"),
        ("Manila","London"),
        ("Manila","Islamabad"),
        ("London","Bilkent"),
        ("London", "Delhi"),
        ("Islamabad", "Bilkent"),
        ("Delhi", "Bilkent")
    ]

    routes = [
        ("BSB", "Paris"),
        ("BSB", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)

    start = "BSB"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
    
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))

  


    start = "Dubai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))
    
    
'''     
    function dijkstra(G, S)
    for each vertex V in G
        distance[V] <- infinite
        previous[V] <- NULL
        If V != S, add V to Priority Queue Q
    distance[S] <- 0
	
    while Q IS NOT EMPTY
        U <- Extract MIN from Q
        for each unvisited neighbour V of U
            tempDistance <- distance[U] + edge_weight(U, V)
            if tempDistance < distance[V]
                distance[V] <- tempDistance
                previous[V] <- U
    return distance[], previous[]
'''

# from PQ import Min_Heap

# import math
# def dijkstraAlgorithm(graph, startingVertex):
#     distance = {}
#     previous = []
#     verticesHeap = Min_Heap([],'heapify');
#     distance[startingVertex] = 0
#     for vertex in graph:
        
#         distance[vertex] =
#         distance[vertex] = math.inf
#         previous[vertex] = None
#         if vertex is not startingVertex:
#             verticesHeap.enqueue(vertex)
            
    
    

# graph = {'A': [['B', 2],['C', 4]],
#          'B': [['C', 1],['D', 7]],
#          'C': [['E', 3]],
#          'D': [['E', 2],['F', 1]],
#          'E': [['F', 5]],
#          'F': []}

