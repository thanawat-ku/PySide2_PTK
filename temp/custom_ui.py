import sys
from PySide2 import QtCore, QtGui, QtWidgets
from power_bar import PowerBar

app = QtWidgets.QApplication(sys.argv)
volume = PowerBar()
volume.show()
app.exec_()
