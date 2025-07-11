from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# ✅ Correct way to get the full path to the JSON file
json_path = os.path.join(os.path.dirname(__file__), "recommendations.json")
with open(json_path) as f:
    data = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["GET"])
def recommend():
    movie = request.args.get("movie")
    recs = data.get(movie, [])[:4]
    return jsonify(recommendations=recs)

if __name__ == "__main__":
    app.run()
