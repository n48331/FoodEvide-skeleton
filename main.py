import math

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two points on the Earth's surface using the haversine formula.

    Arguments:
    lat1 -- Latitude of the first point in degrees
    lon1 -- Longitude of the first point in degrees
    lat2 -- Latitude of the second point in degrees
    lon2 -- Longitude of the second point in degrees

    Returns:
    Distance between the two points in meters
    """
    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Calculate the differences between the latitudes and longitudes
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # Apply the haversine formula
    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    radius_of_earth = 6371000  # Radius of the Earth in meters
    distance = radius_of_earth * c

    return distance


def find_nearest_locations(data, center_lat, center_lon, radius):
    """
    Find the nearest locations within a given radius from a set of data.
    
    Arguments:
    data -- A list of dictionaries containing latitude and longitude data for locations
    center_lat -- Latitude of the center point in degrees
    center_lon -- Longitude of the center point in degrees
    radius -- Radius in kilometers
    
    Returns:
    List of locations within the given radius
    """
    nearest_locations = []
    
    for location in data:
        lat = location['latitude']
        lon = location['longitude']
        
        distance = haversine_distance(center_lat, center_lon, lat, lon)
        
        if distance <= radius:
            nearest_locations.append(location)
    
    return nearest_locations


data = [
    {"name": "Home", "latitude": 11.1848505, "longitude": 75.8435999},
    {"name": "Grand Bakes", "latitude": 11.1838543, "longitude": 75.8435412},
    {"name": "Grand Hotel", "latitude": 11.1828665, "longitude": 75.8458570},
    {"name": "Ramanattukara", "latitude": 11.177580, "longitude": 75.864940}
]

center_lat = 11.1848505
center_lon = 75.8435999
radius = 1500  # Assuming radius of 1500 meters

nearest_locations = find_nearest_locations(data, center_lat, center_lon, radius)

for location in nearest_locations:
    name = location['name']
    lat = location['latitude']
    lon = location['longitude']

    distance = haversine_distance(center_lat, center_lon, lat, lon)

    if distance >= 1000:
        distance = distance / 1000
        print(f"{name}: {distance:.1f} km")
    else:
        print(f"{name}: {distance:.0f} meters")

