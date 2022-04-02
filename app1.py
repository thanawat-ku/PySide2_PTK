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
        self.nameLineEdit = QLineEdit()
        nameLabel.setFixedSize(QSize(120,60))
        self.nameLineEdit.setFixedSize(QSize(230,60))  
        layout1.addWidget(nameLabel)
        layout1.addWidget(self.nameLineEdit)
        layout2 = QHBoxLayout()
        ageLabel = QLabel("Age")
        self.ageSpinBox = QSpinBox()
        ageLabel.setFixedSize(QSize(120,60))
        self.ageSpinBox.setFixedSize(QSize(230,60))  
        layout2.addWidget(ageLabel)
        layout2.addWidget(self.ageSpinBox)
        layout3 = QHBoxLayout()
        genderLabel = QLabel("Gender")
        self.genderComboBox = QComboBox()
        genderLabel.setFixedSize(QSize(120,60))
        self.genderComboBox.setFixedSize(QSize(230,60)) 
        self.genderComboBox.addItems(["Male", "Female"])
        layout3.addWidget(genderLabel)
        layout3.addWidget(self.genderComboBox)
        layout4 = QHBoxLayout()
        okPushButton = QPushButton("OK")
        cancelPushButton = QPushButton("Cancel")
        okPushButton.setFixedSize(QSize(230,60))
        cancelPushButton.setFixedSize(QSize(230,60))
        layout4.addWidget(okPushButton)
        layout4.addWidget(cancelPushButton)

        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addLayout(layout3)
        layout.addLayout(layout4)

        widget = QWidget()
        widget.setLayout(layout)

        
        cancelPushButton.clicked.connect(self.close) 
        okPushButton.clicked.connect(self.okClick)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)
    
    def okClick(self):
        print("Name", self.nameLineEdit.text())
        print("Age", self.ageSpinBox.text())
        print("Gender", self.genderComboBox.currentText())


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
