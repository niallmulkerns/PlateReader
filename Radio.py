# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Radio.ui'
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color:black")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        self.stationPicker = QtWidgets.QComboBox(self.centralwidget)
        self.stationPicker.setGeometry(QtCore.QRect(180, 40, 440, 45))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(20)
        self.stationPicker.setFont(font)
        self.stationPicker.setStyleSheet("QComboBox#stationPicker{\n"
"    color: rgba(163, 122, 122, 255);\n"
"    background-color: white;\n"
"    selection-background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox:drop-down {\n"
"    border-width: 0px;\n"
"}\n"
"\n"
"QComboBox:down-arrow{\n"
"    image: url(noimg); \n"
"    border-width: 0px;\n"
"}\n"
"\n"
"QComboBoxr:on{ \n"
"    background: white;\n"
"}\n"
"\n"
"QListView{ \n"
"    background-color: white;\n"
"    color: rgba(122, 163, 122, 255);\n"
"}")
        self.stationPicker.setCurrentText("")
        self.stationPicker.setObjectName("stationPicker")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(60, 120, 200, 71))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"    color: white;\n"
"    border-style: solid;\n"
"    border-color: white;\n"
"    border-radius: 10px;\n"
"    border-width: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: : rgba(122, 163, 122, 200);\n"
"}\n"
"")
        self.playButton.setObjectName("playButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(300, 120, 200, 71))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.stopButton.setFont(font)
        self.stopButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(110, 126, 141, 255);\n"
"    color: white;\n"
"    border-style: solid;\n"
"    border-color: white;\n"
"    border-radius: 10px;\n"
"    border-width: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color:  rgba(110, 126, 141, 200);\n"
"}\n"
"")
        self.stopButton.setObjectName("stopButton")
        self.bar1 = QtWidgets.QLabel(self.centralwidget)
        self.bar1.setGeometry(QtCore.QRect(40, 270, 30, 301))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bar1.sizePolicy().hasHeightForWidth())
        self.bar1.setSizePolicy(sizePolicy)
        self.bar1.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar1.setText("")
        self.bar1.setObjectName("bar1")
        self.bar2 = QtWidgets.QLabel(self.centralwidget)
        self.bar2.setGeometry(QtCore.QRect(74, 350, 30, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bar2.sizePolicy().hasHeightForWidth())
        self.bar2.setSizePolicy(sizePolicy)
        self.bar2.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar2.setText("")
        self.bar2.setObjectName("bar2")
        self.bar3 = QtWidgets.QLabel(self.centralwidget)
        self.bar3.setGeometry(QtCore.QRect(109, 350, 30, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bar3.sizePolicy().hasHeightForWidth())
        self.bar3.setSizePolicy(sizePolicy)
        self.bar3.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar3.setText("")
        self.bar3.setObjectName("bar3")
        self.bar4 = QtWidgets.QLabel(self.centralwidget)
        self.bar4.setGeometry(QtCore.QRect(144, 350, 30, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bar4.sizePolicy().hasHeightForWidth())
        self.bar4.setSizePolicy(sizePolicy)
        self.bar4.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar4.setText("")
        self.bar4.setObjectName("bar4")
        self.bar5 = QtWidgets.QLabel(self.centralwidget)
        self.bar5.setGeometry(QtCore.QRect(179, 350, 30, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bar5.sizePolicy().hasHeightForWidth())
        self.bar5.setSizePolicy(sizePolicy)
        self.bar5.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar5.setText("")
        self.bar5.setObjectName("bar5")
        self.bar6 = QtWidgets.QLabel(self.centralwidget)
        self.bar6.setGeometry(QtCore.QRect(214, 350, 30, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bar6.sizePolicy().hasHeightForWidth())
        self.bar6.setSizePolicy(sizePolicy)
        self.bar6.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar6.setText("")
        self.bar6.setObjectName("bar6")
        self.bar7 = QtWidgets.QLabel(self.centralwidget)
        self.bar7.setGeometry(QtCore.QRect(249, 350, 30, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bar7.sizePolicy().hasHeightForWidth())
        self.bar7.setSizePolicy(sizePolicy)
        self.bar7.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar7.setText("")
        self.bar7.setObjectName("bar7")
        self.bar8 = QtWidgets.QLabel(self.centralwidget)
        self.bar8.setGeometry(QtCore.QRect(284, 350, 30, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bar8.sizePolicy().hasHeightForWidth())
        self.bar8.setSizePolicy(sizePolicy)
        self.bar8.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar8.setText("")
        self.bar8.setObjectName("bar8")
        self.bar9 = QtWidgets.QLabel(self.centralwidget)
        self.bar9.setGeometry(QtCore.QRect(319, 350, 30, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bar9.sizePolicy().hasHeightForWidth())
        self.bar9.setSizePolicy(sizePolicy)
        self.bar9.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar9.setText("")
        self.bar9.setObjectName("bar9")
        self.bar10 = QtWidgets.QLabel(self.centralwidget)
        self.bar10.setGeometry(QtCore.QRect(354, 350, 30, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bar10.sizePolicy().hasHeightForWidth())
        self.bar10.setSizePolicy(sizePolicy)
        self.bar10.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar10.setText("")
        self.bar10.setObjectName("bar10")
        self.bar11 = QtWidgets.QLabel(self.centralwidget)
        self.bar11.setGeometry(QtCore.QRect(389, 350, 31, 221))
        self.bar11.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar11.setText("")
        self.bar11.setObjectName("bar11")
        self.bar12 = QtWidgets.QLabel(self.centralwidget)
        self.bar12.setGeometry(QtCore.QRect(425, 350, 30, 221))
        self.bar12.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar12.setText("")
        self.bar12.setObjectName("bar12")
        self.bar13 = QtWidgets.QLabel(self.centralwidget)
        self.bar13.setGeometry(QtCore.QRect(460, 350, 30, 221))
        self.bar13.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar13.setText("")
        self.bar13.setObjectName("bar13")
        self.bar14 = QtWidgets.QLabel(self.centralwidget)
        self.bar14.setGeometry(QtCore.QRect(495, 350, 30, 221))
        self.bar14.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar14.setText("")
        self.bar14.setObjectName("bar14")
        self.bar15 = QtWidgets.QLabel(self.centralwidget)
        self.bar15.setGeometry(QtCore.QRect(530, 350, 30, 221))
        self.bar15.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar15.setText("")
        self.bar15.setObjectName("bar15")
        self.bar16 = QtWidgets.QLabel(self.centralwidget)
        self.bar16.setGeometry(QtCore.QRect(565, 350, 30, 221))
        self.bar16.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar16.setText("")
        self.bar16.setObjectName("bar16")
        self.bar17 = QtWidgets.QLabel(self.centralwidget)
        self.bar17.setGeometry(QtCore.QRect(600, 350, 30, 221))
        self.bar17.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar17.setText("")
        self.bar17.setObjectName("bar17")
        self.bar18 = QtWidgets.QLabel(self.centralwidget)
        self.bar18.setGeometry(QtCore.QRect(635, 350, 30, 221))
        self.bar18.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar18.setText("")
        self.bar18.setObjectName("bar18")
        self.bar19 = QtWidgets.QLabel(self.centralwidget)
        self.bar19.setGeometry(QtCore.QRect(670, 350, 30, 221))
        self.bar19.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar19.setText("")
        self.bar19.setObjectName("bar19")
        self.bar20 = QtWidgets.QLabel(self.centralwidget)
        self.bar20.setGeometry(QtCore.QRect(705, 350, 30, 221))
        self.bar20.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar20.setText("")
        self.bar20.setObjectName("bar20")
        self.bar21 = QtWidgets.QLabel(self.centralwidget)
        self.bar21.setEnabled(True)
        self.bar21.setGeometry(QtCore.QRect(740, 350, 30, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bar21.sizePolicy().hasHeightForWidth())
        self.bar21.setSizePolicy(sizePolicy)
        self.bar21.setStyleSheet("QLabel{\n"
"    background-color: rgba(122, 163, 122, 255);\n"
"}")
        self.bar21.setText("")
        self.bar21.setObjectName("bar21")
        self.visPicker = QtWidgets.QComboBox(self.centralwidget)
        self.visPicker.setGeometry(QtCore.QRect(540, 135, 200, 45))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(20)
        self.visPicker.setFont(font)
        self.visPicker.setStyleSheet("QComboBox{\n"
"    color: rgba(163, 122, 122, 255);\n"
"    background-color: white;\n"
"    selection-background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox:drop-down {\n"
"    border-width: 0px;\n"
"}\n"
"\n"
"QComboBox:down-arrow{\n"
"    image: url(noimg); \n"
"    border-width: 0px;\n"
"}\n"
"\n"
"QComboBoxr:on{ \n"
"    background: white;\n"
"}\n"
"\n"
"QListView{ \n"
"    background-color: white;\n"
"    color: rgba(122, 163, 122, 255);\n"
"}")
        self.visPicker.setCurrentText("")
        self.visPicker.setObjectName("visPicker")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backButton.setText(_translate("MainWindow", "Home"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
