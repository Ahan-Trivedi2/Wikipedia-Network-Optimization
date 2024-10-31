import time
from flask import Flask, render_template, request, jsonify
from read_csv import read_csv, read_nodes
from create_graph import convert_csv_to_graph, get_vertex_number
from algorithms import *

# Initialize Flask application
app = Flask(__name__)

# Load graph data
# Read vertex labels from CSV file and set up file path for edges
_, labels = read_csv(file_path="output.csv")
file_path = 'output.csv'

# Convert CSV data to graph representation with vertices, edges, and vertex-to-index mapping
vertices, edges, vertex_to_index = convert_csv_to_graph(file_path)
g = Graph(vertices, edges)  # Create graph object

# Define route for home page
@app.route("/", methods=["GET", "POST"])
def home():
    # Check if the request is a POST request
    if request.method == "POST":
        input1 = request.form.get("input1")  # Get starting vertex from form
        input2 = request.form.get("input2")  # Get ending vertex from form

        # Run Bellman-Ford algorithm and time the execution
        start_time = time.time()
        belman_ford_result = belman_ford(get_vertex_number(input1, vertex_to_index), get_vertex_number(input2, vertex_to_index), g)
        belman_ford_time = time.time() - start_time  # Calculate elapsed time

        # Run optimized Dijkstra algorithm and time the execution
        start_time = time.time()
        dijkstra_result = dijkstra_optimized(get_vertex_number(input1, vertex_to_index), get_vertex_number(input2, vertex_to_index), g)
        dijkstra_time = time.time() - start_time  # Calculate elapsed time

        # Run Floyd-Warshall algorithm and time the execution
        start_time = time.time()
        floyd_warshall_result = floyd_warshall(get_vertex_number(input1, vertex_to_index), get_vertex_number(input2, vertex_to_index), g)
        floyd_warshall_time = time.time() - start_time  # Calculate elapsed time

        # Handle timeout case for Floyd-Warshall
        if floyd_warshall_result == -1:
            floyd_warshall_result = "Took too Long"  # Indicate timeout in results
            floyd_warshall_time = "Timeout"  # Set time as "Timeout" if algorithm timed out

        # Render results page with algorithm results and times
        return render_template('results.html', belman_ford_result=belman_ford_result, dijkstra_result=dijkstra_result,
                               floyd_warshall_result=floyd_warshall_result, belman_ford_time=belman_ford_time, 
                               dijkstra_time=dijkstra_time, floyd_warshall_time=floyd_warshall_time)
    
    # If request is GET, render the main index page
    return render_template("index.html")

# Define route for suggestions based on input query (autocomplete feature)
@app.route("/suggest", methods=["GET"])
def suggest():
    query = request.args.get("query", "").lower()  # Get query parameter and convert to lowercase
    matches = [item for item in labels if query in item.lower()]  # Find labels that match query
    return jsonify(matches[:10])  # Return top 10 matching results as JSON

# Define additional suggestion route with similar functionality
@app.route("/suggest2", methods=["GET"])
def suggest2():
    query = request.args.get("query", "").lower()  # Get query parameter and convert to lowercase
    matches = [item for item in labels if query in item.lower()]  # Find labels that match query
    return jsonify(matches[:10])  # Return top 10 matching results as JSON

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
