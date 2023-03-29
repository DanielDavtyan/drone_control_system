import pygame
import time
from djitellopy import Tello


# initialize pygame
pygame.init()

# set screen dimensions
screen_width = 640
screen_height = 480

# create screen
screen = pygame.display.set_mode((screen_width, screen_height))

# set font for text
font = pygame.font.Font(None, 36)

# initialize drone
drone = Tello()

# connect to drone
drone.connect()

# start video stream
drone.streamon()

drone.takeoff()

# set initial values for drone movement
x_speed = 0
y_speed = 0
z_speed = 0
yaw_speed = 0

# set loop speed in seconds
loop_speed = 0.1


# define function to update drone movement based on key input
def update_speeds():
    global x_speed, y_speed, z_speed, yaw_speed

    # reset movement speeds
    x_speed = 0
    y_speed = 0
    z_speed = 0
    yaw_speed = 0

    # get keys pressed
    keys = pygame.key.get_pressed()

    # set movement speeds based on keys pressed
    if keys[pygame.K_UP]:
        z_speed = 30
    elif keys[pygame.K_DOWN]:
        z_speed = -30

    if keys[pygame.K_LEFT]:
        yaw_speed = -50
    elif keys[pygame.K_RIGHT]:
        yaw_speed = 50

    if keys[pygame.K_w]:
        x_speed = 30
    elif keys[pygame.K_s]:
        x_speed = -30

    if keys[pygame.K_a]:
        y_speed = -30
    elif keys[pygame.K_d]:
        y_speed = 30


# main loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update drone movement based on key input
    update_speeds()

    # send movement commands to drone
    drone.send_rc_control(yaw_speed, x_speed, y_speed, z_speed)

    # get current frame from drone camera
    frame = drone.get_frame_read().frame

    # display current frame on screen
    frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
    screen.blit(frame, (0, 0))

    # add text to screen
    text = font.render("Use arrow keys to control drone", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # update display
    pygame.display.update()

    # wait for loop speed
    time.sleep(loop_speed)

# stop video stream
drone.streamoff()

drone.land()


# quit pygame
pygame.quit()
