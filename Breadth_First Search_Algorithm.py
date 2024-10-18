from collections import deque

def breadth_first_search(graph, start_node, target_node):
    queue = deque([(start_node, [start_node])])
    visited = set([start_node])  
    
    while queue:
        current_vertex, path = queue.popleft()
        
        if current_vertex == target_node:
            return path
        
        for neighbor in graph.get(current_vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))  

    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

start_node = 'A'
target_node = 'G'

result_path = breadth_first_search(graph, start_node, target_node)
print("BFS path:", result_path)
