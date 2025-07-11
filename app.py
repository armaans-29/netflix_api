from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# Load data
json_path = os.path.join(os.path.dirname(__file__), "recommendations.json")
with open(json_path) as f:
    data = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["GET"])
def recommend():
    movie = request.args.get("movie")
    recs = data.get(movie, [])
    return render_template("index.html", recommendations=recs, movie=movie)

if __name__ == "__main__":
    app.run()
