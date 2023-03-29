import pygame
import time

from drone_control_system.tello_edu_script.command_getter.command_getter import CommandGetter
from drone_control_system.tello_edu_script.command_getter.commands import Command
from drone_control_system.tello_edu_script.websocket_client.client import Client
from local_front.pygame_front import PyFront
from drone.drone import Drone

drone = Drone()

drone.stream_on()

drone.take_off()

run_local = True

command = Command()

if run_local:
    command_getter = CommandGetter(command)
else:
    websocket_client = ""  # create client
    client = Client(command, websocket_client)
    client.recv()

py_front = PyFront(drone.drone, 1024, 1024)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if run_local:
        speeds, commands = command_getter.get_speeds_and_commands()
        command.set_speed(*speeds)
        command.set_commands(commands)

    speeds, commands = command.get_speeds_and_commands()

    drone.run_command(commands)

    py_front.print_frame()

    drone.drone.send_rc_control(*speeds)

    pygame.display.update()

    time.sleep(0.01)

drone.drone.streamoff()

drone.drone.land()

py_front.quit()
