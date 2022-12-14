# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlateReader.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background: black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(270, 505, 200, 80))
        self.frame.setStyleSheet("QFrame{\n"
"    border: 2px solid white;\n"
"    background-color: transparent;\n"
"    border-radius:5px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(0, 0, 200, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setStyleSheet("QLCDNumber{\n"
"    border: white;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"}")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(10, 505, 110, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"background:  rgba(122, 163, 122, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(122, 163, 122, 200);\n"
"}")
        self.startButton.setObjectName("startButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(0, 0, 120, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("QPushButton#backButton{\n"
"    border-width: 2px;\n"
"    border-style: none;\n"
"    border-color: white;\n"
"    border-radius: 10px;\n"
"    background-color: rgba(110, 126, 141, 255);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#backButton:pressed{\n"
"    padding-left: 2px;\n"
"    padding-top: 2px;\n"
"    background-color: rgba(110, 126, 141, 200);\n"
"}\n"
"")
        self.backButton.setObjectName("backButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(140, 505, 110, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.stopButton.setFont(font)
        self.stopButton.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"background: rgba(163, 122, 122, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background:  rgba(163, 122, 122, 200);\n"
"}\n"
"")
        self.stopButton.setObjectName("stopButton")
        self.GraphWidget = PlotWidget(self.centralwidget)
        self.GraphWidget.setGeometry(QtCore.QRect(10, 74, 780, 421))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GraphWidget.sizePolicy().hasHeightForWidth())
        self.GraphWidget.setSizePolicy(sizePolicy)
        self.GraphWidget.setMaximumSize(QtCore.QSize(100000, 1000000))
        self.GraphWidget.setStyleSheet("QWidget{\n"
"    background: none;\n"
"}")
        self.GraphWidget.setObjectName("GraphWidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(790, 0, 10, 600))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(16)
        self.progressBar.setFont(font)
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setStyleSheet("QProgressBar:chunk{\n"
"    border-radius: 10px;\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}\n"
"\n"
"QProgressBar{\n"
"    background-color: transparent;\n"
"    border-radius: 10px;\n"
"    color: black;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setObjectName("progressBar")
        self.upButton = QtWidgets.QPushButton(self.centralwidget)
        self.upButton.setGeometry(QtCore.QRect(485, 505, 75, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upButton.sizePolicy().hasHeightForWidth())
        self.upButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.upButton.setFont(font)
        self.upButton.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: none;\n"
"border-radius: 5px;\n"
"color: white;\n"
"background:  rgba(122, 163, 122, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background:   rgba(200, 200, 200, 200);\n"
"}\n"
"")
        self.upButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../.designer/backup/designer icons/icons/control-090.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upButton.setIcon(icon)
        self.upButton.setIconSize(QtCore.QSize(32, 32))
        self.upButton.setObjectName("upButton")
        self.downButton = QtWidgets.QPushButton(self.centralwidget)
        self.downButton.setGeometry(QtCore.QRect(485, 550, 75, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downButton.sizePolicy().hasHeightForWidth())
        self.downButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.downButton.setFont(font)
        self.downButton.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: none;\n"
"border-radius: 5px;\n"
"color: white;\n"
"background:   rgba(163, 122, 122, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background:  rgba(200, 200, 200, 200);\n"
"}\n"
"")
        self.downButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../.designer/backup/designer icons/icons/control-270.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downButton.setIcon(icon1)
        self.downButton.setIconSize(QtCore.QSize(32, 32))
        self.downButton.setObjectName("downButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(580, 500, 211, 30))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: white;\n"
"}")
        self.label.setObjectName("label")
        self.minsPerDataLabel = QtWidgets.QLabel(self.centralwidget)
        self.minsPerDataLabel.setGeometry(QtCore.QRect(580, 535, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.minsPerDataLabel.setFont(font)
        self.minsPerDataLabel.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"    border-radius: 5px;\n"
"}")
        self.minsPerDataLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.minsPerDataLabel.setObjectName("minsPerDataLabel")
        self.downButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.downButton_2.setGeometry(QtCore.QRect(720, 540, 60, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downButton_2.sizePolicy().hasHeightForWidth())
        self.downButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.downButton_2.setFont(font)
        self.downButton_2.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: none;\n"
"border-radius: 5px;\n"
"color: white;\n"
"background:   rgba(122, 163, 122, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background:  rgba(200, 200, 200, 200);\n"
"}\n"
"")
        self.downButton_2.setText("")
        self.downButton_2.setIcon(icon1)
        self.downButton_2.setIconSize(QtCore.QSize(32, 32))
        self.downButton_2.setObjectName("downButton_2")
        self.upButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.upButton_2.setGeometry(QtCore.QRect(650, 540, 60, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upButton_2.sizePolicy().hasHeightForWidth())
        self.upButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.upButton_2.setFont(font)
        self.upButton_2.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: none;\n"
"border-radius: 5px;\n"
"color: white;\n"
"background:  rgba(163, 122, 122, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background:   rgba(200, 200, 200, 200);\n"
"}\n"
"")
        self.upButton_2.setText("")
        self.upButton_2.setIcon(icon)
        self.upButton_2.setIconSize(QtCore.QSize(32, 32))
        self.upButton_2.setObjectName("upButton_2")
        self.frame.raise_()
        self.startButton.raise_()
        self.stopButton.raise_()
        self.GraphWidget.raise_()
        self.progressBar.raise_()
        self.backButton.raise_()
        self.upButton.raise_()
        self.downButton.raise_()
        self.label.raise_()
        self.minsPerDataLabel.raise_()
        self.downButton_2.raise_()
        self.upButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.backButton.setText(_translate("MainWindow", "Home"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.label.setText(_translate("MainWindow", "Mins per Datapoint"))
        self.minsPerDataLabel.setText(_translate("MainWindow", "10"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
