import sys

from PySide2.QtCore import Qt,QSize
from PySide2.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        layout1 = QHBoxLayout()
        nameLabel = QLabel("Name")
        nameLineEdit = QLineEdit()
        nameLabel.setFixedSize(QSize(120,60))
        nameLineEdit.setFixedSize(QSize(230,60))  
        layout1.addWidget(nameLabel)
        layout1.addWidget(nameLineEdit)
        layout2 = QHBoxLayout()
        ageLabel = QLabel("Age")
        ageSpinBox = QSpinBox()
        ageLabel.setFixedSize(QSize(120,60))
        ageSpinBox.setFixedSize(QSize(230,60))  
        layout2.addWidget(ageLabel)
        layout2.addWidget(ageSpinBox)
        layout3 = QHBoxLayout()
        genderLabel = QLabel("Gender")
        genderComboBox = QComboBox()
        genderLabel.setFixedSize(QSize(120,60))
        genderComboBox.setFixedSize(QSize(230,60)) 
        genderComboBox.addItems(["Male", "Female"])
        layout3.addWidget(genderLabel)
        layout3.addWidget(genderComboBox)
        layout4 = QHBoxLayout()
        okPushButton = QPushButton("OK")
        cancelPushButton = QPushButton("Cancel")
        okPushButton.setFixedSize(QSize(230,60))
        cancelPushButton.setFixedSize(QSize(230,60))
        cancelPushButton.clicked.connect(self.close) 
        layout4.addWidget(okPushButton)
        layout4.addWidget(cancelPushButton)

        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addLayout(layout3)
        layout.addLayout(layout4)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
