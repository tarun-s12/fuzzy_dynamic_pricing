import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=%t+%w+%C"
    response = requests.get(url)

    weather_data = response.text.strip().split()

    try:
        temperature = float(weather_data[0].replace('°C', '').replace('+', ''))
        wind_speed = float(weather_data[1].replace('km/h', '').replace('↘', '').replace('↗', '').replace('↑', '').replace('↓', '').strip())
        
        return {
            'temperature': temperature,
            'condition': weather_data[2],
            'wind_speed': wind_speed
        }
    except IndexError:
        return {"error": "Invalid data format"}
    except ValueError:
        return {"error": "Unable to extract numeric values"}
