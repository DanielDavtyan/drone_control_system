import time
import enum

from djitellopy import Tello


class State(enum):
    ON_FLOOR = 1
    TAKE_OFF = 2
    WAITING = 3
    MOVE = 4
    FLIP = 5
    LAND = 6


class DroneState:

    def __init__(self):
        self.state = State.ON_FLOOR
        self.drone = Tello()
        self.speeds = Speed()
        self.drone.connect()

    def take_off(self):
        if self.state != State.ON_FLOOR:
            return  # TODO raise exaption for state changing
        self.state = State.TAKE_OFF
        self.drone.takeoff()  # TODO Handle error
        self.state = State.WAITING

    def flip_back(self):
        if self.state != State.WAITING:
            return  # TODO Handle this case (throw this case)
        self.state = State.FLIP
        self.drone.flip_back()  # TODO Catch command not completed error! (call again)
        self.state = State.WAITING

    def land(self):
        if self.state != State.WAITING:
            return  # TODO
        self.state = State.LAND
        self.drone.land()  # TODO Catch command not completed error! (call again)
        self.state = State.ON_FLOOR

    def get_battery(self):
        return self.drone.get_battery()

    def send_speed(self):
        if self.state != State.WAITING:
            return

        self.state = State.MOVE

        while self.state == State.MOVE:
            current_speed = self.speeds.get_speeds()
            if current_speed == (0, 0, 0, 0):
                self.state = State.WAITING
            self.drone.send_rc_control(*current_speed)
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
