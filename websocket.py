import dataclasses
import json
import threading
import asyncio
import websockets
import asyncio
import datetime
import random
import websockets

from listener import Listener
from packet import DashPacket
from signal import DataListener


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


#
#
class JsonSender(DataListener):
    def __init__(self):
        self.data = None

    def recv(self, data: DashPacket):
        self.data = data

    async def time(self, websocket, path):
        while True:
            if self.data is None:
                print("no data")
                continue
            now = datetime.datetime.utcnow().isoformat() + "Z"
            x = json.dumps(self.data, cls=EnhancedJSONEncoder)
            print(x)
            await websocket.send(x)
            await asyncio.sleep(random.random() * 3)

    #
    #
    # async def hello(websocket, path):
    #     name = await websocket.recv()
    #     print(f"< {name}")
    #
    #     greeting = f"Hello {name}!"
    #
    #     await websocket.send(greeting)
    #     print(f"> {greeting}")
    #
    #

    # if __name__ == '__main__':


sender = JsonSender()

listener = Listener(sender)
x = threading.Thread(target=listener.go)
x.start()
#
#     # start_server = websockets.serve(hello, "localhost", 8765)
#     #
#     # asyncio.get_event_loop().run_until_complete(start_server)
#     # asyncio.get_event_loop().run_forever()
#
#     start_server = websockets.serve(time, "127.0.0.1", 5678)
#
#     asyncio.get_event_loop().run_until_complete(start_server)
#     asyncio.get_event_loop().run_forever()


import asyncio
import websockets


async def hello(websocket, path):
    # name = await websocket.recv()
    # print(f"<<< {name}")
    #
    # greeting = f"Hello {name}!"

    await websocket.send("x")
    # print(f">>> {greeting}")


async def main():
    print("main")
    async with websockets.serve(sender.time, "localhost", 5678):
        await asyncio.Future()  # run forever


print("x")

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
print("y")

asyncio.run(main())
