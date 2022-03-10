#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   API Nasa NEOW service https://api.nasa.gov/neo/"""

import sys
import requests
from pprint import pprint

API = "https://api.nasa.gov/neo/rest/v1/feed?api_key="

# function for returning our NASA API key (we don't want this in our code)
def nasakey():
    """returns the API key provided by api.nasa.gov"""
    with open("/home/student/.nasa.key", "r") as nk:
        nasakey = nk.read()
    return nasakey.rstrip("\n") # return the key with "\n" stripped (if it is present)

def main():
    """runtime"""

    r = requests.get(f"{API}{nasakey()}") # put together our API call
    
    # determine if the 200 response code was returned (all other codes are undesirable)
    if r.status_code != 200:
        sys.exit()

    # strip off the json from our response
    neo_data = r.json()

    print(neo_data.get('near_earth_objects').get('2022-03-17')[0].keys())

    # loop across near earth objects (returns dates)
    for date in neo_data.get('near_earth_objects'):
        print(f'Diplaying data for {date}')
        for asteroid in neo_data.get('near_earth_objects').get(date): # loop across a date (retiurns an asteroid)
            if not asteroid.get('is_potentially_hazardous_asteroid'): # is this value false?
                print(f'Asteroid ID: {asteroid.get("id")} Asteroid Name: {asteroid.get("name")}') # print out asteroid name, id
            else: # else print out all data
                print(asteroid)

if __name__ == "__main__":
    main()
