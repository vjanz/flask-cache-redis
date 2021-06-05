import requests
from flask import Flask, jsonify, request
from flask_caching import Cache  # Import Cache from flask_caching module

app = Flask(__name__)
app.config.from_object('config.Config')  # Set the configuration variables to the flask application
cache = Cache(app)  # Initialize Cache


@app.route("/universities")
@cache.cached(timeout=30, query_string=True)
def get_universities():
    API_URL = "http://universities.hipolabs.com/search?country="
    search = request.args.get('country')
    r = requests.get(f"{API_URL}{search}")
    return jsonify(r.json())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
