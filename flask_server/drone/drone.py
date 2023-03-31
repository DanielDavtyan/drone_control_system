import time

from djitellopy import Tello
from flask_server.state_machine.state_machine import DroneState


class Drone:
    def __init__(self):
        self.drone = Tello()
        self.drone.connect()
        self.speeds = Speed()
        self.state = DroneState

    def stream_on(self):
        self.drone.streamon()

    def take_off(self):
        self.state.take_off()
        self.drone.takeoff()
        self.state.waiting()

    def flip_back(self):
        self.state.flip_back()
        self.drone.flip_back()
        self.state.waiting()

    def land(self):
        self.drone.land()
        self.drone.land()
        self.drone.on_floor()

    def get_battery(self):
        return self.drone.get_battery()

    def send_speed(self):
        while self.state.state == "waiting":
            self.drone.send_rc_control(*self.speeds.get_speeds())
            time.sleep(0.03)


class Speed:
    def __init__(self):
        self.last_update_time = time.time()
        self.forward = 0
        self.left = 0
        self.up = 0
        self.yaw = 0

    def set_speed(self, forward, left, up, yaw):
        self.last_update_time = time.time()
        self.forward = forward
        self.left = left
        self.up = up
        self.yaw = yaw

    def get_speeds(self):
        res = int(self.left), int(self.forward), int(self.up), int(self.yaw)
        if time.time() - self.last_update_time > 0.1:
            self.reset()
        return res

    def reset(self):
        self.left = self.forward = self.up = self.yaw = 0
