from abc import ABCMeta, abstractmethod

from PyQt5.QtCore import QObject, pyqtSignal

from packet import DashPacket


class DataListener(metaclass=ABCMeta):
    @abstractmethod
    def recv(self, data: DashPacket):
        pass


class SignalCommunicate(QObject):
    got_new_sensor_data = pyqtSignal(DashPacket)


class SignalCommunicateAdapter(DataListener):
    def __init__(self, sc: SignalCommunicate):
        self.sc = sc

    def recv(self, data: DashPacket):
        self.sc.got_new_sensor_data.emit(data)
