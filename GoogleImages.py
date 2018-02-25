import urllib.request
import json

#my google static map key = AIzaSyCVReYL_jNGToQ1obg-AN31KCu6XMq5XAI
#https://maps.googleapis.com/maps/api/staticmap?center=0,0&zoom=1&size=100x100&key=AIzaSyCVReYL_jNGToQ1obg-AN31KCu6XMq5XAI

BASE_STATIC_MAP_URL = "https://maps.googleapis.com/maps/api/staticmap?"

def build_directions_url(center: str) -> str:
    """Builds URL for Directions API, taking in starting and endings"""
    query_parameters = [("center", center), ("zoom", 15), ("size", "600x600"), ("scale", 2)]
    return BASE_STATIC_MAP_URL + urllib.parse.urlencode(query_parameters)

if __name__ == "__main__":
    url = build_directions_url("Los Angeles, CA")
    print(url)