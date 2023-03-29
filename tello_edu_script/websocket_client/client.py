import base64
import json

UDP_IP = '0.0.0.0'
UDP_PORT = 11111

WEBSOCKET_IP = "127.0.0.1"
WEBSOCKET_PORT = 8888


class Client:
    def __init__(self, commands, websocket):
        self.commands = commands
        self.websocket = websocket

    # async def command_receiver(self):

    async def recv(self):
        while True:
            res = json.loads(self.websocket.recv())
            speeds, commands = res["speeds"], res["commands"]
            self.commands.set_speeds(*speeds)
            self.commands.set_commands(commands)

    # def frame_sender(self):
    #     frame = self.drone.get_frame_read().frame
    #     encoded_frame = base64.b64encode(frame)
    #     protocol =
    #     socket.socket.connect()
