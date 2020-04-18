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
        
        
        for node in self.graph[start]:
            queue.append(node)
            visited_nodes.add(node)
            search_order.append(node)
        
        while queue:
            current_node = queue.popleft()
            
            for node in self.graph[str(current_node)]:
                if node not in visited_nodes:
                    visited_nodes.add(node)
                    queue.append(node)
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
            for adjacent in self.graph[str(node)]:
                if adjacent not in visited_nodes:
                    visited_nodes.add(adjacent)
                    recursion_order.append(adjacent)
                    traverse(adjacent)
                    
        visited_nodes = {int(start)}
        recursion_order = []
        
        for node in self.graph[start]:
            if node not in visited_nodes:
                recursion_order.append(node)
                traverse(node)
        
        return recursion_order

if __name__ == '__main__':
    g = {
        '1': [2, 3, 6, 7],
        '2': [1, 4],
        '3': [1, 5, 6, 7],
        '4': [2],
        '5': [3],
        '6': [1, 3, 9],
        '7': [1, 3, 8],
        '8': [7],
        '9': [6]
    }
    
    graph = Graph(g)
    
    print(f'Graph: {graph.graph}')
    
    print('#'*8)
    
    print('Breadth First Search visiting order: ')
    print(graph.bfs('1'))
    
    print('#'*8)
    
    print('Depth First Search visiting order: ')
    print(graph.dfs('1'))
