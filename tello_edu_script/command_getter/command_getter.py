import time

import pygame


class CommandGetter:
    def __init__(self, commands):
        self.last_time = {}
        self.commands = commands

    def get_speeds_and_commands(self):
        return self._get_pressed_keys()

    def _get_pressed_keys(self):
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
        speeds = (forward, right, up, yaw)
        return speeds, commands
