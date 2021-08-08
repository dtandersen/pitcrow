import pyqtgraph as pg
from pyqtgraph import mkPen

from packet import DashPacket
from signal import SignalCommunicate


class Oversteer(pg.GraphicsLayoutWidget):
    def __init__(self):
        super(Oversteer, self).__init__()
        # self.data = []

        self.plotItem = self.addPlot(title="Oversteer")

        # self.plotItem.disableAutoRange()
        # self.plotItem.setXRange(0, 3600)
        # self.plotItem.setYRange(100, 250)
        self.leftFront = self.plotItem.plot([], pen=mkPen('r'))
        self.rightFront = self.plotItem.plot([], pen=mkPen('g'))
        # self.leftRear = self.plotItem.plot([], pen=mkPen('b'))
        # self.rightRear = self.plotItem.plot([], pen=mkPen('w'))
        # self.plotItem.autoRange()
        self.time = []
        self.leftFrontData = []
        self.rightFrontData = []
        self.leftRearData = []
        self.rightRearData = []

    def activate_signal(self, sc: SignalCommunicate):
        sc.got_new_sensor_data.connect(self.onNewData)

    def onNewData(self, packet: DashPacket):
        self.append(self.time, packet.CurrentRaceTime)

        # self.append(self.leftFrontData, packet.TireSlipAngleFrontLeft)
        # self.append(self.rightFrontData, packet.TireSlipAngleFrontRight)
        # self.append(self.leftRearData, packet.TireSlipAngleRearLeft)
        # self.append(self.rightRearData, packet.TireSlipAngleRearRight)

        front = (packet.TireSlipAngleFrontLeft + packet.TireSlipAngleFrontRight) / 2
        rear = (packet.TireSlipAngleRearLeft + packet.TireSlipAngleRearRight) / 2
        oversteer = abs(rear) - abs(front)
        self.append(self.leftFrontData, oversteer)
        self.append(self.rightFrontData, 0)
        self.leftFront.setData(self.time, self.leftFrontData)
        self.rightFront.setData(self.time, self.rightFrontData)
        # self.leftRear.setData(self.time, self.leftRearData)
        # self.rightRear.setData(self.time, self.rightRearData)

    def append(self, values: list, value):
        if len(values) > 3600:
            values.pop(0)

        values.append(value)
