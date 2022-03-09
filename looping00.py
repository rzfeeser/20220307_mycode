#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - a simple for loop"""

import uuid


# for-loop is perfect for stepping through this list
iplist = ["10.1.1.1", "10.2.2.2", "10.3.3.3"] # list of IP (str)

# 'ip' is just a variable as we step through iplist
for ip in iplist:
    print(ip)   # we indent to show this is the code we want to run each time
                # through the loop



howmany = int(input("How many UUIDs should be generated? "))

print("Generating UUIDs...")

# range is required because an int cannot be looped
for rando in range(howmany):
    print( uuid.uuid4() )   # each time through the loop produce a UUID

