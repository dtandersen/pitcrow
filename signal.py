from abc import ABCMeta, abstractmethod

from PyQt5.QtCore import QObject, pyqtSignal

from packet import DashPacket


class TelemetryListener(metaclass=ABCMeta):
    @abstractmethod
    def receive(self, data: DashPacket):
        pass


class SignalCommunicate(QObject):
    got_new_sensor_data = pyqtSignal(DashPacket)


class SignalCommunicateAdapter(TelemetryListener):
    def __init__(self, sc: SignalCommunicate):
        self.sc = sc

    def receive(self, data: DashPacket):
        self.sc.got_new_sensor_data.emit(data)
