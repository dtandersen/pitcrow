import sys
import threading
from PyQt5 import QtWidgets

from listener import Listener
from plotter import SignalCommunicate, MainWindow


def stop_listener():
    listener.stop()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    sc = SignalCommunicate()
    listener = Listener(sc)
    plugins = [
        # 'widget.tiretemp.TireTemperature',
        # 'widget.tireangle.TireAngle',
        # 'widget.oversteer.Oversteer',
        'widget.FrictionCircle',
    ]
    mainWindow = MainWindow(plugins)

    mainWindow.on_exit = stop_listener
    mainWindow.listener = listener
    mainWindow.activate_signal(sc)

    x = threading.Thread(target=listener.go)
    x.start()

    mainWindow.show()
    mainWindow.resize(800, 600)
    mainWindow.raise_()
    sys.exit(app.exec_())
