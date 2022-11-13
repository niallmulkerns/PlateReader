# PlateReader
Code for running a simple plate reader desk toy using PyQT5.

## Purpose

This respository is created as a backup to the offline storage. Originally, this was concieved as a desk adornment that has the functions of a plate reader (i.e. able to read fluorescence signals over time), whilst also having practical everyday purposes (e.g. weather, time, etc...).

## System Overview

The complete physical setup tested consists of a Raspberry Pi 4 microcontroller attached to a Waveshare 5" capacitive touchscreen (https://www.waveshare.com/5inch-hdmi-lcd-h.htm), as well as a small electronics setup to control the laser and photodiode for the plate reader functionality. The electronic schematics are beyond the scope of this, but can be added on request. In addition, the set up of the Raspberry Pi with the screen can be found online, but I will post the contents of the config file as this wasincredibly difficult to get working correctly. The screen was simply connected by HDMI and USB, with no additional setup needed to use the touchscreen.

## Requirements

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

Please enjoy this code and I hope it helps you! 
