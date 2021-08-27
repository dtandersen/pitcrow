import dataclasses
import json
import asyncio
from typing import Optional

import websockets

from telemetry import UdpTelemetrySource, TelemetrySource
from packet import DashPacket
from signal import TelemetryListener




class TelemetryServer(TelemetryListener):
    def __init__(self, telemetry_source: TelemetrySource):
        self.data = None
        self.websocket = None
        self.telemetry_source = telemetry_source

    def receive(self, data: DashPacket):
        # if self.websocket is None:
        #     return

        # print("got data")
        self.data = data
        # x = json.dumps(self.data, cls=EnhancedJSONEncoder)
        # try:
        #     print("sending" + x)
        #     asyncio.run(self.websocket.send(x))
        # except ConnectionClosedOK:
        #     pass

    async def time(self, websocket, path):
        self.websocket = websocket
        self.telemetry_source.init()
        while True:
            self.telemetry_source.receive()
            if self.data is None:
                # print("no data")
                continue

            x = json.dumps(self.data, cls=EnhancedJSONEncoder)
            self.data = None
            await websocket.send(x)


async def main():
    telemetry_source = UdpTelemetrySource([])
    server = TelemetryServer(telemetry_source)
    telemetry_source.watchers = [server]

    async with websockets.serve(server.time, "localhost", 5678):
        await asyncio.Future()  # run forever


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
