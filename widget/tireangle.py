import pyqtgraph as pg
from pyqtgraph import mkPen

from packet import DashPacket
from signal import SignalCommunicate


class TireAngle(pg.GraphicsLayoutWidget):
    def __init__(self):
        super(TireAngle, self).__init__()

        self.plotItem = self.addPlot(title="Tire Angle")
        self.plotItem.addLegend()

        self.leftFront = self.plotItem.plot([], pen=mkPen('b'), name="Front Left")
        self.rightFront = self.plotItem.plot([], pen=mkPen('c'), name="Front Right")
        self.leftRear = self.plotItem.plot([], pen=mkPen('g'), name="Rear Left")
        self.rightRear = self.plotItem.plot([], pen=mkPen('y'), name="Rear Right")
        self.time = []
        self.leftFrontData = []
        self.rightFrontData = []
        self.leftRearData = []
        self.rightRearData = []

    def activate_signal(self, sc: SignalCommunicate):
        sc.got_new_sensor_data.connect(self.onNewData)

    def onNewData(self, packet: DashPacket):
        self.append(self.time, packet.CurrentRaceTime)

        self.append(self.leftFrontData, packet.TireSlipAngleFrontLeft)
        self.append(self.rightFrontData, packet.TireSlipAngleFrontRight)
        self.append(self.leftRearData, packet.TireSlipAngleRearLeft)
        self.append(self.rightRearData, packet.TireSlipAngleRearRight)

        self.leftFront.setData(self.time, self.leftFrontData)
        self.rightFront.setData(self.time, self.rightFrontData)
        self.leftRear.setData(self.time, self.leftRearData)
        self.rightRear.setData(self.time, self.rightRearData)

    def append(self, values: list, value):
        if len(values) > 3600:
            values.pop(0)

        values.append(value)
