import random

def random_walk_search(graph, start_node, target_node):
    path = [start_node]
    visited = set([start_node])  
    while path[-1] != target_node:
        current_node = path[-1]
        if current_node in graph and graph[current_node]:  
            next_node = random.choice(graph[current_node])
            if next_node not in visited:
                visited.add(next_node)
                path.append(next_node)
        else:
            break
    
    return path if path[-1] == target_node else None

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

result_path = random_walk_search(graph, start_node, target_node)
print("Random Walk Search path:", result_path)
