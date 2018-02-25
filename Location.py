import urllib.request
import json


MAPQUEST_API_KEY = "JD8gAgQEGf7xWnDTnW0KRoymDcuIcqzR"
MAPQUEST_SECRET = "HP3Q0rZnTzg5NskH"

BASE_DIRECTIONS_API_URL = "http://open.mapquestapi.com/directions/v2"

def build_directions_url(locations: list) -> str:
    """Builds URL for Directions API, taking in starting and endings"""
    query_parameters = [('key', MAPQUEST_API_KEY),
                        ('from', locations[0])]
    for end in locations[1:]:
        query_parameters.append(("to", end))
    return BASE_DIRECTIONS_API_URL + '/route?' + urllib.parse.urlencode(query_parameters)

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
    for item in info_dict['route']['legs']:
        for dir in item['maneuvers']:
            string += dir['narrative'] + "\n"
    return string


if __name__ == "__main__":
    url = build_directions_url(["Berkeley, CA", "San Jose, CA"])
    json_dict = get_dict(url)
    print(output(json_dict))
    