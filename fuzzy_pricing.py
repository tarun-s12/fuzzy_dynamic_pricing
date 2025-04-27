import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

from models import create_fuzzy_variables
from rules import create_rules
from data_providers import TimeDataProvider, WeatherDataProvider
from config import CURRENCY_SYMBOL, BASE_PRICE

class FuzzyPricingSystem:    
    def __init__(self, base_price=BASE_PRICE):
        self.base_price = base_price
        
        self.variables = create_fuzzy_variables()
        self.rules = create_rules(self.variables)
        self.control_system = ctrl.ControlSystem(self.rules)
        self.simulation = ctrl.ControlSystemSimulation(self.control_system)
        
        self.time_provider = TimeDataProvider()
        self.weather_provider = WeatherDataProvider()
    
    def calculate_price_adjustment(self, demand, availability, urgency, proximity, 
                                  weather=None, time_of_day=None, day_of_week=None, 
                                  season=None, city="Coimbatore"):
        weather_description = None
        temperature = None
        
        time_of_day, day_of_week, season = self.time_provider.get_current_time_data()
        
        if weather is None:
            weather, temperature, weather_description = self.weather_provider.get_weather_data(city)
        
        self.simulation.input['demand'] = demand
        self.simulation.input['availability'] = availability
        self.simulation.input['urgency'] = urgency
        self.simulation.input['proximity'] = proximity
        self.simulation.input['weather'] = weather
        self.simulation.input['time_of_day'] = time_of_day
        self.simulation.input['day_of_week'] = day_of_week
        self.simulation.input['season'] = season
        
        try:
            self.simulation.compute()
            adjustment_percent = self.simulation.output['price_adjustment']
            adjusted_price = self.base_price * (1 + adjustment_percent / 100)
            
            result = {
                'inputs': {
                    'demand': demand,
                    'availability': availability,
                    'urgency': urgency,
                    'proximity': proximity,
                    'weather': weather,
                    'time_of_day': time_of_day,
                    'day_of_week': day_of_week,
                    'season': season
                },
                'price_adjustment_percent': adjustment_percent,
                'base_price': self.base_price,
                'currency_symbol': CURRENCY_SYMBOL,
                'adjusted_price': adjusted_price
            }
            
            time_str, day_str, season_str = self.time_provider.get_time_description(
                time_of_day, day_of_week, season
            )
            result['real_time_data'] = {
                'time': time_str,
                'day': day_str,
                'season': season_str,
                'data_source': "mock" if weather_description else "default"
            }
            
            if weather_description and temperature:
                result['real_time_data']['weather'] = {
                    'condition': weather_description,
                    'temperature': temperature
                }
            
            return result
            
        except Exception as e:
            raise ValueError(f"Error computing price adjustment: {e}")
    
    def visualize_output(self, demand, availability, urgency, proximity, 
                        weather=None, city="London"):
        result = self.calculate_price_adjustment(
            demand, availability, urgency, proximity,
            weather, city=city
        )
        
        price_adjustment = self.variables['price_adjustment']
        price_adjustment.view(sim=self.simulation)
        
        title_parts = [
            f"Price Adjustment (Demand={demand}%, Avail={availability}%, Urg={urgency}%",
            f"Prox={proximity}%, Weather={result['inputs']['weather']}%"
        ]
        
        real_data = result['real_time_data']
        time_info = f"Time={real_data['time']}, Day={real_data['day']}, Season={real_data['season']}"
        
        if 'weather' in real_data:
            weather_info = f"{real_data['weather']['condition']}, {real_data['weather']['temperature']}°C"
            title_parts.append(f"Weather: {weather_info}")
        
        title_parts.append(time_info)
        title_parts.append(f"Base Price: {CURRENCY_SYMBOL}{result['base_price']}/hr → Adj: {CURRENCY_SYMBOL}{result['adjusted_price']:.2f}/hr")
        
        plt.title('\n'.join(title_parts))
        plt.show()
        
        return result