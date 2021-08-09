import pyqtgraph as pg
from pyqtgraph import mkPen

from packet import DashPacket
from signal import SignalCommunicate
from widget.base import BasePlot


class TireTemperature(BasePlot):
    def __init__(self):
        super(TireTemperature, self).__init__()

        self.plotItem = self.addPlot(title="Tire Temperature")

        self.leftFront = self.plotItem.plot([], pen=mkPen('r'))
        self.rightFront = self.plotItem.plot([], pen=mkPen('g'))
        self.leftRear = self.plotItem.plot([], pen=mkPen('b'))
        self.rightRear = self.plotItem.plot([], pen=mkPen('w'))
        self.time = []
        self.leftFrontData = []
        self.rightFrontData = []
        self.leftRearData = []
        self.rightRearData = []

    def onNewData(self, packet: DashPacket):
        self.append(self.time, packet.DistanceTraveled)

        self.append(self.leftFrontData, packet.TireTempFrontLeft)
        self.append(self.rightFrontData, packet.TireTempFrontRight)
        self.append(self.leftRearData, packet.TireTempRearLeft)
        self.append(self.rightRearData, packet.TireTempRearRight)

        self.leftFront.setData(self.time, self.leftFrontData)
        self.rightFront.setData(self.time, self.rightFrontData)
        self.leftRear.setData(self.time, self.leftRearData)
        self.rightRear.setData(self.time, self.rightRearData)
