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

if __name__ == "__main__":
    main()
