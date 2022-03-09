#!/usr/bin/env python3
"""exploring challenge 01 and 02"""

import netifaces

def macgetter(interface_name):
    """pass an interface name (string) will return the MAC"""
    mac = netifaces.ifaddresses(interface_name)[netifaces.AF_LINK][0]['addr']
    return mac # string




def ipgetter(interface_name):
    """pass an interface name (string) will return the IP"""
    ip = netifaces.ifaddresses(wallawalla)[netifaces.AF_INET][0]['addr']
    return ip # string



def main():
    """run time"""
    print(netifaces.interfaces())

    for i in netifaces.interfaces():
        print('\n****** details of interface - ' + i + ' ******')
        try:
            print('MAC: ', end='') # This print statement will always print MAC without an end of line
            print( macgetter(i) ) # Prints the MAC address
            print('IP: ', end='')  # This print statement will always print IP without an end of line
            print( ipgetter(i) ) # Prints the IP address
        except:          # This is a new line
            print('Could not collect adapter information') # Print an error message

if __name__ == "__main__":
    main()
