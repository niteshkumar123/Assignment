from function import weather, wind_speed, pressure
import sys
import requests

url = open("api_url", 'r').read()

if __name__ == "__main__":

    response = requests.get(url).json()
    res = response['list']
    assert isinstance(res, object)

    while True:
        choice = int(input("please select  1 - Get Weather , 2 - Get Wind Speed , 3 - Get Pressure , 0 - exit"))
        if choice == 1:
            print(weather(res))
        elif choice == 2:
            print(wind_speed(res))
        elif choice == 3:
            print(pressure(res))
        elif choice == 0:
            sys.exit()
        else:
            pass
