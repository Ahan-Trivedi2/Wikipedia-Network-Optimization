import time
class graph:
    def __init__(self, vertices, edges):
        self.edges = edges
        self.vertices = vertices
        

def belman_ford(start, end, graph):

    length = {vertex: float('inf') for vertex in graph.vertices}
    length[start] = 0

    for _ in range(len(graph.vertices) - 1):

        updated = False
        for u, v in graph.edges:
            if(length[u] != float('inf') and (length[u] + 1) < length[v]):
                length[v] = length[u] + 1
                updated = True

        if not updated:
            break

    return length[end]


def floyd_warshall(start, end, graph):
    
    time_now = time.time()
    # Number of vertices
    V = len(graph.vertices)
    
    # Initialize the distance matrix with the same values as the graph
    dist = [[float('inf')] * V for _ in range(V)]
    
    for u,v in graph.edges:
        dist[u][v] = 1
    
    # Set the distance from each vertex to itself to zero
    for i in range(V):
        dist[i][i] = 0

    # Update distances considering each vertex as an intermediate vertex
    for k in range(V):
        for i in range(V):
            for j in range(V):        
                if time_now + 5 < time.time():
                    return -1
                # If vertex k is on the shortest path from i to j, then update dist[i][j]
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist[start][end]

def dijkstra(start, end, graph):

    V = len(graph.vertices)
    
    adj_matrix = [[float('inf')] * V for _ in range(V)]
    
    for u, v in graph.edges:
        adj_matrix[u][v] = 1

    distances = [float('inf')] * V
    distances[start] = 0
    visited = set()

    while len(visited) < V:
        min_distance = float('inf')
        current_vertex = None

        for vertex in range(V):
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                current_vertex = vertex

        if current_vertex is None: 
            break

        if current_vertex == end:
            return distances[end]

        visited.add(current_vertex)

        for neighbor in range(V):
            if adj_matrix[current_vertex][neighbor] != float('inf') and neighbor not in visited:
                new_distance = distances[current_vertex] + adj_matrix[current_vertex][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    
    return distances[end]
