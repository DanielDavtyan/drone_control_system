from djitellopy import Tello


class Drone:
    def __init__(self):
        self.drone = Tello()
        self.drone.connect()

    def stream_on(self):
        self.drone.streamon()

    def take_off(self):
        self.drone.takeoff()

    def flip_back(self):
        self.drone.flip_back()

    def run_command(self, commands):
        for command in commands:
            print(getattr(self, command))
            print(command)
            getattr(self, command)()
