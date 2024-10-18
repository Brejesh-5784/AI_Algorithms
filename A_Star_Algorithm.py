import heapq

def a_star_algorithm(graph, start_node, goal_node, cost_function, heuristic_function):
    priority_queue = [(0 + heuristic_function(start_node, goal_node), 0, [start_node])]
    explored_nodes = set()
    
    while priority_queue:
        _, current_cost, path_travelled = heapq.heappop(priority_queue)
        current_node = path_travelled[-1]
        
        if current_node == goal_node:
            return path_travelled
        
        if current_node not in explored_nodes:
            explored_nodes.add(current_node)
            
            for neighbor in graph.get(current_node, []):
                if neighbor not in explored_nodes:
                    new_path = path_travelled + [neighbor]
                    total_cost = current_cost + cost_function(current_node, neighbor)
                    priority_value = total_cost + heuristic_function(neighbor, goal_node)
                    heapq.heappush(priority_queue, (priority_value, total_cost, new_path))
    
    return None

# Example usage
graph_structure = {
    'A': {'B': 1, 'C': 2},
    'B': {'D': 3, 'E': 4},
    'C': {'F': 2},
    'D': {},
    'E': {'G': 2},
    'F': {'G': 1},
    'G': {}
}

def cost_function(node1, node2):
    return graph_structure[node1][node2]

def heuristic_function(node, goal_node):
    return abs(ord(goal_node) - ord(node))

start_node = 'A'
goal_node = 'G'

path_result = a_star_algorithm(graph_structure, start_node, goal_node, cost_function, heuristic_function)
if path_result:
    print("A* algorithm found the path:", path_result)
else:
    print("No path found.")
