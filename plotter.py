#!/usr/bin/env python

from PyQt5 import QtWidgets
import pyqtgraph as pg
from PyQt5.QtWidgets import QWidget, QMainWindow

from signal import SignalCommunicate


class MyWidget(pg.GraphicsLayoutWidget):
    def __init__(self, parent=None):
        # super().__init__(parent=parent)
        super(MyWidget, self).__init__()
        self.data = []
        # self.mainLayout = QtWidgets.QVBoxLayout()
        # self.setLayout(self.mainLayout)

        # self.timer = QtCore.QTimer(self)
        # self.timer.setInterval(100)  # in milliseconds
        # self.timer.start()
        # self.timer.timeout.connect(self.onNewData)

        self.plotItem = self.addPlot(title="Lidar points")

        self.plotDataItem = self.plotItem.plot([], pen=None,
                                               symbolBrush=(255, 0, 0), symbolSize=5, symbolPen=None)
        self.x = []
        self.y = []

    def activate_signal(self, sc: SignalCommunicate):
        sc.got_new_sensor_data.connect(self.onNewData)

    def setData(self, x, y):
        self.plotDataItem.setData(x, y)

    def onNewData(self, x0, y0):
        # numPoints = 1000
        # x = np.random.normal(size=numPoints)
        # y = np.random.normal(size=numPoints)
        if len(self.x) > 3600:
            self.x.pop(0)
        if len(self.y) > 3600:
            self.y.pop(0)
        self.x.append(x0)
        self.y.append(y0)
        self.setData(self.x, self.y)


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

        self.pgcustom = MyWidget()  # class abstract both the classes
        self.pgcustom1 = MyWidget()  # "" "" ""
        self.stackedLayout.addWidget(self.pgcustom)
        self.stackedLayout.addWidget(self.pgcustom1)
        # self.show()

        widget = QWidget()
        widget.setLayout(self.stackedLayout)
        self.setCentralWidget(widget)
        self.show()

    def activate_signal(self, sc: SignalCommunicate):
        self.pgcustom.activate_signal(sc)
        self.pgcustom1.activate_signal(sc)

    def closeEvent(self, event):
        self.on_exit()
