# src/utils/transport.py
import json
from src.data.sample_fares import FARES

def get_fare_summary():
    return [f"{item['route']}: PKR {item['fare']}" for item in FARES]

