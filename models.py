import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def create_fuzzy_variables():
    demand = ctrl.Antecedent(np.arange(0, 101, 1), 'demand')  
    availability = ctrl.Antecedent(np.arange(0, 101, 1), 'availability')  
    urgency = ctrl.Antecedent(np.arange(0, 101, 1), 'urgency')  
    proximity = ctrl.Antecedent(np.arange(0, 101, 1), 'proximity')  
    weather = ctrl.Antecedent(np.arange(0, 101, 1), 'weather')    
    time_of_day = ctrl.Antecedent(np.arange(0, 24, 1), 'time_of_day')  
    day_of_week = ctrl.Antecedent(np.arange(1, 8, 1), 'day_of_week')  
    season = ctrl.Antecedent(np.arange(1, 5, 1), 'season')  
    price_adjustment = ctrl.Consequent(np.arange(-15, 26, 1), 'price_adjustment')  

    demand['low'] = fuzz.trimf(demand.universe, [0, 0, 40])
    demand['moderate'] = fuzz.trimf(demand.universe, [20, 50, 80])
    demand['high'] = fuzz.trimf(demand.universe, [60, 100, 100])

    availability['scarce'] = fuzz.trimf(availability.universe, [0, 0, 40])
    availability['moderate'] = fuzz.trimf(availability.universe, [20, 50, 80])
    availability['plentiful'] = fuzz.trimf(availability.universe, [60, 100, 100])

    urgency['low'] = fuzz.trimf(urgency.universe, [0, 0, 40])
    urgency['medium'] = fuzz.trimf(urgency.universe, [20, 50, 80])
    urgency['high'] = fuzz.trimf(urgency.universe, [60, 100, 100])

    proximity['far'] = fuzz.trimf(proximity.universe, [0, 0, 40])
    proximity['medium'] = fuzz.trimf(proximity.universe, [20, 50, 80])
    proximity['near'] = fuzz.trimf(proximity.universe, [60, 100, 100])

    weather['poor'] = fuzz.trimf(weather.universe, [0, 0, 40])
    weather['fair'] = fuzz.trimf(weather.universe, [20, 50, 80])
    weather['good'] = fuzz.trimf(weather.universe, [60, 100, 100])

    time_of_day['early_morning'] = fuzz.trimf(time_of_day.universe, [0, 0, 8])
    time_of_day['business_hours'] = fuzz.trimf(time_of_day.universe, [7, 12, 17])
    time_of_day['evening'] = fuzz.trimf(time_of_day.universe, [16, 19, 22])
    time_of_day['night'] = fuzz.trimf(time_of_day.universe, [21, 23, 23])

    day_of_week['weekday'] = fuzz.trimf(day_of_week.universe, [1, 3, 5])
    day_of_week['weekend'] = fuzz.trimf(day_of_week.universe, [5, 6.5, 7])

    season['winter'] = fuzz.trimf(season.universe, [1, 1, 2])
    season['spring'] = fuzz.trimf(season.universe, [1.5, 2, 3])
    season['summer'] = fuzz.trimf(season.universe, [2.5, 3, 4])
    season['fall'] = fuzz.trimf(season.universe, [3.5, 4, 4])

    price_adjustment['decrease'] = fuzz.trimf(price_adjustment.universe, [-15, -15, 0])
    price_adjustment['maintain'] = fuzz.trimf(price_adjustment.universe, [-5, 0, 5])
    price_adjustment['increase'] = fuzz.trimf(price_adjustment.universe, [0, 15, 25])
    
    return {
        'demand': demand,
        'availability': availability,
        'urgency': urgency,
        'proximity': proximity,
        'weather': weather,
        'time_of_day': time_of_day,
        'day_of_week': day_of_week,
        'season': season,
        'price_adjustment': price_adjustment
    }