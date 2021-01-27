#This file will create a new .csv in its folder

import requests
import pandas as panda

url = 'http://themodel.live/data/orderedresults.csv'
response = requests.get(url)
datacsv = response.content

csvfile = open('bballdata.csv', 'wb')
csvfile.write(datacsv)
csvfile.close()

data = panda.read_csv('bballdata.csv')

#converts from mountain time to eastern time 
def convertTime(time):
    if (time[2] != ':') or (time[5] != ':'):
        return 'invalid time'
    elif time[0:2] == '22':
        return '00' + time[2:8]
    elif time[0:2] == '23':
        return '01' + time[2:8]
    else:
        toConvert = time[0:2]
        converted = int(toConvert)
        converted += 2
        newTime = str(converted) + time[2:8]
        return newTime

#changes each time value in the .csv
size = len(data)
for n in range(size - 1):
    mountainTime = data._get_value(n, 'time')
    data._set_value(n, "time", convertTime(mountainTime))

#overwites old time values in the .csv, saving new time values
data.to_csv('bballdata.csv', index=False)