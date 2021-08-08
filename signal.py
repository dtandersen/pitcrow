from PyQt5.QtCore import QObject, pyqtSignal

from packet import DashPacket


class SignalCommunicate(QObject):
    got_new_sensor_data = pyqtSignal(DashPacket)
