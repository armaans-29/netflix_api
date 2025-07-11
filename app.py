from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open("recommendations.json") as f:
    data = json.load(f)


@app.route("/recommend", methods=["GET"])
def recommend():
    movie = request.args.get("movie", "").strip().lower()

    # Try to find a matching key ignoring case
    for key in data:
        if key.lower() == movie:
            return jsonify(recommendations=data[key][:4])

    return jsonify(recommendations=[])


if __name__ == "__main__":
    app.run()
