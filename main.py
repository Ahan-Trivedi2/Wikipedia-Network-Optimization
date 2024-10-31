from create_graph import convert_csv_to_graph, get_vertex_number
from algorithms import *

# Call the function with the path to your CSV file
file_path = 'output.csv'
vertices, edges, vertex_to_index = convert_csv_to_graph(file_path)

g = graph(vertices, edges)

print(floyd_warshall((get_vertex_number('Pleasant Valley, Portland, Oregon', vertex_to_index)),(get_vertex_number('Honeybees', vertex_to_index)),g))
print(get_vertex_number('Portland, Oregon', vertex_to_index))
print(get_vertex_number('Discrete mathematics', vertex_to_index))