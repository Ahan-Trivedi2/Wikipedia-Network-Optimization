import pandas as pd
import numpy as np

def read_csv(file_path):
    df = pd.read_csv(file_path)
    print(df.head())

    # Extract unique nodes
    nodes = pd.concat([df['id1'], df['id2']]).unique()
    nodes.sort()

    # Create a mapping from node id to index
    node_index = {node: i for i, node in enumerate(nodes)}

    # Initialize an empty adjacency matrix
    adj_matrix = np.zeros((len(nodes), len(nodes)), dtype=int)

    # Populate the adjacency matrix
    for _, row in df.iterrows():
        i, j = node_index[row['id1']], node_index[row['id2']]
        import random
        if random.random() > .8:
            adj_matrix[i][j] = 2
        else:
            adj_matrix[i][j] = 1
        # adj_matrix[j][i] = 1  # Assuming an undirected graph

    # Print the adjacency matrix
    print("Adjacency Matrix:")
    print(adj_matrix)

    # Create list of indices and labels
    index_labels = [node for node, _i in node_index.items()]
    print("Index-Label Mapping:")
    print(index_labels)

    return adj_matrix, index_labels

# Example usage:
# adj_matrix, index_labels = read_csv('your_file_path.csv')