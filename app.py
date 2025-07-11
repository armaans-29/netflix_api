from flask import Flask, request, render_template
import json
import os

app = Flask(__name__)

# Load JSON file safely
json_path = os.path.join(os.path.dirname(__file__), "recommendations.json")
with open(json_path, "r") as f:
    data = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["GET"])
def recommend():
    movie_input = request.args.get("movie", "").strip().lower()
    recommendations = []

    for title, recs in data.items():
        if title.strip().lower() == movie_input:
            recommendations = recs
            break

    return render_template("index.html", movie=request.args.get("movie", ""), recommendations=recommendations)

if __name__ == "__main__":
    app.run()
