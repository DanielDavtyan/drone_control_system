class Command:
    def __init__(self):
        self.forward = self.right = self.up = self.yaw = 0
        self.commands = []

    def set_speed(self, forward, right, up, yaw):
        self.forward = forward
        self.right = right
        self.up = up
        self.yaw = yaw

    def set_commands(self, commands):
        self.commands = commands

    def reset(self):
        self.forward = self.right = self.up = self.yaw = 0
        self.commands = []

    def get_speeds_and_commands(self):
        res = (self.right, self.forward, self.up, self.yaw), self.commands
        self.reset()
        return res