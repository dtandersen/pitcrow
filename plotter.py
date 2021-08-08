from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow
import importlib

from signal import SignalCommunicate


class Window(QMainWindow):
    def __init__(self, plugins: list[str]):
        super(Window, self).__init__()
        self.plugins = plugins
        self.pluginReferences = []
        self.initUI()  # call the UI set up

    # set up the UI
    def initUI(self):
        self.setWindowTitle("My App")
        self.stackedLayout = QtWidgets.QVBoxLayout()

        for plugin in self.plugins:
            module_name, class_name = plugin.rsplit(".", 1)
            module = importlib.import_module(module_name)
            class_ = getattr(module, class_name)
            instance = class_()
            self.pluginReferences.append(instance)
            self.stackedLayout.addWidget(instance)

        widget = QWidget()
        widget.setLayout(self.stackedLayout)
        self.setCentralWidget(widget)
        self.show()

    def activate_signal(self, sc: SignalCommunicate):
        for p in self.pluginReferences:
            p.activate_signal(sc)

    def closeEvent(self, event):
        self.on_exit()
