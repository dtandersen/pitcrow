import socket
from abc import ABCMeta, abstractmethod
from typing import List

from tornado import gen

from packet import DashCodec, DashPacket
from signal import TelemetryListener

UDP_IP = '0.0.0.0'
UDP_PORT = 20127


class TelemetrySource(metaclass=ABCMeta):
    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def receive(self):
        pass


class UdpTelemetrySource(TelemetrySource):
    def __init__(self, watchers: List[TelemetryListener]):
        self.watchers = watchers
        self.running = True
        self.lastTime = -1
        self.codec = DashCodec()
        self.sock: socket = None

    def run(self):
        self.init()
        while self.running:
            self.receive()

    def init(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((UDP_IP, UDP_PORT))

    def receive(self) -> DashPacket:
        data, addr = self.sock.recvfrom(1024)
        packet = self.codec.unpack(data)

        if packet.CurrentRaceTime != 0 and packet.CurrentRaceTime != self.lastTime:
            for watcher in self.watchers:
                watcher.receive(packet)

            self.lastTime = packet.CurrentRaceTime

        return packet

    async def receive2(self) -> DashPacket:
        self.sock.setblocking(False)
        while True:
            try:
                data, addr = self.sock.recvfrom(1024)
                packet = self.codec.unpack(data)

                if packet.CurrentRaceTime != 0 and packet.CurrentRaceTime != self.lastTime:
                    print(f"received udp {packet.TimestampMS}", flush=True)
                    for watcher in self.watchers:
                        watcher.receive(packet)

                    self.lastTime = packet.CurrentRaceTime

                    return packet
                await gen.sleep(1 / 120)
            except BlockingIOError:
                await gen.sleep(1 / 120)

    def stop(self):
        self.running = False
