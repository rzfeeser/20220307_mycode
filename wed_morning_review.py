#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Wed morning review - For looping across imaginative datasets possibly returned by
   Dell EMC PyU4V"""

import time

# for loop across simple list - fake list of arrays
disk_list = [600293, 203928, 103858, 30389]
for disk in disk_list:
    print(disk)

time.sleep(4)

# for loop across list of dictionaries
disk_list = [
        {'array': '600293', 'disk_ids':['a','b','c','d','e','f','g']}, 
        {'array': '203928', 'disk_ids':['h', 'i', 'j', 'k']}, 
        {'array': '103858', 'disk_ids':['l', 'm', 'n']}, 
        {'array': '30389', 'disk_ids':['o', 'p', 'q']}
        ]

# print out the dictionary each time through list
for disk in disk_list:
    print(disk)

time.sleep(4)

# print out a single value from the dictionary each time through the list
for disk in disk_list:
    print(disk.get('disk_ids'))

time.sleep(4)

# nested for loop
for disk in disk_list:
    for drive in disk.get('disk_ids'):
        print(drive)

time.sleep(4)

# for loop across simple dictionary
disk_list = {'array': '600293', 'disk_ids':['a','b','c','d','e','f','g']}

# display each disk id
for disk in disk_list.get('disk_ids'):
    print(disk)




# Get a list of physical disks installed in the array
#disk_list = conn.system.get_disk_id_list()
# Get disk information for each disk installed
#for disk in disk_list.get('disk_ids'):
#    disk_info = conn.system.get_disk_details(disk_id=disk)
