import socket

from packet import DashCodec
from signal import DataListener

UDP_IP = '0.0.0.0'
UDP_PORT = 20127


class Listener:
    def __init__(self, sc: DataListener):
        self.sc = sc
        self.running = True
        self.lastLap = 0

    def go(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))

        codec = DashCodec()
        distOffset = 0
        while self.running:
            data, addr = sock.recvfrom(1024)
            packet2 = codec.unpack(data)
            if packet2.LapNumber is not self.lastLap:
                distOffset = packet2.DistanceTraveled
                self.lastLap = packet2.LapNumber

            packet2.DistanceTraveled = packet2.DistanceTraveled - distOffset
            # print(f"{packet2.Yaw:.2f} {packet2.Pitch:.2f} {packet2.Roll:.2f}")

            if packet2.IsRaceOn == 1:
                self.sc.recv(packet2)

    def stop(self):
        self.running = False
