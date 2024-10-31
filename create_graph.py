import csv

def convert_csv_to_graph(file_path):
    # Open and read the CSV file with utf-8 encoding
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header

        # Collecting unique vertices and edges
        vertices_set = set()
        edges = []

        for row in reader:
            source, target = row
            vertices_set.add(source)
            vertices_set.add(target)
            edges.append((source, target))

    # Converting vertices to indices
    vertices = sorted(vertices_set)  # Sort vertices for consistent indexing
    vertex_to_index = {v: i for i, v in enumerate(vertices)}

    # Convert edges to indices
    indexed_edges = [(vertex_to_index[src], vertex_to_index[dst]) for src, dst in edges]

    # Index-based vertices list
    vertices_list = list(range(len(vertices)))
    
    return vertices_list, indexed_edges, vertex_to_index

def get_vertex_number(vertex_name, vertex_to_index):
    """Return the vertex number for a given vertex name."""
    return vertex_to_index.get(vertex_name, None)

"""
# Call the function with the path to your CSV file
file_path = 'output.csv'
vertices, edges, vertex_to_index = convert_csv_to_graph(file_path)

# Output the result
print("Vertices:", vertices)
print("Edges:", edges)

# Example usage of get_vertex_number
vertex_name = 'Discrete mathematics'
vertex_number = get_vertex_number(vertex_name, vertex_to_index)

if vertex_number is not None:
    print(f"The vertex number for '{vertex_name}' is {vertex_number}.")
else:
    print(f"'{vertex_name}' does not exist in the graph.")
"""