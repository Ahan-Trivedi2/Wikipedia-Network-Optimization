from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample list for live search suggestions
suggestions = [
    "Apple",
    "Banana",
    "Cherry",
    "Date",
    "Elderberry",
    "Fig",
    "Grape",
    "Honeydew",
]


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
    query = request.args.get("query", "").lower()
    matches = [item for item in suggestions if query in item.lower()]
    return jsonify(matches)


@app.route("/suggest2", methods=["GET"])
def suggest2():
    query = request.args.get("query", "").lower()
    matches = [item for item in suggestions if query in item.lower()]
    return jsonify(matches)


if __name__ == "__main__":
    app.run(debug=True)
