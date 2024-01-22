import heapq

def dijkstra(graph, start, end):
    priority_queue = [(0, start)]
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    previous = {node: None for node in graph}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    
    path.reverse()

    return path, distances[end]

graph = {
    "Kyiv": {"Lviv": 541, "Kharkiv": 479, "Odesa": 476},
    "Lviv": {"Uzhhorod": 248, "Kyiv": 541, "Dnipro": 950},
    "Kharkiv": {"Dnipro": 218, "Dnipro": 386},
    "Dnipro": {"Odesa": 480, "Donetsk": 266, "Kyiv": 399},
    "Odesa": {"Lviv": 796, "Kyiv": 476},
    "Uzhhorod": {"Lviv": 220, "Kyiv": 919, "Odesa": 1018},
    "Donetsk": {"Odesa": 674}
}

shortest_path, shortest_distance = dijkstra(graph, "Uzhhorod", "Donetsk")

print(f"Shortest path: {shortest_path}")
print(f"Shortest distance: {shortest_distance} km")
