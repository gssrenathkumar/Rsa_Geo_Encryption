import requests
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

# Data Requests
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x','y','z']
res = requests.get('https://ipinfo.io/')
data = res.json()
city = data['city']
location = data['loc'].split(',')

#Geo_lat_long_convertor
# Algorithm convertor
def geo_lat_long_convertor(latitude,longitude,time_minute,time_am_pm):
        if time_am_pm =="AM":
            latitude=latitude+float(time_minute)
            longitude=longitude-float(time_minute)
            latitude=round(latitude,4)
            longitude=round(longitude,4)
        else:
            latitude=latitude-float(time_minute)
            longitude=longitude+float(time_minute)
            latitude=round(latitude,4)
            longitude=round(longitude,4)
        return latitude,longitude


def encryption(lat_code,long_code,time_minute):
        lat_password_string=""
        long_password_string=""
        lat_code=str(lat_code).replace(".","0")
        long_code=str(long_code).replace(".","1")
        lat_code=str(lat_code).replace("-","0")
        long_code=str(long_code).replace("-","1")
        for i in str(lat_code):
            lat_password_string += alphabet[(int(i)+time_minute)%26]
        for i in str(long_code):
            long_password_string += alphabet[(int(i)+time_minute)%26]
        return lat_password_string,long_password_string
    
def timer(time_zone):
    IST = pytz.timezone(time_zone)
    datetime_ist = datetime.now(IST)
    seconds=datetime_ist.strftime('%S')
    return seconds



def password_encrypter(seconds):
    # Final Latitude and Longitude
    # Getting time from timezone
    IST = pytz.timezone(time_zone)
    datetime_ist = datetime.now(IST)
    time_minute=int(datetime_ist.strftime('%M'))
    time_am_pm=datetime_ist.strftime('%p')

    # Seconds Timer
    lat_code,long_code=geo_lat_long_convertor(latitude,longitude,time_minute,time_am_pm)

    lat_password,long_password=encryption(lat_code,long_code,time_minute)   
    final_key=lat_password+long_password
    return final_key




latitude = float(location[0])
longitude = float(location[1])
# TimeZone Tracker
tf = TimezoneFinder()
time_zone=tf.timezone_at(lng=float(longitude), lat=float(latitude))

seconds=timer(time_zone)
password=password_encrypter(seconds)
print(password)