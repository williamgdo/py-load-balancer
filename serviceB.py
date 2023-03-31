from flask import Flask, request, jsonify
from pymongo import MongoClient
import time
import json

# global variables
SERVICE_NAME = "A'"
CONNECTION_STRING = "mongodb://localhost:27017/"


# the service A' should compute b^a
def compute(a, b):
    return b**a


client = MongoClient(CONNECTION_STRING)
db = client["project"]
calculations = db["calculations"]

app = Flask(__name__)


@app.route("/calculate", methods=["POST"])
def calculate():
    inputJson = request.get_json(force=True)
    # force=True, above, is necessary if another developer
    # forgot to set the MIME type to 'application/json'

    x = inputJson["x"]
    y = inputJson["y"]
    ts = time.time()
    result = compute(x, y)

    document = {
        "timestamp": ts,
        "a": x,
        "b": y,
        "resultado": result,
        "microservice": SERVICE_NAME,
    }

    # store in BD
    calculations.insert_one(document)

    return json.dumps(document, default=str)


@app.route("/values", methods=["GET"])
def values():
    calculationsDocuments = calculations.find({}, {"_id": False})
    # removes _id from documents because ObjectId is not JSON serializable

    return jsonify([row for row in calculationsDocuments])
    # one liner for making a JSON with all rows from calculationsDocuments


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    # debug=True detects change
