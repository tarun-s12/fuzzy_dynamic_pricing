import geocoder
from geopy.distance import geodesic

MAX_DISTANCE = 50

def get_current_location():
    g = geocoder.ip('me')
    if g.ok and g.latlng:
        return (g.latlng[0], g.latlng[1])
    else:
        raise ValueError("Could not retrieve current location.")

def calculate_distance(lat1, lon1, lat2, lon2):
    return geodesic((lat1, lon1), (lat2, lon2)).kilometers

def calculate_proximity(distance):
    proximity = (1 - (distance / MAX_DISTANCE)) * 100
    proximity = max(min(proximity, 100), 0)  

    return proximity

def find_proximity(target_lat, target_lon):
    try:
        current_lat, current_lon = get_current_location()

        distance_km = calculate_distance(current_lat, current_lon, target_lat, target_lon)
        return calculate_proximity(round(distance_km, 2))

    except Exception as e:
        print(f"Error: {e}")

