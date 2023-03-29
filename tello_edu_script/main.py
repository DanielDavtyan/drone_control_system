import pygame
import time

from local_front.pygame_front import PyFront
from tello_edu_script.drone.drone import Drone


drone = Drone()

drone.stream_on()

drone.take_off()


py_front = PyFront(drone.drone)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    speeds, commands = drone.get_pressed_keys()

    drone.speed.set_speed(*speeds)

    drone.run_command(commands)

    py_front.print_frame()

    drone.drone.send_rc_control(*drone.speed.get_speeds())

    pygame.display.update()

    time.sleep(0.01)

drone.drone.streamoff()

drone.drone.land()

py_front.quit()
