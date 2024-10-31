import time
from flask import Flask, render_template, request, jsonify
from read_csv import read_csv, read_nodes
from create_graph import convert_csv_to_graph, get_vertex_number
from algorithms import *

app = Flask(__name__)

# Sample adjacency matrix
#adjacency_matrix = read_csv(file_path = 'wikipedia/chameleon/musae_chameleon_edges.csv')
_, labels = read_csv(file_path="output.csv")
file_path = 'output.csv'
vertices, edges, vertex_to_index = convert_csv_to_graph(file_path)
g = graph(vertices, edges)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print("D")
        input1 = request.form.get("input1")
        input2 = request.form.get("input2")
        # Perform search or handle the form data as needed
        print("A")
        start_time = time.time()
        belman_ford_result = belman_ford((get_vertex_number(input1, vertex_to_index)),(get_vertex_number(input2, vertex_to_index)),g)
        belman_ford_time = time.time() - start_time
        print("B")
        dijkstra_result = dijkstra((get_vertex_number(input1, vertex_to_index)),(get_vertex_number(input2, vertex_to_index)),g)
        dijkstra_time = time.time() - start_time - belman_ford_time
        print("E")
        floyd_warshall_result = floyd_warshall((get_vertex_number(input1, vertex_to_index)),(get_vertex_number(input2, vertex_to_index)),g)
        floyd_warshall_time = time.time() - start_time - belman_ford_time - dijkstra_time
        print("C")
        if floyd_warshall_result == -1:
            floyd_warshall_result = "Took too Long"
            floyd_warshall_time = "Timeout"
        return render_template('results.html', belman_ford_result=belman_ford_result, dijkstra_result=dijkstra_result,
                               floyd_warshall_result=floyd_warshall_result, belman_ford_time=belman_ford_time, 
                               dijkstra_time=dijkstra_time, floyd_warshall_time=floyd_warshall_time)
    return render_template("index.html")

@app.route("/suggest", methods=["GET"])
def suggest():
    query = request.args.get("query", "").lower()
    matches = [item for item in labels if query in item.lower()]
    return jsonify(matches[:10])

@app.route("/suggest2", methods=["GET"])
def suggest2():
    print("suggest2")
    query = request.args.get("query", "").lower()
    matches = [item for item in labels if query in item.lower()]
    return jsonify(matches[:10])


if __name__ == "__main__":
    app.run(debug=True)
