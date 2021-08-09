from pyqtgraph import mkPen, mkBrush

from packet import DashPacket
from widget.base import BasePlot


class Oversteer(BasePlot):
    def __init__(self):
        super(Oversteer, self).__init__()

        self.plotItem = self.addPlot(title="Oversteer")

        self.leftFront = self.plotItem.plot([], brush=mkBrush('r'))
        self.rightFront = self.plotItem.plot([], brush=mkBrush('g'))
        self.time = []
        self.leftFrontData = []
        self.rightFrontData = []
        self.leftRearData = []
        self.rightRearData = []

    def onNewData(self, packet: DashPacket):
        self.append(self.time, packet.DistanceTraveled)

        front = (packet.TireSlipAngleFrontLeft + packet.TireSlipAngleFrontRight) / 2
        rear = (packet.TireSlipAngleRearLeft + packet.TireSlipAngleRearRight) / 2
        oversteer = abs(rear) - abs(front)
        self.append(self.leftFrontData, oversteer)
        self.append(self.rightFrontData, 0)
        self.leftFront.setData(self.time, self.leftFrontData)
        self.rightFront.setData(self.time, self.rightFrontData)
