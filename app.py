from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(_name_)

# Load recommendations.json using the correct path
json_path = os.path.join(os.path.dirname(_file_), "recommendations.json")
with open(json_path) as f:
    data = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['GET'])
def recommend():
    movie = request.args.get("movie")
    recs = data.get(movie, [])[:4]  # Limit to first 4 recommendations
    return jsonify(recommendations=recs)

if _name_ == "_main_":
    app.run()