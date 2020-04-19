from collections import deque

class Graph:
    """
    Graph object with implementations of various graph algorithms
    """
    def __init__(self, graph):
        self.graph = graph
    
    
    def bfs(self, start):
        """
        Breadth First Search implementation
        Returning the visiting order
        """
        visited_nodes = {int(start)}
        queue = deque()
        
        search_order = []
        
        
        for node in self.graph[start].edges:
            queue.append(node[0])
            visited_nodes.add(node[0])
            search_order.append(node)
        
        while queue:
            current_node = queue.popleft()
            
            for node in self.graph[str(current_node)].edges:
                if node[0] not in visited_nodes:
                    visited_nodes.add(node[0])
                    queue.append(node[0])
                    search_order.append(node)
                    
        return search_order
    
    def dfs(self, start):
        """
        Depth First Search implementation
        Returning the visiting order from recursion
        """
        def traverse(node):
            """
            Helper function to recurse on nodes in graph
            """
            for adjacent in self.graph[str(node)].edges:
                if adjacent[0] not in visited_nodes:
                    visited_nodes.add(adjacent[0])
                    recursion_order.append(adjacent)
                    traverse(adjacent[0])
                    
        visited_nodes = {int(start)}
        recursion_order = []
        
        for node in self.graph[start].edges:
            if node[0] not in visited_nodes:
                recursion_order.append(node)
                traverse(node[0])
        
        return recursion_order
    
    def dijkstra(self, start, end=None):
        """
        Implementation of Dijkstras for computing shortest path
        """
        # Initialize all the nodes distance and previous node to compute the path
        for node in self.graph:
            self.graph[node].dist = 10000
            self.graph[node].prev = None
        
        self.graph[start].dist = 0
        vertices = set(self.graph.keys())
        
        # Iterate through every vertex once
        while vertices:
            # Instead of a set, this could be a min-heap
            current_node = min(vertices, key = lambda x: self.graph[x].dist)
            
            # Go through each neighbour and see if we can "optimize" distance
            for node in self.graph[current_node].edges:
                tmp_dist = self.graph[current_node].dist + node[1]
                
                # Update distance and update path to the node
                if tmp_dist < self.graph[str(node[0])].dist:
                    self.graph[str(node[0])].dist = tmp_dist
                    self.graph[str(node[0])].prev = current_node
            
            vertices.remove(current_node)
        
        # Return a nice output for best route
        if end is not None:
            path, current_vertex = deque(), end
            while self.graph[current_vertex].prev is not None:
                path.appendleft(current_vertex)
                current_vertex = self.graph[current_vertex].prev

            if path:
                path.appendleft(current_vertex)
            print(f'Fastest route from Node {start} to Node {end} with cost {self.graph[end].dist}' )
            for count, node in enumerate(path):
                if count + 1 == len(path):
                    print(node)
                else:
                    print(f'{node} -> ', end='')
        else:
            print('Outputting smallest distances in every node:')
            print('#'*8)
            for node in self.graph:
                print(f'Distance to Node {node} from Node {start}: {self.graph[node].dist}')

class Node:
    def __init__(self, edges, dist=None, prev=None):
        self.edges = edges
        self.dist = dist
        self.previous = prev
    
    def add_edge(self, edge):
        self.edges = self.edges.append(edge)
        

if __name__ == '__main__':
    g = {
        '1': Node([(2, 8), (3, 4), (4, 7)]),
        '2': Node([(5, 11)]),
        '3': Node([(5, 17), (6, 10)]),
        '4': Node([(6, 14)]),
        '5': Node([(7, 5)]),
        '6': Node([(7, 9)]),
        '7': Node([])
    }

    graph = Graph(g)
    
    print('Breadth First Search visiting order: ')
    print(graph.bfs('1'))

    print('#'*8)

    print('Depth First Search visiting order: ')
    print(graph.dfs('1'))
    
    print('#'*8)
    
    print('Dijkstras Algorithm for path finding: ')
    graph.dijkstra('1', '7')
    graph.dijkstra('1') 
