from flask import Flask, request, jsonify, render_template
import json

app = Flask(_name_)

with open("recommendations.json") as f:
    data = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["GET"])
def recommend():
    movie = request.args.get("movie")
    recs = data.get(movie, [])
    return jsonify(recommendations=recs)

if _name_ == "_main_":
    app.run(debug=True)