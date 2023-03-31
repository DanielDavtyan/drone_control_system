import time

from djitellopy import Tello


class Drone:
    def __init__(self):
        self.drone = Tello()
        self.drone.connect()
        self.speeds = Speed()
        self.takeoff = False
        self.is_fliping = False

    def stream_on(self):
        self.drone.streamon()

    def take_off(self):
        self.drone.takeoff()
        self.takeoff = True

    def flip_back(self):
        self.drone.flip_back()

    def land(self):
        self.takeoff = False
        self.drone.land()

    def get_battery(self):
        return self.drone.get_battery()

    def run_command(self, commands):
        for command in commands:
            print(getattr(self, command))
            print(command)
            getattr(self, command)()

    def send_speed(self):
        while self.takeoff:
            if self.is_fliping:
                continue
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
