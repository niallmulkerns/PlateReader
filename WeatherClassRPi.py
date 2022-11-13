import requests
import json
# import numpy as np
from datetime import datetime
import wget
from platform import system as OS

class Weather:
    def __init__(self, cityName="London"):
        self.api_key = "xxxxx"
        self.city = cityName
        self.country_code = 826 # Uk code iso 3166?
        self.numDataPoints = 24*5//3 # number of 3hr data points in 5 days
        #
        # self.currentUrl = f"http://api.openweathermap.org/data/2.5/weather?q={self.city},,{self.country_code}&limit=5&appid={self.api_key}&units=metric"
        # self.hourlyUrl = f"http://api.openweathermap.org/data/2.5/forecast?q={self.city},,{self.country_code}&limit=5&appid={self.api_key}&units=metric&cnt={self.numDataPoints}"
        self.currentUrl = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&limit=5&appid={self.api_key}&units=metric"
        self.hourlyUrl = f"http://api.openweathermap.org/data/2.5/forecast?q={self.city}&limit=5&appid={self.api_key}&units=metric&cnt={self.numDataPoints}"
        # self.dailyUrl = f"http://api.openweathermap.org/data/2.5/forecast/daily?q={self.city},,{self.country_code}&limit=5&appid={self.api_key}&units=metric&cnt={self.numDays}"

    def retrieveAll(self):
        self.retrieveCurrentData()
        self.retrieveHourlyData()
        # self.retrieveDailyData()

    def retrieveCurrentData(self):
        self.currentResponse = requests.get(self.currentUrl)
        self.currentWeather = json.loads(self.currentResponse.text)
        # self.iconUrl = f"http://openweathermap.org/img/wn/{self.iconNum}.png"
        # self.icon = wget.download(self.iconUrl, out = "C:\\Users\\nm13747\\OneDrive - University of Bristol\\Aggie\\Software\\icons")

    def retrieveHourlyData(self):
        self.hourlyResponse = requests.get(self.hourlyUrl)
        self.hourlyWeather = json.loads(self.hourlyResponse.text)
        # self.hourlytIconNum = self.currentWeather["weather"][0]["icon"]

    # def retrieveDailyData(self):
    #     self.dailyResponse = requests.get(self.dailyUrl)
    #     self.dailyWeather = json.loads(self.dailyResponse.text)

    def updateAll(self):
        self.updateCurrentData()
        self.updateHourlyData()
        # self.updateDailyData()

    def updateCurrentData(self):
        self.currentTemp = self.currentWeather["main"]["temp"]
        self.currentHumidity = self.currentWeather["main"]["humidity"]
        try:
            self.currentRain = self.currentWeather["rain"]["1h"]
        except:
            self.currentRain = 0
        self.currentSunriseTime = datetime.utcfromtimestamp(self.currentWeather["sys"]["sunrise"]).strftime('%H:%M')
        self.currentSunsetTime = datetime.utcfromtimestamp(self.currentWeather["sys"]["sunset"]).strftime('%H:%M')
        self.currentDescription = self.currentWeather["weather"][0]["main"] + " - " + self.currentWeather["weather"][0]["description"]
        self.currentIconNum = self.currentWeather["weather"][0]["icon"]
        if OS() == "Linux":
            self.currentIconLoc = f"/home/pi/Aggie/icons/{self.currentIconNum}.png"
        else:
            self.currentIconLoc = f"C:\\Users\\Niall\\OneDrive - University of Bristol\\Aggie\\Software\\icons\\{self.currentIconNum}.png"

        # self.currentIconLoc = f"/home/pi/Aggie/icons/{self.currentIconNum}.png"

    def updateHourlyData(self):
        self.dataPoints = self.hourlyWeather["list"]
        self.hourlyTemps = [dp["main"]["temp"] for dp in self.dataPoints]
        self.hourlyHumidities = [dp["main"]["humidity"] for dp in self.dataPoints]
        self.hourlyIcons = [dp["weather"][0]["icon"] for dp in self.dataPoints]
        self.hourlyRain = [round(dp["pop"]*100) for dp in self.dataPoints]
        self.hourlyDescriptions = [dp["weather"][0]["main"] + " - " + dp["weather"][0]["description"] for dp in self.dataPoints]
        self.hourlyTimes = [datetime.utcfromtimestamp(dp["dt"]).strftime("%H:%M") for dp in self.dataPoints]
        self.hourlyDates = [datetime.utcfromtimestamp(dp["dt"]).strftime("%d/%m/%Y") for dp in self.dataPoints]
        self.hourlyDays = [datetime.utcfromtimestamp(dp["dt"]).strftime("%A") for dp in self.dataPoints]
        if OS() == "Linux":
            self.hourlyIconLocs = [f"/home/pi/Aggie/icons/{icon}.png" for icon in self.hourlyIcons]
        else:
            self.hourlyIconLocs = [f"C:\\Users\\Niall\\OneDrive - University of Bristol\\Aggie\\Software\\icons\\{icon}.png" for icon in self.hourlyIcons]

def main():
    test = Weather()
    test.retrieveCurrentData()
    test.retrieveHourlyData()
    # test.retrieveDailyData()
    test.updateCurrentData()
    # print(test.hourlyWeather)
    test.updateHourlyData()
    # test.updateDailyData()
    print(test.currentTemp, test.currentHumidity)
    # print(test.currentDescription)
    # print(test.currentSunriseTime, test.currentSunsetTime)
    # print(test.currentWeather)

#     for i in ["01", "02", "03", "04", "09", "10", "11", "13", "50"]:
#         url1 = f"http://openweathermap.org/img/wn/{i}d@4x.png"
#         wget.download(url1, out = f"C:\\Users\\nm13747\\OneDrive - University of Bristol\\Aggie\\Software\\icons\\{i}d.png")
#         url2 = f"http://openweathermap.org/img/wn/{i}n@4x.png"
#         wget.download(url2, out = f"C:\\Users\\nm13747\\OneDrive - University of Bristol\\Aggie\\Software\\icons\\{i}n.png")
# main()
