#!/usr/bin/python3

import argparse # accept flags from CLI

import requests # make HTTP lookup

def token_getter(ip, username, password):
    # create the "finished" API to be queried
    token_api = f'https://{ip}/redfish/v1/SessionService/Sessions'
    # make our API request
    r = requests.post(token_api, json={'UserName': username, 'Password': password})
    return r.headers['X-Auth token']



def main():
    """run time code"""

    token = token_getter(args.i, args.u, args.p)
    


if __name__ == "__main__":
    # start to declare flag logic
    parser = argparse.ArgumentParser(description='Interact with iDRAC')
    
    # user may set UserName
    parser.add_argument('-u', metavar="IDRACUSER", type=str, default='root', help='Defines the iDRAC username')

    # user may set Password
    parser.add_argument('-p', metavar="IDRACPW", type=str, default='qwerty', help='Defines the iDRAC password')

    # user may set the IP of the IDRAC to be contacted
    parser.add_argument('-i', metavar="IDRACIP", type=str, help='IP address of the iDRAC')
    
    # creates an args object
    args = parser.parse_args()
    main()
