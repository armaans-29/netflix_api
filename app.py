from flask import Flask, request, render_template
import json
import os

app = Flask(__name__)

# Load recommendations and normalize keys to lowercase
json_path = os.path.join(os.path.dirname(__file__), "recommendations.json")
with open(json_path) as f:
    raw_data = json.load(f)
    data = {k.lower(): v for k, v in raw_data.items()}  # <-- normalize keys

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend", methods=["GET"])
def recommend():
    movie = request.args.get("movie", "").lower()  # <-- convert user input to lowercase
    recs = data.get(movie, [])
    return render_template("index.html", recommendations=recs, movie=movie)
