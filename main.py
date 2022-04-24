import random
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QFileDialog


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Select CSV File")
        self.text = QtWidgets.QLabel("Call Center", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)

        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.csvToHtml)

    @QtCore.Slot()
    def csvToHtml(self):
        print("start def to convert csv to html")
        filename = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "CSV files (*.csv)")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 200)
    widget.show()

    sys.exit(app.exec())
