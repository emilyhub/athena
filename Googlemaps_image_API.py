'''
Created on Feb 25, 2018

@author: Christine
'''

import urllib.request
import json


GOOGLE_API_KEY = 'AIzaSyDkN61iYzq13gNouJTLf2Oqw1_MkIpxefE'
# MAPQUEST_SECRET = "HP3Q0rZnTzg5NskH"

BASE_DIRECTIONS_API_URL = "https://maps.googleapis.com/maps/api/directions"

def build_directions_url(locations: list) -> str:
    """Builds URL for Directions API, taking in starting and endings"""
    query_parameters = [('key', GOOGLE_API_KEY ),
                        ('origin', locations[0])]
    for end in locations[1:]:
        query_parameters.append(("destination", end))
    return BASE_DIRECTIONS_API_URL + '/json?' + urllib.parse.urlencode(query_parameters)

def get_dict(url: str)-> dict:
    """Takes a URL and returns a dict representing the 
    parsed JSON response"""
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        
        return json.loads(json_text) #loads converts JSON text to python pbject
    
    finally:
        if response != None: #close response once we are done
            response.close()
                      

def output(info_dict) -> str:
    """Returns string representing directions in navigation"""
    string = "DIRECTIONS\n"
    for item in info_dict['routes']['legs']:
        for dir in item['maneuver']:
            string += dir['html_instructions'] + "\n"
    return string


if __name__ == "__main__":
    url = build_directions_url(["Los Angeles, CA", "Arcadia, CA"])
    print(url)
    json_dict = get_dict(url)
    print(output(json_dict))