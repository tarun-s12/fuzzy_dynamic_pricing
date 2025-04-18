import os
from datetime import datetime

from mock_data import MOCK_WEATHER_DATA, DEFAULT_WEATHER_DATA

class TimeDataProvider:
    def get_current_time_data(self):
        now = datetime.now()
        current_hour = now.hour
        current_day = now.isoweekday()
        month = now.month

        if month in [12, 1, 2]:
            current_season = 1
        elif month in [3, 4, 5]:
            current_season = 2
        elif month in [6, 7, 8]:
            current_season = 3
        else:
            current_season = 4
        
        return current_hour, current_day, current_season
    
    @staticmethod
    def get_time_description(hour, day, season):
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        seasons = ["Winter", "Spring", "Summer", "Fall"]
        
        time_str = f"{hour}:00"
        day_str = weekdays[day-1]
        season_str = seasons[season-1]
        
        return time_str, day_str, season_str


class WeatherDataProvider:    
    def get_weather_data(self): #Change to current city
        return self._get_mock_weather_data(city)
    
    def _get_mock_weather_data(self, city):
        city_data = MOCK_WEATHER_DATA.get(city, DEFAULT_WEATHER_DATA)
        
        temperature = city_data["temperature"]
        condition = city_data["condition"]
        wind_speed = city_data["wind_speed"]
        
        weather_score = self._calculate_weather_score(temperature, condition, wind_speed)
        return weather_score, temperature, condition
    
    def _calculate_weather_score(self, temperature, condition, wind_speed):
        if 20 <= temperature <= 25:
            temp_factor = 40
        elif 15 <= temperature < 20 or 25 < temperature <= 30:
            temp_factor = 30
        elif 10 <= temperature < 15 or 30 < temperature <= 35:
            temp_factor = 20
        elif 5 <= temperature < 10 or 35 < temperature <= 40:
            temp_factor = 10
        else:
            temp_factor = 0
            
        good_conditions = ["Clear", "Clouds"]
        fair_conditions = ["Mist", "Haze", "Fog", "Dust"]
        poor_conditions = ["Rain", "Drizzle", "Snow", "Thunderstorm"]
        
        if condition in good_conditions:
            condition_factor = 40
        elif condition in fair_conditions:
            condition_factor = 20
        elif condition in poor_conditions:
            condition_factor = 0
        else:
            condition_factor = 20
            
        if wind_speed < 5:
            wind_factor = 20
        elif wind_speed < 10:
            wind_factor = 10
        elif wind_speed < 15:
            wind_factor = 5
        else:
            wind_factor = 0
            
        return temp_factor + condition_factor + wind_factor