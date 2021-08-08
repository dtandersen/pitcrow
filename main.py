import sys
import threading
from PyQt5 import QtWidgets
import OpenGL
import pyqtgraph as pg

from listener import Listener
from plotter import SignalCommunicate, Window


def stop_listener():
    listener.stop()


if __name__ == '__main__':
    #     app = QtWidgets.QApplication(sys.argv)
    #
    #     # pg.setConfigOptions(antialias=False)  # True seems to work as well
    #
    #     win = Window()
    #     # win.show()
    #     # win.resize(800, 600)
    #     # win.raise_()
    #     sys.exit(app.exec_())

    # pg.setConfigOption('useOpenGL', True)
    # pg.setConfigOption('enableExperimental', True)
    app = QtWidgets.QApplication(sys.argv)

    sc = SignalCommunicate()
    listener = Listener(sc)
    plugins = ['widget.tiretemp.TireTemperature', 'widget.tireangle.TireAngle', 'widget.oversteer.Oversteer']
    win = Window(plugins)

    win.on_exit = stop_listener
    win.listener = listener
    win.activate_signal(sc)

    # listener = Listener(sc)
    x = threading.Thread(target=listener.go)
    x.start()

    # pg.setConfigOptions(antialias=False)  # True seems to work as well

    win.show()
    win.resize(800, 600)
    win.raise_()
    sys.exit(app.exec_())
    # listener.stop()
    # app.exec_()
