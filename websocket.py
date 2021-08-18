import dataclasses
import json
import threading
import datetime
import random
import asyncio
import websockets
from websockets.exceptions import ConnectionClosedOK

from listener import Listener
from packet import DashPacket
from signal import DataListener


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


class JsonSender(DataListener):
    def __init__(self):
        self.data = None
        self.websocket = None

    def recv(self, data: DashPacket):
        # if self.websocket is None:
        #     return

        print("got data")
        self.data = data
        # x = json.dumps(self.data, cls=EnhancedJSONEncoder)
        # try:
        #     print("sending" + x)
        #     asyncio.run(self.websocket.send(x))
        # except ConnectionClosedOK:
        #     pass

    async def time(self, websocket, path):
        self.websocket = websocket
        listener.init()
        while True:
            listener.read_data()
            if self.data is None:
                print("no data")
                continue

            x = json.dumps(self.data, cls=EnhancedJSONEncoder)
            self.data = None
            await websocket.send(x)


async def main():
    async with websockets.serve(sender.time, "localhost", 5678):
        await asyncio.Future()  # run forever


sender = JsonSender()
listener = Listener(sender)
# x = threading.Thread(target=listener.go)
# x.start()

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
