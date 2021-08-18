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
        self.distOffset = 0
        self.lastTime = -1

    def init(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((UDP_IP, UDP_PORT))

        self.codec = DashCodec()
        self.distOffset = 0

    def go(self):
        self.init()
        while self.running:
            self.read_data()

    def read_data(self):
        data, addr = self.sock.recvfrom(1024)
        packet2 = self.codec.unpack(data)
        # if packet2.LapNumber is not self.lastLap:
        #     self.distOffset = packet2.DistanceTraveled
        #     self.lastLap = packet2.LapNumber
        #
        # packet2.DistanceTraveled = packet2.DistanceTraveled - self.distOffset
        # print(f"{packet2.Yaw:.2f} {packet2.Pitch:.2f} {packet2.Roll:.2f}")

        if packet2.CurrentRaceTime != 0 and packet2.CurrentRaceTime != self.lastTime:
            # print("updated")
            self.sc.recv(packet2)
            self.lastTime = packet2.CurrentRaceTime

    def stop(self):
        self.running = False
