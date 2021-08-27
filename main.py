import sys
import threading
from PyQt5 import QtWidgets

from telemetry import UdpTelemetrySource
from plotter import SignalCommunicate, MainWindow
from signal import SignalCommunicateAdapter


def stop_listener():
    listener.stop()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    sc = SignalCommunicate()
    adapter = SignalCommunicateAdapter(sc)
    listener = UdpTelemetrySource([adapter])
    plugins = [
        # 'widget.TireTemperature',
        # 'widget.TireAngle',
        # 'widget.Oversteer',
        # 'widget.FrictionCircle',
        'widget.PitchGradient',
        # 'widget.RollGradient',
    ]
    mainWindow = MainWindow(plugins)

    mainWindow.on_exit = stop_listener
    mainWindow.listener = listener
    mainWindow.activate_signal(sc)

    x = threading.Thread(target=listener.run)
    x.start()

    mainWindow.show()
    # mainWindow.resize(800, 600)
    mainWindow.raise_()
    sys.exit(app.exec_())
