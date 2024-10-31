import time
import heapq

# Define a graph class to store vertices and edges
class Graph:
    def __init__(self, vertices, edges):
        self.edges = edges  # List of edges as pairs (u, v)
        self.vertices = vertices  # List of vertices

# Implementation of Bellman-Ford algorithm
def belman_ford(start, end, graph):
    # Initialize distances from start to all vertices as infinite
    length = {vertex: float('inf') for vertex in graph.vertices}
    length[start] = 0  # Distance from start to itself is 0

    # Relax all edges V-1 times (for each vertex except the start)
    for _ in range(len(graph.vertices) - 1):
        updated = False  # Track if an update occurs to stop early if none

        # Iterate over each edge (u, v) to relax distances
        for u, v in graph.edges:
            # Check if a shorter path from u to v exists
            if length[u] != float('inf') and (length[u] + 1) < length[v]:
                length[v] = length[u] + 1  # Update shortest distance
                updated = True

        # If no updates occurred, break out of the loop early
        if not updated:
            break

    return length[end]  # Return shortest path from start to end

# Implementation of Floyd-Warshall algorithm
def floyd_warshall(start, end, graph):
    time_now = time.time()  # Track start time for timeout
    V = len(graph.vertices)  # Number of vertices

    # Initialize distance matrix with infinity, and set distances for edges
    dist = [[float('inf')] * V for _ in range(V)]
    for u, v in graph.edges:
        dist[u][v] = 1  # Distance from u to v is 1

    # Set distance from each vertex to itself to zero
    for i in range(V):
        dist[i][i] = 0

    # Floyd-Warshall main loop: consider each vertex as an intermediate point
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # Exit if the process takes too long (timeout in 5 seconds)
                if time_now + 5 < time.time():
                    return -1  # Return -1 if timeout occurs

                # Update shortest path from i to j if going through k is shorter
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist[start][end]  # Return shortest path from start to end

# Implementation of Dijkstra's algorithm with an adjacency matrix
def dijkstra(start, end, graph):
    V = len(graph.vertices)  # Number of vertices

    # Create an adjacency matrix with infinity values
    adj_matrix = [[float('inf')] * V for _ in range(V)]
    for u, v in graph.edges:
        adj_matrix[u][v] = 1  # Set distance from u to v to 1

    # Initialize distances and visited set
    distances = [float('inf')] * V
    distances[start] = 0  # Distance from start to itself is 0
    visited = set()  # Track visited vertices

    while len(visited) < V:
        # Find the unvisited vertex with the smallest distance
        min_distance = float('inf')
        current_vertex = None
        for vertex in range(V):
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                current_vertex = vertex

        # Exit if no accessible vertex is found
        if current_vertex is None:
            break

        # Return the distance to the end vertex if found
        if current_vertex == end:
            return distances[end]

        visited.add(current_vertex)  # Mark vertex as visited

        # Update distances of neighbors of the current vertex
        for neighbor in range(V):
            if adj_matrix[current_vertex][neighbor] != float('inf') and neighbor not in visited:
                new_distance = distances[current_vertex] + adj_matrix[current_vertex][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances[end]  # Return shortest path from start to end

# Optimized implementation of Dijkstra's algorithm with priority queue (min-heap)
def dijkstra_optimized(start, end, graph):
    # Convert edges to adjacency list for more efficient lookup
    adj_list = {i: [] for i in range(len(graph.vertices))}
    for u, v in graph.edges:
        adj_list[u].append((v, 1))  # (neighbor, weight)

    # Initialize distances and priority queue
    distances = [float('inf')] * len(graph.vertices)
    distances[start] = 0  # Distance from start to itself is 0
    priority_queue = [(0, start)]  # (distance, vertex) pairs in min-heap

    while priority_queue:
        # Extract the vertex with the minimum distance
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Return the distance to the end vertex if reached
        if current_vertex == end:
            return current_distance

        # Process each neighbor of the current vertex
        for neighbor, weight in adj_list[current_vertex]:
            distance = current_distance + weight

            # If a shorter path to neighbor is found, update distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Push updated distance to the priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances[end]  # Return shortest path from start to end
