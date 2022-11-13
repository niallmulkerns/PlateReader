# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 13:12:23 2022

PyQT5 test script

@author: nm13747
"""

#from PyQt5 import Qwidget
from PyQt5 import QtWidgets, QtGui
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMessageBox, QStackedWidget
from PyQt5.uic import loadUi
import sys
from glob import glob
import vlc
from platform import system as OS
# import PyQt5.QtWebEngineWidgets as QWeb
from home import Ui_MainWindow as home_ui
from plateReader import Ui_MainWindow as pr_ui
from pictureFrame import Ui_MainWindow as pf_ui
# from visualiser import Ui_Form as vis_ui
from clockWeather import Ui_MainWindow as clw_ui
from Radio import Ui_MainWindow as rad_ui
from timer import Ui_MainWindow as tim_ui
from PyQt5.QtCore import QTimer, QTime, Qt, QDate, QUrl
from WeatherClassRPi import Weather
import requests
import numpy as np
from audioVis import getFakeRadioFFT
from gpiozero import LED, Button
from time import sleep


class TimerWindow(QMainWindow, tim_ui):
    def __init__(self):
        super(TimerWindow, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        loadUi('Timer.ui', self)
        self.initInteraction()
        self.showFullScreen()


    def initInteraction(self):
        self.lcdNumber.display("00:00:00")
        self.countingDown = False
        self.timerTimer = QTimer(self)
        self.timerTimer.setTimerType(Qt.PreciseTimer)
        self.flashTimer = QTimer(self, interval = 500, timeout = self.flash)
        self.timerTimer.timeout.connect(self.timerTick)
        self.backButton.clicked.connect(self.toHome)
        self.timerDialHours.valueChanged.connect(self.updateTimer)
        self.timerDialMins.valueChanged.connect(self.updateTimer)
        self.timerDialSecs.valueChanged.connect(self.updateTimer)
        self.startTimer.clicked.connect(self.initiateTimer)
        self.resetTimer.clicked.connect(self.reinitiateTimer)
        self.pomoTimer.clicked.connect(lambda: self.lcdNumber.display("00:20:00"))

    def toHome(self):
        self.close()

    def updateTimer(self):
        self.lcdNumber.display(f"{self.timerDialHours.value():02}:{self.timerDialMins.value():02}:{self.timerDialSecs.value():02}")

    def endTimer(self):
        self.timerTimer.stop()
        self.flashTimer.start()
        # self.flashTimer.timeout.connect(self.flash)
        self.flashBool = True

        self.lcdNumber.display("00:00:00")

    def flash(self):
        self.startTimer.hide()
        self.pomoTimer.hide()
        self.timerDialSecs.hide()
        self.timerDialMins.hide()
        self.timerDialHours.hide()
        self.frame_2.hide()
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.backButton.hide()
        if self.flashBool:
            self.setStyleSheet("QWidget{\nbackground-color: rgba(0, 0, 0, 255);\n}")
            self.flashBool = False
        else:
            self.setStyleSheet("QWidget{\nbackground-color: rgba(255, 255, 255, 255);\n}")
            self.flashBool = True

    def reinitiateTimer(self):
        if self.timerTimer.isActive():
            self.timerTimer.stop()
        if self.flashTimer.isActive():
            self.startTimer.show()
            self.pomoTimer.show()
            self.timerDialSecs.show()
            self.timerDialMins.show()
            self.timerDialHours.show()
            self.frame_2.show()
            self.label.show()
            self.label_2.show()
            self.label_3.show()
            self.backButton.show()
            self.flashTimer.stop()
        self.lcdNumber.display("00:00:00")
        self.timerDialSecs.setValue(0)
        self.timerDialMins.setValue(0)
        self.timerDialHours.setValue(0)
        self.updateTimer()
        self.setStyleSheet("QWidget{\n background-color: rgba(0, 0, 0, 255)}")

    def timerTick(self):
        self.lcdNumber.display(f"{self.cachedHours:02}:{self.cachedMins:02}:{self.cachedSecs:02}")
        if self.cachedSecs == 0:
            if self.cachedMins == 0:
                if self.cachedHours == 0:
                    self.endTimer()
                else:
                    self.cachedHours -= 1
                    self.cachedMins = 59
                    self.cachedSecs = 59
            else:
                self.cachedMins -= 1
                self.cachedSecs = 59
        else:
            self.cachedSecs -= 1

    def initiateTimer(self):
        self.timerTimer.start(1000)
        self.cachedHours = self.timerDialHours.value()
        self.cachedMins = self.timerDialMins.value()
        self.cachedSecs = self.timerDialSecs.value()

class PictureWindow(QMainWindow, pf_ui):
    def __init__(self):
        super(PictureWindow, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        loadUi('Frame.ui', self)
        self.initInteraction()


    def initInteraction(self):
        if OS() == "Linux":
            self.pictureList = glob(r"/home/pi/Aggie/photoframeimgs/*")
        else:
            self.pictureList = glob(r"C:\Users\Niall\OneDrive - University of Bristol\Aggie\Software\photoframeimgs\*")
        print(self.pictureList)
        np.random.shuffle(self.pictureList)
        print(self.pictureList)
        self.currentPicture = 0
        # print(self.pictureList)
        self.backButton.clicked.connect(self.toHome)
        self.rightPicButton.clicked.connect(self.increasePicture)
        self.leftPicButton.clicked.connect(self.decreasePicture)
        self.increasePicture()

    def toHome(self):
        self.close()

    def increasePicture(self):
        self.currentPicture += 1
        if self.currentPicture > len(self.pictureList)-1:
            self.currentPicture = 0
        self.currentPixmap = QtGui.QPixmap(self.pictureList[self.currentPicture])
        picWidth, picHeight =  self.currentPixmap.size().width(), self.currentPixmap.size().height()
        print(picHeight, picWidth)
        if picHeight < picWidth:
            self.finalPixmap = self.currentPixmap.transformed(QtGui.QTransform().rotate(0))
            print("rotated")
        else:
            self.finalPixmap = self.currentPixmap
            print("not rotated")
        self.pictureFrameLabel.setPixmap(self.finalPixmap)


    def decreasePicture(self):
        self.currentPicture -= 1
        if self.currentPicture < 0:
            self.currentPicture = len(self.pictureList)-1
        self.currentPixmap = QtGui.QPixmap(self.pictureList[self.currentPicture])
        picWidth, picHeight = self.currentPixmap.size().width(), self.currentPixmap.size().height()
        print(picHeight, picWidth)
        if picHeight < picWidth:
            self.finalPixmap = self.currentPixmap.transformed(QtGui.QTransform().rotate(0))
            print("rotated")
        else:
            self.finalPixmap = self.currentPixmap
            print("not rotated")
        self.pictureFrameLabel.setPixmap(self.finalPixmap)

class PlateWindow(QMainWindow, pr_ui):
    def __init__(self):
        super(PlateWindow, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        loadUi('PlateReader.ui', self)
        self.initInteraction()
        self.showFullScreen()


    def initInteraction(self):
        # self.led = LED(4)
        self.led = 0
        # self.led.off()
        self.timeHours = 0
        self.timeMins = 0
        self.timeSecs = 0
        self.cachedHours = 0
        self.cachedMins = 0
        self.cachedSecs = 0
        self.progressBar.setValue(0)
        self.minsPerData = 10
        self.minsPerDataLabel.setText(f"{self.minsPerData}")
        self.progress = 0
        self.timeSinceData = 0
        self.dataPoints = []
        self.measurementData = []
        self.lcdNumber.display(f"{self.timeHours:02}:{self.timeMins:02}:{self.timeSecs:02}")
        self.countdown = QTimer(self)
        self.dataTimer = QTimer(self)
        self.countdown.timeout.connect(self.updateProgress)
        self.dataTimer.timeout.connect(self.takeDataPoints)
        self.setGraphParams()
        self.backButton.clicked.connect(self.toHome)
        self.upButton.clicked.connect(self.increaseTime)
        self.downButton.clicked.connect(self.decreaseTime)
        self.upButton_2.clicked.connect(self.increaseNum)
        self.downButton_2.clicked.connect(self.decreaseNum)
        self.startButton.clicked.connect(self.startReading)
        self.stopButton.clicked.connect(self.endReading)

    def increaseTime(self):
        self.timeHours += 1
        self.updateDisplay()

    def decreaseTime(self):
        self.timeHours -= 1
        self.updateDisplay()

    def increaseNum(self):
        self.minsPerData += 1
        self.updateDisplay()

    def decreaseNum(self):
        self.minsPerData -= 1
        self.updateDisplay()

    def updateDisplay(self):
        if not self.countdown.isActive():
            self.lcdNumber.display(f"{self.timeHours:02}:{self.timeMins:02}:{self.timeSecs:02}")
            self.minsPerDataLabel.setText(f"{self.minsPerData}")
        else:
            self.lcdNumber.display(f"{self.cachedHours:02}:{self.cachedMins:02}:{self.cachedSecs:02}")

    def startReading(self):
        self.cachedHours = self.timeHours
        self.cachedMins = self.timeMins
        self.cachedSecs = self.timeSecs
        self.totalTime = self.timeHours*3600 + self.timeMins*60 + self.timeSecs
        self.dataPoints.append(self.takeMeasurement())
        self.countdown.start(1000)

    def setGraphParams(self):
        self.plot = self.GraphWidget.plot([],[])
        styles = {"color": "gray", "font-size": "20px"}
        self.GraphWidget.setBackground(None)
        self.GraphWidget.setLabel("left", "Fluorescence Intensity (A.U.)", **styles)
        self.GraphWidget.setLabel("bottom", "Time (mins)", **styles)

    def updateProgress(self):
        self.timerTick()
        if (self.timeSinceData == self.minsPerData*60):
            self.dataPoints.append(self.takeMeasurement())
            self.timeSinceData = 0
            # self.GraphWidget.plot([i for i in range(len(self.dataPoints))], self.dataPoints, color="r")
            self.plot.setData([i*self.minsPerData for i in range(len(self.dataPoints))], self.dataPoints, pen = "gray", symbol = "o", symbolPen = "pink", symbolBrush="pink")

        self.currentTime = self.cachedHours*3600 + self.cachedMins*60 + self.cachedSecs
        self.progressBar.setValue(round((1-self.currentTime/self.totalTime)*100))

    def takeMeasurement(self):
        self.measurementData = []
        # self.led.on()
        self.dataTimer.start(200)
        sleep(5)
        self.dataTimer.stop()
        return self.measurementData

    def takeDataPoints(self):
        # comm with rpi pico here
        # get value back
        self.measurementData.append()

    def endReading(self):
        self.countdown.stop()
        self.cachedHours = 0
        self.cachedMins = 0
        self.cachedSecs = 0
        self.timeHours = 0
        self.timeMins = 0
        self.timeSecs = 0
        self.updateDisplay()

    def timerTick(self):
        self.updateDisplay()
        if self.cachedSecs == 0:
            if self.cachedMins == 0:
                if self.cachedHours == 0:
                    self.endReading()
                else:
                    self.cachedHours -= 1
                    self.cachedMins = 59
                    self.cachedSecs = 59
            else:
                self.cachedMins -= 1
                self.cachedSecs = 59
        else:
            self.cachedSecs -= 1
        self.timeSinceData += 1



    def toHome(self):
        self.close()

class ClockWeatherWindow(QMainWindow, clw_ui):
    def __init__(self):
        super(ClockWeatherWindow, self).__init__()
        # self.setWindowFlag(Qt.FramelessWindowHint)
        loadUi('clockWeather.ui', self)
        self.initInteraction()
        self.showFullScreen()
        self.iconNums = ["01", "02", "03", "04", "09", "10", "11", "13", "50"]
        # self.iterator = 0
        # print(self.iterator)
        # print(self.cityPicker.currentText())
        self.showTime()
        self.showWeather(self.cityPicker.currentText())
        clockTimer = QTimer(self)
        weatherTimer = QTimer(self)
        weatherTimer.timeout.connect(lambda: self.showWeather(self.cityPicker.currentText()))
        clockTimer.timeout.connect(self.showTime)
        clockTimer.start(1000)
        weatherTimer.start(2000)

    def showTime(self):
        currentTime = QTime.currentTime()
        currentDay = QDate.currentDate()
        timeString= currentTime.toString('hh:mm:ss')
        labelDayOfWeek = currentDay.toString('dddd')
        labelDate = currentDay.toString('dd MMMM yyyy')
        self.timeLabel.setText(timeString)
        self.currentDay.setText(labelDayOfWeek)
        self.currentDate.setText(labelDate)

    def showWeather(self, locArg):
        # print("Fetching Weather...")
        self.getWeather = Weather(locArg)
        self.getWeather.retrieveAll()
        self.getWeather.updateAll()

        # self.getWeather.currentIconNum = str(self.iconNums[self.iterator])+"d"

        if OS() == "Linux":
            self.getWeather.currentIconLoc = f"/home/pi/Aggie/icons/{self.getWeather.currentIconNum}.png"
        else:
            self.getWeather.currentIconLoc = f"C:\\Users\\Niall\\OneDrive - University of Bristol\\Aggie\\Software\\icons\\{self.getWeather.currentIconNum}.png"
        # print(self.getWeather.currentIconLoc)
        # print(f"{self.getWeather.currentTemp:.1f} <sup>o</sup>C")
        self.currentTemp.setText(f"{self.getWeather.currentTemp:.1f} <sup>o</sup>C")
        self.currentHumidity.setText(str(self.getWeather.currentHumidity) + " %")
        self.currentWeatherDescription.setText(self.getWeather.currentDescription)
        self.currentIcon.setPixmap(QtGui.QPixmap(self.getWeather.currentIconLoc))
        self.updateBackground()
        # self.iterator += 1
        # print(self.getWeather.hourlyIconLocs)
        self.futureTime1.setText(self.getWeather.hourlyTimes[0])
        self.futureTemp1.setText(str(round(self.getWeather.hourlyTemps[0])) + " <sup>o</sup>C")
        self.futureIcon1.setPixmap(QtGui.QPixmap(self.getWeather.hourlyIconLocs[0]))
        self.futurePrecip1.setText(f"{self.getWeather.hourlyRain[0]} %")

        self.futureTime2.setText(self.getWeather.hourlyTimes[1])
        self.futureTemp2.setText(str(round(self.getWeather.hourlyTemps[1])) + " <sup>o</sup>C")
        self.futureIcon2.setPixmap(QtGui.QPixmap(self.getWeather.hourlyIconLocs[1]))
        self.futurePrecip2.setText(f"{self.getWeather.hourlyRain[1]} %")

        self.futureTime3.setText(self.getWeather.hourlyTimes[2])
        self.futureTemp3.setText(str(round(self.getWeather.hourlyTemps[2])) + " <sup>o</sup>C")
        self.futureIcon3.setPixmap(QtGui.QPixmap(self.getWeather.hourlyIconLocs[2]))
        self.futurePrecip3.setText(f"{self.getWeather.hourlyRain[2]} %")

        self.futureTime4.setText(self.getWeather.hourlyTimes[3])
        self.futureTemp4.setText(str(round(self.getWeather.hourlyTemps[3])) + " <sup>o</sup>C")
        self.futureIcon4.setPixmap(QtGui.QPixmap(self.getWeather.hourlyIconLocs[3]))
        self.futurePrecip4.setText(f"{self.getWeather.hourlyRain[3]} %")

        self.futureTime5.setText(self.getWeather.hourlyTimes[4])
        self.futureTemp5.setText(str(round(self.getWeather.hourlyTemps[4])) + " <sup>o</sup>C")
        self.futureIcon5.setPixmap(QtGui.QPixmap(self.getWeather.hourlyIconLocs[4]))
        self.futurePrecip5.setText(f"{self.getWeather.hourlyRain[4]} %")

    def updateBackground(self):
        pass
        # if self.getWeather.currentIconNum[:-1] in ["01", "02"]:
        #     self.setStyleSheet("QWidget{\nbackground-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(220, 96, 65, 255));\n}")
        # elif self.getWeather.currentIconNum[:-1] in ["03", "50"]:
        #     self.setStyleSheet("QWidget{\nbackground-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(160, 160, 160, 255));\n}")
        # elif self.getWeather.currentIconNum[:-1] in ["04", "09"]:
        #     self.setStyleSheet("QWidget{\nbackground-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(50, 50, 50, 255));\n}")
        # elif self.getWeather.currentIconNum[:-1] == "13":
        #     self.setStyleSheet("QWidget{\nbackground-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(92, 186, 223, 255));\n}")
        # elif self.getWeather.currentIconNum[:-1] == "10":
        #     self.setStyleSheet("QWidget{\nbackground-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(14, 110, 148, 255));\n}")
        # elif self.getWeather.currentIconNum[:-1] == "11":
        #     self.setStyleSheet("QWidget{\nbackground-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(228, 222, 57, 255));\n}")
        # else:
        #     self.setStyleSheet("QWidget{\nbackground-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(75, 153, 161, 255));\n}")

    def initInteraction(self):
        # self.backButton.clicked.connect(self.toHome)
        self.cityList = sorted(["London", "Cambridge", "Durham", "Reading", "Bristol", "Basingstoke", "Cardiff", "Rzeszow"])
        self.cityPicker.addItems(self.cityList)
        self.cityPicker.currentIndexChanged.connect(self.onChanged)

    def onChanged(self):
        pass
        # print(self.cityPicker.currentText())
        # self.focus()
        # self.showWeather()


    # def toHome(self):
    #     self.close()

# class VisualiserWindow(vis_ui):
#     def __init__(self):
#         super(VisualiserWindow, self).__init__()
#         self.setWindowFlag(Qt.FramelessWindowHint)
#         loadUi('Visualiser.ui', self)
#         self.initInteraction()
#         self.showFullScreen()
#
#
#     def initInteraction(self):
#         self.backButton.clicked.connect(self.toHome)
#         # self.webWidget = QWeb.QWebEngineView()
#         self.webWidget.load(QUrl("https://www.windy.com/?54.402,-7.377,5"))
#         # self.webWidget.show()
#
#     def toHome(self):
#         self.close()

class RadioWindow(QMainWindow,  rad_ui):
        def __init__(self):
            super(RadioWindow, self).__init__()
            # self.setWindowFlag(Qt.FramelessWindowHint)
            loadUi('Radio.ui', self)
            self.initInteraction()
            self.showFullScreen()

        def initInteraction(self):
            self.bars = [self.bar1, self.bar2, self.bar3, self.bar4, self.bar5, self.bar6, self.bar7, self.bar8, self.bar9, self.bar10,
            self.bar11, self.bar12, self.bar13, self.bar14, self.bar15, self.bar16, self.bar17, self.bar18, self.bar19, self.bar20, self.bar21]
            self.numBars = len(self.bars)

            self.stations = {
            "BBC Radio 1" : "http://stream.live.vc.bbcmedia.co.uk/bbc_radio_one",
            "BBC Radio 1 Xtra" : "http://stream.live.vc.bbcmedia.co.uk/bbc_1xtra",
            # "BBC Radio 1 Relax" : "http://stream.live.vc.bbcmedia.co.uk/bbc_1relax",
            # "BBC Radio 1 Dance" : "http://stream.live.vc.bbcmedia.co.uk/bbc_radio_one_dance",
            "BBC Radio 2" : "http://stream.live.vc.bbcmedia.co.uk/bbc_radio_two",
            "BBC Radio 3" : "http://stream.live.vc.bbcmedia.co.uk/bbc_radio_three",
            "BBC Radio 4" : "http://stream.live.vc.bbcmedia.co.uk/bbc_radio_fourfm",
            "BBC Radio 5 Live" : "http://stream.live.vc.bbcmedia.co.uk/bbc_radio_five_live",
            "BBC Radio 6 Music" : "http://stream.live.vc.bbcmedia.co.uk/bbc_6music",
            "Classic FM" : "http://media-ice.musicradio.com/ClassicFMMP3",
            "Heart UK" : "http://media-ice.musicradio.com/HeartUK",
            "Heart 80s" : "http://media-ice.musicradio.com/Heart80s",
            "Heart 90s" : "http://media-ice.musicradio.com/Heart90s",
            "Heart 00s" : "http://media-ice.musicradio.com/Heart00s",
            "Capital UK" : "https://media-ssl.musicradio.com/CapitalUK"
            }
            self.visStyles = ["FFT", "Wave", "None"]
            self.stationPicker.addItems(sorted(self.stations.keys()))
            self.stationPicker.currentIndexChanged.connect(self.changedStation)
            self.changedStation()
            self.visPicker.addItems(self.visStyles)
            self.visPicker.currentIndexChanged.connect(self.initVis)
            self.initVis()
            self.playButton.clicked.connect(lambda: self.play())
            self.stopButton.clicked.connect(lambda: self.stop())

            self.refreshTimer = QTimer(self)
            self.refreshTimer.timeout.connect(self.getNewData)
            self.refresh = int(1/(180/60/1000))
            # self.refreshTimer.start(self.refresh)

            self.interpTimer = QTimer(self)
            self.interpTimer.timeout.connect(self.updateVis)
            self.update = int(self.refresh/4)
            # self.interpTimer.start(self.update)

            self.oldVisData = getFakeRadioFFT(self.numBars)
            self.newVisData = getFakeRadioFFT(self.numBars)
            self.updateVis()
            # self.player=self.instance.media_player_new()

        def play(self):
            self.instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
            self.player = self.instance.media_player_new()
            self.media = self.instance.media_new(self.stations[self.stationPicker.currentText()])
            self.player.set_media(self.media)
            self.player.play()
            if not self.refreshTimer.isActive():
                self.refreshTimer.start(self.refresh)
            if not self.interpTimer.isActive():
                self.interpTimer.start(self.update)

        def stop(self):
            self.player.stop()
            if self.refreshTimer.isActive():
                self.refreshTimer.stop()
            if self.interpTimer.isActive():
                self.interpTimer.stop()

        def initVis(self):
            self.visStyle = self.visPicker.currentText()
            # print(f"current text = {self.visPicker.currentText()}")
            if self.visStyle == "FFT":
                self.oldVisData = getFakeRadioFFT(self.numBars)
            elif self.visStyle == "None":
                self.oldVisData == np.array([0]*self.numBars)
            elif self.visStyle == "Wave":
                self.oldVisData = (0.4*np.sin(1*np.arange(self.numBars)/self.numBars*(2*np.pi))
                                    + 0.2*np.sin(20*np.arange(self.numBars)/self.numBars*(2*np.pi))
                                    + 0.5)

        def changedStation(self):
            try:
                self.player.stop()
            except Exception:
                pass
            self.instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
            self.player = self.instance.media_player_new()
            self.media = self.instance.media_new(self.stations[self.stationPicker.currentText()])
            self.player.set_media(self.media)
            # self.session = requests.Session()

        def getNewData(self):
            if self.visStyle == "FFT":
                self.newVisData = getFakeRadioFFT(self.numBars)
            elif self.visStyle == "None":
                pass
            elif self.visStyle == "Wave":
                # self.newVisData = np.roll(self.oldVisData)
                pass

        def updateVis(self):
            if self.visStyle == "FFT":
                self.barHeights = self.oldVisData + (self.newVisData - self.oldVisData)/(self.refresh/self.update)
                self.oldVisData = self.barHeights
                # print(self.oldVisData, (self.newVisData - self.oldVisData)/(self.refresh/self.update) )

                self.barHeights = self.barHeights*200 #scaling factor for size of area
                self.barX = [40 + i*34 for i in range(self.numBars)]
                self.barY = [571 - self.barHeights[i] for i in range(self.numBars)]

                for i, bar in enumerate(self.bars):
                    bar.resize(30, int(self.barHeights[i]))
                    bar.move(int(self.barX[i]), int(self.barY[i]))

            elif self.visStyle == "Wave":
                print("wave!")
                self.oldVisData = np.roll(self.oldVisData, 1)
                self.barHeights = self.oldVisData*200
                # print(self.oldVisData)
                self.barX = [40 + i*34 for i in range(self.numBars)]
                self.barY = [571 - self.barHeights[i] for i in range(self.numBars)]
                for i, bar in enumerate(self.bars):
                    bar.resize(30, int(self.barHeights[i]))
                    bar.move(int(self.barX[i]), int(self.barY[i]))

            elif self.visStyle == "None":
                for i, bar in enumerate(self.bars):
                    bar.resize(0, 0)
                    bar.move(0, 0)


            # try:
            #     self.artistlist, self.trackList = getInfo(self.stationPicker.currentText())
            # except Exception:
            #     print("No artists found")
            # print(self.artistlist, self.tracklist)

class HomeWindow(QMainWindow, home_ui):
    def __init__(self):
        super(HomeWindow, self).__init__()
        loadUi("PresentUI.ui", self)


        self.initInteraction()
        self.showFullScreen()

    def initInteraction(self):
        self.showTime()
        self.showDate()
        self.showWeather()

        self.timeTimer = QTimer(self)
        self.weatherTimer = QTimer(self)
        self.weatherTimer.timeout.connect(self.showWeather)
        self.timeTimer.timeout.connect(self.showTime)
        self.timeTimer.timeout.connect(self.showDate)
        self.timeTimer.start(1000)
        self.weatherTimer.start(2000)

    def showTime(self):
        currentTime = QTime.currentTime()
        labelTime = currentTime.toString('hh:mm')
        self.ClockLabel.setText(labelTime)

    def showDate(self):
        currentDay = QDate.currentDate()
        labelDay = currentDay.toString('dddd')
        # labelYear = currentDay.toString('dd MMM yyyy')
        labelDate = currentDay.toString("dd MMMM")
        labelYear = currentDay.toString('yyyy')
        self.ClockLabel_3.setText(labelDay)
        self.ClockLabel_2.setText(labelDate)
        self.ClockLabel_4.setText(labelYear)

    def showWeather(self):
        self.location = "Basingstoke"
        self.getWeather = Weather(self.location)
        self.getWeather.retrieveCurrentData()
        self.getWeather.updateCurrentData()

        self.TempValue.setText(f"{self.getWeather.currentTemp:.0f} <sup>o</sup>C")
        self.RainValue.setText(f"{self.getWeather.currentRain:.1f} mm")
        self.locationLabel.setText(self.location)
        self.WeatherPic.setPixmap(QtGui.QPixmap(self.getWeather.currentIconLoc))


def window():
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    print('Screen: %s' % screen.name())
    size = screen.size()
    print('Size: %d x %d' % (size.width(), size.height()))
    rect = screen.availableGeometry()
    print('Available: %d x %d' % (rect.width(), rect.height()))

    home = HomeWindow()
    plate = PlateWindow()
    frame = PictureWindow()
    # visualise = VisualiserWindow()
    radio = RadioWindow()
    clockWeather = ClockWeatherWindow()
    timing = TimerWindow()

    w = QStackedWidget()
    w.addWidget(home)
    w.addWidget(plate)
    w.addWidget(frame)
    # w.addWidget(visualise)
    w.addWidget(radio)
    w.addWidget(clockWeather)
    w.addWidget(timing)

    # self.PlateReader.clicked.connect(self.openPlateReader)
    # self.PhotoFrame.clicked.connect(self.openPictureFrame)
    # self.Visualiser.clicked.connect(self.openVisualiser)
    # self.ClockWeather.clicked.connect(self.openClockWeather)
    # self.Timer.clicked.connect(self.openTimer)
    # self.closeButton.clicked.connect(self.closeSystem)

    home.PlateReader.clicked.connect(lambda: w.setCurrentIndex(1))
    home.PhotoFrame.clicked.connect(lambda: w.setCurrentIndex(2))
    home.Radio.clicked.connect(lambda: w.setCurrentIndex(3))
    home.ClockWeather.clicked.connect(lambda: w.setCurrentIndex(4))
    home.Timer.clicked.connect(lambda: w.setCurrentIndex(5))
    home.closeButton.clicked.connect(lambda: sys.exit(app.exec_()))

    plate.backButton.clicked.connect(lambda: w.setCurrentIndex(0))
    frame.backButton.clicked.connect(lambda: w.setCurrentIndex(0))
    radio.backButton.clicked.connect(lambda: w.setCurrentIndex(0))
    clockWeather.backButton.clicked.connect(lambda: w.setCurrentIndex(0))
    timing.backButton.clicked.connect(lambda: w.setCurrentIndex(0))


    # w.resize(800, 600)
    w.showFullScreen()
    w.show()

    # ui = MyWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    sys.exit(app.exec_())

window()
