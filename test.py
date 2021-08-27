#!/usr/bin/env python

# WS server example

import asyncio
import sys

import websockets

async def hello(websocket, path):
    name = await websocket.receive()
    print(f"<<< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f">>> {greeting}")

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  # run forever

# if sys.platform == "win32" and (3, 8, 0) <= sys.version_info < (3, 9, 0):
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(main())