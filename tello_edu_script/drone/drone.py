import time

import pygame
from djitellopy import Tello


class Speed:
    def __init__(self):
        self.forward = self.right = self.up = self.yaw = 0

    def set_speed(self, forward, right, up, yaw):
        self.forward = forward
        self.right = right
        self.up = up
        self.yaw = yaw

    def get_speeds(self):
        return self.right, self.forward, self.up, self.yaw


class Drone:
    def __init__(self):
        self.drone = Tello()
        self.drone.connect()
        self.speed = Speed()
        self.last_time = {}

    def stream_on(self):
        self.drone.streamon()

    def take_off(self):
        self.drone.takeoff()

    def flip_back(self):
        self.drone.flip_back()

    def get_pressed_keys(self):
        forward = 0
        right = 0
        up = 0
        yaw = 0
        commands = []

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            forward += 30
        if keys[pygame.K_DOWN]:
            forward -= 30
        if keys[pygame.K_LEFT]:
            right -= 30
        if keys[pygame.K_RIGHT]:
            right += 30
        if keys[pygame.K_w]:
            up += 30
        if keys[pygame.K_s]:
            up -= 30
        if keys[pygame.K_a]:
            yaw -= 30
        if keys[pygame.K_d]:
            yaw += 30
        if keys[pygame.K_f]:
            if "flip_back" in self.last_time:
                if time.time() - self.last_time["flip_back"] > 2:
                    return
            self.last_time["flip_back"] = time.time()
            commands.append("flip_back")
        speeds = (right, forward, up, yaw)
        return speeds, commands

    def run_command(self, commands):
        for command in commands:
            print(getattr(self, command))
            print(command)
            getattr(self, command)()