import time

import pygame


class PyFront:
    def __init__(self, drone, screen_width, screen_height):
        # initialize pygame
        pygame.init()

        # set screen dimensions
        self.screen_width = screen_width
        self.screen_height = screen_height

        # create screen
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # set font for text
        self.font = pygame.font.Font(None, 36)

        self.drone = drone

    def print_frame(self):
        # get current frame from drone camera
        frame = self.drone.get_frame_read().frame

        # display current frame on screen
        frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        self.screen.blit(frame, (0, 0))

        # add text to screen
        text = self.font.render("Use arrow keys to control drone", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

        # update display
        pygame.display.update()

    @staticmethod
    def quit():
        pygame.quit()
