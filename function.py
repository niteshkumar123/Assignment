import datetime as dt
from datetime import date


def weather(res):
    Y = input("Year : ")
    M = input("Month : ")
    D = input("Day : ")
    input_date = dt.date(int(Y),int(M),int(D))
    t = 0.0
    c = 0
    for l in res:
        weather_date = date.fromtimestamp(l['dt'])
        if input_date == weather_date:
             t = t + l['main']['temp']
             c = c + 1

    if c == 0:
        return "Data not exist on date : " + input_date
    return "Average temperature on " + str(input_date) + " : " + str(round(t / c, 1))


def wind_speed(res):
    Y = input("Year : ")
    M = input("Month : ")
    D = input("Day : ")
    input_date = dt.date(int(Y),int(M),int(D))
    t = 0.0
    c = 0
    for l in res:
         wdate = date.fromtimestamp(l['dt'])
         if input_date == wdate:
             t = t + l['wind']['speed']
             c = c + 1

    if c == 0:
        return "Data not exist on date : " + input_date
    return "Wind speed on " + str(input_date) + " : " + str(round(t / c, 1))


def pressure(res):
    Y = input("Year : ")
    M = input("Month : ")
    D = input("Day : ")
    input_date = dt.date(int(Y),int(M),int(D))
    t = 0.0
    c = 0
    for l in res:
         wdate = date.fromtimestamp(l['dt'])
         if input_date == wdate:
             t = t + l['main']['pressure']
             c = c + 1
    if c == 0:
        return "Data not exist on date : " + input_date

    return "pressure on " + str(input_date) + " : " + str(round(t / c, 1))
