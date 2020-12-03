import requests

from pprint import pprint

def weather_search():

    while True:
        search_how = input("\nWould you like to search by city or zipcode? ").upper()
        if search_how == "CITY":
            city = input("\nEnter city: ").upper()
            print("\n----SENDING REQUEST----")
            print("\nConnecting to data host...")
            city_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=5f4d428f75f6478347c4bb688789fc59'.format(city)
            city_req = requests.get(city_url)
            city_data = city_req.json()
            if city_req.status_code == 200:
                print("Data host connection successful...")
                print("\n----REQUEST SUCCESSFUL----")
                print("\n-NOW DISPLAYING CURRENT WEATHER DATA FOR REQUESTED LOCATION: ",city,"\n")
                for key, value in city_data.items():
                    print(key, ' : ', value)
                while True:
                    would_conv = input("\nThe temperature displayed is in kelvin. \n(Y/N) Would you like to convert to farneheit or celsius? ").upper()
                    if would_conv == "Y":
                        cel_far = input("\n(C/F) Celsius or farenheit? ").upper()
                        if cel_far == "C":
                            temp = float(input("Temp: "))
                            conv_c = temp - 273.15
                            print("Temp in celsius: ",conv_c)
                            break
                        if cel_far == "F":
                            temp = float(input("Temp: "))
                            conv_f = (temp - 273.15) * 9//5 + 32
                            print("Temp in farenheit: ",conv_f)
                            break
                        if cel_far != "C" and cel_far != "F":
                            print("-----INVALID ENTRY-----")
                            continue
                    if would_conv == "N":
                        break
                    if would_conv != "Y" and would_conv != "N":
                        print("-----INVALID ENTRY")
            if city_req.status_code == 400:
                print("\n------BAD REQUEST------")
                print("\n-------TRY AGAIN-------")
            if city_req.status_code == 403:
                print("\n----FORBIDDEN REQUEST----")
                print("\n-------TRY AGAIN-------")
            if city_req.status_code == 404:
                print("\n---",city, " NOT FOUND---")
                print("\n-------TRY AGAIN-------")
            break
        if search_how == "ZIPCODE":
            zipcode = int(input("\nEnter zipcode:"))
            print('\n------SENDING REQUEST------')
            print("\nConnecting to data host...")
            zipcode_url = 'http://api.openweathermap.org/data/2.5/weather?zip={}&appid=5f4d428f75f6478347c4bb688789fc59'.format(zipcode)
            zipcode_req = requests.get(zipcode_url)
            zipcode_data = zipcode_req.json()
            if zipcode_req.status_code == 200:
                print("Data host connection successful...")
                print("\n----REQUEST SUCCESSFUL----")
                print("\n-NOW DISPLAYING CURRENT WEATHER DATA FOR REQUESTED LOCATION: ",zipcode,"\n")
                for key, value in zipcode_data.items():
                    print(key, ' : ', value)
                while True:
                    would_conv = input("\nThe temperature displayed is in kelvin. \n(Y/N) Would you like to convert to farneheit or celsius? ").upper()
                    if would_conv == "Y":
                        cel_far = input("\n(C/F) Celsius or farenheit? ").upper()
                        if cel_far == "C":
                            temp = float(input("Temp: "))
                            conv_c = temp - 273.15
                            print("Temp in celsius: ",conv_c)
                            break
                        if cel_far == "F":
                            temp = float(input("Temp: "))
                            conv_f = (temp - 273.15) * 9//5 + 32
                            print("Temp in farenheit: ",conv_f)
                            break
                        if cel_far != "C" and cel_far != "F":
                            print("-----INVALID ENTRY-----")
                            continue
                    if would_conv == "N":
                        break
                    if would_conv != "Y" and would_conv != "N":
                        print("-----INVALID ENTRY")
            if zipcode_req.status_code == 400:
                print("\n------BAD REQUEST------")
                print("\n-------TRY AGAIN-------")
            if zipcode_req.status_code == 403:
                print("\n----FORBIDDEN REQUEST----")
                print("\n-------TRY AGAIN-------")
            if zipcode_req.status_code == 404:
                print("\n---REQUEST NOT FOUND---")
                print("\n-------TRY AGAIN-------") 
            break
        if search_how != "CITY" or search_how != "ZIPCODE":
            print("\n-------INVALID ENTRY-------")
            continue

def main():
    
    print("-------WHEATHER INQUIRY-------")
    
    while True:
        yn_search = input("\n(Y/N) Would you like to recieve current weather data? ").upper()
        if yn_search == "Y":
            weather_search()
        if yn_search == "N":
            print("\nWell this is awkward...")
            input("Press ENTER to break the tension. ")
            continue
        if yn_search != "Y" and yn_search != "N":
            print("\n------INVALID ENRTY------")
            continue

main()









