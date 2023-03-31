import json

from flask import Flask, request
from drone_control_system.flask_server.drone.drone import Drone
from drone_control_system.flask_server.helpers.helpers import validate_parameters

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


@app.route("/battery", methods=["GET"])
def battery():
    response = json.dumps({"battery_level": drone.get_battery()})
    return response


@app.route("/land")
def land():
    drone.land()
    drone.takeoff = False
    return json.dumps({"test": "test"})


@app.route("/flip_back")
def flip_back():
    drone.is_fliping = True
    drone.flip_back()
    drone.is_fliping = False
    return json.dumps({"test": "test"})


app.run(port=8888)
