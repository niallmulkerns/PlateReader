# PlateReader
Code for running a simple plate reader desk toy using PyQT5.

# Purpose

This respository is created as a backup to the offline storage. Originally, this was concieved as a desk adornment that has the functions of a plate reader (i.e. able to read fluorescence signals over time), whilst also having practical everyday purposes (e.g. weather, time, etc...).

# System Overview

The complete physical setup tested consists of a Raspberry Pi 4 microcontroller attached to a [Waveshare 5" capacitive touchscreen](https://www.waveshare.com/5inch-hdmi-lcd-h.htm), as well as a small electronics setup to control the laser and photodiode for the plate reader functionality. The electronic schematics are beyond the scope of this, but can be added on request. In addition, the set up of the Raspberry Pi with the screen can be found online, but I will post the contents of the config file as this wasincredibly difficult to get working correctly. The screen was simply connected by HDMI and USB, with no additional setup needed to use the touchscreen.

# Requirements

You will need to install
- Python 3+
- PyQT5
- glob (glob2)
- requests
- json
- datetime
- wget
- platform
- vlc
- numpy
- matplotlib
- gpiozero

to get full functionality. In addition, to view and change the .ui files, you will need to install PyQT Designer (this is bundled in `pyqt5-tools`).

# How it Works

The main file is `PresentUIRpi.py`, which should be run to bring the UI. By default, this is set to be full screen, but by pressing "close", the whole program will be ended. When run remotely on the RPi, a cron job is set up to run a shell script that waits for 30 seconds, then moves to the correct directory and runs `PresentUIRPI.py`. On the home screen, there are currently 5 distict applications that can be accessed:

## Timer 

This is simply a timer application that allows you to set up a timer that will expire and the screen will flash to alert you to when this is finished. It also comes with the built in function to set up a pomodoro timer (20 min intervals).

### To do/known bugs:
- Timer does not show finishing if you move away from that screen, only when you go back to that page.
- Timer needs a audio cue for when finished. 

## Weather/Clock

This page uses [OpenWeather API](https://openweathermap.org/) to fetch the real-time weather for any location that you may add to the list of location in the dropdown menu (`self.cityList`). Importing and parsing of the data is handled in `WeatherClass.py` - you will need to insert your own api key in `self.api_key` here by signing up for an account. The images for the weather icons are stored in the `icons` folder, these should not be changed. 

### To do/known bugs:
- TBD

## Plate Reader

This page allows you to control and visualise the progress of the real plate reader. Without the correct hardware/electronics, this is not a useful page. It will take readings every x minutes as specified on the page, and then update the graph in real time as the data progresses. It is unlikely to be very accurate, even when fully working, and is not intended for any diagnostic purposes, merely for fun :)

### To do/known bugs:
- Code not complete for this section. Throws no errors, but the electronics is not complete.

## Picture Window

This application simply displays images on the screen, and allows you to move between them by pressing the corresponding side of the screen. The images should be placed in the `platereaderimgs` folder. 

### To do/known bugs:
- Known bug of improper behaviour on import. PyQT5 will auto-rotate the image on import such that any portrait images are displayed incorrectly. 
- A swipe mechanism to change picture would be better. 

## Radio

**NB: This will not work if you are using a screen that does not have audio capabilities!**
This application allows you play any online radio station that has an available free stream. Currently this is set to be a few UK radio stations, but this can be changed by simply updating `self.stations` to include the display name and the link. There are also a few available visualisers, but one of the main things that would be nice would be a real time fft analysis of the signal (though this may not be feasible given the limited processing power of the RPI). The radio will continue to work even when the application window is changed.

### To do/known bugs:
- Implement a real-time audio fft visualiser (may require external microphone).


## *Unused Currently: Visualiser*

*This page allows you to display any website in the screen. However, the `QWeb` package is not possible to install on RPi currently, so a workaround would be needed to implement this page. I am sure that there is one, but for the moment it is shelved.*

Please enjoy this code and I hope it helps you! 
