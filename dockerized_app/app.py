
from flask import Flask, jsonify
import requests

app = Flask(__name__)

URL = "https://rickandmortyapi.com/api/character"

@app.route("/data", methods=["GET"])
def get_data():
    params = {
        "species": "Human",
        "status": "Alive",
        "origin": "Earth"
    }
    response = requests.get(URL, params=params)
    data = response.json()
    
    characters = []
    for character in data["results"]:
        name = character["name"]
        location = character["origin"]["name"]
        image = character["image"]
        characters.append({"Name": name, "Location": location, "Image": image})
    
    return jsonify(characters)

@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
