from flask import Flask, render_template, request, jsonify
from read_csv import read_csv

app = Flask(__name__)

# Sample adjacency matrix
#adjacency_matrix = read_csv(file_path = 'wikipedia/chameleon/musae_chameleon_edges.csv')


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        input1 = request.form.get("input1")
        input2 = request.form.get("input2")
        dropdown = request.form.get("dropdown")
        # Perform search or handle the form data as needed
        return f"You searched for: Input 1 = {input1}, Input 2 = {input2}, Dropdown = {dropdown}"
    return render_template("index.html")

@app.route("/suggest", methods=["GET"])
def suggest():
    limited_matrix, labels = read_csv(file_path="output_short.csv")

    query = request.args.get("query", "").lower()
    matches = [item for item in labels if query in item.lower()]
    return jsonify(matches)

@app.route("/suggest2", methods=["GET"])
def suggest2():
    limited_matrix, labels = read_csv(file_path="output_short.csv")
    query = request.args.get("query", "").lower()
    matches = [item for item in labels if query in item.lower()]
    return jsonify(matches)

@app.route("/get_adjacency_matrix", methods=["GET"])
def get_adjacency_matrix():
    limited_matrix, labels = read_csv(file_path="output_short.csv")
    # Return a submatrix for visualization to reduce complexity
    submatrix_size = len(labels)
    limited_matrix = limited_matrix[:submatrix_size, :submatrix_size]
    return jsonify({"matrix": limited_matrix.tolist(), "labels": labels[:submatrix_size]})

if __name__ == "__main__":
    app.run(debug=True)
