'''
Created on Feb 25, 2018

@author: Christine
'''
import re
from bs4 import BeautifulSoup
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
                      

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return(cleantext)

def output(info_dict) -> str:
    """Returns string representing directions in navigation"""
    
    string = "DIRECTIONS\n"
    
    for route_list in info_dict['routes']:
        for k,v in route_list.items():
            if k=='legs':
                for item in v:
                    for k1,v1 in item.items():
                        if k1=='steps':
                            for i in v1:
                                for i1,p1 in i.items():
                                    if i1=='html_instructions':
                                        cleanhtml(p1)
                                        string += cleanhtml(p1) + "\n"
    return string


if __name__ == "__main__":
    url = build_directions_url(["Los Angeles, CA", "Arcadia, CA"])
    json_dict = get_dict(url)
    print(output(json_dict))