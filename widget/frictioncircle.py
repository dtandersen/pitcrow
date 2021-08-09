from pyqtgraph import mkPen, mkBrush

from packet import DashPacket
from widget.base import BasePlot


class FrictionCircle(BasePlot):
    def __init__(self):
        super(FrictionCircle, self).__init__()

        self.plotItem = self.addPlot(title="Friction Circle")

        self.gplot = self.plotItem.plot([], pen=None, symbol='o', size=1)
        self.lateral = []
        self.longitudinal = []

    def onNewData(self, packet: DashPacket):
        self.append(self.lateral, packet.AccelerationX)
        self.append(self.longitudinal, packet.AccelerationZ)

        self.gplot.setData(self.lateral, self.longitudinal)
