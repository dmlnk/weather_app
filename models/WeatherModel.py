import requests
import json
import pycountry
from datetime import datetime


class WeatherModel:

    def __init__(self):
        self.__api_key = "e8405d46153d3ee34b4b53a3dc7ec18b"
        self.current_data = None
        self.weather_data = None
        self.air_poll_data = None

    # Getting location data_____________________________________________________________________________
    def current_api_call(self, city_name):
        url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (city_name, self.__api_key)
        response = requests.get(url)
        self.current_data = json.loads(response.text)

        if self.current_data['cod'] == '400' or self.current_data['cod'] == '404':
            return False

        return True

    def get_country_code(self):
        return self.current_data['sys']['country']

    def get_country_name(self):
        country = pycountry.countries.get(alpha_2=self.current_data['sys']['country'])
        return country.name

    def get_city_name(self):
        return self.current_data['name']

    def get_city_id(self):
        return self.current_data['id']

    def get_coords(self):
        return self.current_data['coord']

    # Get weather data_____________________________________________________________________________
    def weather_api_call(self, lat, lon, units='metric'):
        url = "http://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=%s" % (
            lat, lon, self.__api_key, units)
        response = requests.get(url)
        data = json.loads(response.text)
        # print(data)
        self.weather_data = data

    def get_current_info(self):
        return self.weather_data["current"]

    def get_hourly_info(self):
        return self.weather_data["hourly"]

    def get_daily_info(self):
        return self.weather_data["daily"]

    def get_weather_description(self):
        return self.weather_data["current"]['weather'][0]['description'].title()

    def get_location(self):
        city = self.get_city_name()
        country = self.get_country_name()
        return "{}, {}".format(city, country)

    def get_time_date(self):
        timestamp = self.weather_data['current']['dt']
        return datetime.utcfromtimestamp(timestamp).strftime("%d %b %Y")

    def get_time(self, timestamp):
        return datetime.utcfromtimestamp(timestamp).strftime('%H:%M')

    def get_date(self, timestamp):
        return datetime.utcfromtimestamp(timestamp).strftime('%d.%m')

    def get_day(self, timestamp):
        return datetime.utcfromtimestamp(timestamp).strftime('%A')

    def get_full_day(self, timestamp):
        return datetime.utcfromtimestamp(timestamp).strftime('%a, %b %d')

    def get_icon(self):
        return 'img2/{}@2x.png'.format(self.weather_data["current"]['weather'][0]['icon'])

    def get_temperature(self):
        return "{}°C".format(int(self.weather_data["current"]['temp']))

    def get_feels_like(self):
        return "Feels like: {}°C".format(int(self.weather_data['current']['feels_like']))

    def get_visibility(self):
        return "Visibility: {} km".format(int(self.weather_data['current']['visibility'] / 1000))

    def get_wind(self):
        return "Wind: {}m/s".format(self.weather_data['current']['wind_speed'])

    def get_humidity(self):
        return "Humidity: {}%".format(self.weather_data['current']['humidity'])

    def get_sunrise(self):
        return "Sunrise: {}".format(self.get_time(self.weather_data['current']['sunrise']))

    def get_sunset(self):
        return "Sunrise: {}".format(self.get_time(self.weather_data['current']['sunset']))

    def get_uvi(self):
        return "UV index: {}".format(self.weather_data['current']['uvi'])

    def get_clouds(self):
        return "Cloudiness: {}%".format(self.weather_data['current']['clouds'])

    def get_pressure(self):
        return "Pressure: {}hPa".format(self.weather_data['current']['pressure'])

    # Day details_____________________________________________________________________________
    def get_d_icon(self, day):
        return 'img2/{}@2x.png'.format(self.weather_data["daily"][day]['weather'][0]['icon'])

    def get_d_description(self, day):
        return self.weather_data["daily"][day]['weather'][0]['description'].title()

    def get_d_date(self, day):
        timestamp = self.weather_data["daily"][day]['dt']
        return datetime.utcfromtimestamp(timestamp).strftime('%B %d')

    def get_d_max_temp(self, day):
        return "{}°C".format(int(self.weather_data["daily"][day]['temp']['max']))

    def get_d_min_temp(self, day):
        return "{}°C".format(int(self.weather_data["daily"][day]['temp']['min']))

    def get_d_day_temp(self, day):
        return "{}°C".format(int(self.weather_data["daily"][day]['temp']['day']))

    def get_d_night_temp(self, day):
        return "{}°C".format(int(self.weather_data["daily"][day]['temp']['night']))

    def get_d_morn_temp(self, day):
        return "{}°C".format(int(self.weather_data["daily"][day]['temp']['morn']))

    def get_d_evn_temp(self, day):
        return "{}°C".format(int(self.weather_data["daily"][day]['temp']['eve']))

    def get_d_max_feels(self, day):
        return "{}°C".format(int(self.weather_data["daily"][day]['feels_like']['max']))

    def get_d_min_feels(self, day):
        return "{}°C".format(int(self.weather_data["daily"][day]['feels_like']['min']))

    def get_d_day_feels(self, day):
        return "{}°C".format(int(self.weather_data["daily"][day]['feels_like']['day']))

    def get_d_night_feels(self, day):
        return "{}°C".format(int(self.weather_data["daily"][day]['feels_like']['night']))

    def get_d_morn_feels(self, day):
        return "{}°C".format(int(self.weather_data["daily"][day]['feels_like']['morn']))

    def get_d_evn_feels(self, day):
        return "{}°C".format(int(self.weather_data["daily"][day]['feels_like']['eve']))

    def get_d_precipitation(self, day):
        return "Precipitation: {}%".format(int(self.weather_data["daily"][day]['pop']) * 100)

    def get_d_humidity(self, day):
        return "Humidity: {}%".format(self.weather_data["daily"][day]['humidity'])

    def get_d_wind(self, day):
        return "Wind speed: {}m/s".format(self.weather_data["daily"][day]['wind_speed'])

    def get_d_uv(self, day):
        return "UV index: {}".format(self.weather_data["daily"][day]['uvi'])

    def get_d_pressure(self, day):
        return "Pressure: {}hPa".format(self.weather_data["daily"][day]['pressure'])

    def get_d_dew_point(self, day):
        return "Dew Point {}°C".format(self.weather_data["daily"][day]['dew_point'])

    # Get air pollution data_____________________________________________________________________________
    def pollution_api_call(self, lat, lon):
        url = "http://api.openweathermap.org/data/2.5/air_pollution?lat=%s&lon=%s&appid=%s" % (lat, lon, self.__api_key)
        response = requests.get(url)
        self.air_poll_data = json.loads(response.text)
        return self.air_poll_data

    def get_quality_index(self):
        if self.air_poll_data['list'][0]['main']['aqi'] == 1:
            return {'status': 'Good', 'color': '#35F32E'}
        elif self.air_poll_data['list'][0]['main']['aqi'] == 2:
            return {'status': 'Fair', 'color': '#CBE63E'}
        elif self.air_poll_data['list'][0]['main']['aqi'] == 3:
            return {'status': 'Moderate', 'color': '#EFEF08'}
        elif self.air_poll_data['list'][0]['main']['aqi'] == 4:
            return {'status': 'Poor', 'color': '#E56767'}
        elif self.air_poll_data['list'][0]['main']['aqi'] == 5:
            return {'status': ' Very Poor', 'color': '#F91818'}

    def get_co(self):
        return "CO: {} μg/m3".format(self.air_poll_data['list'][0]['components']['co'])

    def get_no(self):
        return "NO: {} μg/m3".format(self.air_poll_data['list'][0]['components']['no'])

    def get_no2(self):
        return "NO2: {} μg/m3".format(self.air_poll_data['list'][0]['components']['no2'])

    def get_o3(self):
        return "O3: {} μg/m3".format(self.air_poll_data['list'][0]['components']['o3'])

    def get_so2(self):
        return "SO2: {} μg/m3".format(self.air_poll_data['list'][0]['components']['so2'])

    def get_pm2_5(self):
        return "PM2.5: {} μg/m3".format(self.air_poll_data['list'][0]['components']['pm2_5'])

    def get_pm10(self):
        return "PM10: {} μg/m3".format(self.air_poll_data['list'][0]['components']['pm10'])

    def get_nh3(self):
        return "NH3: {} μg/m3".format(self.air_poll_data['list'][0]['components']['nh3'])
