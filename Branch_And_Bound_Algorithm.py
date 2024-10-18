import heapq

# Branch and Bound Greedy with Exit Condition
def branch_and_bound_greedy_exit(graph, start_node, target_node, cost_function, heuristic_function, max_iterations):
    priority_queue = [(0 + heuristic_function(start_node, target_node), 0, [start_node])]
    optimal_cost = float('inf')
    optimal_path = None
    count = 0
    
    while priority_queue:
        count += 1
        if count > max_iterations:
            return optimal_path
        
        (_, current_cost, current_path) = heapq.heappop(priority_queue)
        current_node = current_path[-1]
        
        if current_node == target_node:
            if current_cost < optimal_cost:
                optimal_cost = current_cost
                optimal_path = current_path
            return optimal_path
        
        for neighbor in graph.get(current_node, []):
            if neighbor not in current_path:
                new_path = current_path + [neighbor]
                new_cost = current_cost + cost_function(current_node, neighbor)
                if new_cost < optimal_cost:
                    priority = new_cost + heuristic_function(neighbor, target_node)
                    heapq.heappush(priority_queue, (priority, new_cost, new_path))
    
    return optimal_path


# Branch and Bound with Heuristic
def branch_and_bound_with_heuristic(graph, start_node, target_node, cost_function, heuristic_function):
    priority_queue = [(0 + heuristic_function(start_node, target_node), 0, [start_node])]
    explored = set()
    
    while priority_queue:
        (_, current_cost, current_path) = heapq.heappop(priority_queue)
        current_node = current_path[-1]
        
        if current_node == target_node:
            return current_path
        
        if current_node not in explored:
            explored.add(current_node)
            for neighbor in graph.get(current_node, []):
                if neighbor not in explored:
                    updated_path = current_path + [neighbor]
                    updated_cost = current_cost + cost_function(current_node, neighbor)
                    priority_value = updated_cost + heuristic_function(neighbor, target_node)
                    heapq.heappush(priority_queue, (priority_value, updated_cost, updated_path))
    
    return None


# Branch and Bound Greedy
def branch_and_bound_greedy(graph, start_node, target_node, cost_function, heuristic_function):
    priority_queue = [(0 + heuristic_function(start_node, target_node), 0, [start_node])]
    minimum_cost = float('inf')
    optimal_path = None
    
    while priority_queue:
        _, current_cost, current_path = heapq.heappop(priority_queue)
        current_node = current_path[-1]
        
        if current_node == target_node:
            if current_cost < minimum_cost:
                minimum_cost = current_cost
                optimal_path = current_path
            continue
        
        for neighbor in graph.get(current_node, []):
            if neighbor not in current_path:
                updated_path = current_path + [neighbor]
                path_cost = current_cost + cost_function(current_node, neighbor)
                if path_cost < minimum_cost:
                    priority = path_cost + heuristic_function(neighbor, target_node)
                    heapq.heappush(priority_queue, (priority, path_cost, updated_path))
    
    return optimal_path


# Basic Branch and Bound
def branch_and_bound(graph, start_node, goal_node, cost_function):
    queue = [(0, [start_node])]
    optimal_cost = float('inf')
    optimal_path = None
    
    while queue:
        current_cost, current_path = heapq.heappop(queue)
        current_node = current_path[-1]
        
        if current_node == goal_node:
            if current_cost < optimal_cost:
                optimal_cost = current_cost
                optimal_path = current_path
            continue
        
        for neighbor in graph.get(current_node, []):
            if neighbor not in current_path:
                new_path = current_path + [neighbor]
                new_cost = current_cost + cost_function(current_node, neighbor)
                if new_cost < optimal_cost:
                    heapq.heappush(queue, (new_cost, new_path))
    
    return optimal_path


# Heuristic function based on alphabetical difference
def heuristic_function(node, goal):
    return ord(goal) - ord(node)


# Uniform cost function (constant for this example)
def cost_function(node1, node2):
    return 1


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}


# Example usage for each function
start_node = 'A'
target_node = 'G'
max_iterations = 10

print("Branch and Bound Greedy with Exit path:", branch_and_bound_greedy_exit(graph, start_node, target_node, cost_function, heuristic_function, max_iterations))
print("Branch and Bound with Heuristic path:", branch_and_bound_with_heuristic(graph, start_node, target_node, cost_function, heuristic_function))
print("Branch and Bound Greedy path:", branch_and_bound_greedy(graph, start_node, target_node, cost_function, heuristic_function))
print("Branch and Bound path:", branch_and_bound(graph, start_node, target_node, cost_function))
