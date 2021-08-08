import socket

from packet import DashCodec
from plotter import SignalCommunicate

UDP_IP = '0.0.0.0'
UDP_PORT = 20127


class Listener:
    def __init__(self, sc: SignalCommunicate):
        self.sc = sc
        self.running = True

    def go(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))

        codec = DashCodec()
        while self.running:
            data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
            # print("received message: %s" % data)
            packet2 = codec.unpack(data)
            # print(f"{packet2.TireTempFrontLeft:.1f} {packet2.TireTempFrontRight:.1f} {packet2.TireTempRearLeft:.1f} {packet2.TireTempRearRight:.1f}")
            print(
                f"{packet2.TireSlipRatioFrontLeft:.1f} {packet2.TireSlipRatioFrontRight:.1f} {packet2.TireSlipRatioRearLeft:.1f} {packet2.TireSlipRatioRearRight:.1f}")
            # self.win.onNewData(packet2.TireTempRearRight)
            if packet2.IsRaceOn == 1:
                self.sc.got_new_sensor_data.emit(packet2.CurrentRaceTime, packet2.TireTempRearRight)

    def stop(self):
        self.running = False
