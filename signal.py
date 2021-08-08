import PyQt5


class SignalCommunicate(PyQt5.QtCore.QObject):
    # https://stackoverflow.com/a/45620056
    got_new_sensor_data = PyQt5.QtCore.pyqtSignal(float, float)
    position_updated = PyQt5.QtCore.pyqtSignal(float)
