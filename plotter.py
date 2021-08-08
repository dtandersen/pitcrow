#!/usr/bin/env python

from PyQt5 import QtWidgets
import pyqtgraph as pg
from PyQt5.QtWidgets import QWidget, QMainWindow
from pyqtgraph import mkPen

from packet import DashPacket
from signal import SignalCommunicate


class TireTemperature(pg.GraphicsLayoutWidget):
    def __init__(self):
        super(TireTemperature, self).__init__()
        # self.data = []

        self.plotItem = self.addPlot(title="Tire Temperature")

        # self.plotItem.disableAutoRange()
        # self.plotItem.setXRange(0, 3600)
        # self.plotItem.setYRange(100, 250)
        self.leftFront = self.plotItem.plot([], pen=mkPen('r'))
        self.rightFront = self.plotItem.plot([], pen=mkPen('g'))
        self.leftRear = self.plotItem.plot([], pen=mkPen('b'))
        self.rightRear = self.plotItem.plot([], pen=mkPen('w'))
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

        self.append(self.leftFrontData, packet.TireTempFrontLeft)
        self.append(self.rightFrontData, packet.TireTempFrontRight)
        self.append(self.leftRearData, packet.TireTempRearLeft)
        self.append(self.rightRearData, packet.TireTempRearRight)

        self.leftFront.setData(self.time, self.leftFrontData)
        self.rightFront.setData(self.time, self.rightFrontData)
        self.leftRear.setData(self.time, self.leftRearData)
        self.rightRear.setData(self.time, self.rightRearData)

    def append(self, values: list, value):
        if len(values) > 3600:
            values.pop(0)

        values.append(value)


class TireAngle(pg.GraphicsLayoutWidget):
    def __init__(self):
        super(TireAngle, self).__init__()
        # self.data = []

        self.plotItem = self.addPlot(title="Tire Angle")
        self.plotItem.addLegend()

        # self.plotItem.disableAutoRange()
        # self.plotItem.setXRange(0, 3600)
        # self.plotItem.setYRange(100, 250)
        self.leftFront = self.plotItem.plot([], pen=mkPen('b'), name="Front Left")
        self.rightFront = self.plotItem.plot([], pen=mkPen('c'), name="Front Right")
        self.leftRear = self.plotItem.plot([], pen=mkPen('g'), name="Rear Left")
        self.rightRear = self.plotItem.plot([], pen=mkPen('y'), name="Rear Right")
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


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()  # call the UI set up

    # set up the UI
    def initUI(self):
        # self.layout = QVBoxLayout(self)  # create the layout
        self.setWindowTitle("My App")
        self.stackedLayout = QtWidgets.QVBoxLayout()
        # self.setMainLayout(self.layout)

        self.pgcustom = TireTemperature()  # class abstract both the classes
        self.pgcustom1 = TireAngle()  # "" "" ""
        self.oversteer = Oversteer()  # "" "" ""
        self.stackedLayout.addWidget(self.pgcustom)
        self.stackedLayout.addWidget(self.pgcustom1)
        self.stackedLayout.addWidget(self.oversteer)
        # self.show()

        widget = QWidget()
        widget.setLayout(self.stackedLayout)
        self.setCentralWidget(widget)
        self.show()

    def activate_signal(self, sc: SignalCommunicate):
        self.pgcustom.activate_signal(sc)
        self.pgcustom1.activate_signal(sc)
        self.oversteer.activate_signal(sc)

    def closeEvent(self, event):
        self.on_exit()
