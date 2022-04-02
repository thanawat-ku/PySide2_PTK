from ast import arguments
import sys

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Signal,QTimer

from time import strftime, localtime

class Backend(QObject):
    updated = Signal(int, arguments=['gear'])
    def __init__(self):
        super().__init__()
        self.r = 0
        # Define timer.
        self.timer = QTimer()
        self.timer.setInterval(1000)  # msecs 100 = 1/10th sec
        self.timer.timeout.connect(self.update_gear)
        self.timer.start()

    def update_gear(self):
        self.r = self.r + 1
        if self.r==7:
            self.r=0
        print(self.r)
        self.updated.emit(self.r)

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')

# Define our backend object, which we pass to QML.
backend = Backend()

engine.rootObjects()[0].setProperty('backend', backend)

sys.exit(app.exec_())