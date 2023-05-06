from geopy.geocoders import Nominatim


async def get_city(lat, long):
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(f'{str(lat)},{str(long)}')
        return str(location).split(', ')[-5]
    except:
        return None
