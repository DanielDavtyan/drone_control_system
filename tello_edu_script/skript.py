import cv2
import numpy as np
import socket
import time

# IP address and port of the WebSocket server
SERVER_IP = "localhost"
SERVER_PORT = 8765

# Tello drone IP address and port
TELLO_IP = "192.168.10.1"
TELLO_PORT = 8889

# Create a UDP socket to send commands to the Tello drone
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Connect to the Tello drone
sock.sendto(b"command", (TELLO_IP, TELLO_PORT))

# Main loop
while True:
    # Get video frame from Tello drone
    try:
        cap = cv2.VideoCapture("udp://@0.0.0.0:11111")
        ret, frame = cap.read()
        if not ret:
            raise Exception("Failed to read frame from Tello drone")
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(1)
        continue

    # Encode video frame as JPEG
    _, encoded_frame = cv2.imencode(".jpg", frame)

    # Send video frame to WebSocket server
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, SERVER_PORT))
            s.sendall(encoded_frame.tobytes())
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(1)
        continue

    # Wait for a moment before capturing the next video frame
    time.sleep(0.1)