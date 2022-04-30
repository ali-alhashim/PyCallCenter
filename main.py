import os
import csv
import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QFileDialog


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Select CSV File")
        self.text = QtWidgets.QLabel("Call Center", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)

        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.csv_rearrange)

    @QtCore.Slot()
    def csv_rearrange(self):
        print("start def to rearrange  csv ")
        BASE_DIR = os.getcwd()
        filename = QFileDialog.getOpenFileName(self, 'Open file', BASE_DIR, "CSV files (*.csv)")
        # print(filename[0])
        dataNoDuplicate = set()
        with open(filename[0]) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            data = []
            resultData = []
            for row in csvReader:
                data.append([row[0], row[11]])
                dataNoDuplicate.add(row[0])

        # print(data)  # original data in list with duplicate date & time
        # print(dataNoDuplicate)
        dataNoDuplicateList = list(dataNoDuplicate)
        i = 0
        ii = 0
        totalCalls = 0
        while i <= len(dataNoDuplicateList) - 1:
            totalCalls = 0
            ii = 0
            while ii <= len(data) - 1:
                if dataNoDuplicateList[i] == data[ii][0]:
                    try:
                        totalCalls = totalCalls + int(data[ii][1])
                    except:
                        print(None)

                ii = ii + 1
            resultData.append([dataNoDuplicateList[i], totalCalls])
            i = i + 1
        print(resultData)
        csvFile = open('FileName.csv', 'w')
        csvFile.write("Date & Time, Total Calls")
        x = 0
        while x <= len(resultData) - 1:
            csvFile.write(resultData[x][0] + "," + str(resultData[x][1]) + '\n')
            x = x + 1
        csvFile.close()
        print("Done!")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 200)
    widget.show()

    sys.exit(app.exec())
