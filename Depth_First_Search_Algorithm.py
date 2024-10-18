def depth_first_search(graph, start_node, target_node):
    stack = [(start_node, [start_node])]
    visited_nodes = set([start_node])  
    
    while stack:
        current_vertex, current_path = stack.pop()
        
        if current_vertex == target_node:
            return current_path
        
        for neighbor in reversed(graph.get(current_vertex, [])):  
            if neighbor not in visited_nodes:
                visited_nodes.add(neighbor)
                stack.append((neighbor, current_path + [neighbor]))
    
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

result_path = depth_first_search(graph, start_node, target_node)
print("DFS path:", result_path)
