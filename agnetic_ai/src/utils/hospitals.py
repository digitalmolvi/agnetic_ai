# src/utils/hospitals.py
import math

# Dummy list for demo
HOSPITALS = [
    {"name": "Civil Hospital Karachi", "lat": 24.8615, "lon": 67.0099},
    {"name": "Aga Khan Hospital", "lat": 24.867, "lon": 67.048},
]

def haversine(lat1, lon1, lat2, lon2):
    from math import radians, cos, sin, sqrt, atan2
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))

def find_nearby_hospitals(lat, lon):
    return sorted([
        {"name": h["name"], "distance_km": round(haversine(lat, lon, h["lat"], h["lon"]), 2)}
        for h in HOSPITALS
    ], key=lambda x: x["distance_km"])

