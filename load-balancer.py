# basic server example

import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
# loadbalancer = Flask(__name__)

BACKENDS = ["http://service-a:5000", "http://service-b:5000"]
# 5000 is the default port for flask applications
CURRENT_BACKEND = 0


@app.route("/power", methods=["POST"])
def postPower():
    global CURRENT_BACKEND
    inputJson = request.get_json(force=True)
    # force=True, above, is necessary if another developer
    # forgot to set the MIME type to 'application/json'

    x = inputJson["x"]
    y = inputJson["y"]

    dictToSend = {"x": x, "y": y}

    try:
        res = requests.post(BACKENDS[CURRENT_BACKEND] + "/calculate", json=dictToSend)

        CURRENT_BACKEND = (CURRENT_BACKEND + 1) % 2

        dictFromServer = res.json()
        return dictFromServer
    except Exception as e:
        print("An exception occurred: " + str(e))
        return jsonify(message="An exception occurred: " + str(e))


# we can make the load-balancer request in loop by making the request over and over until completed
# requestCompleted = False
# while requestCompleted == False:
#     try:
#         res = requests.post(BACKENDS[CURRENT_BACKEND] + "/calculate", json=dictToSend)
#         requestCompleted = True
#     except requests.exceptions.RequestException as e:
#         CURRENT_BACKEND = (CURRENT_BACKEND + 1) % 2
#         time.sleep(5)

# dictFromServer = res.json()
# return dictFromServer


@app.route("/power", methods=["GET"])
def getPower():
    global CURRENT_BACKEND

    try:
        res = requests.get(BACKENDS[CURRENT_BACKEND] + "/values")

        CURRENT_BACKEND = (CURRENT_BACKEND + 1) % 2

        dictFromServer = res.json()
        return dictFromServer
    except Exception as e:
        print("An exception occurred: " + str(e))
        return jsonify(message="An exception occurred: " + str(e))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
