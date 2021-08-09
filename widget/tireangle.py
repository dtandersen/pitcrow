import pyqtgraph as pg
from pyqtgraph import mkPen

from packet import DashPacket
from signal import SignalCommunicate
from widget.base import BasePlot


class TireAngle(BasePlot):
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

    def onNewData(self, packet: DashPacket):
        self.append(self.time, packet.DistanceTraveled)

        self.append(self.leftFrontData, packet.TireSlipAngleFrontLeft)
        self.append(self.rightFrontData, packet.TireSlipAngleFrontRight)
        self.append(self.leftRearData, packet.TireSlipAngleRearLeft)
        self.append(self.rightRearData, packet.TireSlipAngleRearRight)

        self.leftFront.setData(self.time, self.leftFrontData)
        self.rightFront.setData(self.time, self.rightFrontData)
        self.leftRear.setData(self.time, self.leftRearData)
        self.rightRear.setData(self.time, self.rightRearData)
