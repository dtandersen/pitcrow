import pyqtgraph as pg

from signal import SignalCommunicate


class BasePlot(pg.GraphicsLayoutWidget):
    def activate_signal(self, sc: SignalCommunicate):
        sc.got_new_sensor_data.init(self.onNewData)

    def append(self, values: list, value):
        if len(values) > 3600:
            values.pop(0)

        values.append(value)