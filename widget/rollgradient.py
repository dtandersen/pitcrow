import math

from pyqtgraph import mkPen, mkBrush

from packet import DashPacket
from widget.base import BasePlot


class RollGradient(BasePlot):
    def __init__(self):
        super(RollGradient, self).__init__()

        self.plotItem = self.addPlot(title="Roll Gradient")

        self.frontRoll = self.plotItem.plot([], pen=None, symbol='o', size=1)
        self.lateral = []
        self.roll = []

    def onNewData(self, packet: DashPacket):
        self.append(self.lateral, packet.AccelerationX)
        self.append(self.roll, packet.Roll * 180 / math.pi)

        self.frontRoll.setData(self.lateral, self.roll)


class PitchGradient(BasePlot):
    def __init__(self):
        super(PitchGradient, self).__init__()

        self.plotItem = self.addPlot(title="Pitch Gradient")

        self.frontRoll = self.plotItem.plot([], pen=None, symbol='o', size=1)
        self.longAccel = []
        self.pitch = []

    def onNewData(self, packet: DashPacket):
        self.append(self.longAccel, packet.AccelerationZ)
        self.append(self.pitch, packet.Pitch * 180 / math.pi)

        self.frontRoll.setData(self.longAccel, self.pitch)
