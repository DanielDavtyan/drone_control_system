import json

from flask import Flask, request
from flask_server.drone.drone import Drone
from flask_server.helpers.helpers import validate_parameters

app = Flask(__name__)

drone = Drone()


@app.route("/speed")
def set_speed():
    validate_parameters(["forward", "left", "up", "yaw"], request.form.to_dict())
    coordinates = request.form.to_dict()
    drone.speeds.set_speed(**coordinates)
    return json.dumps({"success": "test"})


@app.route("/take_off")
def take_off():
    try:
        drone.take_off()
        drone.send_speed()
        return json.dumps({"status": "Succeeded"})
    except Exception as exception:
        return json.dumps({"exception": str(exception)})


@app.route("/land")
def land():
    drone.land()
    return json.dumps({"test": "test"})


@app.route("/flip_back")
def flip_back():
    drone.flip_back()
    drone.send_speed()
    drone.state.waiting()
    return json.dumps({"test": "test"})


@app.route("/battery", methods=["GET"])
def battery():
    response = json.dumps({"battery_level": drone.get_battery()})
    return response


app.run(port=8888)
