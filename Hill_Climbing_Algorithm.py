def hill_climbing(graph, start_node, target_node, heuristic_func):
    current_node = start_node
    path = [current_node]
    
    while current_node != target_node:
        neighbors = graph.get(current_node, [])
        if not neighbors:
            return None
        
        next_node, next_heuristic = min(
            ((neighbor, heuristic_func(neighbor, target_node)) for neighbor in neighbors),
            key=lambda x: x[1]
        )
        
        if next_heuristic >= heuristic_func(current_node, target_node):
            return None
        
        current_node = next_node
        path.append(current_node)
    
    return path

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

def heuristic(node, goal):
    return ord(goal) - ord(node)

start_node = 'A'
target_node = 'G'

result_path = hill_climbing(graph, start_node, target_node, heuristic)
print("Hill Climbing path:", result_path)
