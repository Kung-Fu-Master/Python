import os
import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = os.getcwd() + os.sep + "weather_worldMap_16" + os.sep + "death_valley_2014.csv"
#filename = os.getcwd() + os.sep + "weather_data16" + os.sep + "sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    highs, lows = [], []
    dates = []
    for row in reader:
        try:
            high = int(row[1])
            low = int(row[3])
            date = datetime.strptime(row[0], "%Y-%m-%d")
        except ValueError:
            print(date, "missing date")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)
    #print(highs)

    #fig = plt.figure(dpi=128, figsize=(10,6))
    fig = plt.figure(dpi=128)
    plt.plot(dates, highs, c="red", alpha=0.5)
    plt.plot(dates, lows, c="blue", alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
    plt.title("Daily high temperature 2018, Auguest")
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)
    plt.show()


#print(os.path.abspath('.')) #current working directory
#print(os.path.abspath(os.curdir)) #current working directory
#print(os.path.abspath('..')) #current working directory parent directory


